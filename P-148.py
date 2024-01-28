# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:07:47 2023

@author: Sumit
"""


from tkinter import *
import random



root=Tk()

root.title("Picnic")
root.geometry("400x400")

list_label = Label(root)
random_item_picnic = Label(root)

picnic = ["Bottle","Sandwich","Lunchbox","Chocolate","Chips","Mat"]

list_label["text"] = str(picnic)
 
def random():
    randomised_item = random.randint(0,5)
    items = picnic[randomised_item]
    random_item_picnic["text"] = "Put Item Number "+str(items)+" Into Bag."





btn = Button(root, text="Generate Random Item",  command = random)
btn.place(relx = 0.5, rely = 0.6, anchor=CENTER)

list_label.place(relx = 0.5, rely = 0.5, anchor=CENTER)

random_item_picnic.place(relx = 0.5, rely = 0.4)
root.mainloop()