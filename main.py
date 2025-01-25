import secrets
import string
import qrcode
import tkinter as tk
from PIL import Image, ImageTk

def generate_wifi_password(length=63):
    chars = string.ascii_letters + string.digits + "@#$%&*()-+=[]{}|:,."
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase), 
        secrets.choice(string.digits),
        secrets.choice("@#$%&*()-+=[]{}|:,.")
    ]
    password.extend(secrets.choice(chars) for _ in range(length - 4))
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def display_qr():
    num_iterations = secrets.randbelow(11) + 7
    password = None
    
    for _ in range(num_iterations):
        password = generate_wifi_password()
    
    print(f"Generated Password: {password}")
    qr = qrcode.make(password)
    
    window = tk.Tk()
    window.title("Password QR Code")
    
    qr_photo = ImageTk.PhotoImage(qr)
    label = tk.Label(window, image=qr_photo)
    label.image = qr_photo
    label.pack(padx=20, pady=20)
    
    window.mainloop()

if __name__ == "__main__":
    display_qr()