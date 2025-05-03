# image64 – Base64 Image Encoder/Decoder Utility

A simple command-line tool for encoding images to Base64 and decoding Base64 strings back to images. Built in Python.

## 📦 Features

- Encode an image into a Base64 `.txt` file.
- Decode a Base64 `.txt` file back into the original image.
- Usable from any terminal on Linux.

---

## 🚀 Installation (Linux)

### 1. Clone or download the script

```bash
git clone https://github.com/gil7788/image-base64-encoder.git
cd image-base64-encoder
```

---
### 2. Make the script executable
```bash
chmod +x image64.py
```

---

### 3. Move it to a directory in your `$PATH`

To make the command available globally:

```bash
sudo cp image64.py /usr/local/bin/image64
```

---

### ✅ Now you can run it from anywhere using:

```bash
image64 encode path/to/image.png
image64 decode path/to/image.txt output_image.png
```

---

## 🧪 Usage

### Encode an image

```bash
image64 encode cat.jpg cat.txt
```

➡️ Creates a `cat.txt` file in the same directory with the Base64 string.

---

### Decode an image

```bash
image64 decode cat.txt cat_restored.jpg
```

➡️ Reconstructs the image from the Base64 text file.

---

## 🛠 Dependencies

- Python 3.x (usually pre-installed on Linux)

Check your version:
```bash
python3 --version
```

---

## 📄 License

MIT – free to use, modify, and distribute.
