# Simple cashier system, optimized for german use, where writing prices with , is common

import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

price = input("Preis in €: ")
price = locale.atof(price) # inputs will be turned into floats, no matter if they are written with . or
discount_in_percent = input("Rabatt in %: ") ,
discount_in_percent = locale.atof(discount_in_percent)
discount_in_euro = price/100 * discount_in_percent
new_price = price - discount_in_euro
print("Der Preis mit", locale.format_string('%.2f', discount_in_percent), "% Rabatt beträgt",
      locale.format_string('%.2f', new_price), "€")

payment = input("Der Kunde zahlt: ")
payment = locale.atof(payment)
change = payment - new_price

# Summary written with ,
print("Gegeben:", locale.format_string('%.2f', payment), "€, Preis:", locale.format_string('%.2f', new_price), "€")
print("Change:", locale.format_string('%.2f', change), "€")
