
#credits to chatgpt for the sql part, i dont know sql and dont plan on learning it ; i know the module sqlite3 the actual sql parts are what chatgpt created.#
## Dev Notes ## -- add change credentials command and finish check if good password function also encrypt passwords

## all built in python imports so no need to pip install anything :)
import sqlite3
import os
import time

conn = sqlite3.connect("passwords.db")


d = conn.cursor()

d.execute(''' 
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')


def add_pass(website,username,password):
    d.execute('''
        INSERT INTO passwords (website, username, password)
        VALUES (?, ?, ?)
    ''', (website, username, password))
    conn.commit()


def gcbw(website):
    d.execute('''
        SELECT username, password FROM passwords WHERE website = ?
    ''', (website,))
    return d.fetchall()


def get_specific_website_credentials(web):
    for credential in gcbw(web):
        return credential




def handle_inputs():

    os.system("cls")
    d.execute('SELECT DISTINCT website FROM passwords')
    websites = d.fetchall()
    if websites:
        pass_hub()
    else:
        print("[!] You have no existing passwords saved. Please enter a website you want to save credentials for.")
        first_site = input("\n\n\n> ")
        if "." in first_site:
            try:
                os.system("cls")
                first_username = input("Please enter the username you want for the website: ")
                time.sleep(1)
                os.system("cls")
                first_password = input("Please enter the password you want for the website: ")
                if check_if_good_password(first_password) == "valid":
                    add_pass(first_site, first_username, first_password)
                    print(f"[*] Password added for {first_site}!")
                    time.sleep(3)
                    pass_hub()
                elif check_if_good_password(first_password) == "invalid":
                    os.system("cls")
                    print("invalid password try a new one... ")
                    time.sleep(3)
                    return handle_inputs()
            except Exception as e:
                print(f"[!] {Exception}")
                time.sleep(4)
                return handle_inputs()
        else:
            print("Please enter the link of the website..")
            time.sleep(2)
            return handle_inputs()


def check_if_good_password(p):
    if len(p) < 8:
        return "invalid"
    else:
        return "valid"

def website_creator(G):
    os.system("cls")
    if "." in G:
        b = input("Username: ")
        c = input("Password: ")
        if check_if_good_password(c) == "invalid":
            print("invalid password try a new one... (minimum 8 characters)")
            time.sleep(2)
            pass_hub()
        else:
            add_pass(G, b, c)
            time.sleep(2)
            pass_hub()

def pass_hub():
    os.system("cls")
    d.execute('SELECT DISTINCT website FROM passwords')
    websites = d.fetchall()
    print("---WEBSITES---")
    print(websites)
    print("---------------")
    print("\n\ntype create to add a website\ntype view to view a websites credentials\ntype delete to delete a website and its credentials\n\n\n\n\n")
    listener = input("> ")
    if listener.lower() == "create":
        create_command()
    elif listener.lower() == "view":
        view_command()
    elif listener.lower() == "delete":
        delete_command()
    else:
        print("command doesnt exist")
        time.sleep(2)
        return pass_hub()

def create_command():
    os.system("cls")
    a = input("Enter the new website link: ")
    time.sleep(2)
    website_creator(a)

def view_command():
    d.execute('SELECT DISTINCT website FROM passwords')
    websites = d.fetchall()
    if websites:
        os.system("cls")
        print(websites)
        a = input("\nWhich website would you like to view (type the link you entered when creating): ")
        f = get_specific_website_credentials(a)
        if f == None:
            print("Website doesnt exist returning to pass hub... ")
            time.sleep(2)
            pass_hub()
        else:
            print(f)
            u = input("\nType return to go back to pass hub: ")
            if u.lower() == "return":
                pass_hub()
            else:
                os.system("cls")
                print("wel u typed something that isnt return because ur retarded so im gonna just return u anyways u idiot")
                time.sleep(2)
                pass_hub()
    else:
        print("Unknown Error Restart Program")
        input()


def delete_command():
    d.execute('SELECT DISTINCT website FROM passwords')
    os.system("cls")
    print(d.fetchall())
    website = input("which website would you like to delete? ")
    d.execute('DELETE FROM passwords WHERE website = ?', (website,))
    conn.commit()
    time.sleep(2)
    os.system("cls")
    print("site deleted successfully | yeah if u typed the wrong link it didnt delete you dumbass")
    time.sleep(2)
    pass_hub()



handle_inputs()
