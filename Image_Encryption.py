import PIL.Image as Image
import secrets
import random
import tkinter as tk
from tkinter import filedialog
import hashlib

def load_image(image_path):
    image = Image.open(image_path)
    return image.convert("RGB")

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    return file_path

def check_image_size(image, key):
    total_pixels = image.width * image.height
    if total_pixels >= 512:
        return True
    else:
        print(f"Image is too small to embed the key. Total pixels: {total_pixels}.")
        return False

def encrypt_image(image, key):
    im_pixels = image.load()
    width, height = image.size

    for i in range(width):
        for j in range(height):
            r, g, b = im_pixels[i, j]
            im_pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    ek = secrets.randbelow(10**128) * key
    bek = format(ek, '0512b') 

    chunk_size = 8
    key_chunks = [int(bek[i:i + chunk_size], 2) % 256 for i in range(0, len(bek), chunk_size)]
    chunk_count = len(key_chunks)

    c = 0
    for i in range(width):
        for j in range(height):
            r, g, b = im_pixels[i, j]
            im_pixels[i, j] = (r ^ key_chunks[c % chunk_count], g ^ key_chunks[(c + 1) % chunk_count], b ^ key_chunks[(c + 2) % chunk_count])
            c += 3

    bit_index = 0
    for i in range(width):
        for j in range(height):
            if bit_index < len(bek):
                r, g, b = im_pixels[i, j]
                r = (r & ~1) | int(bek[bit_index])
                bit_index += 1
                if bit_index < len(bek):
                    g = (g & ~1) | int(bek[bit_index])
                    bit_index += 1
                if bit_index < len(bek):
                    b = (b & ~1) | int(bek[bit_index])
                    bit_index += 1
                im_pixels[i, j] = (r, g, b)
            if bit_index >= len(bek):
                break
    random.seed(key)
    for _ in range(width * height // 2):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        im_pixels[x1, y1], im_pixels[x2, y2] = im_pixels[x2, y2], im_pixels[x1, y1]

    return image

def decrypt_image(image, key):
    im_pixels = image.load()
    width, height = image.size

    random.seed(key)
    swaps = []
    for _ in range(width * height // 2):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        swaps.append((x1, y1, x2, y2))
    for x1, y1, x2, y2 in reversed(swaps):
        im_pixels[x1, y1], im_pixels[x2, y2] = im_pixels[x2, y2], im_pixels[x1, y1]

    bek = ''
    for i in range(width):
        for j in range(height):
            if len(bek) < 512:
                r, g, b = im_pixels[i, j]
                bek += str(r & 1)
                if len(bek) < 512:
                    bek += str(g & 1)
                if len(bek) < 512:
                    bek += str(b & 1)
            if len(bek) >= 512:
                break

    ek = int(bek, 2)

    chunk_size = 8
    key_chunks = [int(bek[i:i + chunk_size], 2) % 256 for i in range(0, len(bek), chunk_size)]
    chunk_count = len(key_chunks)

    c = 0
    for i in range(width):
        for j in range(height):
            r, g, b = im_pixels[i, j]
            im_pixels[i, j] = (r ^ key_chunks[c % chunk_count], g ^ key_chunks[(c + 1) % chunk_count], b ^ key_chunks[(c + 2) % chunk_count])
            c += 3

    for i in range(width):
        for j in range(height):
            r, g, b = im_pixels[i, j]
            im_pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    return image

def save_image(image, output_path):
    image.save(output_path)

def main():
    root = tk.Tk()
    root.title("Image Encryption/Decryption")
    root.geometry("400x350")

    def browse_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            image_path_entry.delete(0, tk.END)
            image_path_entry.insert(0, file_path)

    def process_image():
        action = action_var.get()
        key = key_entry.get()
        image_path = image_path_entry.get()

        if not key:
            print("Invalid key")
            return
        transformed_key = ''.join(str(ord(char)) if not char.isdigit() else char for char in key)

        # Hash the transformed key to a fixed length integer
        hashed_key = hashlib.sha256(transformed_key.encode()).hexdigest()
        key = int(hashed_key, 16) % (10**16)  # Reduce the key to a manageable size

        if not image_path:
            print("No file selected.")
            return

        image = load_image(image_path)
        if not check_image_size(image, key):
            print("Image is too small to embed the key.")
            return

        if action == 'Encrypt':
            encrypted_image = encrypt_image(image, key)
            output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if output_path:
                save_image(encrypted_image, output_path)
                print(f"Encrypted image saved at {output_path}")
            else:
                print("No save location selected.")
        elif action == 'Decrypt':
            decrypted_image = decrypt_image(image, key)
            output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if output_path:
                save_image(decrypted_image, output_path)
                print(f"Decrypted image saved at {output_path}")
            else:
                print("No save location selected.")

    action_var = tk.StringVar(value="Encrypt")
    action_label = tk.Label(root, text="Select Action:")
    action_label.pack(pady=10)
    action_frame = tk.Frame(root)
    action_frame.pack(pady=10)
    encrypt_radio = tk.Radiobutton(action_frame, text="Encrypt", variable=action_var, value="Encrypt")
    encrypt_radio.pack(side=tk.LEFT, padx=5)
    decrypt_radio = tk.Radiobutton(action_frame, text="Decrypt", variable=action_var, value="Decrypt")
    decrypt_radio.pack(side=tk.LEFT, padx=5)

    image_path_label = tk.Label(root, text="Image Path:")
    image_path_label.pack(pady=10)
    image_path_frame = tk.Frame(root)
    image_path_frame.pack(pady=10)
    image_path_entry = tk.Entry(image_path_frame, width=30)
    image_path_entry.pack(side=tk.LEFT, padx=5)
    browse_button = tk.Button(image_path_frame, text="Browse", command=browse_image)
    browse_button.pack(side=tk.LEFT, padx=5)

    key_label = tk.Label(root, text="Enter Key (integer):")
    key_label.pack(pady=10)
    key_entry = tk.Entry(root)
    key_entry.pack(pady=10)

    process_button = tk.Button(root, text="Process Image", command=process_image)
    process_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
