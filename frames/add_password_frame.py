import tkinter as tk
from tkinter import messagebox
from crypto_utils import encrypt_message  
#from frames.password_management_frame import PasswordManagementFrame
from frames.base_frame import BaseFrame

class AddPasswordFrame(BaseFrame):
    def init_ui(self):
        tk.Label(self, text="Enter the site/app name:").pack()
        self.site_entry = tk.Entry(self)
        self.site_entry.pack()

        tk.Label(self, text="Enter the password:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Save", command=self.save_new_password).pack()

    def save_new_password(self):
        site = self.site_entry.get()
        password = self.password_entry.get()
        if site and password:
            self.app.password_store[site] = encrypt_message(password, self.app.key).decode()
            self.app.save_password_store()
            messagebox.showinfo("Success", "Password added successfully.")
            self.app.switch_to_password_management()
        else:
            messagebox.showerror("Error", "Site and Password cannot be empty.")
