from PIL import Image 

def text_to_binary(text):
    binary_message = ''.join(format(ord(char), '08b') for char in text)
    return binary_message

def binary_to_text(binary_message):
    text = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    return text

def encode_image(img, message):
    binary_message = text_to_binary(message)
    data_index = 0

    img = img.convert('RGB')
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Encode the message in the least significant bit of each color channel
            if data_index < len(binary_message):
                pixels[x, y] = (r & 0b11111110 | int(binary_message[data_index]), g, b)
                data_index += 1

    return img

def decode_image(img):
    binary_message = ''
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, _, _ = pixels[x, y]
            binary_message += str(r & 1)

    return binary_to_text(binary_message)

def main():
    #encoding
    original_image =Image.open("Butterfly.jpg")
    secret_message =input("ENTER YOUR MESSAGE:")
    original_image.show()
    encoded_image = encode_image(original_image, secret_message)
    encoded_image.save("encoded_image.png")

    #decoding
    encoded_image = Image.open("encoded_image.png")
    decoded_message = decode_image(encoded_image)
    print("Decoded Message:", decoded_message)

if __name__ == "__main__":
    main()
