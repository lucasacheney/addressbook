import os
import time


filepath = input("What is the name of the directory you would like to use for the address book?\n$")
filename = input("What is the name of the address book file?\n$")
completepath = filepath+filename
print(completepath)

def clear():
  if (os.name == "posix"):
    os.system("clear")
  else:
    os.system("cls")

def cont():
  cont_program = input("\nContinue?\n(y)es or (n)o:")
  if cont_program == "y":
    clear()
    repeat()
  elif cont_program == "n":
    print("Thank you for using the Address Book!")
    time.sleep(2)
    clear()
    quit()
  elif cont_program:
    print("Please select a valid option.")
    time.sleep(2)
    clear()
    cont()

def add():
  name = input("Name:")
  address = input("Address:")
  phone = input("Phone Number:")

  with open(completepath, 'a') as f:
    f.write(name + "|" + address + "|" + phone + "\n")

def view():
  with open(completepath, 'r') as f:
    for line in f.readlines():
      data = line.rstrip()
      name, address, phone = data.split("|")
      print("Name:", name, "| Address:", address, "| Phone:", phone)


def repeat():
  
  while True:
    mode = input("\nWould you like to\n(v)iew the address book\n(a)dd a new address or\n(q)uit?\n$")
    if mode == "q":
      clear()
      quit()
    elif mode == "v":
      view()
      cont()
    elif mode == "a":
      add()
      cont()

repeat()
