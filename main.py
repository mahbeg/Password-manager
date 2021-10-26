from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    main_list = []
    [main_list.append(random.choice(numbers)) for number in range(1, 3)]
    [main_list.append(random.choice(letters)) for letter in range(0, 4)]
    [main_list.append(random.choice(symbols)) for symbol in range(0, 2)]
    random.shuffle(main_list)

    password = "".join(main_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty box", message="Please fill all of the boxes")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def search():
    website = web_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Find")
    else:
        if website in data:
            result = data[website]
            print(result)
            em = result["email"]
            pas = result["password"]
            messagebox.showinfo(title="search result", message=f"your email is {em}/"
                                                           f" your password is {pas}")
        else:
            messagebox.showerror(title="Oops", message="this website does not exist")


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_file = PhotoImage(file="../logo/logo.png")
canvas.create_image(100, 100, image=image_file)
canvas.grid(column=1, row=0)

#Labels
web_label_name = Label(text="Website name:")
web_label_name.grid(column=0, row=1, sticky="e")

email_label_name = Label(text="Email/username:")
email_label_name.grid(column=0, row=2, sticky="e")

password_label_name = Label(text="Password:")
password_label_name.grid(column=0, row=3, sticky="e")

#Entry
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, sticky="w")

email_entry = Entry(width=53)
email_entry.insert(0, "mahsa.beglari@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")

password_entry = Entry(width=34)

password_entry.grid(column=1, row=3, sticky="w")

#Button

password_button = Button(text="Generate password", command=password_generator)
password_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add to file", width=45, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1, sticky="w")



windows.mainloop()
