import tkinter as tk
from tkinter import messagebox
from crypto_utils import derive_key  
from frames.password_management_frame import PasswordManagementFrame
from frames.base_frame import BaseFrame


class LoginFrame(BaseFrame):
    def init_ui(self):
        tk.Label(self, text="Enter Master Password:").pack()
        
        self.master_password_entry = tk.Entry(self, show="*")
        self.master_password_entry.pack()

        tk.Button(self, text="Submit", command=self.verify_master_password).pack()

    def verify_master_password(self):
        entered_password = self.master_password_entry.get()
        try:
            with open(self.app.salt_file, "rb") as file:
                salt = file.read()
            self.app.key = derive_key(entered_password, salt)
            self.app.password_store = self.app.load_password_store()
            if not self.app.password_store:
                messagebox.showerror("Error", "Failed to decrypt password store.")
                return
            self.app.switch_frame(PasswordManagementFrame)
        except FileNotFoundError:
            messagebox.showerror("Error", "Necessary files not found.")
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: {}".format(str(e)))