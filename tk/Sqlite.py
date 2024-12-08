from tkinter import *
from database import *
from tkinter import ttk
from tkinter import messagebox

db = Database("SqliteData.db")

window = Tk()
window.title("sample")
window.geometry("1920x1080")
name = StringVar()
age = StringVar()
gender = StringVar()
address = StringVar()
contact = StringVar()
mail = StringVar()

frame1 = Frame(window, padx=20, pady=20, bg="#636e72")
frame1.pack(side=TOP, fill=X)

lblTitle = Label(frame1, bg="#636e72", text="REGISTRATION", font=("times", 16, "bold"), fg="white", pady=10)
lblTitle.grid(columnspan=2)

lblName = Label(frame1, text="name", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
lblName.grid(row=1, column=0)

txtName = Entry(frame1, textvariable=name, font=("times", 16), width=43)
txtName.grid(row=1, column=1)

lblAge = Label(frame1, text="age", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
lblAge.grid(row=2, column=0)

txtAge = Entry(frame1, font=("times", 16), textvariable=age, width=43)
txtAge.grid(row=2, column=1)

lblgen = Label(frame1, text="Gender", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
lblgen.grid(row=3, column=0)

cb = ttk.Combobox(frame1, width=41, textvariable=gender, state="readonly", font=("times", 16))
cb['values'] = ("male", "female", "Others")
cb.grid(row=3, column=1)

lblAdd = Label(frame1, text="Address", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
lblAdd.grid(row=4, column=0)

txtAdd = Entry(frame1, textvariable=address, font=("times", 16), width=43)
txtAdd.grid(row=4, column=1)

lblCon = Label(frame1, text="Contact", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
lblCon.grid(row=5, column=0)

txtCon = Entry(frame1, textvariable=contact, font=("times", 16), width=43)
txtCon.grid(row=5, column=1)

lblmail = Label(frame1, text="Mail", bg="#636e72", fg="white", font=("times", 16, "bold"), pady=10)
lblmail.grid(row=6, column=0)

txtMail = Entry(frame1, textvariable=mail, font=("times", 16), width=43)
txtMail.grid(row=6, column=1)

btn_frame = Frame(frame1, bg="#2d3436")
btn_frame.grid(row=7, column=1, columnspan=4)

def fetchData():
    table.delete(*table.get_children())
    count = 0
    for row in db.fetch_record():
        count += 1
        table.insert("", END, values=(count, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

def addData():
    if txtName.get() == "" or txtAge.get() == "" or txtAdd.get() == "" or txtCon.get() == "" or txtMail.get() == "":
        messagebox.showinfo("message", "please fill All Records")
    else:
        db.insert(txtName.get(), txtAge.get(), cb.get(), txtAdd.get(), txtCon.get(), txtMail.get())
        fetchData()
        clearData()
        messagebox.showinfo("message", "Records insert Successfully")

def getrecord(event):
    global row
    Srow = table.focus()
    data = table.item(Srow)
    row = data['values']
    name.set(row[2])
    age.set(row[3])
    gender.set(row[4])
    address.set(row[5])
    contact.set(row[6])
    mail.set(row[7])

def updateData():
    if txtName.get() == "" or txtAge.get() == "" or txtAdd.get() == "" or cb.get() == "" or txtCon.get() == "" or txtMail.get() == "":
        messagebox.showinfo("message", "please Fill All Records")
    else:
        db.update_record(txtName.get(), txtAge.get(), cb.get(), txtAdd.get(), txtCon.get(), txtMail.get(), row[1])
        fetchData()
        clearData()
        messagebox.showinfo("message", "record update Successfully")

def deleteData():
    db.remove_record(row[1])
    fetchData()
    clearData()
    messagebox.showinfo("message", "record deleted Successfully")

def clearData():
    name.set("")
    age.set("")
    gender.set("")
    contact.set("")
    mail.set("")
    address.set("")

btnSub = Button(btn_frame, text="Insert", bg="#01a3a4", fg="white", width=6, padx=20, pady=5, font=("times", 16, "bold"), command=addData)
btnSub.grid(row=0, column=0)

btnUp = Button(btn_frame, text="Update", bg="#F79F1F", fg="white", width=6, padx=20, pady=5, font=("times", 16, "bold"), command=updateData)
btnUp.grid(row=0, column=1)

btnDel = Button(btn_frame, text="Delete", bg="#ee5253", fg="white", width=6, padx=20, pady=5, font=("times", 16, "bold"), command=deleteData)
btnDel.grid(row=0, column=2)

btnClr = Button(btn_frame, text="Clear", bg="#DEAA79", fg="white", width=6, padx=20, pady=5, font=("times", 16, "bold"), command=clearData)
btnClr.grid(row=0, column=3)

myFrame = Frame(window)
myFrame.place(x=0, y=425, width=1920, height=500)

style = ttk.Style()
style.configure("Treeview", font=("times", 15), rowheight=35)
style.configure("Treeview.Heading", font=("times", 16, "bold"))

table = ttk.Treeview(myFrame, columns=(0, 1, 2, 3, 4, 5, 6, 7), show='headings')
table.column(0, anchor=CENTER, stretch=NO)
table.column(1,stretch=NO, width=0)
table.column(3, anchor=CENTER)
table.column(6, anchor=CENTER)

table.heading(0, text="S.no")
table.heading(1, text="ID")
table.heading(2, text="NAME")
table.heading(3, text="AGE")
table.heading(4, text="GENDER")
table.heading(5, text="ADDRESS")
table.heading(6, text="CONTACT")
table.heading(7, text="MAIL")
table.bind("<ButtonRelease-1>", getrecord)
table.pack(fill=X)

fetchData()

window.mainloop()