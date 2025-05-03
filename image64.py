import base64
import sys
from pathlib import Path


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded


def decode_base64_to_image(base64_string, output_path):
    with open(output_path, "wb") as image_output:
        image_output.write(base64.b64decode(base64_string))


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  Encode: python image64.py encode <image_path>")
        print("  Decode: python image64.py decode <base64_file> <output_image_path>")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "encode":
        image_path = sys.argv[2]
        encoded = encode_image_to_base64(image_path)

        # Save to file
        output_file = Path(image_path).with_suffix(".txt")
        with open(output_file, "w") as f:
            f.write(encoded)

        print("Base64 encoded string saved to:", output_file)

    elif mode == "decode":
        if len(sys.argv) < 4:
            print("Please provide base64 text file and output image path.")
            sys.exit(1)

        base64_file = sys.argv[2]
        output_path = sys.argv[3]

        with open(base64_file, "r") as f:
            base64_string = f.read()
        decode_base64_to_image(base64_string, output_path)
        print(f"Image saved to {output_path}")

    else:
        print("Invalid mode. Use 'encode' or 'decode'.")


if __name__ == "__main__":
    main()
