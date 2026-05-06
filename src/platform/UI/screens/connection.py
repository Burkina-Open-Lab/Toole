import customtkinter as ctk

class ConnectionScreen(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.build_ui()
        
    def build_ui(self):
        self.user_name = ctk.CTkLabel(self,text="Nom:..")
        self.user_name.pack(pady=10)

        self.connect_button = ctk.CTkButton(self, text="Connexion", command=self.on_connect)
        self.connect_button.pack(pady=10)

        self.users_list = ctk.CTkTextbox(self, height=150)
        self.users_list.pack(pady=10)

        self.logs = ctk.CTkTextbox(self, height=100)
        self.logs.pack(pady=10)

    def on_connect(self):
        # username = self.user_name.get()

        # # TODO: connecter via backend
        # self.add_log(f"Connexion de {username}")
        pass
    
    def add_log(self, message):
        # self.logs.insert("end", message + "\n")
        pass

def update_users(self, users):
    # self.users_list.delete("0.0", "end")

    # for user, status in users:
    #     self.users_list.insert("end", f"{user} - {status}\n")
    pass

def get_users(self):
    # return [
    #     ("Papa_Z", "Connecté"),
    #     ("Madeleine_Y", "En attente")
    # ]
    # self.update_users(self.controller.get_users())
    pass