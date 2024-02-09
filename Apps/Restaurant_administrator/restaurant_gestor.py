from tkinter import *

#INIT TKINTER
app = Tk()

#SIZE CONFIGURATION
app.geometry('1000x600+250+75')
#AVOID RESIZING
app.resizable(0,0)
#WINDOW TITLE
app.title('ADMIN-REST')
#WINDOW COLOR
app.config(bg='red')


#TOP PANEL
top_panel = Frame(app,bd=1, relief =FLAT )
top_panel.pack(side=TOP)
title_label = Label(top_panel,text='Invoice System', fg = 'black',font=('Arial',58),bg='red',width=23,highlightbackground='black')
title_label.grid(row=0,column=0)


#LEFT PANEL
left_panel = Frame(app,bd=1, relief =FLAT )
left_panel.pack(side=LEFT)
#COST PANEL
cost_panel = Frame(left_panel,bd=1, relief =FLAT )
cost_panel.pack(side=BOTTOM)
#MEALS PANEL
meals_panel = LabelFrame(left_panel,text='Meals',font=('Dosis',19,'bold'),bd = 1, relief=FLAT, fg='red', highlightbackground='black')
meals_panel.pack(side=LEFT)
#DRINKS PANEL
drinks_panel = LabelFrame(left_panel,text='Dinks',font=('Dosis',19,'bold'),bd = 1, relief=FLAT, fg='red', highlightbackground='black')
drinks_panel.pack(side=LEFT)
#DESERTS PANEL
deserts_panel = LabelFrame(left_panel,text='Dinks',font=('Dosis',19,'bold'),bd = 1, relief=FLAT, fg='red', highlightbackground='black')
deserts_panel.pack(side=LEFT)


#RIGHT PANEL
right_panel = Frame(app,bd=1, relief =FLAT )
right_panel.pack(side=RIGHT)
#CALCULATOR PANEL
calculator_panel = Frame(right_panel,bd=1, relief =FLAT)
calculator_panel.pack(side=TOP)
#RECEIPT PANEL
receipt_panel = Frame(right_panel,bd=1, relief =FLAT)
receipt_panel.pack(side=TOP)
#BUTTONS PANEL
buttons_panel = Frame(right_panel,bd=1, relief =FLAT)
buttons_panel.pack(side=TOP)


#LIST OF PRODUCTS
list_foods = ['Chicken','Stake','Pizza','Burger','Turtle']
list_drinks = ['water','Bear','Wine','Coffee','Vodka']
list_deserts = ['pie','cake','ice cream']


#GENERATE MEALS ITEMS
food_variables = []
square_food = []
text_square_food = []

counter = 0

for f in list_foods :
    #CHECKBUTTON CREATION
    food_variables.append('')
    food_variables[counter] = IntVar()
    f = Checkbutton(meals_panel,text=f.title(),font=('Dosis',19,'bold'),onvalue=1,offvalue=0,variable = food_variables[counter])
    f.grid(row=counter,column=0,sticky=NW)

    #REGISTER SQUARES CREATION
    square_food.append('')
    text_square_food.append("")
    text_square_food[counter]= StringVar()
    text_square_food[counter].set(0)
    square_food[counter]= Entry(meals_panel, font=('Dosis',17,'bold'),bd = 1 , width=6, state=DISABLED,textvariable=text_square_food[counter])
    square_food[counter].grid(row = counter,column=1)


    counter+=1

#GENERATE DRINKS ITEMS
drink_variables = []
square_drink = []
text_square_drink = []
counter_1 = 0

for d in list_drinks :
    # CHECKBUTTON CREATION
    drink_variables.append('')
    drink_variables[counter_1] = IntVar()
    f = Checkbutton(drinks_panel,text=d.title(),font=('Dosis',19,'bold'),onvalue=1,offvalue=0,variable = drink_variables[counter_1])
    f.grid(row=counter_1,column=0,sticky=NW)

    #REGISTER SQUARES CREATION
    square_drink.append('')
    text_square_drink.append("")
    text_square_drink[counter_1]= StringVar()
    text_square_drink[counter_1].set(0)
    square_drink[counter_1]= Entry(drinks_panel, font=('Dosis',17,'bold'),bd = 1 , width=6, state=DISABLED,textvariable=text_square_drink[counter_1])
    square_drink[counter_1].grid(row = counter_1,column=1)

    counter_1+=1

#GENERATE DESERTS ITEMS
deserts_variables = []
square_deserts = []
text_square_deserts = []
counter_2 = 0

for de in list_deserts :
    # CHECKBUTTON CREATION
    deserts_variables.append('')
    deserts_variables[counter_2] = IntVar()
    f = Checkbutton(deserts_panel,text=de.title(),font=('Dosis',19,'bold'),onvalue=1,offvalue=0,variable = deserts_variables[counter_2])
    f.grid(row=counter_2, column=0, sticky=NW)

    #REGISTER SQUARES CREATION
    square_deserts.append('')
    text_square_deserts.append("")
    text_square_deserts[counter_2]=StringVar()
    text_square_deserts[counter_2].set(0)
    square_deserts[counter_2]= Entry(deserts_panel, font=('Dosis',17,'bold'),bd = 1 , width=6, state=DISABLED,textvariable=text_square_deserts[counter_2])
    square_deserts[counter_2].grid(row = counter_2,column=1)


    counter_2+=1

#KEEP THE WINDOW OPEN
app.mainloop()
