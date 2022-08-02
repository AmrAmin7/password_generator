import json
from tkinter import *
from tkinter import messagebox
import pyperclip
from random import randint , choice , shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def password_generator():
	letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' ,
	           'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' ,
	           'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' ,
	           'Y' , 'Z']
	numbers = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
	symbols = ['!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+' , '-' , '/' , '[' , ']']

	password_letter = [choice(letters) for _ in range(randint(6 , 8))]
	password_symbols = [choice(symbols) for _ in range(randint(2 , 3))]
	password_number = [choice(numbers) for _ in range(randint(2 , 3))]

	password_list = password_letter + password_symbols + password_number
	shuffle(password_list)

	passwd = "".join(password_list)
	password_entry.delete(0 , END)
	password_entry.insert(0 , passwd)
	pyperclip.copy(passwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website = web_entry.get()
	e_mail = email_entry.get()
	password = password_entry.get()

	new_data = {
		website: {
			"email": e_mail ,
			"password": password ,
		}
	}
	if len(website) == 0 or len(password) == 0 or len(e_mail) == 0:
		messagebox.showinfo(title="Warning" , message="Please make sure you haven't left any fields empty. ")
	else:
		try:
			with open("data.json" , "r") as data_file:
				# Reading old data
				data = json.load(data_file)
		except FileNotFoundError:
			with open("data.json" , "w") as data_file:
				json.dump(new_data , data_file , indent=4)
		else:
			# Updating old data with new data
			data.update(new_data)

			with open("data.json" , "w") as data_file:
				# Saving updated data
				json.dump(new_data , data_file , indent=4)
		finally:
			web_entry.delete(0 , END)
			# email_entry.delete(0 , END)
			password_entry.delete(0 , END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
	website = web_entry.get()
	try:
		with open("data.json" , "r") as data_file:
			data = json.load(data_file)
	except FileNotFoundError:
			messagebox.showinfo(title="Error" , message="No Data File Found.")
	else:
		if website in data:
			e_mail = data[website]["email"]
			password = data[website]["password"]
			messagebox.showinfo(title=website , message=f"Email: {e_mail}\nPassword: {password}")
		else:
			messagebox.showinfo(title="Error" , message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50)

canvas = Canvas(height=200 , width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100 , 100 , image=logo_img)
canvas.grid(row=0 , column=1)

# Labels
web_label = Label(text="Website:")
web_label.grid(row=1 , column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2 , column=0)
password_label = Label(text="Password:")
password_label.grid(row=3 , column=0)

# Entry
web_entry = Entry(width=21)
web_entry.grid(row=1 , column=1)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2 , column=1 , columnspan=2)
email_entry.insert(0 , "amr@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3 , column=1)

# Button
search_button = Button(text="Search" , width=13 , command=find_password)
search_button.grid(row=1 , column=2)
generate_password_button = Button(text="Generate Password" , command=password_generator)
generate_password_button.grid(row=3 , column=2)
add_button = Button(text="Add" , width=36 , command=save)
add_button.grid(row=4 , column=1 , columnspan=2)


window.mainloop()
