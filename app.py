import customtkinter as ctk
from toplevel import open_login_window

root = ctk.CTk()
root.geometry("800x800")
root.title('Inventory Management System')


ctk.set_appearance_mode('light')
# ctk.set_default_color_theme('green') 
ctk.set_default_color_theme('inventory/custom_theme.json')

def log_out():
    open_login_window(root, log_out_button)
    log_out_button.configure(state='disabled')

dashboard_label = ctk.CTkLabel(root, text="Dashboard", font=ctk.CTkFont(size=30, weight="bold"))
dashboard_label.pack(pady=20)

log_out_button = ctk.CTkButton(root, text="Log Out", state='disabled', command=log_out)
log_out_button.pack(pady=10)

open_login_window(root, log_out_button)

root.mainloop()
