import customtkinter as ctk # pyright: ignore[reportMissingImports]
from screens.transfer import load_transfer_screen
from screens.connection import load_connection_screen


## c'est le menu --------------------------------------
indicate_color = "#158aff"
def indicate(indicator,pages):
    connect_indicate.configure(fg_color=menu_frame_color)
    tranfert_indicate.configure(fg_color=menu_frame_color)

    indicator.configure(fg_color=indicate_color)
    for widget in main_frame.winfo_children():
        widget.destroy()
    pages(main_frame)

main_screen = ctk.CTk()
main_screen.geometry("800x600")
main_screen.title("Toole")

menu_frame = ctk.CTkFrame(main_screen,width=180,
                          border_width=1,
                          border_color="white")
menu_frame.pack(side='left',fill='y',pady=5,padx=5)

menu_frame_color = menu_frame.cget('fg_color')
title_label = ctk.CTkLabel(menu_frame,text="Toolé",font=('bold',20))
title_label.place(x=10,y=50)

connect_indicate = ctk.CTkLabel(menu_frame,text=" ",width=5,height=30,fg_color=indicate_color)
connect_indicate.place(x=3,y=100)
connect_btn = ctk.CTkButton(menu_frame,text="connection",
                        font=('bold',18),fg_color=menu_frame_color,hover=False,
                        command=lambda:indicate(indicator=connect_indicate,pages=load_connection_screen))
connect_btn.place(x=10,y=100)

tranfert_indicate = ctk.CTkLabel(menu_frame,text=" ",width=5,height=30,fg_color=menu_frame_color)
tranfert_indicate.place(x=3,y=150)
tranfert_btn = ctk.CTkButton(menu_frame,text="Send",
                             font=('bold',16),fg_color=menu_frame_color,hover=False,
                             command=lambda:indicate(indicator=tranfert_indicate,pages=load_transfer_screen))
tranfert_btn.place(x=10,y=150)

### fin du menu a gauche
#=====================================================================================

#la partie princpal

main_frame = ctk.CTkFrame(main_screen)
load_connection_screen(main_frame)
main_frame.pack(side='left',fill='both',expand=True,pady=5,padx=5)

main_screen.mainloop()