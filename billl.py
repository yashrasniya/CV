import os
import go
import sqlite3
import json, subprocess,calculation





#
# creattabel()
# openfile()
# shownum()
def time():
    global datetime, date
    import datetime
    datetime_1 = datetime.datetime.now()
    datetime_1 = str(datetime_1)
    date = datetime_1[0:10]
    time = datetime_1[11:19]
    time = time.replace(":", "")
    date_1 = date.replace("-", "")
    datetime = f"{date_1}{time}"


def num2words(num):
    under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    above_100 = {100: 'Hundred', 1000: 'Thousand', 100000: 'Lack', 10000000: 'Crore'}

    if num < 20:
        return under_20[num]

    if num < 100:
        return tens[(int)(num / 10) - 2] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])

    # find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
    pivot = max([key for key in above_100.keys() if key <= num])

    return num2words((int)(num / pivot)) + ' ' + above_100[pivot] + (
        '' if num % pivot == 0 else ' ' + num2words(num % pivot))


def var(var):
    global name
    if var == 1:
        name = "nos"
    else:
        name = "sqit"


def show():
    oid = input("enter a oid num: ")

    one = sqlite3.connect("one.db")
    cursor = one.cursor()
    cursor.execute(f"SELECT * FROM data WHERE oid=:oid",
                   {"oid": oid}
                   )
    value = cursor.fetchall()
    list = ["invoicenum", "date", "gst", "gstin"]
    xyz = 0






def histryshow():
    try:
        entry_1.delete(0, last=1000)
        entry_4.delete(0, last=1000)
        entry_5_1.delete(0, last=1000)
        entry_5.delete(0, last=1000)
        entry_3.delete(0, last=1000)
        entry_2.delete(0, last=1000)
        oid = entry_oid.get()

        one = sqlite3.connect("one.db")
        cursor = one.cursor()
        cursor.execute(f"SELECT * FROM histry_profile_4 WHERE oid=:oid",
                       {"oid": oid}
                       )
        value = cursor.fetchall()
        text.delete(1.0, 10000.0)

        for value in value:
            entry_1.insert(0, value[0])
            entry_4.insert(0, value[1])
            entry_5_1.insert(0, value[2])
            entry_5.insert(0, value[3])
            entry_3.insert(0, value[4])
            entry_2.insert(0, value[5])

        def happy(value):
            print(value)
            entry_7.delete(0, 1000)
            entry_8.delete(0, 1000)
            entry_8_1.delete(0, 1000)
            entry_9.delete(0, 1000)
            try:
                get = int(entry_rate.get())
            except:
                messagebox.showerror("ERROR", "ENTER WRITE VALUE")
            entry_7.insert(0, str(value[get][0]))
            entry_8.insert(0, str(value[get][1]))
            entry_8_1.insert(0, str(value[get][2]))
            entry_9.insert(0, str(value[get][3]))
            root_1.destroy()

        row = 1
        column = 1
        num = 1
        root_1 = Tk()

        joky = json.loads(value[6])

        for ks in json.loads(value[6]):
            but = Label(root_1, text=f"{num}:{ks}")
            but.grid(row=row, column=column)
            row += 1
            num += 1
        entry_rate = Entry(root_1)
        entry_rate.grid(row=row, column=column)
        but = Button(root_1, text="show", command=lambda: happy(joky))
        but.grid(row=row + 1, column=1)
        one.commit()
        one.close()
        root_1.mainloop()
    except:
        messagebox.showerror("ERROR", "ENTER right OID num")
        root_1.destroy()




from tkinter import *
from tkinter import messagebox


root = Tk()
root.config(bg="white")
root.geometry("580x480")
root.title("BILL")


list_name = []


def chang():
    ent_7 = entry_7.get()
    ent_9_list=entry_9.get().split(" ")
    print(ent_9_list)
    try:
        ent_8 = int(entry_8.get())
        ent_9 = float(ent_9_list[0])
        if entry_8_1.get() == "":
            ent_8_1 = 1
        else:
            ent_8_1 = float(entry_8_1.get())
        list_name.append((ent_7, ent_8, ent_9, ent_8_1,ent_9_list))
    except:
        messagebox.showerror("ERROR", "ENTER INT VALUE")


    entry_7.delete(0, last=END)
    entry_8.delete(0, last=END)
    entry_9.delete(0, last=END)
    entry_8_1.delete(0, last=END)

try:
    calculation.clculation.creattabel("self")
    calculation.clculation.openfile("self")
except:
    pass

calculation.clculation.shownum("self")
entry_1 = Entry(root, bd=4)
entry_1.grid(row=1, column=1, pady=4)

# entry_1.insert(0, num)
entry_2 = Entry(root, bd=4)
entry_2.grid(row=2, column=1, pady=4)

entry_3 = Entry(root, bd=4)
entry_3.grid(row=3, column=1, pady=4)

entry_4 = Entry(root, bd=4)
entry_4.grid(row=4, column=1, pady=4)

