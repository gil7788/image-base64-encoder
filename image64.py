#!/usr/bin/env python3
import base64
import sys
from pathlib import Path

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def decode_base64_to_image(base64_string, output_path):
    with open(output_path, "wb") as image_output:
        image_output.write(base64.b64decode(base64_string))

def main():
    if len(sys.argv) != 4:
        print("Usage:")
        print("  Encode: image64 encode <input_image_path> <output_text_path>")
        print("  Decode: image64 decode <input_text_path> <output_image_path>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    if mode == "encode":
        try:
            encoded = encode_image_to_base64(input_path)
            with open(output_path, "w") as f:
                f.write(encoded)
            print(f"✅ Image encoded and saved to: {output_path}")
        except Exception as e:
            print(f"❌ Encoding failed: {e}")
            sys.exit(1)

    elif mode == "decode":
        try:
            with open(input_path, "r") as f:
                base64_string = f.read()
            decode_base64_to_image(base64_string, output_path)
            print(f"✅ Image decoded and saved to: {output_path}")
        except Exception as e:
            print(f"❌ Decoding failed: {e}")
            sys.exit(1)

    else:
        print("❌ Invalid mode. Use 'encode' or 'decode'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
