from tkinter import *

def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    print(firstname_info, lastname_info, age_info)

    file = open('user.txt','a')
    file.write(f"firstname: {firstname_info}")
    file.write('\n')
    file.write(f"lastname: {lastname_info}")
    file.write('\n')
    file.write(f"age: {age_info}")
    file.close()
    print("User ", firstname_info, 'has been registered successfullly')

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    age_entry.delete(0, END)

screen = Tk()
screen.geometry('500x500')
screen.title("Python Form")


heading = Label(text = 'Python Form', bg = "green", fg = "black", height='3', width = '500')
heading.pack()

firstname_text = Label(text = 'Firstname: ')
lastname_text = Label(text = 'Lastname: ')
age_text = Label(text = 'Age: ')
firstname_text.place(x = 15, y = 70)
lastname_text.place(x = 15, y = 140)
age_text.place(x = 15, y = 210)


# Set variables for input boxes. 
firstname = StringVar()
lastname = StringVar()
age = IntVar()


# Create input boxes with corresponding variables. 
firstname_entry = Entry(textvariable = firstname, width='30')
lastname_entry = Entry(textvariable = lastname, width ='30')
age_entry = Entry(textvariable = age, width= '30')


firstname_entry.place(x = 15, y = 100)
lastname_entry.place(x = 15, y = 180)
age_entry.place(x = 15, y = 240)


register = Button(screen, text = 'Register', width='30', height='2', command = save_info, bg= 'green')
register.place(x = 15,y = 290)
