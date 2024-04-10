import tkinter as tk
#from frames.password_management_frame import PasswordManagementFrame
from frames.base_frame import BaseFrame


class ListSitesFrame(BaseFrame):
    def init_ui(self):
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(self, yscrollcommand=scrollbar.set)
        for site in sorted(self.app.password_store.keys()):
            listbox.insert(tk.END, site)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

        tk.Button(self, text="Back", command=lambda: self.app.switch_to_password_management()).pack()