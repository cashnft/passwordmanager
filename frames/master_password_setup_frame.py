import tkinter as tk
from tkinter import messagebox
import json
from crypto_utils import derive_key, generate_salt, encrypt_message  
from frames.password_management_frame import PasswordManagementFrame
from frames.base_frame import BaseFrame

class MasterPasswordSetupFrame(BaseFrame):
    def init_ui(self):
        tk.Label(self, text="Set Master Password:").pack()
        
        self.master_password_entry = tk.Entry(self, show="*")
        self.master_password_entry.pack()

        tk.Label(self, text="Confirm Master Password:").pack()

        self.confirm_master_password_entry = tk.Entry(self, show="*")
        self.confirm_master_password_entry.pack()

        tk.Button(self, text="Submit", command=self.set_master_password).pack()

    def set_master_password(self):
        password = self.master_password_entry.get()
        confirm_password = self.confirm_master_password_entry.get()

        if password and confirm_password and password == confirm_password:
            salt = generate_salt()
            with open(self.app.salt_file, "wb") as file:
                file.write(salt)
            
            self.app.key = derive_key(password, salt)
            
            initial_password_store = {}
            encrypted_data = encrypt_message(json.dumps(initial_password_store), self.app.key)
            with open(self.app.passwords_file, 'wb') as file:
                file.write(encrypted_data)
            
            messagebox.showinfo("Success", "Master password set successfully.")
            self.app.switch_frame(PasswordManagementFrame)
        else:
            messagebox.showerror("Error", "Passwords do not match or are empty.")