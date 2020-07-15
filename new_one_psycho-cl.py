from tkinter import *
import datetime
#display work in calculator
head = Tk()
head.title('"psycho" $$ calculator')#  calcultor name
head.geometry('600x700')
head.configure(bg = 'black')
data = StringVar()
lbl=Label(head,anchor=CENTER,bg="green",textvariable=data,background = "yellow",fg  = 'red',font=30)#display culculator
lbl.pack(expand=True,fill='y')
roww=Frame(head,bg="blue")
roww.pack(expand=True, fill ="both")
row1=Frame(head)
row1.pack(expand=True, fill ="both")
row2=Frame(head,bg="green")
row2.pack(expand=True, fill ="both")
row3=Frame(head,bg="pink")
row3.pack(expand=True, fill ="both")
row4=Frame(head,bg="black")
row4.pack(expand=True, fill ="both")
row5=Frame(head,bg="black")
row5.pack(expand=True, fill ="both")



a = 0
value = " "
oprator = ''
# 28 to 126 button actions
def button_1():
      global value
      value = value+'1'
      data.set(value)
def button_2() :
    global value
    value = value+'2'
    data.set(value)
def button_3():
    global value
    value = value+'3'
    data.set(value)
def button_4() :
    global value
    value = value+'4'
    data.set(value)
def button_5():
    global value
    value = value+'5'
    data.set(value)
def button_6() :
    global value
    value = value+'6'
    data.set(value)
def button_7():
    global value
    value = value+'7'
    data.set(value)
def button_8() :
    global value
    value = value+'8'
    data.set(value)
def button_9() :
    global value
    value = value+'9'
    data.set(value)
def button_0():
    global value
    value = value+'0'
    data.set(value)


def button_00():
    global value
    value = value + '00'
    data.set(value)

def button_dot():
    global value
    value = value + '.'
    data.set(value)
def btnplus():
    global a
    global operator
    global value
    a=int(value)
    operator ="+"
    value = value + "+"
    data.set(value)
def button_multi():
    global a
    global operator
    global value
    a=int(value)
    operator ="*"
    value = value + "x"
    data.set(value)
def button_div():
    global a
    global operator
    global value
    a=int(value)
    operator ="/"
    value = value + "/"
    data.set(value)
def button_sub():
    global a
    global operator
    global value
    a=int(value)
    operator ="-"
    value = value + "-"
    data.set(value)
def button_cler():
    global a
    global operator
    global value
    a = 0
    operator = ""
    value = ""
    data.set(value)
    data.set(value)

def percentage():
    global value
    value = int(value)
    value = value / 100
    data.set(value)


#129 to 155 button operators

def result():
    global a
    global operator
    global value
    valu = value
    if operator == "+":
        x = float((valu.split("+")[1]))
        c = a+x
        data.set(c)
        value=str(c)
    if operator == "*":
        x = float((valu.split("x")[1]))
        c=a*x
        data.set(c)
        value=str(c)
    if operator == "/":
        x = float((valu.split("/")[1]))
        c=a/x
        data.set(c)
        value=str(c)
    if operator == "-":
        x = float((valu.split("-")[1]))
        c=a-x
        data.set(c)
        value=str(c)




#first row buttons
button_x=Button(row1,text="x",bg="blue",borderwidth=0,relief=FLAT,font=("button_clicked",30),command=button_multi)
button_x.pack(side=LEFT,expand= True,fill="both")
button9=Button(row1,text="9",bg="orange",borderwidth=0,relief=FLAT, font=("button_clicked",25),command=button_9)
button9.pack(side=LEFT,expand= True,fill="both")
button8=Button(row1,text="8",bg = '#008080',borderwidth = 0,relief = FLAT,font=('button_clicked',25),command = button_8)
button8.pack(side=LEFT,expand= True,fill="both")
button7=Button(row1,text="7",bg='pink',borderwidth=0,relief=FLAT,font=('button_clicked',25),command=button_7)
button7.pack(side=LEFT,expand= True,fill="both")

#second row buttons

buttonsub=Button(row2,text=" -",bg="blue",borderwidth=0,relief=FLAT,font=("button_clicked",30),command=button_sub)
buttonsub.pack(side=LEFT,expand= True,fill="both")

button6=Button(row2,text="6",bg="deepskyblue",borderwidth=0,relief=FLAT,font=('button_clicked',25),command=button_6)
button6.pack(side=LEFT,expand= True,fill="both")
button5=Button(row2,text="5",bg="maroon",borderwidth=0,relief=FLAT,font=("button_clicked",25),command=button_5)
button5.pack(side=LEFT,expand= True,fill="both")
button4=Button(row2,text="4",bg="gold",borderwidth=0,relief=FLAT,font=("button_clicked",25),command=button_4)
button4.pack(side=LEFT,expand= True,fill="both")

#third row buttons
buttondvi=Button(row3,text=" /",borderwidth=0,bg="blue",relief=FLAT,font=("button_clicked",30),command=button_div)
buttondvi.pack(side=LEFT,expand= True,fill="both")


button3=Button(row3,text="3",bg="magenta",borderwidth=0,relief=FLAT,font=("button_clicked",25),command=button_3)
button3.pack(side=LEFT,expand= True,fill="both")
button2=Button(row3,text="2",bg="#4B0082",borderwidth=0,relief=FLAT,font=("button_clicked",25),command=button_2)
button2.pack(side=LEFT,expand= True,fill="both")
button1=Button(row3,text="1",bg="#0838F6",borderwidth=0,relief=FLAT,font=("button_clicked",25),command=button_1)
button1.pack(side=LEFT,expand= True,fill="both")

#fourth row buttons

buttonp_s=Button(row4,text=" %",borderwidth=0,relief=FLAT,bg="blue",font=("button_clicked",30),command=percentage)
buttonp_s.pack(side=LEFT,expand= True,fill="both")
buttondot=Button(row4,text=" . ",borderwidth=0,relief=FLAT,bg="#F9240C",font=("button_clicked",25),command=button_dot)
buttondot.pack(side=LEFT,expand= True,fill="both")
buttonzero=Button(row4,text="0 ",borderwidth=0,relief=FLAT,bg="#63F90C",font= ('button_clicked',25),command=button_0)
buttonzero.pack(side=LEFT,expand= True,fill="both")
buttondublezero=Button(row4,text="00 ",borderwidth=0,relief=FLAT,bg="#0CF9D9",font=("button_clicked",25),command=button_00)
buttondublezero.pack(side=LEFT,expand= True,fill="both")

#fifeth  row buttons

buttonplus=Button(row5,text=" +",borderwidth=0,bg="red",relief=FLAT,font=("button_clicked",15),command=btnplus)
buttonplus.pack(side=LEFT,expand= True,fill="both")
#result button
btnx=Button(row5,text="=",bg="#0CF924",borderwidth=0,relief=FLAT,font=("button_clicked",14),command=result)
btnx.pack(side=LEFT,expand= True,fill="both")

#cler button

buttoncler=Button(row5,text=" c",borderwidth=0,bg="#D1F90C",relief=FLAT,font=("button_clicked",30),command=button_cler)
buttoncler.pack(side=LEFT,expand= True,fill="both")

print(datetime.datetime.today())
head.mainloop()