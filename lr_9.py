"""
Окно входа и регистрации
Хабарова Наталья ИСИбд-21
"""
import tkinter as tk

users = {}

def show_password():
    if show_password_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")
        
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in users and users[username] == password:
        login_successful()
    else:
        login_failed()

def login_successful():
    root.withdraw()
    
    success_window = tk.Toplevel(root)
    success_window['bg'] = 'CadetBlue1'
    success_window.geometry('700x800')
    success_window.title("Вход успешно завершен!")
    success_label = tk.Label(success_window, text="Вход успешно завершен!", font=("Arial", 14), bg = 'CadetBlue1')
    success_label.pack(padx=20, pady=10)

def login_failed():
    error_window = tk.Toplevel(root)
    error_window['bg'] = 'CadetBlue1'
    error_window.title("Войти")
    error_label = tk.Label(error_window, text="Неправильное имя пользователя или пароль. Пожалуйста, попробуйте еще раз.", font=("Arial", 14), bg='CadetBlue1' )
    error_label.pack(padx=20, pady=10)

def register():
    username = entry_username.get()
    password = entry_password.get()
    
    if len(username) == 0 or len(password) == 0:
        registration_failed("Требуется имя пользователя и пароль.")
    elif username in users:
        registration_failed("Имя пользователя уже занято. Пожалуйста, выберите другое имя пользователя.")
    else:
        users[username] = password
        registration_successful()

def registration_successful():
    success_window = tk.Toplevel(root)
    success_window['bg'] = 'CadetBlue1'
    success_window.title("Регистрация")
    success_label = tk.Label(success_window, text="Вы успешно зарегистрировались.", font=("Arial", 14), bg='CadetBlue1')
    success_label.pack(padx=20, pady=10)

def registration_failed(error_message):
    error_window = tk.Toplevel(root)
    error_window['bg'] = 'CadetBlue1'
    error_window.title("Регистрация")
    error_label = tk.Label(error_window, text=error_message, font=("Arial", 14), bg='CadetBlue1')
    error_label.pack(padx=20, pady=10)


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root['bg'] = 'CadetBlue1'
root.title("Окно входа/регистрации")


title_label = tk.Label(root, text="Войдите или зарегистрируйтесь", font=("Arial", 24), bg='CadetBlue1')
title_label.pack(pady=20)


label_username = tk.Label(root, text="Имя пользователя:",bg='CadetBlue1')
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)
entry_username.focus()


label_password = tk.Label(root, text="Пароль:", bg='CadetBlue1')
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(root, text="Показать пароль", variable=show_password_var, command=show_password, font=("Arial", 12), bg='CadetBlue1')
show_password_checkbox.pack()


button_login = tk.Button(root, text="Вход", font=("Arial", 14), command=login)
button_login.pack(pady=10)


button_register = tk.Button(root, text="Регистрация", font=("Arial", 14), command=register)
button_register.pack(pady=10)


root.mainloop()
