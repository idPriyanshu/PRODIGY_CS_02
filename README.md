# 🚀 PRODIGY_CS_02

## 📝 Task Overview

**Task:** Pixel Manipulation for Image Encryption  
**Description:** Develop a simple image encryption tool using pixel manipulation. Perform operations like swapping pixel values or applying basic mathematical transformations to encrypt and decrypt images.  
**Status:** ✅ Completed

---

## 🌟 Features

- **Encrypt & Decrypt Images**: Users can encrypt and decrypt images by applying transformations to pixel values. 🔒🔓
- **Random Key Embedding**: Embed a secret encryption key into the image pixels using XOR operations and least significant bit (LSB) manipulation. 💡
- **Pixel Swapping**: Random pixel swapping enhances security by further obfuscating the image. 🔄
- **User-Friendly GUI**: An intuitive graphical interface guides users through the encryption and decryption process. 🖥️

---

## 🛠️ How It Works

### Key Variables

- **`ek` (Encryption Key)**: 
  - A secret, randomly generated number used for encryption.
  - Generated using `secrets.randbelow()` and combined with a user-provided key for added security. 🔑
  - Embedded in the image, ensuring decryption is only possible with the correct key.

- **`bek` (Binary Encryption Key)**: 
  - Binary representation of `ek`, embedded into the LSBs of the image pixels. 💾

### 🔒 Encryption Process

1. **Initial Pixel Modification**: Add the encryption key value to each RGB component of the image pixels. 🎨
2. **Embed `bek`**: Insert the binary form of `ek` into the LSBs of the image pixels. 📥
3. **XOR Operation**: Apply XOR between `bek` chunks and pixel values to enhance security. 🔀
4. **Random Pixel Swapping**: Swap pixels randomly based on the key for further obfuscation. 🔄

### 🔓 Decryption Process

1. **Reverse Pixel Swapping**: Undo the pixel swaps using the key. 🔁
2. **Extract `bek`**: Reconstruct `bek` from the image’s pixel LSBs. 🧩
3. **Restore Pixel Values**: Reverse XOR operations and subtract the encryption key to retrieve the original image. 🎨

---

## 📦 Dependencies

- **Pillow**: For image processing.
- **tkinter**: For the graphical user interface (GUI).
- **hashlib**: For hashing the encryption key.
- **secrets**: For secure random number generation.

---

## 📥 Installation

1. **Install Python**: Ensure Python 3.6 or later is installed. Download it from [python.org](https://www.python.org/downloads/).
2. **Install Dependencies**:
   ```bash
   pip install pillow
   sudo apt-get install python3-tk
   ```

---

## ▶️ Usage Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/idPriyanshu/PRODIGY_CS_02.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd PRODIGY_CS_02
   ```

3. **Run the Program**:
   ```bash
   python Image_Encryption.py
   ```

4. **Select Action**: Choose either **Encrypt** or **Decrypt** in the GUI. 🔐🔓
5. **Browse Image**: Select an image file (`.png`, `.jpg`, etc.) from your system. 📂
6. **Enter Key**: Provide an integer key for encryption or decryption. 🔑
7. **Process Image**: Click the button to encrypt or decrypt the image. Save the output file. 💾

---

## 🔒 Example

- **Encryption**:
  - Input: Original image and a key.
  - Output: Encrypted image with the embedded key.

- **Decryption**:
  - Input: Encrypted image and the correct key.
  - Output: Original image restored.

---

## 🔐 Security Considerations

- **Key Confidentiality**: Ensure the encryption key is securely stored. Without it, decryption is impossible. 🔑
- **Strong Randomness**: The use of `secrets.randbelow()` ensures high unpredictability in key generation. 💡

---

## 📜 License

This project is open-source and can be used for educational purposes. 📖

---

## 👨‍💻 Developer

Developed by [@idPriyanshu](https://www.github.com/idPriyanshu) during the **Prodigy Cyber Security Internship Program**.  

---

