# Alternative version of the cashier system program with Loops

import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

answer = "j"

while answer == "j":
    price = input("Preis in €: ")
    price = locale.atof(price)
    discount_in_percent = input("Rabatt in %: ")
    discount_in_percent = locale.atof(discount_in_percent)
    discount_in_euro = price / 100 * discount_in_percent
    new_price = round(price - discount_in_euro, 2)
    print("Der Preis mit", locale.format_string('%.2f', discount_in_percent), "% Rabatt beträgt",
          locale.format_string('%.2f', new_price), "€")

    payment = input("Der Kunde zahlt: ")
    payment = locale.atof(payment)
    change = payment - new_price

    if change < 0:
        print("Das gezahlte Geld reicht nicht aus.")
    else:
        print("Gegeben:", locale.format_string('%.2f', payment),
              "€, Preis:", locale.format_string('%.2f', new_price), "€")
        print("Change:", locale.format_string('%.2f', change), "€")
        answer = input("Weiter machen? Dann gib bitte 'j' ein: ")

print("Beendet.")
