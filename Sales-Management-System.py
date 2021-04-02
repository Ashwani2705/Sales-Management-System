# Designing a Sales Management System

from tkinter import *
import time;
import datetime
import pygame,sys,random
import tkinter.messagebox

pygame.init()
root= Tk()
root.title("Sales Management System")
root.geometry('1300x700+0+0')
root.configure(background= "white")

#====================== FRAME ===========================================================================================
ABC = Frame(root, bg="powder blue", bd=20, relief=RIDGE)
ABC.grid()
ABC1 = Frame(ABC, bg="cadet blue", bd=10, relief=RIDGE)
ABC1.grid(row=0,column=0,columnspan=4, sticky=W)
ABC2 = Frame(ABC, bg="cadet blue", bd=10, relief=RIDGE)
ABC2.grid(row=1,column=0,sticky=W)
ABC3 = Frame(ABC, bg="cadet blue", bd=10, relief=RIDGE)
ABC3.grid(row=1,column=1,sticky=W)
ABC4 = Frame(ABC, bg="cadet blue", bd=10, relief=RIDGE)
ABC4.grid(row=1,column=2,sticky=W)
ABC5 = Frame(ABC4, bg="cadet blue", bd=10, relief=RIDGE)
ABC5.grid(row=0,column=0,sticky=W)
ABC6 = Frame(ABC4, bg="cadet blue", bd=10, relief=RIDGE)
ABC6.grid(row=1,column=0, columnspan= 4,sticky=W)

#====================== VARIABLES ===========================================================================================
Tax = StringVar()
Subtotal = StringVar()
Total = StringVar()

Jeans_Jaggers = StringVar()
Coats_Jackets = StringVar()
Sportwear_w = StringVar()
Dresses = StringVar()
Skirts = StringVar()
Swimwear_w = StringVar()
SchoolUniform = StringVar()
Kidswear = StringVar()
Jackets_Blazers = StringVar()
Former_Trouser = StringVar()
Sportwear_m = StringVar()
Pyjamas = StringVar()
Swimwear_m = StringVar()
Socks = StringVar()
Shoes = StringVar()
Shirt =StringVar()

Jeans_Jaggers.set("0")
Coats_Jackets.set("0")
Sportwear_w.set("0")
Dresses.set("0")
Skirts.set("0")
Swimwear_w.set("0")
SchoolUniform.set("0")
Kidswear.set("0")
Jackets_Blazers.set("0")
Former_Trouser.set("0")
Sportwear_m.set("0")
Pyjamas.set("0")
Swimwear_m.set("0")
Socks.set("0")
Shoes.set("0")
Shirt.set("0")

