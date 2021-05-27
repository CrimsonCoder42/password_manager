from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email_user = eu_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 :
        messagebox.showerror("Error", "Please fill out all fields.")
    else:
        is_ok = messagebox.askokcancel(title="Title", message="Information saved, would you like to continue?")
        if is_ok:
            with open("my_file.txt", "a") as data_file:
                data_file.write(f"{website} | {email_user} | {password}\n")
                website_input.delete(0, END)
                eu_input.delete(0, END)
                password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


#website label

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

#Email/Username Label

eu_label = Label(text="Email/Username:")
eu_label.grid(column=0, row=2)

#password label

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#website input

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

#Email/User input

eu_input = Entry(width=35)
eu_input.grid(column=1, row=2, columnspan=2)

#password input

password_input = Entry(width=21)
password_input.grid(column=1, row=3)


# Generate button
gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



# Add button



window.mainloop()