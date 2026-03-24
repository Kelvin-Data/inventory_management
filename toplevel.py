import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from CTkMessagebox import CTkMessagebox
import pickle
import os
     
def open_login_window(root, log_out_button):

    toplevel = ctk.CTkToplevel(root)

    toplevel.geometry("500x580")
    toplevel.title("Login")
    
    def segmented_button_event(value):
        if value == "Log In":
            login_heading.configure(text="Login to your account")
            confirm_password_label.grid_forget()
            confirm_password_entry.grid_forget()
            show.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
            login_button.configure(text="Log In", image=login_icon)
        else:
            login_heading.configure(text="Create a new account")
            confirm_password_label.grid(column=0, row=3, padx=10, pady=10)
            confirm_password_entry.grid(column=1, row=3, padx=10, pady=10)
            show.grid_forget()
            login_button.configure(text="Sign Up", image=signup_icon)

    def show_password():
        show_state = show.get()
        if show_state == 1:
            login_password.configure(show="")  
        else:
            login_password.configure(show="*")
    

    def log_in():
        value = login_signup_var.get()
        email = login_email.get()
        password = login_password.get()
        confirm_password = confirm_password_entry.get()
        
        # Load existing users
        if os.path.exists('inventory/users.pkl'):
            with open('inventory/users.pkl', 'rb') as f:
                users = pickle.load(f)
        else:
            users = {}

        # ------------------ LOGIN ------------------
        if value == "Log In":
            if email in users and users[email] == password:
                CTkMessagebox(title="Success", message="Logged in successfully!", icon="check")
                toplevel.destroy()
                log_out_button.configure(state='normal')
                return
                
            if email == '' or password == '':
                CTkMessagebox(title="Error", message="All fields are required!", icon="cancel")
                clear_fields()
                return
            
            else:
                CTkMessagebox(title="Error", message="Invalid email or password!", icon="cancel")
                clear_fields()
                return

        # ------------------ SIGN UP ------------------
        else:
            if password != confirm_password:
                CTkMessagebox(title="Error", message="Passwords do not match!", icon="cancel")
                clear_fields()
                return

            if email in users:
                CTkMessagebox(title="Error", message="User already exists!", icon="cancel")
                clear_fields()
                return
            
            if email == '' or password == '' or confirm_password == '':
                CTkMessagebox(title="Error", message="All fields are required!", icon="cancel")
                clear_fields()
                return
            else:
                # Save new user
                users[email] = password
                with open('inventory/users.pkl', 'wb') as f:
                    pickle.dump(users, f)
                clear_fields()
                CTkMessagebox(title="Success", message="Account created successfully!", icon="check")
                login_signup_var.set("Log In")
                segmented_button_event("Log In")
                
            
    def clear_fields():
        login_email.delete(0, 'end')
        login_password.delete(0, 'end')
        confirm_password_entry.delete(0, 'end')
     

    font_bold = ctk.CTkFont(family="Roboto", size=20, weight="bold")
    
    login_image = CTkImage(
        dark_image=Image.open("inventory/media/coding.png"),
        size=(150, 150)
    )

    login_title = CTkImage(
            dark_image=Image.open("inventory/media/title.png"),
            size=(500, 100)
        )

    login_icon = CTkImage(
            dark_image=Image.open("inventory/media/login.png"),
            size=(30, 30))
    
    signup_icon = CTkImage(
            dark_image=Image.open("inventory/media/signup.png"),
            size=(30, 30))
    
    login_signup_var = ctk.StringVar(value="Log In")
    login_signup = ctk.CTkSegmentedButton(
        toplevel, 
        values=["Log In", "Sign Up"],  
        variable=login_signup_var,                                            
        command=segmented_button_event)
    login_signup.pack(padx=10, pady=10)
    
    login_image = ctk.CTkLabel(toplevel, image=login_image, text="") 
    login_image.pack(padx=0, pady=0)

    login_title = ctk.CTkLabel(toplevel, image=login_title, text="")
    login_title.pack(padx=0, pady=0)
    
    login_frame = ctk.CTkFrame(toplevel)
    login_frame.pack(padx=10, pady=10)

    login_heading= ctk.CTkLabel(login_frame, text="Login to your account", 
                            font=font_bold)
    login_heading.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

    login_label_1 = ctk.CTkLabel(login_frame, text="Email:", 
                            font=font_bold)
    login_label_1.grid(column=0, row=1, padx=10, pady=10)

    login_email = ctk.CTkEntry(login_frame, 
                            placeholder_text="Enter your email address",
                            width=200)
    login_email.grid(column=1, row=1, padx=10, pady=10)

    login_label_2 = ctk.CTkLabel(login_frame, text="Password:", 
                            font=ctk.CTkFont(size=20, weight="bold"))
    login_label_2.grid(column=0, row=2, padx=10, pady=10)

    login_password = ctk.CTkEntry(login_frame, 
                                placeholder_text="Enter your password", 
                                width=200,show="*")
    login_password.grid(column=1, row=2, padx=10, pady=10)
    
    confirm_password_label = ctk.CTkLabel(login_frame, text="Confirm Password:",    
                            font=ctk.CTkFont(size=20, weight="bold"))
    confirm_password_label.grid_forget()
            
    confirm_password_entry = ctk.CTkEntry(login_frame, 
                                placeholder_text="Confirm your password",
                                width=200,
                                show="*")
    confirm_password_entry.grid_forget()

    show = ctk.CTkCheckBox(login_frame, text="Show Password", 
                        command=show_password)
    show.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
    
    login_button = ctk.CTkButton(login_frame, text="Log In",  
                        image=login_icon, 
                        compound="left", 
                        font=font_bold,
                        width=200,
                        command=log_in)
    login_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    return toplevel
