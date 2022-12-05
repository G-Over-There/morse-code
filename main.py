from code import code
from tkinter import *

# Constants
FONT = "Roboto"

# ----- Functionality -----
def default_decrypt():
    user_input.delete(0, END)
    user_input.insert(0, "...")
    action_button.config(text="Decrypt")


def default_encrypt():
    user_input.delete(0, END)
    user_input.insert(0, "Enter words...")
    action_button.config(text="Encrypt")


def button_clicked():
    if action_button.cget('text') == "Decrypt":
        morse_to_decrypt = user_input.get()
        decripted_text = [code[_] for _ in morse_to_decrypt.split()]
        result_label.config(text=''.join(decripted_text))

    elif action_button.cget('text') == "Encrypt":
        words_to_encrypt = user_input.get()
        reversed_code = {letter: morse for morse, letter in code.items()}
        encrypted_code = [reversed_code[_] for _ in [*words_to_encrypt]]
        print(encrypted_code)
        result_label.config(text='  '.join(encrypted_code))

    else:
        result_label.config(text="Please choose whether you want to encrypt or decrypt.")


# ----- UI SETUP -----
win = Tk()
win.title("Morse Convertor")
win.minsize(width=400, height=250)
win.config(padx=50, pady=50, bg="black")

# Dictionary to create multiple buttons
values = {"Decrypt Morse": "1",
          "Ecnrypt Words": "2"
          }

v = IntVar()

user_input = Entry(width=30)
user_input.grid(column=1, row=0)


decrypt_radio = Radiobutton(win, text="Decrypt Morse", variable=v, value=0, background="black", foreground="green",
                             font=(FONT, 16, "bold"), command=default_decrypt)
decrypt_radio.grid(column=2, row=1)

encrypt_radio = Radiobutton(win, text="Encrypt Setence", variable=v, value=1, background="black", foreground="green",
                             font=(FONT, 16, "bold"), command=default_encrypt)
encrypt_radio.grid(column=2, row=2)

result_label = Label(text="Text will appear here...", font=(FONT, 24), background="black", foreground="green")
result_label.grid(column=1, row=3)

action_button = Button(text="Decrypt", command=button_clicked)
action_button.grid(column=1, row=2, pady=20)

win.mainloop()
