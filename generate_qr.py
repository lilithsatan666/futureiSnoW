import qrcode

# Data for the QR code
qr_data = "Iffi-E 240612"

# Generate QR code
img = qrcode.make(qr_data)

# Save as PNG
img.save("/workspaces/futureiSnoW/qr_code_Iffi-E_240612.png")
print("QR code image saved as qr_code_Iffi-E_240612.png")
