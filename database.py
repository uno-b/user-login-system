import sqlite3


def create_tables():
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT UNIQUE  
    );
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS notes (
        note_id TEXT PRIMARY KEY,
        note TEXT,
        username TEXT,
        FOREIGN KEY (username) REFERENCES users (username)
        ON UPDATE CASCADE ON DELETE CASCADE
    );
    """)

    conn.commit()
    conn.close()


def add_user(user):
    username = user.get_username()
    password = user.get_password()
    email = user.get_email()
    phone_number = user.get_phone_number()

    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)",
                   (username, password, email, phone_number))

    conn.commit()
    conn.close()


def delete_user(username):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM notes WHERE username = (?)", (username,))

    cursor.execute("DELETE FROM users WHERE username = (?)", (username,))

    conn.commit()
    conn.close()


def add_note(note_id, note, username):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO notes (note_id, note, username) VALUES (?, ?, ?)", (note_id, note, username))

    conn.commit()
    conn.close()


def delete_note(note_id):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("DELETE from notes WHERE note_id = (?)", (note_id,))

    conn.commit()
    conn.close()


def login_verify(username, password):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = (?) AND password = (?)", (username, password))
    result = cursor.fetchone()

    conn.commit()
    conn.close()

    if result is None or result == "":
        return False
    else:
        return True


def get_notes(username):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes WHERE username = (?)", (username,))
    result = cursor.fetchall()

    conn.commit()
    conn.close()

    return result


def get_user_data(username):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = (?)", (username,))
    result = cursor.fetchone()

    conn.commit()
    conn.close()

    return result


# Following functions are for testing purposes


def check_if_user_exists(user):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = (?)", (user.get_username(),))
    result = cursor.fetchone()

    conn.commit()
    conn.close()

    if result is None or result == "":
        return False
    else:
        return True


def check_if_note_exists(note_id):
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes WHERE note_id = (?)", (note_id,))
    result = cursor.fetchone()

    conn.commit()
    conn.close()

    if result is None or result == "":
        return False
    else:
        return True


def check_tables():
    conn = sqlite3.connect("user_info.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM notes")
    print(cursor.fetchall())

    conn.commit()
    conn.close()
