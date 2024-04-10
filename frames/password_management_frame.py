import tkinter as tk
from frames.base_frame import BaseFrame
from frames.add_password_frame import AddPasswordFrame
from frames.retrieve_password_frame import RetrievePasswordFrame
from frames.list_sites_frame import ListSitesFrame


class PasswordManagementFrame(BaseFrame):
    def init_ui(self):
        tk.Button(self, text="Add Password", command=self.add_password_interface).pack()
        tk.Button(self, text="Retrieve Password", command=self.retrieve_password_interface).pack()
        tk.Button(self, text="List All Sites/Apps", command=self.list_sites_interface).pack()

    def add_password_interface(self):
        self.app.switch_frame(AddPasswordFrame)

    def retrieve_password_interface(self):
        self.app.switch_frame(RetrievePasswordFrame)

    def list_sites_interface(self):
        self.app.switch_frame(ListSitesFrame)