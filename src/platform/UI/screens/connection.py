import customtkinter as ctk # pyright: ignore[reportMissingImports]


def load_connection_screen(parent_frame):
    # --- TITRE DE L'ONGLET ---
    title_label = ctk.CTkLabel(parent_frame, text="TAB : CONNECTION", font=("Arial", 14, "bold"), text_color="gray")
    title_label.pack(pady=(10, 5), padx=20, anchor="nw")

    # --- 1. SECTION CONFIGURATION ---
    config_frame = ctk.CTkFrame(parent_frame, fg_color="#1e1e1e", corner_radius=10)
    config_frame.pack(fill="x", padx=20, pady=10)

    ctk.CTkLabel(config_frame, text="CONFIGURATION", font=("Arial", 12, "bold")).pack(anchor="nw", padx=15, pady=5)
    
    # Ligne Username
    user_row = ctk.CTkFrame(config_frame, fg_color="transparent")
    user_row.pack(fill="x", padx=15, pady=5)
    ctk.CTkLabel(user_row, text="Username :").pack(side="left")
    username_entry = ctk.CTkEntry(user_row, placeholder_text="Gérard_BIT", width=250, fg_color="#2b2b2b", border_color="#3f3f3f")
    username_entry.pack(side="left", padx=10)

    # Bouton d'action Connect (le grand bouton bleu)
    connect_btn = ctk.CTkButton(config_frame, text="Action : Connect", fg_color="#158aff", hover_color="#1a73e8", height=35)
    connect_btn.pack(fill="x", padx=15, pady=15)

    # --- 2. SECTION AVAILABLE USERS ---
    users_frame = ctk.CTkFrame(parent_frame, fg_color="#1e1e1e", corner_radius=10)
    users_frame.pack(fill="both", expand=True, padx=20, pady=10)

    ctk.CTkLabel(users_frame, text="AVAILABLE USERS (Local Network)", font=("Arial", 12, "bold")).pack(anchor="nw", padx=15, pady=5)

    # Liste scrollable pour les utilisateurs
    user_list_canvas = ctk.CTkScrollableFrame(users_frame, fg_color="transparent")
    user_list_canvas.pack(fill="both", expand=True, padx=5, pady=5)

    # Exemple d'ajout d'un utilisateur (à mettre dans une boucle plus tard)
    add_user_row(user_list_canvas, "Madeleine_Y", "Pending acceptance...", "orange")
    add_user_row(user_list_canvas, "Papa_Z", "Connected", "green")
    add_user_row(user_list_canvas, "Admin_BIT", "Available", "green")

    #en gros ici c'est: ---  SECTION ACTIVITY LOGS ---
    logs_frame = ctk.CTkFrame(parent_frame, fg_color="#1e1e1e", corner_radius=10)
    logs_frame.pack(fill="x", padx=20, pady=(10, 20))

    ctk.CTkLabel(logs_frame, text="ACTIVITY LOGS", font=("Arial", 12, "bold")).pack(anchor="nw", padx=15, pady=5)

    # La zone de texte pour les logs (en lecture seule)
    activity_log_box = ctk.CTkTextbox(logs_frame, height=100, fg_color="#141414", 
                                      text_color="#a0a0a0", font=("Consolas", 11),
                                      border_width=1, border_color="#2b2b2b")
    activity_log_box.pack(fill="x", padx=15, pady=(0, 15))
    
    # On désactive l'édition pour que l'utilisateur ne puisse pas écrire dedans
    activity_log_box.configure(state="disabled")

    # Petit test : ajoutons un log par défaut
    add_log_entry(activity_log_box, "System initialized. Waiting for connection...")

# Fonction utilitaire pour créer une ligne d'utilisateur
def add_user_row(parent, name, status, color):
    row = ctk.CTkFrame(parent, fg_color="transparent")
    row.pack(fill="x", pady=2)
    
    # Icône (on peut mettre une image ici plus tard)
    icon = ctk.CTkLabel(row, text="👤", font=("Arial", 16))
    icon.pack(side="left", padx=10)
    
    ctk.CTkLabel(row, text=name).pack(side="left")
    
    # Indicateur de statut (le petit point)
    status_label = ctk.CTkLabel(row, text=f"● {status}", text_color=color, font=("Arial", 11))
    status_label.pack(side="right", padx=10)


def add_log_entry(textbox, message):
    # On doit temporairement activer la box pour écrire dedans
    textbox.configure(state="normal")
    
    # On ajoute le message avec un saut de ligne
    textbox.insert("end", f"> {message}\n")
    
    # On scrolle automatiquement vers le bas pour voir le dernier log
    textbox.see("end")
    
    # On verrouille à nouveau
    textbox.configure(state="disabled")