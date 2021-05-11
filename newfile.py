import tkinter as tk
import csv
from collections import defaultdict
import itertools
from functools import reduce

columns = defaultdict(list)


with open('alldataforzipcodes.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

statelist = (columns['State'])
salestaxlist = (columns['EstimatedCombinedRate'])
zipcodelist = (columns['ZipCode'])






finaldictionary = {k:v for k,v in zip(zipcodelist, salestaxlist)}


finaldictionaryint = dict((k,float(v)) for k,v in finaldictionary.items())



# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('500x300')
# Function for getting Input
# from textbox and printing it 
# at label widget

lbl = tk.Label(frame, text = "Please input your zip code")
lbl.pack() 


def calculatetaxes():
    inp = inputtxt.get(1.0, "end-1c")
    inputforprice = inputforamount.get(100.0)
    if inp in finaldictionaryint.keys():
        lbl.config(text = "Calculated Taxes: "+inp)
        print(inputforprice)
    else: 
        lbl.config(text = ".."+inputforprice)
    
  
# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 1,
                   width = 10)
  
inputtxt.pack()

amount = tk.Label(frame, text = "Please enter product/service price")
amount.pack()

inputforamount = tk.Text(frame,
height = 1, width = 10)

inputforamount.pack()
  
# Button Creation
printButton = tk.Button(frame,
                        text = "Calculate", 
                        command = calculatetaxes)
printButton.pack()
  
# Label Creation

frame.mainloop()