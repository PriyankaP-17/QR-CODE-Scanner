import qrcode

def convert_to_qr(input_data, filename="generated_qr.png"):
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    # Add any data (text, link, number, file path, etc.)
    qr.add_data(str(input_data))
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"✅ QR Code saved as '{filename}'")

    # Optional: Show the image
    img.show()

# --- Example Usage ---
user_input = input("Enter anything to convert into a QR code: ")
convert_to_qr(user_input)
