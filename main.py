from frames.login_frame import LoginFrame
from frames.master_password_setup_frame import MasterPasswordSetupFrame
from frames.password_management_frame import PasswordManagementFrame
import tkinter as tk
from tkinter import messagebox
import json
import os
from crypto_utils import encrypt_message, decrypt_message  

class PasswordManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Password Manager')
        self.geometry('400x300')
        self.salt_file = "salt.enc"
        self.passwords_file = "passwords.enc"
        self.key = None  
        self.password_store = {}

        if not os.path.exists(self.salt_file) or not os.path.exists(self.passwords_file):
            self.switch_frame(MasterPasswordSetupFrame)
        else:
            self.switch_frame(LoginFrame)
    def switch_to_master_password_setup(self):
        self.switch_frame(MasterPasswordSetupFrame)
    def switch_to_password_management(self):
     
        self.switch_frame(PasswordManagementFrame)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()

    def load_password_store(self):
        if os.path.exists(self.passwords_file):
            with open(self.passwords_file, 'rb') as file:
                encrypted_data = file.read()
                try:
                    decrypted_data = decrypt_message(encrypted_data, self.key)
                    return json.loads(decrypted_data)
                except Exception:
                    return {}  
        else:
            return {}

    def save_password_store(self):
        encrypted_data = encrypt_message(json.dumps(self.password_store), self.key)
        with open(self.passwords_file, 'wb') as file:
            file.write(encrypted_data)

if __name__ == "__main__":
    app = PasswordManagerApp()
    app.mainloop()