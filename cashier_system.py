# Simple cashier system, optimized for german use, where writing prices with , is common

import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

# input of price and payment
price = input("Gib hier den Preis ein: ")
payment = input("Der Kunde zahlt: ")

# inputs will be turned into floats, no matter if they are written with . or ,
price = locale.atof(price)
payment = locale.atof(payment)

change = payment - price

# Output of the change, written with ,
print("Das Rückgeld beträgt:", locale.format_string('%.2f', change), "€")
