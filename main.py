import tkinter as tk
from app import encrypt, decrypt

def encrypt_text():
    plaintext = entry_plaintext.get()
    key = entry_key.get()

    cipher = encrypt(plaintext, key)
    label_result.config(text="Cipher: " + cipher)

def decrypt_text():
    cipher = entry_cipher.get()
    key = entry_key.get()

    plaintext = decrypt(cipher, key)
    label_result.config(text="Decrypted Text: " + plaintext)

def toggle_mode():
    mode = button_mode.cget("text")
    if mode == "Encrypt Mode":
        button_mode.config(text="Decrypt Mode")
        entry_plaintext.config(state="normal")
        entry_cipher.config(state="disabled")
        button_action.config(text="Encrypt", command=encrypt_text)
        label_result.config(text="")
    else:
        button_mode.config(text="Encrypt Mode")
        entry_plaintext.config(state="disabled")
        entry_cipher.config(state="normal")
        button_action.config(text="Decrypt", command=decrypt_text)
        label_result.config(text="")
    


# Create the main window
window = tk.Tk()
window.title("Columnar Cipher")

# Set the window size
window.geometry("500x300")  # Set the width and height of the window

# Create labels and entry fields for plaintext, key, and cipher
label_plaintext = tk.Label(window, text="Enter the plaintext:")
label_plaintext.pack()

entry_plaintext = tk.Entry(window, width=50)  # Set the width of the entry field
entry_plaintext.pack()

label_key = tk.Label(window, text="Enter the key:")
label_key.pack()

entry_key = tk.Entry(window, width=50)  # Set the width of the entry field
entry_key.pack()

label_cipher = tk.Label(window, text="Enter the cipher:")
label_cipher.pack()

entry_cipher = tk.Entry(window, width=50)  # Set the width of the entry field
entry_cipher.pack()

# Create buttons for encryption and decryption
button_action = tk.Button(window, text="Encrypt", command=encrypt_text)
button_action.pack()

# Create a button to toggle between encryption and decryption modes
button_mode = tk.Button(window, text="Decrypt Mode", command=toggle_mode)
button_mode.pack()

# Create a label to display the result
label_result = tk.Label(window, text="")
label_result.pack()

# Start the main event loop
window.mainloop()
