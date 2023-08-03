import pracdataacc as data

def insert():
    name = input("Add name: ")
    email = input("Add email address: ")
    phone_number = input("Add phone number: ")
    address = input("Add address: ")
    print(str(data.insert_into_table(name,email,phone_number,address)) + " id is inserted.")

def search():
    name = input("You wanna seach for: ")
    print(data.search(name))

def remove():
    name = input("You wanna delete: ")
    data.remove(name)

while True:
    menu = input("Select menu: ")
    if menu == "e":
        break
    elif menu == "i":
        insert()
    elif menu == "l":
        print(data.listing("contacts"))
    elif menu == "s":
        search()
    elif menu == "d":
        remove()
    else:
        print("Wrong character")