entry_5_1 = Entry(root, bd=4)
entry_5_1.grid(row=1, column=3, pady=4)

entry_6_1 = Entry(root, bd=4)
entry_6_1.grid(row=2, column=3, pady=4)

entry_5 = Entry(root, bd=4)
entry_5.grid(row=3, column=3, pady=4)

entry_6 = Entry(root, bd=4)
entry_6.grid(row=4, column=3, pady=4)

entry_7 = Entry(root, bd=4)
entry_7.grid(row=9, column=1, pady=4)

entry_8 = Entry(root, bd=4)
entry_8.grid(row=10, column=1, pady=4)

entry_9 = Entry(root, bd=4)
entry_9.grid(row=9, column=3, pady=4)

entry_8_1 = Entry(root, bd=4)
entry_8_1.grid(row=10, column=3, pady=4)

entry_oid = Entry(root, bd=4)
entry_oid.grid(row=11, column=1, pady=4)
time()
la=calculation.clculation.time("self")
entry_2.insert(0, f"{la[0:2]}-{la[2:4]}-{la[4:8]}" )
# entry_3.insert(0, "happy")
label_1 = Label(root, text="Invoice No.", bg="white", bd=4)
label_1.grid(row=1, column=0, pady=4)
label_2 = Label(root, text="Invoice Date", bg="white", bd=4)
label_2.grid(row=2, column=0, pady=4)
label_3 = Label(root, text="Name", bg="white", bd=4)
label_3.grid(row=3, column=0, pady=4)
label_4 = Label(root, text="Address", bg="white", bd=4)
label_4.grid(row=4, column=0, pady=4)
label_5_1 = Label(root, text="GSTIN", bg="white", bd=4)
label_5_1.grid(row=1, column=2, pady=4)
label_6_1 = Label(root, text="sate code", bg="white", bd=4)
label_6_1.grid(row=2, column=2, pady=4)
label_5 = Label(root, text="GST in %", bg="white", bd=4)
label_5.grid(row=3, column=2, pady=4)
label_6 = Label(root, text="sate", bg="white", bd=4)
label_6.grid(row=4, column=2, pady=4)

label_hed = Label(root, text="Only for Bill", bg="yellow", fg="black", padx=250)
label_hed.grid(row=0, column=0, columnspan=4)

label_7 = Label(root, text="NAME OF PRODUCT", bg="white", bd=4)
label_7.grid(row=9, column=0, pady=4)
label_8 = Label(root, text="Qty.", bg="white", bd=4)
label_8.grid(row=10, column=0, pady=4)
label_8_1 = Label(root, text="Rate", bg="white", bd=4)
label_8_1.grid(row=9, column=2, pady=4)
label_9 = Label(root, text="Size in fit", bg="white", bd=4)
label_9.grid(row=10, column=2, pady=4)
label_oid = Label(root, text="OID", bg="white", bd=4)
label_oid.grid(row=11, column=0, pady=4)
entry_6_1.insert(0, "05")

button_1 = Button(root, text="sumit", padx=270, pady=10, command= lambda : go.Summit(entry_1,entry_2,entry_3,entry_4,entry_5,entry_5_1,entry_6,entry_6_1,entry_7,entry_8,entry_8_1,entry_9,v_1,v_2,root,list_name), bg="white", bd=4)
button_1.grid(row=14, column=0, columnspan=4)
# button_1.place()

button_2 = Button(root, text="Save", padx=125, command=chang, bg="white", bd=4, activeforeground="red",
                  activebackground="white")
button_2.grid(row=5, column=0, columnspan=2)

# button_oid_1 = Button(root, text="show_1",command=show_pro,bg="white",bd=4,activeforeground="red",activebackground="white")
# button_oid_1.grid(row=14, column=2, columnspan=10,rowspan=3)

mb_1 = Menubutton(root, text="-------", relief=RAISED, padx=125, bg="white", bd=4)
mb_1.grid(row=5, column=2, columnspan=2)
mb_1.menu = Menu(mb_1, tearoff=0)
mb_1["menu"] = mb_1.menu
v_1 = StringVar()
v_2 = StringVar()
chek_1 = mb_1.menu.add_checkbutton(label="nos", onvalue="nos", offvalue="", variable=v_1)
chek_2 = mb_1.menu.add_checkbutton(label="sqft", onvalue="sqft", offvalue="", variable=v_2)

text = Text(root, height=10, width=74, bg="black", fg="white")
# text.grid(row=20,column=0,columnspan=4)
button_oid = Button(root, text="show", command= lambda :go.Show(entry_1,entry_2,entry_3,entry_4,entry_5,entry_5_1,entry_7,entry_8,entry_8_1,entry_9,entry_oid), bg="white", padx=125, bd=4, activeforeground="red",
                    activebackground="white")
button_oid.grid(row=11, column=2, columnspan=2)
entry_8_1.insert(0, "1")
entry_6.insert(0, "Uttrakhand")
calculation.clculation.openfile('self')
entry_1.insert(0,calculation.clculation.shownum("self"))

root.mainloop()
