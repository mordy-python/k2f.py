from tkinter import *

root = Tk()
root.config(bg="lightblue")
root.geometry("375x250")
root.title("Kelvin to Farenheit")
def convert():
    fbox.delete(0, END)
    k2c = float(kbox.get()) - 273.15
    c2f = round((k2c * (9/5) + 32), 2)
    fbox.insert(0, c2f)
    kbox.delete(0, END)

font = ("arial", 16)

h1 = Label(root, text="Kelvin to Farenheight converter", bg=root["bg"], font=font)
klabel = Label(root, text="Kelvin:", bg=root["bg"], font=font)
flabel = Label(root, text="Farenheight:", bg=root["bg"], font=font)
kbox = Entry(root)
fbox = Entry(root)
convbtn = Button(root, text="Convert", command=convert)

h1.grid(row=0, column=0, pady=20, columnspan=3, padx=30)
klabel.grid(row=1, column=0, pady=10, padx=30)
kbox.grid(row=1, column=1)
convbtn.grid(row=2, column=1)
flabel.grid(row=3, column=0, pady=10, padx=30)
fbox.grid(row=3,column=1)


root.mainloop()