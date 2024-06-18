# from tkinter import *

# root = Tk()
# root.title("Currency Converter")
# root.geometry("400x400")
# root.config(bg="black")

# lab_title = Label(root, text="Currency Converter", font=("Times New Roman", 20), bg="black", fg="white")
# lab_title.place(x=90, y=20, height=40, width=220)

# entry = Entry(width=30,font = ("Helvectica",10),fg="grey")
# entry.place(x=95,y=80)
# entry.insert(0,"Enter the input....")

# clicked = StringVar() 
# # initial menu text 
# clicked.set( "USD" ) 
# options = [
#     "USD",
#     "EUR",
#     "JPY",
#     "BGN",
#     "CZK",
#     "DKK",
#     "GBP",
#     "AUD",
#     "CAD",
#     "INR"
# ]

# drop = OptionMenu( root , clicked , *options ) 
# drop.grid(row=1, column=1, padx=10, pady=10)
# drop.place(x=30,y=100)
# drop.pack() 

# root.mainloop()

import requests
import json

currencies = [
    "USD",
    "EUR",
    "JPY",
    "BGN",
    "CZK",
    "DKK",
    "GBP",
    "AUD",
    "CAD",
    "INR"
]

print("********************")
print("CURRENCY CONVERTER!!")
print("********************")
print(currencies)
base_c = input("Enter the base currency :").upper()
converted_c = input("Enter the targeted currency :").upper()
amount = float(input(f"Enter amount in {base_c} :"))

api_url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_77zA894fLLSSWvV9vRGEBSnIe0Y1oKg9QH3wHGK4&base_currency={base_c}&currencies={converted_c}"
api_req = requests.get(api_url)
api_dict = json.loads(api_req.text)

if 'data' in api_dict:
    for i,key in api_dict['data'].items():
        print(f"The amount converted from {base_c} to {converted_c} is {round(key*amount,3)}")


       


