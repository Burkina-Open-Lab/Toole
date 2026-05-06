import customtkinter as ctk
from screens.connection import ConnectionScreen
from screens.transfer import TransferScreen
# from controller.controller import FakeController

class App(ctk.CTk):
    def __int__(self):
        super().__init()
        self.title("toole - Cluster Manager")
        self.geometry("900x600")

        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.navigation_fram = ctk.CTkFrame(self,corner_radius=0)
        self.navigation_fram.grid(row=0,column=0,sticky="nsew")

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0,sticky="nsew")

        self.show_screen(ConnectionScreen)

        def show_screen(self, screen_class):
            for child in self.container.winfo_children():
                child.destroy()

                new_screen = screen_class(self.container,controller=None)
                new_screen.pack(fill="both", expand=True)