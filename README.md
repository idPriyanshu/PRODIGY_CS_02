# 🚀 PRODIGY_CS_02

## 📝 Task Overview

**Task:** Pixel Manipulation for Image Encryption  
**Description:** Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.  
**Status:** ✅ Completed

## Features:
- **Encrypt**: Embed a secret key into an image. 🔒
- **Decrypt**: Retrieve the original image by using the correct secret key. 🔓
- **Random Number Embedding**: A random number is embedded in the image pixels using XOR operations and the least significant bits (LSB). 💡
- **Pixel Swapping**: Random pixel swapping further obfuscates the image, adding another layer of security. 🔄
- **Random Key Generation**: The encryption key is generated using a secure random number generator and is then embedded into the image in binary form. 🔑

---

## Core Concepts:
### Key Variables:
- **`ek` (Encryption Key)**: 
   - `ek` is a secret, randomly generated number used as the core encryption key. It is produced using `secrets.randbelow()` and is multiplied by a user-provided key for additional security. 🛠️
   - **Purpose**: `ek` drives the encryption and is embedded in the image to allow for decryption. Without the correct `ek`, the decryption will fail. 🚫
   - **Size**: The size of `ek` is large (128 bits), ensuring strong randomness. ⚙️

- **`bek` (Binary Encryption Key)**:
   - `bek` is the binary representation of `ek` that is embedded into the image during encryption. It is a 512-bit string formed from the binary form of `ek`. 💾
   - **Purpose**: `bek` is used to modify the pixel values in the image. Each chunk of `bek` influences a set of RGB values of the image pixels. 🎨

### 🔒 Encryption Process:
1. **Initial Pixel Modification**: The RGB values of each pixel are modified by adding the key value to each color channel. This serves as a simple encryption step. 🎨
2. **Embedding `bek` into Pixels**: 
   - The `bek` (binary form of `ek`) is embedded into the least significant bits (LSB) of the image’s pixel values. 💾
   - This process is done bit by bit for each pixel, modifying the LSBs of the RGB components. 🖼️
3. **XOR with Chunks**: 
   - The `bek` is divided into 8-bit chunks (1 byte), and each chunk is used to XOR the RGB values of the image pixels in a round-robin fashion. This step makes the encryption stronger by mixing the image pixel data with the encryption key. 🔀
4. **Random Pixel Swapping**: 
   - After embedding the `bek` into the pixels, the image undergoes random pixel swaps using a seed based on the key. This ensures that even if an attacker has access to the encrypted image, it's harder to decipher without the key. 🔄

### 🔓 Decryption Process:
1. **Reverse Pixel Swapping**: The pixel swaps applied during encryption are reversed using the same key to restore the image to its previous state. 🔄
2. **Extract `bek` from Image**: 
   - The least significant bits (LSB) of the image pixels are read to reconstruct the `bek` binary string. 📈
3. **Reconstruct `ek`**: 
   - The `bek` is converted back into the original `ek` value by interpreting the binary string as a large integer. 🧮
4. **XOR to Restore Original Pixel Values**: 
   - The pixel values are XORed with the chunks of `bek` to restore the original image, reversing the modifications made during encryption. ⚙️
5. **Final Pixel Adjustment**: 
   - The pixel values are then adjusted by subtracting the original key, undoing the initial encryption step and returning the image to its unencrypted form. 🎨

---
## 📦 Dependencies

This project requires the following Python modules:
- **Pillow (PIL)**: For image processing.
- **tkinter**: For creating the graphical user interface (GUI).
- **hashlib**: For hashing the encryption key.
- **random**: For generating the secret random number (`ek`).

---
## 📥 Installation Instructions

### 1. Install Python
Ensure Python 3.6 or later is installed. Download it from the [official Python website](https://www.python.org/downloads/).

### 2. Install Required Modules

#### For `Pillow`:
- Open the terminal and run:
  ```bash
  pip install pillow

#### For `tkinter`:
- Open the terminal and run:
  ```bash
  sudo apt-get install python3-tk

## ▶️ Usage Instructions
### 1. 📂 Clone the repository:
     ```bash
     git clone https://github.com/idPriyanshu/PRODIGY_CS_02.git

### 2. 📂 Navigate to the project directory:
     ```bash
     cd PRODIGY_CS_02

### 3. ▶️ Run the program:
      ```bash
      python Image_Encryption.py### 4. Run the Script: 
   - Execute the script to open the GUI. 🖥️

### 5. Select Action: 
   - Choose either **Encrypt** or **Decrypt**. 🔐🔓

### 6. Browse for Image: 
   - Click the **Browse** button to select an image file (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`) from your system. 📂

### 7. Enter Key: 
   - Enter an integer key. This key will be used to generate a random encryption key (`ek`), which is embedded into the image for encryption. 🔑

### 8. Process Image: 
   - Click **Process Image** to encrypt or decrypt the selected image. The processed image will be saved in the chosen location. ⚙️

### 9. Save Processed Image: 
   - After the image is processed, you will be prompted to save the resulting image. 💾

---

## Example:

- **Encryption**: 
   - **Input**: A secret image and an integer key. 
   - **Output**: The encrypted image with the secret key embedded into the pixels. 🔒🖼️

- **Decryption**: 
   - **Input**: An encrypted image and the correct secret key. 
   - **Output**: The original image restored. 🔓🖼️

---

## Code Breakdown:
- **Image Processing**: The image is loaded and converted into RGB format for pixel manipulation. 🖼️🔄
- **Key Generation**: The secret key is hashed to generate a fixed-length integer that is used to derive the `ek`. 🔑🧮
- **Pixel Encryption/Decryption**: The image pixels are modified using XOR and the least significant bits to embed and later extract the encryption key (`ek`). 🔀

## Security Considerations:
- **Key Management**: Ensure that the secret key (`ek`) is kept safe. Without the key, it will be impossible to decrypt the image. 🔐
- **Randomness**: The use of a secure random number generator (`secrets.randbelow()`) ensures that the encryption key is highly unpredictable. 🔑

## License:
This project is open-source and can be freely used for educational purposes. 📜

---

### Final Notes:
This tool demonstrates a simple yet secure image encryption/decryption technique using random number generation, pixel manipulation, and XOR operations. The embedding of the secret key into the image pixels ensures that the encryption is strong and secure, while also being difficult to reverse without the correct key. 🔒🔑
