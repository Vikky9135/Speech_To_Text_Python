import qrcode

# Replace this with your LinkedIn profile URL
linkedin_url = "https://www.linkedin.com/in/vikram-r-02264523b/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border
)
qr.add_data(linkedin_url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code to a file
img.save("linkedin_qr_code.png")
print("QR code generated and saved as 'linkedin_qr_code.png'.")
