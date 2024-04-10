import tkinter as tk
class BaseFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.app = parent
        self.init_ui()

    def init_ui(self):
        pass  