from tkinter import filedialog
import customtkinter as ctk        # pyright: ignore[reportMissingImports] # Pour l'interface moderne
from tkinter import filedialog     # UNIQUEMENT pour la boîte de sélection
import os


selected_items = [] # Ma liste globale pour stocker les chemins


def select_files(display_container): # On ajoute l'endroit où on veut afficher
    paths = filedialog.askopenfilenames() 
    if paths:
        for p in paths:
            # On évite d'ajouter deux fois le même fichier
            if p not in selected_items:
                selected_items.append(p)
        
        # On passe le container à la fonction de rafraîchissement
        update_selection_display(display_container)

def select_folder(container):
    path = filedialog.askdirectory()
    if path:
        if path not in selected_items:
            selected_items.append(path)
        update_selection_display(container)

def paste_from_clipboard(container):
    try:
        # On demande à la fenêtre principale le contenu du presse-papier
        content = container.clipboard_get() 
        # Ici, on pourrait décider de créer un fichier temporaire 
        # ou juste stocker le texte pour l'envoyer en C
        selected_items.append(f"TEXT: {content[:20]}...") 
        update_selection_display(container)
    except:
        print("Le presse-papier est vide !")

def update_selection_display(container):
    for w in container.winfo_children():
        w.destroy()
        
    for i, item in enumerate(selected_items):
        vignette = ctk.CTkFrame(container, width=70, height=70, corner_radius=10)
        vignette.grid(row=0, column=i, padx=5, pady=5)
        # On force la taille du cadre pour qu'il reste carré
        vignette.grid_propagate(False)

        is_dir = os.path.isdir(item)
        if is_dir:
            icon_text = "📁"
            color = "#2c3e50" # Couleur un peu différente pour les dossiers
        else:
            icon_text = "📄"
            color = "#34495e" 
        
        vignette.configure(fg_color=color)
        icon = ctk.CTkLabel(vignette, text=icon_text, font=("Arial", 25))
        icon.place(relx=0.5, rely=0.5, anchor="center")

        name = os.path.basename(item)
        name_label = ctk.CTkLabel(vignette, text=name[:8], font=("Arial", 10))
        name_label.place(relx=0.5, rely=0.8, anchor="center")
        # Taille du fichier (seulement si c'est un fichier)
        if not is_dir:
            size_bytes = os.path.getsize(item)
            size_mb = size_bytes / (1024 * 1024)
            ctk.CTkLabel(vignette, text=f"{size_mb:.1f} MB", text_color="gray", font=("Arial", 10)).pack()

        btn_close = ctk.CTkButton(vignette, text="X", width=20, height=20, 
                                fg_color="red", hover_color="#AA0000",
                                command=lambda p=item: remove_item(p, container))
        btn_close.place(x=45, y=5) # Petit bouton en haut du carré

        # Cadre d'aperçu horizontal (ton image actuelle)
    preview_frame = ctk.CTkScrollableFrame(container, height=180, orientation="horizontal", label_text="Éléments sélectionnés")

    # --- NOUVEAU : SECTION DESTINATAIRES ---
    recipient_frame = ctk.CTkFrame(container, fg_color="#1e1e1e", corner_radius=10)
    recipient_frame.pack(fill="x", padx=20, pady=10)
    
    ctk.CTkLabel(recipient_frame, text="CHOOSE RECIPIENT", font=("Arial", 12, "bold")).pack(anchor="nw", padx=15, pady=10)

    # On peut mettre les utilisateurs en ligne (horizontal) ou en liste
    users_container = ctk.CTkFrame(recipient_frame, fg_color="transparent")
    users_container.pack(fill="x", padx=15, pady=5)

    # Exemple de bouton radio pour un utilisateur
    recipient_var = ctk.StringVar(value="everyone")
    
    ctk.CTkRadioButton(users_container, text="Everyone (Broadcast)", variable=recipient_var, value="everyone").pack(side="left", padx=20)
    ctk.CTkRadioButton(users_container, text="Madeleine_Y", variable=recipient_var, value="user1").pack(side="left", padx=20)
    
    # Le bouton final d'envoi
    send_btn = ctk.CTkButton(container, text="Action : Send", fg_color="#158aff", height=45, font=("Arial", 16, "bold"))
    send_btn.pack(fill="x", padx=20, pady=20)




def load_transfer_screen(parent_frame):

    title = ctk.CTkLabel(parent_frame, text="SÉLECTION DU CONTENU", font=("bold", 20))
    title.pack(pady=10, padx=20, anchor="nw")

    
    selection_frame = ctk.CTkFrame(parent_frame, fg_color="transparent")
    selection_frame.pack(pady=20)

    btn1 = ctk.CTkButton(selection_frame, 
                            text=f"File\n📄", 
                            width=90, height=90,
                            font=("Arial", 14),
                            command=lambda: select_files(preview_frame)) 
    btn1.grid(row=0, column=0, padx=10)

    btn2 = ctk.CTkButton(selection_frame, 
                            text=f"Folder\n📁", 
                            width=90, height=90,
                            font=("Arial", 14),
                            command=lambda: select_folder(preview_frame)) 
    btn2.grid(row=0, column=1, padx=10)

    preview_frame = ctk.CTkScrollableFrame(parent_frame, 
                                          height=90, 
                                          label_text="Éléments sélectionnés",
                                          orientation="horizontal") # Défilement de gauche à droite
    preview_frame.pack(fill="x", padx=20, pady=20)


def remove_item(item_path, container):
    # On retire l'élément de la liste
    selected_items.remove(item_path)
    # On redessine tout
    update_selection_display(container)
