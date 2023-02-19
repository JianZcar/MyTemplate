import tkinter
import functions_j

users = []


def display_txt(x):
    output_box = tkinter.Label(frame, text=x, width=25)
    output_box.grid(row=3, column=0)
    output_box.grid_configure()


class GetData:
    def __init__(self):
        self.username = None
        self.password = None
        self.to_login = None
        self.list = users

    def login(self):
        self.username = user_name_entry.get().strip()
        self.password = user_password_entry.get().strip()
        if functions_j.sign_user_2(True, self.list, self.username, self.password) == 'Invalid':
            display_txt('Invalid Username or Password')
        else:
            display_txt('Log in Successful')

    def signup(self):
        self.username = user_name_entry.get()
        self.password = user_password_entry.get()
        if functions_j.sign_user_2(False, self.list, self.username, self.password) == 'Invalid':
            if self.username == '' or self.password == '':
                display_txt('Invalid Username or Password')
            else:
                display_txt('Username taken')
        else:
            display_txt('Sign up Successful')


window = tkinter.Tk()
window.title('Template')

frame = tkinter.Frame(window)
frame.pack()

user_login_frame = tkinter.LabelFrame(frame, text='')
user_login_frame.grid(row=0, column=0)
user_login_frame.grid_configure(padx=5, pady=10)

user_button_frame = tkinter.LabelFrame(frame)
user_button_frame.grid(row=1, column=0)
user_login_frame.grid_configure()

user_name_label = tkinter.Label(user_login_frame, text='Username')
user_password_label = tkinter.Label(user_login_frame, text='Password')
user_name_label.grid(row=0, column=0)
user_password_label.grid(row=0, column=1)

user_name_entry = tkinter.Entry(user_login_frame)
user_password_entry = tkinter.Entry(user_login_frame)
user_name_entry.grid(row=1, column=0)
user_password_entry.grid(row=1, column=1)
user_name_entry.grid_configure(pady=10)
user_password_entry.grid_configure(pady=10)

b = GetData()

login_button = tkinter.Button(user_button_frame, text='Log in', command=b.login)
login_button.grid(row=0, column=0)
login_button.grid_configure(padx=10)

signin_button = tkinter.Button(user_button_frame, text='Sign in', command=b.signup)
signin_button.grid(row=0, column=1)
signin_button.grid_configure(padx=10)


for widget in user_login_frame.winfo_children():
    widget.grid_configure(padx=10)


window.mainloop()
