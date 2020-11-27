import json
import uuid
from functools import partial
from tkinter import *
from tkinter.ttk import *

import requests

import database
import user


def destroy_screen():
    screen.destroy()


def destroy_registration_screens():
    register_success_screen.destroy()
    register_screen.destroy()


def destroy_register_error_screen():
    register_error_screen.destroy()


def destroy_login_error_screen():
    login_error_screen.destroy()


def destroy_note_not_saved_screen():
    note_not_saved_screen.destroy()


def destroy_note_saved_screen():
    note_saved_screen.destroy()
    create_note_screen.destroy()


def destroy_view_notes_screen():
    view_notes_screen.destroy()


def destroy_note_deleted_screen():
    note_deleted_screen.destroy()
    delete_note_screen.destroy()


def destroy_note_not_deleted_screen():
    note_not_deleted_screen.destroy()


def destroy_view_profile_screen():
    view_profile_screen.destroy()


def logout():
    session_screen.destroy()


def register_error():
    global register_error_screen
    register_error_screen = Toplevel(screen)
    register_error_screen.title("Error")
    register_error_screen.geometry("150x100")

    Label(register_error_screen, text="").pack()
    Label(register_error_screen, text="Register Error").pack()
    Label(register_error_screen, text="").pack()

    Button(register_error_screen, width=5, text="OK", command=destroy_register_error_screen).pack()


def register_success():
    global register_success_screen
    register_success_screen = Toplevel(screen)
    register_success_screen.title("Success")
    register_success_screen.geometry("150x100")

    Label(register_success_screen, text="").pack()
    Label(register_success_screen, text="Registration was successful.").pack()
    Label(register_success_screen, text="").pack()

    Button(register_success_screen, width=5, text="OK", command=destroy_registration_screens).pack()


def login_success(username):
    session(username)
    login_screen.destroy()


def login_error():
    global login_error_screen
    login_error_screen = Toplevel(screen)
    login_error_screen.title("Error")
    login_error_screen.geometry("150x100")

    Label(login_error_screen, text="").pack()
    Label(login_error_screen, text="User Not Found").pack()
    Label(login_error_screen, text="").pack()

    Button(login_error_screen, width=5, text="OK", command=destroy_login_error_screen).pack()


def note_not_saved():
    global note_not_saved_screen
    note_not_saved_screen = Toplevel(screen)
    note_not_saved_screen.title("Error")
    note_not_saved_screen.geometry("150x100")

    Label(note_not_saved_screen, text="").pack()
    Label(note_not_saved_screen, text="Note Not Saved").pack()
    Label(note_not_saved_screen, text="").pack()

    Button(note_not_saved_screen, width=5, text="OK", command=destroy_note_not_saved_screen).pack()


def note_saved():
    global note_saved_screen
    note_saved_screen = Toplevel(screen)
    note_saved_screen.title("Success")
    note_saved_screen.geometry("150x100")

    Label(note_saved_screen, text="").pack()
    Label(note_saved_screen, text="Note Saved").pack()
    Label(note_saved_screen, text="").pack()

    Button(note_saved_screen, width=5, text="OK", command=destroy_note_saved_screen).pack()


def save(note, current_username):
    try:
        database.add_note(str(uuid.uuid4()), note.get(), current_username)
        note_saved()
    except:
        note_not_saved()


def generate_quote(content):
    parameters = {
        "method": "getQuote",
        "key": 1,
        "format": "json",
        "lang": "en"
    }

    r = requests.get("http://api.forismatic.com/api/1.0/", params=parameters)
    quote = json.loads(r.text)["quoteText"]

    content.delete(0, END)
    content.insert(0, quote)


def create_note(current_username):
    note = StringVar()
    global create_note_screen
    create_note_screen = Toplevel(screen)
    create_note_screen.title("Create a Note")
    create_note_screen.geometry("700x250")

    Label(create_note_screen, text="Add an inspirational quote!").pack()
    Label(create_note_screen, text="").pack()
    Button(create_note_screen, text="Generate a Quote", command=lambda: generate_quote(content)).pack()
    Label(create_note_screen, text="").pack()
    Label(create_note_screen, text="Write the content of your note: ").pack()
    Label(create_note_screen, text="").pack()
    content = Entry(create_note_screen, textvariable=note, width=100)
    content.pack()
    Label(create_note_screen, text="").pack()

    Button(create_note_screen, text="Save", command=lambda: save(note, current_username)).pack()


def view_notes(current_username):
    global view_notes_screen
    view_notes_screen = Toplevel(screen)
    view_notes_screen.title("View Notes")
    view_notes_screen.minsize(300, 100)

    notes = database.get_notes(current_username)

    for index, note in enumerate(notes):
        Label(view_notes_screen, text="").pack()
        Label(view_notes_screen, text="{}: {}".format(index + 1, note[1])).pack()
        Label(view_notes_screen, text="").pack()

    Label(view_notes_screen, text="").pack()
    Button(view_notes_screen, text="Close", command=destroy_view_notes_screen).pack()
    Label(view_notes_screen, text="").pack()


def delete_note1(note_id):
    try:
        database.delete_note(note_id)
        print("Deleted ID: " + note_id)

        global note_deleted_screen
        note_deleted_screen = Toplevel(screen)
        note_deleted_screen.title("Success")
        note_deleted_screen.geometry("150x100")

        Label(note_deleted_screen, text="").pack()
        Label(note_deleted_screen, text="Note Deleted").pack()
        Label(note_deleted_screen, text="").pack()

        Button(note_deleted_screen, width=5, text="OK", command=destroy_note_deleted_screen).pack()

    except:
        global note_not_deleted_screen
        note_saved_screen = Toplevel(screen)
        note_saved_screen.title("Success")
        note_saved_screen.geometry("150x100")

        Label(note_saved_screen, text="").pack()
        Label(note_saved_screen, text="Note Not Deleted").pack()
        Label(note_saved_screen, text="").pack()

        Button(note_saved_screen, width=5, text="OK", command=destroy_note_not_deleted_screen).pack()