#====================== FUNCTION DECLARATION =================================================================================================
def iExit():
    iExit = tkinter.messagebox.askyesno("Sales_Management_System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():
    txtReceipt.delete("1.0",END)
    Jeans_Jaggers.set("0")
    Coats_Jackets.set("0")
    Sportwear_w.set("0")
    Dresses.set("0")
    Skirts.set("0")
    Swimwear_w.set("0")
    SchoolUniform.set("0")
    Kidswear.set("0")
    Jackets_Blazers.set("0")
    Former_Trouser.set("0")
    Sportwear_m.set("0")
    Pyjamas.set("0")
    Swimwear_m.set("0")
    Socks.set("0")
    Shoes.set("0")
    Shirt.set("0")

def Total():
    I1 = float(Jeans_Jaggers.get())
    I2 = float( Coats_Jackets.get())
    I3 = float(Sportwear_w.get())
    I4 = float(Dresses.get())
    I5 = float(Skirts.get())
    I6 = float(Swimwear_w.get())
    I7 = float(SchoolUniform.get())
    I8 = float(Kidswear.get())
    I9 = float(Jackets_Blazers.get())
    I10 = float(Former_Trouser.get() )
    I11 = float(Sportwear_m.get())
    I12 = float(Pyjamas.get())
    I13 = float(Swimwear_m.get())
    I14 = float(Shirt.get())
    I15 = float(Socks.get())
    I16 = float(Shoes.get())
    
    PI1 = ("Rs ") + str('%.2f'%(I1*100))
    PI2 = ("Rs ") + str('%.2f'%(I2*100))
    PI3 = ("Rs ") + str('%.2f'%(I3*100))
    PI4 = ("Rs ") + str('%.2f'%(I4*100))
    PI5 = ("Rs ") + str('%.2f'%(I5*100))
    PI6 = ("Rs ") + str('%.2f'%(I6*100))
    PI7 = ("Rs ") + str('%.2f'%(I7*100))
    PI8 = ("Rs ") + str('%.2f'%(I8*100))
    PI9 = ("Rs ") + str('%.2f'%(I9*100))
    PI10 = ("Rs ") + str('%.2f'%(I10*100))
    PI11 = ("Rs ") + str('%.2f'%(I11*100))
    PI12 = ("Rs ") + str('%.2f'%(I12*100))
    PI13 = ("Rs ") + str('%.2f'%(I13*100))
    PI14 = ("Rs ") + str('%.2f'%(I14*100))
    PI15 = ("Rs ") + str('%.2f'%(I15*100))
    PI16 = ("Rs ") + str('%.2f'%(I16*100))

    PW = (I1*100) + (I2*100) +(I3*100) + (I4*100) + (I5*100) + (I6*100)      #PW= total price of women's items bought
    PM = (I9*100) + (I10*100) +(I11*100) +(I12*100) +(I13*100) + (I14*100)    #PM= total price of men's items bought
    PK = (I7*100) + (I8*100)                                                 #PK= total price of kid's items bought
    PA = (I15*100) + (I16*100)                                              #PA= total price of accessorie's items bought

    Subtotal = ("Rs") + str('%.2f'%(PW + PM + PK + PA))
    Tax = ("Rs") + str('%.2f'%((PW + PM + PK + PA) *0.15))
    TT = (PW + PM + PK + PA)
    TC = (PW + PM + PK + PA) *0.15
    Total=  ("Rs ") + str('%.2f'%(TT + TC))

    txtReceipt.insert(END,'Items\t\t\t'+'Cost of Items\n')
    txtReceipt.insert(END,"------------------------------------------------------------------\n")
    txtReceipt.insert(END,"Jeans_Jaggers\t\t\t"+ PI1+"\n")
    txtReceipt.insert(END,"Coats_Jackets\t\t\t"+ PI2+"\n")
    txtReceipt.insert(END,"Sportswear_Women\t\t\t"+ PI3+"\n")
    txtReceipt.insert(END,"Dresses\t\t\t"+ PI4+"\n")
    txtReceipt.insert(END,"Skirts\t\t\t"+ PI5+"\n")
    txtReceipt.insert(END,"Swimwear_Women\t\t\t"+ PI6+"\n")
    txtReceipt.insert(END,"School Uniform\t\t\t"+ PI7+"\n")
    txtReceipt.insert(END,"Kidswear\t\t\t"+ PI8+"\n")
    txtReceipt.insert(END,"Jackets_Blazers\t\t\t"+ PI9+"\n")
    txtReceipt.insert(END,"Former_Trouser\t\t\t"+ PI10+"\n")
    txtReceipt.insert(END,"Sportswear_Men\t\t\t"+ PI11+"\n")
    txtReceipt.insert(END,"Pyjamas\t\t\t"+ PI12+"\n")
    txtReceipt.insert(END, "Swimwear_Men\t\t\t" + PI13+"\n")
    txtReceipt.insert(END,"Shirts\t\t\t"+ PI14+"\n")
    txtReceipt.insert(END,"Socks\t\t\t"+ PI15+"\n")
    txtReceipt.insert(END,"Shoes\t\t\t"+ PI16+"\n")
    txtReceipt.insert(END,"TOTAL COST\t\t\t"+Total+"\n")


#====================== UPPER LABELS FOR DATE, TIME AND HEADING INSIDE FRAME ABC1 =================================================================================================
lbldate = Label(ABC1, text= "DATE\t", font=('arial',30,'bold'), padx=9, pady=9,
bd=14, bg="cadet blue", fg="Cornsilk", justify=CENTER).grid(row=0,column=0)

lbltitle = Label(ABC1, text= "\tSales Management Systems\t", font=('arial',30,'bold'), padx=9, pady=9,
bd=5, bg="cadet blue", fg="Cornsilk", justify=CENTER).grid(row=0,column=1)

lbltime = Label(ABC1, text="\tTIME", font=('arial',30,'bold'), padx=9, pady=9,
bd=5, bg="cadet blue", fg="Cornsilk", justify=CENTER).grid(row=0,column=2)

#====================== LABELS I=================================================================================================
lblWomen = Label(ABC2, text="Women",font=('arial',20,'bold'), pady=1, bg="white", bd=8,fg="black", width=25,
justify=CENTER).grid(row=0,column=0,columnspan=2)

lblJeansJeggers = Label(ABC2, text="Jeans & Jeggers",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=1,column=0,sticky=W)

lblCoatsJackets = Label(ABC2, text="Coats & Jackets",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=2,column=0,sticky=W)

lblSportwear = Label(ABC2, text="Sportwear",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=3,column=0,sticky=W)

lblDresses = Label(ABC2, text="Dresses",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=4,column=0,sticky=W)

lblSkirts = Label(ABC2, text="Skirts",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=5,column=0,sticky=W)

lblSwimwear = Label(ABC2, text="Swimwear",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=6,column=0,sticky=W)

lblSchoolUniform = Label(ABC2, text="School Uniform",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=8,column=0,sticky=W)

lblkidswear = Label(ABC2, text="Kids Wear",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=9,column=0,sticky=W)

#====================== ENTRY BOXES I =================================================================================================
txtJeansJeggers = Entry(ABC2, textvariable=Jeans_Jaggers, font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=1,column=1,pady=1)

txtCoatsJackets = Entry(ABC2, textvariable= Coats_Jackets,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=2,column=1,pady=1)

txtSportwear = Entry(ABC2, textvariable=Sportwear_w ,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=3,column=1,pady=1)

txtDresses = Entry(ABC2, textvariable=Dresses ,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=4,column=1,pady=1)

txtSkirts = Entry(ABC2, textvariable=Skirts ,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=5,column=1,pady=1)

txtSwimwear = Entry(ABC2, textvariable=Swimwear_w ,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=6,column=1,pady=1)

lblKid = Label(ABC2, text="Kid",font=('arial',20,'bold'), pady=1, bg="white", bd=8,fg="black", width=25,
justify=CENTER).grid(row=7,column=0,columnspan=2)

txtSchoolUniform = Entry(ABC2, textvariable= SchoolUniform,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=8,column=1,pady=1)

txtKidswear = Entry(ABC2, textvariable=Kidswear ,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=9,column=1,pady=1)

#====================== LABELS II=================================================================================================
lblMen = Label(ABC2, text="Men",font=('arial',20,'bold'), pady=1, bg="white", bd=8,fg="black", width=25,
justify=CENTER).grid(row=0,column=6,columnspan=2)

lblJacketsBlazers = Label(ABC2,text="Jackets and Blazers",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=1,column=6,sticky=W)

lblFormerTrouser = Label(ABC2,text="Formal Trousers",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=2,column=6,sticky=W)

lblSportwear = Label(ABC2,text="Sportwear",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=3,column=6,sticky=W)

lblShirt = Label(ABC2,text="Shirts",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=4,column=6,sticky=W)

lblPyjamas = Label(ABC2, text="Pyjamas",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=5,column=6,sticky=W)

lblSwimwear = Label(ABC2,text="Swimwear",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=6,column=6,sticky=W)

lblSocks = Label(ABC2,text="Socks",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=8,column=6,sticky=W)

lblShoes = Label(ABC2,text="Shoes",font=('arial',18,'bold'), bg="powder blue", 
justify=LEFT).grid(row=9,column=6,sticky=W)

#====================== ENTRY BOXES II=================================================================================================
txtJacketsBlazers = Entry(ABC2,textvariable= Jackets_Blazers, font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=1,column=7,pady=1)

txtFormertrouser = Entry(ABC2,textvariable=Former_Trouser , font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=2,column=7,pady=1)

txtSportwear = Entry(ABC2, textvariable= Sportwear_m,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=3,column=7,pady=1)

txtShirt = Entry(ABC2, textvariable= Shirt,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=4,column=7,pady=1)

txtPyjamas = Entry(ABC2, textvariable=Pyjamas ,font=('arial',18,'bold'), bg="powder blue", bd=8,fg="black", width=12,
justify=CENTER).grid(row=5,column=7,pady=1)

txtSwimwear = Entry(ABC2, textvariable=Swimwear_m ,font=('arial',18,'bold'), bg="white", bd=8,fg="black", width=12,
justify=CENTER).grid(row=6,column=7,pady=1)

# ============================== LABEL ACCESSORIES ==========================================================================
lblAccessories = Label(ABC2, text="Accessories",font=('arial',20,'bold'), pady=1, bg="white", bd=8,fg="black", width=25,
justify=CENTER).grid(row=7,column=6,columnspan=2)

# ================================= ENTRY BOXES II CONTINUED==============================================================================
txtSocks = Entry(ABC2,textvariable= Socks, font=('arial',18,'bold'), bg="white", bd=8,fg="black", width=12,
justify=CENTER).grid(row=8,column=7,pady=1)

txtShoes = Entry(ABC2,textvariable= Shoes , font=('arial',18,'bold'), bg="white", bd=8,fg="black", width=12,
justify=CENTER).grid(row=9,column=7,pady=1)

#====================== TEXT BOX TO SHOW BILL =================================================================================================
txtReceipt = Text(ABC5, height=24, width=50, bd=20, font=('arial',9,'bold'))
txtReceipt.grid(row=0,column=0)
txtReceipt.pack()

#====================== BUTTONS =================================================================================================
btnTotal = Button(ABC6, bd=4, fg="black", font=('arial',16,'bold'), bg="powder blue", text="Total",command=Total).grid(row=0,column=0)

btnRest = Button(ABC6, bd=4, fg="black", font=('arial',16,'bold'), bg="powder blue", text="Reset",command=Reset).grid(row=0,column=1)

btnExit = Button(ABC6, bd=4, fg="black", font=('arial',16,'bold'), bg="powder blue", text="Exit",command=iExit).grid(row=0,column=2)



root.mainloop()