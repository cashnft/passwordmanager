import tkinter as tk
from tkinter import Listbox, Scrollbar, messagebox, Label, Entry, Button
from cryptography.fernet import Fernet
import json
import os


def load_key():
   
    return open("secret.key", "rb").read()

def encrypt_message(message, key):
    
  
    f = Fernet(key)
    encoded_message = message.encode()
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
   
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

class PasswordManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Password Manager')
        self.geometry('400x300')

        if not os.path.exists("secret.key"):
            self.generate_key()
        self.key = load_key()

        self.passwords_file = "passwords.enc"
        self.password_store = self.load_password_store()

        
        if not os.path.exists("master_password.enc"):
            self.initialize_master_password_setup_ui()  
        else:
            self.initialize_login_ui()
        
       
    def initialize_login_ui(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        Label(self.main_frame, text="Enter Master Password:").pack()
        
        self.login_master_password_entry = Entry(self.main_frame, show="*")
        self.login_master_password_entry.pack()
        
        Button(self.main_frame, text="Submit", command=self.verify_master_password).pack()

    def initialize_ui(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.create_login_interface()
    def generate_key(self):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    def switch_frame(self, frame_function):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        frame_function()

    def create_login_interface(self):
        Label(self.main_frame, text="Enter Master Password:").pack()
        
        self.master_password_entry = Entry(self.main_frame, show="*")
        self.master_password_entry.pack()
        
        Button(self.main_frame, text="Submit", command=self.verify_master_password).pack()

    def create_password_management_interface(self):
        Button(self.main_frame, text="Add Password", command=lambda: self.switch_frame(self.add_password_interface)).pack()
        Button(self.main_frame, text="Retrieve Password", command=lambda: self.switch_frame(self.retrieve_password_interface)).pack()
        Button(self.main_frame, text="List All Sites/Apps", command=self.list_sites_interface).pack()


    def add_password_interface(self):
        Label(self.main_frame, text="Enter the site/app name:").pack()
        
        self.site_entry = Entry(self.main_frame)
        self.site_entry.pack()

        Label(self.main_frame, text="Enter the password:").pack()
        
        self.password_entry = Entry(self.main_frame, show="*")
        self.password_entry.pack()

        Button(self.main_frame, text="Save", command=self.save_new_password).pack()

    def save_new_password(self):
        site = self.site_entry.get()
        password = self.password_entry.get()
        if site and password:
            self.password_store[site] = encrypt_message(password, self.key).decode()
            self.save_password_store()
            messagebox.showinfo("Success", "Password added successfully.")
            self.switch_frame(self.create_password_management_interface)
        else:
            messagebox.showerror("Error", "Site and Password cannot be empty.")

    def retrieve_password_interface(self):
        Label(self.main_frame, text="Enter the site/app name:").pack()
        
        self.retrieve_site_entry = Entry(self.main_frame)
        self.retrieve_site_entry.pack()

        Button(self.main_frame, text="Retrieve", command=self.retrieve_password).pack()

    def retrieve_password(self):
        site = self.retrieve_site_entry.get()
        if site in self.password_store:
            password = decrypt_message(self.password_store[site].encode(), self.key)
            messagebox.showinfo("Password", f"Password for {site}: {password}")
        else:
            messagebox.showerror("Error", "No password found for this site.")
        self.switch_frame(self.create_password_management_interface)

    def list_sites_interface(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        scrollbar = Scrollbar(self.main_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = Listbox(self.main_frame, yscrollcommand=scrollbar.set)
        for site in sorted(self.password_store.keys()):
            listbox.insert(tk.END, site)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

        
        Button(self.main_frame, text="Back", command=lambda: self.switch_frame(self.create_password_management_interface)).pack()


    def verify_master_password(self):
        entered_password = self.master_password_entry.get()
        try:
            with open("master_password.enc", "rb") as file:
                encrypted_master_password = file.read()
                if entered_password == decrypt_message(encrypted_master_password, self.key):
                    self.switch_frame(self.create_password_management_interface)
                else:
                    messagebox.showerror("Error", "Incorrect master password!")
        except FileNotFoundError:
            messagebox.showerror("Error", "Master password file not found.")
    def initialize_master_password_setup_ui(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        Label(self.main_frame, text="Set Master Password:").pack()
        
        self.master_password_entry = Entry(self.main_frame, show="*")
        self.master_password_entry.pack()

        Label(self.main_frame, text="Confirm Master Password:").pack()

        self.confirm_master_password_entry = Entry(self.main_frame, show="*")
        self.confirm_master_password_entry.pack()

        Button(self.main_frame, text="Submit", command=self.set_master_password).pack()

    def set_master_password(self):
        password = self.master_password_entry.get()
        confirm_password = self.confirm_master_password_entry.get()
     

        if password and confirm_password and password == confirm_password:
            encrypted_master_password = encrypt_message(password, self.key)
            with open("master_password.enc", "wb") as file:
                file.write(encrypted_master_password)
            messagebox.showinfo("Success", "Master password set successfully.")
            self.switch_frame(self.initialize_ui)
        else:
            messagebox.showerror("Error", "Passwords do not match or are empty. Please try again.")

    def load_password_store(self):
        if os.path.exists(self.passwords_file):
            with open(self.passwords_file, 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = decrypt_message(encrypted_data, self.key)
                return json.loads(decrypted_data)
        else:
            return {}

    def save_password_store(self):
        encrypted_data = encrypt_message(json.dumps(self.password_store), self.key)
        with open(self.passwords_file, 'wb') as file:
            file.write(encrypted_data)

if __name__ == "__main__":
    app = PasswordManagerApp()
    app.mainloop()
