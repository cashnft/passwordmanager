import tkinter as tk
from tkinter import messagebox
from crypto_utils import decrypt_message  

from frames.base_frame import BaseFrame

class RetrievePasswordFrame(BaseFrame):
    def init_ui(self):
        tk.Label(self, text="Enter the site/app name:").pack()
        self.site_entry = tk.Entry(self)
        self.site_entry.pack()
        tk.Button(self, text="Back", command=lambda: self.app.switch_to_password_management()).pack()

        tk.Button(self, text="Retrieve", command=self.retrieve_password).pack()

    def retrieve_password(self):
        site = self.site_entry.get()
        if site in self.app.password_store:
            encrypted_password = self.app.password_store[site].encode()
            
            password = decrypt_message(encrypted_password, self.app.key)
            messagebox.showinfo("Password", f"Password for {site}: {password}")
            
            self.app.switch_to_password_management()
            
        else:
            messagebox.showerror("Error", "No password found for this site.")