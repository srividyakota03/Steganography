# Steganography
This steganography project in Python hides a secret message within an image by modifying the least significant bits (LSB) of pixel values, preserving the image's appearance. Using the Pillow library, it encodes text by converting it to binary and embedding it in pixel data, with bitwise operations to encode and decode hidden messages accurately.
Skills: Python Programming, Data Encoding/Decoding, Image Processing.
Tools: Python, Pillow (PIL), Text Editor/IDE

---

## Features
- **Message Encoding**: Hide text messages in images using the LSB method.
- **Message Decoding**: Retrieve hidden messages from encoded images.
- **Image Processing**: Supports common formats like JPEG and PNG.
- **User-Friendly**: Simple implementation for learning and experimentation.

---

## How It Works
1. The text message is converted into binary.
2. The binary data is embedded in the least significant bits of the red channel of each pixel.
3. The encoded image can be saved and shared.
4. Hidden messages are extracted by reading the least significant bits from the image.

---

## Prerequisites
- Python 3.x
- [Pillow](https://pillow.readthedocs.io/en/stable/) library for image handling.

Install the Pillow library:
```bash
pip install Pillow
```
---
## Encoded & Decoded Images
![encoded_image](https://github.com/user-attachments/assets/d4d033a7-7233-44c3-9930-85a2b8568db7)
![Butterfly](https://github.com/user-attachments/assets/2c715549-8626-41ec-b95f-efa40fa85d86)
