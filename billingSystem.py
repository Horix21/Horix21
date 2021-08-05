from tkinter import *

root = Tk()
root.title='Billing System'


sum = 0
#commands

def tip():
    entry4.delete(0, END)
    global sum
    e = int(entry3.get())
    sum1 = sum/100*120
    sum2= sum1+e
    entry4.insert(0, "%.2f" % sum2)

def submit():
    entry1.delete(0, END)
    entry2.delete(0, END)
    global sum
    sum = 0
    #bevarages
    if len(entrySprite.get()) != 0:
        e=int(entrySprite.get())
        sum = sum + e*5
    if len(entryPepsi.get()) != 0:
        e=int(entryPepsi.get())
        sum = sum + e*5
    if len(entryMojito.get()) != 0:
        e=int(entryMojito.get())
        sum = sum + e*7
    if len(entryCapp.get()) != 0:
        e=int(entryCapp.get())
        sum = sum + e*7
    if len(entryFanta.get()) != 0:
        e=int(entryFanta.get())
        sum = sum + e*5
    if len(entryCoca.get()) != 0:
        e=int(entryCoca.get())
        sum = sum + e*5
    if len(entryCold.get()) != 0:
        e=int(entryCold.get())
        sum = sum + e*7
    if len(entryDiet.get()) != 0:
        e=int(entryDiet.get())
        sum = sum + e*6

    #foods 
    if len(entryHot.get()) != 0: 
        e=int(entryHot.get())
        sum = sum + e*3
    if len(entryVeg.get()) != 0:
        e=int(entryVeg.get())
        sum = sum + e*9
    if len(entryPasta.get()) != 0:
        e=int(entryPasta.get())
        sum = sum + e*12
    if len(entryRice.get()) != 0:
        e=int(entryRice.get())
        sum = sum + e*7
    if len(entrySand.get()) != 0:
        e=int(entrySand.get())
        sum = sum + e*2
    if len(entryFires.get()) != 0:
        e=int(entryFires.get())
        sum = sum + e*2
    if len(entrySpag.get()) != 0:
        e=int(entrySpag.get())
        sum = sum +e*15
    if len(entryFazita.get()) != 0:
        e=int(entryFazita.get())
        sum = sum + e*12
    entry1.insert(0, sum)
    sum1=(sum/100)*120
    entry2.insert(0,"%.2f" % sum1)

#bevarages

var1=IntVar()
sprite = Checkbutton(root, text = 'Sprite',variable=var1)
sprite.grid(row=0, column=0,sticky=W)
entrySprite = Entry(root, bd=3)
entrySprite.grid(row=0, column=1)

var2=IntVar()
pepsi = Checkbutton(root, text = 'Pepsi',variable=var2)
pepsi.grid(row=1, column=0,sticky=W)
entryPepsi = Entry(root, bd=3)
entryPepsi.grid(row=1, column=1)

var3=IntVar()
mojito = Checkbutton(root, text = 'Mojito',variable=var3)
mojito.grid(row=2, column=0,sticky=W)
entryMojito = Entry(root, bd=3)
entryMojito.grid(row=2, column=1) 

var4=IntVar()
capp = Checkbutton(root, text = 'Cappucino',variable=var4)
capp.grid(row=3, column=0,sticky=W)
entryCapp = Entry(root, bd=3)
entryCapp.grid(row=3, column=1)

var5=IntVar()
fanta = Checkbutton(root, text = 'Fanta',variable=var5)
fanta.grid(row=4, column=0,sticky=W)
entryFanta = Entry(root, bd=3)
entryFanta.grid(row=4, column=1)

var6=IntVar()
CocaCola = Checkbutton(root, text = 'Coca Cola',variable=var6)
CocaCola.grid(row=5, column=0,sticky=W)
entryCoca = Entry(root, bd=3)
entryCoca.grid(row=5, column=1)

var7=IntVar()
ColdCoffe = Checkbutton(root, text = 'Cold Coffe',variable=var7)
ColdCoffe.grid(row=6, column=0,sticky=W)
entryCold = Entry(root, bd=3)
entryCold.grid(row=6, column=1)

var8=IntVar()
diet = Checkbutton(root, text = 'Diet Coke',variable=var8)
diet.grid(row=7, column=0,sticky=W)
entryDiet = Entry(root, bd=3)
entryDiet.grid(row=7, column=1)

#foods

hotDog = Checkbutton(root, text = 'Hot Dog')
hotDog.grid(row = 0, column=3,sticky=W)
entryHot = Entry(root, bd=3)
entryHot.grid(row = 0, column=4)

VegBurger = Checkbutton(root, text = 'Vegan Burger')
VegBurger.grid(row = 1, column=3,sticky=W)
entryVeg = Entry(root, bd=3)
entryVeg.grid(row = 1, column=4)

Pasta = Checkbutton(root, text = 'Pasta')
Pasta.grid(row = 2, column=3,sticky=W)
entryPasta = Entry(root, bd=3)
entryPasta.grid(row = 2, column=4)

ricePlate = Checkbutton(root, text = 'Rice Plate')
ricePlate.grid(row = 3, column=3,sticky=W)
entryRice = Entry(root, bd=3)
entryRice.grid(row = 3, column=4)

Sandwhich = Checkbutton(root, text = 'Sandwhich')
Sandwhich.grid(row = 4, column=3,sticky=W)
entrySand = Entry(root, bd=3)
entrySand.grid(row = 4, column=4)

Fires = Checkbutton(root, text = 'Fries')
Fires.grid(row = 5, column=3,sticky=W)
entryFires = Entry(root, bd=3)
entryFires.grid(row = 5, column=4)

Spaghetti = Checkbutton(root, text = 'Spaghetti')
Spaghetti.grid(row = 6, column=3,sticky=W)
entrySpag = Entry(root, bd=3)
entrySpag.grid(row = 6, column=4)

Fazitas = Checkbutton(root, text = 'Fazitas')
Fazitas.grid(row = 7, column=3,sticky=W)
entryFazita = Entry(root, bd=3)
entryFazita.grid(row = 7, column=4)

#the button

submit = Button(root, text="submit", padx=300, pady=10, command=submit)
submit.grid(row=8, column=0, columnspan=5)

#total
label = Label(root, text='total')
label.grid(row=9,column=0,sticky=W)

entry1 = Entry(root, bd=3)
entry1.grid(row=9,column=1,columnspan=2)

#fees
label1 = Label(root, text = 'total with fees')
label1.grid(row=10, column=0,sticky=W)

entry2 =Entry(root, bd=3)
entry2.grid(row=10,column=1,columnspan=2)

#tip
label2= Label(root, text = 'how much would you like to tip')
label2.grid(row=11,column=0,sticky=W)

entry3 = Entry(root, bd=3)
entry3.grid(row=11,column=1,columnspan=2)

button12= Button(root, text="tip", command = tip,padx=20,pady=3)
button12.grid(row=11,column=3,padx=10)

#total with tip

label3 = Label (root, text="total with tip")
label3.grid(row=12,column=0,sticky=W)

entry4 = Entry(root, bd=3)
entry4.grid(row = 12, column = 1, columnspan=2)

root.mainloop()