def delete_note(current_username):
    global delete_note_screen
    delete_note_screen = Toplevel(screen)
    delete_note_screen.title("Delete a Note")
    delete_note_screen.minsize(300, 100)

    notes = database.get_notes(current_username)

    for note in notes:
        Label(delete_note_screen, text="").pack()
        Button(delete_note_screen, text="{}".format(note[1]), command=partial(delete_note1, note[0])).pack()
        Label(delete_note_screen, text="").pack()


def remove_account(current_user):
    database.delete_user(current_user)
    destroy_view_profile_screen()
    logout()


def view_profile(current_user):
    global view_profile_screen
    view_profile_screen = Toplevel(screen)
    view_profile_screen.title("View Profile")
    view_profile_screen.geometry("250x220")

    result = database.get_user_data(current_user)

    Label(view_profile_screen, text="").pack()
    Label(view_profile_screen, text="Username: {}".format(current_user)).pack()
    Label(view_profile_screen, text="").pack()
    Label(view_profile_screen, text="Email: {}".format(result[2])).pack()
    Label(view_profile_screen, text="").pack()
    Label(view_profile_screen, text="Phone Number: {}".format(result[3])).pack()
    Label(view_profile_screen, text="").pack()

    Button(view_profile_screen, text="Remove Account", command=lambda: remove_account(current_user)).pack()
    Label(view_profile_screen, text="").pack()
    Button(view_profile_screen, text="Close", command=destroy_view_profile_screen).pack()
    Label(view_profile_screen, text="").pack()


def session(current_username):
    global session_screen
    session_screen = Toplevel(screen)
    session_screen.title("dashboard")
    session_screen.geometry("400x300")

    Label(session_screen, text="").pack()
    Label(session_screen, text="Welcome to the dashboard, {}!".format(current_username)).pack()
    Label(session_screen, text="").pack()

    Button(session_screen, width=30, text="Create a Note", command=lambda: create_note(current_username)).pack()
    Label(session_screen, text="").pack()

    Button(session_screen, width=30, text="View Notes", command=lambda: view_notes(current_username)).pack()
    Label(session_screen, text="").pack()

    Button(session_screen, width=30, text="Delete a Note", command=lambda: delete_note(current_username)).pack()
    Label(session_screen, text="").pack()

    Button(session_screen, width=30, text="View Profile", command=lambda: view_profile(current_username)).pack()
    Label(session_screen, text="").pack()

    Button(session_screen, width=30, text="Logout / Close", command=logout).pack()


def login_verify(username, password):
    if database.login_verify(username, password):
        login_success(username)
    else:
        login_error()


def login():
    global login_screen
    login_screen = Toplevel(screen)
    login_screen.title("Login")
    login_screen.geometry("300x230")
    Label(login_screen, text="").pack()
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username * ").pack()
    username_entry = Entry(login_screen, textvariable=username_verify)
    username_entry.pack()
    Label(login_screen, text="").pack()

    Label(login_screen, text="Password * ").pack()
    password_entry = Entry(login_screen, show="*", textvariable=password_verify)
    password_entry.pack()
    Label(login_screen, text="").pack()

    Button(login_screen, text="Login", width=20,
           command=lambda: login_verify(username_verify.get(), password_verify.get())).pack()


def register_user(username, password, email, phone_number):
    try:
        a_user = user.User(username.get(), password.get(), email.get(), phone_number.get())
        database.add_user(a_user)
        register_success()

    except ValueError:
        register_error()


def register():
    global register_screen
    register_screen = Toplevel(screen)
    register_screen.title("Register")
    register_screen.geometry("300x500")

    username = StringVar()
    password = StringVar()
    email = StringVar()
    phone_number = StringVar()

    Label(register_screen, text="").pack()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()

    Label(register_screen, text="Username * ").pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="- Length between 4 and 20 characters").pack()

    Label(register_screen, text="").pack()

    Label(register_screen, text="Password * ").pack()
    password_entry = Entry(register_screen, show="*", textvariable=password)
    password_entry.pack()
    Label(register_screen, text=" - Length between 4 and 8 characters").pack()
    Label(register_screen, text="- At least one uppercase or lowercase letter").pack()
    Label(register_screen, text="- At least one numeric digit").pack()

    Label(register_screen, text="").pack()

    Label(register_screen, text="Email * ").pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    Label(register_screen, text="").pack()

    Label(register_screen, text="Phone Number ").pack()
    phone_number_entry = Entry(register_screen, textvariable=phone_number)
    phone_number_entry.pack()
    Label(register_screen, text="Mongolian phone format:").pack()
    Label(register_screen, text="########").pack()
    Label(register_screen, text="Ex: 94545454").pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=20,
           command=lambda: register_user(username, password, email, phone_number)).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x200")
    screen.title("Note Taker 1.0")
    Label(text="").pack()
    Label(text="Note Taker 1.0").pack()
    Label(text="").pack()
    Button(text="Login", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Close", width="30", command=destroy_screen).pack()

    screen.mainloop()


main_screen()

'''
Demo Accounts:
Username: Uno123
Password: Uno123

Username: unb170
Password: unb170
'''

# Print tables
# database.check_tables()
