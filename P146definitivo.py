# -*- coding: utf-8 -*-

"""

@author: Aidan

"""

from tkinter import*

root = Tk()

root.title("Proyecto 146")

root.geometry("400x200")

campo = Entry(root)

label = Label(root)

label2 = Label(root)

def fibonacci ():
    
    valor = int(campo.get())
    
    num1 = 0
    
    num2 = 1
    
    sum = 0
    
    sum2 = 0
    
    counter = 1
    
    while(counter <= valor):
        
        label["text"] += str(sum) + " "
        
        label2["text"] = "suma de fibonacci:" + str(sum2) 
        
        counter = counter + 1
        
        num1 = 2
        
        num2 = sum
        
        sum = num1 + num2
        
        sum2 = sum2 + sum

btn = Button(root, text="Serie fibonacci", command=fibonacci )

btn.pack()

campo.pack()

label.pack()

label2.pack()

root.mainloop()