import tkinter as tk
from tkinter import font

def library():
        library_code = entry.get()
        if library_code.lower() == "afghanistan":
            info_text.set('''Country Name : Afghanistan
                 Land Mass : 652864 sq km, 252072 sq mi
                 Population : 43,844,111
                 Capital : Kabul
                 Currency : Afghan Afghani
                 Languages : Pushto, Dari
                 National Animal : Snow Leopard
                 National Bird : Golden Eagle
                 National Flower : Tulip
                 National Fruit : Pomegranate
                 National Sport : Buzkashi''')
        elif library_code.lower() == "albania":
            info_text.set('''Country Name : Albania
                 Land Mass : 28748 sq km, 11100 sq mi
                 Population : 2,771,508
                 Capital : Tiranë
                 Currency : Albanian Lek
                 Language : Albanian
                 National Animal : Eagle
                 National Bird : Eagle
                 National Flower : Red Poppy
                 National Fruit : Cherry
                 National Sport : Football''')
        elif library_code.lower() == "algeria":
            info_text.set('''Country Name : Algeria
                 Land Mass : 2381741 sq km, 919595 sq mi
                 Population : 47,435,312
                 Capital : Algiers
                 Currency : Algerian dinar
                 Languages : Arabic, Tamazight
                 National Animal : Fennec Fox
                 National Bird : Barbary Partridge
                 National Flower : Iris
                 National Fruit : Berber Maraschino Cherry
                 National Sport : Football''')
        elif library_code.lower() == "andorra":
            info_text.set('''Country Name : Andorra
                 Land Mass : 468 sq km, 181 sq mi
                 Population : 82,904
                 Capital : Andorra la Vella
                 Currency : Euro
                 Languages : Catalan
                 National Animal : Bruna d'Andorra Cow
                 National Bird : Lammergeier
                 National Flower : Poet's Narcissus
                 National Fruit : Mango 
                 National Sport : Football''')
        elif library_code.lower() == "angola":
            info_text.set('''Country Name : Angola
                 Land Mass : 1246700 sq km, 481,400 sq mi
                 Population : 38,736,266
                 Capital : Luanda
                 Currency : Angolan Kwanza
                 Languages : Portuguese
                 National Animal : Giant Sable Antelope
                 National Bird : Red-Crested Turaco
                 National Flower : Welwitschia
                 National Fruit : Palm
                 National Sport : Football''')
        elif library_code.lower() == "antigua and barbuda":
            info_text.set('''Country Name : Antigua and Barbuda
                 Land Mass : 440 sq km, 170 sq mi
                 Population : 94,096
                 Capital : Saint John's
                 Currency : East Caribbean Dollar
                 Languages : English
                 National Animal : European Fallow Deer
                 National Bird : Magnificent Frigatebird
                 National Flower : Agave Karatto
                 National Fruit : Antigua Black Pineapple
                 National Sport : Cricket''')
        elif library_code.lower() == "argentina":
            info_text.set('''Country Name : Argentina
                 Land Mass : 2,780,085 km, 1,073,397 sq mi
                 Population : 45,851,378
                 Capital : Buenos Aires
                 Currency : Argentine peso
                 Languages : Spanish
                 National Animal : Rufous Hornero
                 National Bird : Rufous Hornero
                 National Flower : Ceibo
                 National Fruit : Apple'
                 National Sport : Juego del pato''')
        elif library_code.lower() == "armenia":
            info_text.set('''Country Name : Armenia
                 Land Mass : 29,743 sq km, 11,484 sq mi
                 Population : 2,952,365
                 Capital : Yerevan
                 Currency : Armenian Dram
                 Languages : Armenian
                 National Animal : Lion
                 National Bird : Golden Eagle
                 National Flower : Forget-Me-Not
                 National Fruit : Apricot
                 National Sport : Chess''')
        elif library_code.lower() == "australia":
            info_text.set('''Country Name : Australia
                Land Mass : 7,688,287 sq km, 2.968,464 sq mi
                Population : 26,917,297
                Capital : Canberra
                Currency : Australian Dollar
                Language : Australian English
                National Animal : Kangaroo
                National Bird : Emu
                National Flower : Golden Wattle
                National Fruit : Riberry
                National Sport : N/A
                National Sport via Popularity : Cricket''')
        elif library_code.lower() == "austria":
            info_text.set('''Country Name : Austria
                Land Mass : 83,871 sq km, 32,383 sq mi
                Population : 9,113,574
                Capital : Vienna
                Currency : Austrian Schilling (Now Euro €)
                Language : German
                National Animal : Eagle
                National Bird : Eagle
                National Flower : Edelweiss
                National Fruit : Apple
                National Sport(Official) : Football
                National Sport(Unofficial) : Alpine Skiing''')
        elif library_code.lower() == "azerbaijan":
            info_text.set('''Country Name Azerbaijan
                Land Mass : 86,600 sq km, 33,400 sq mi
                Population : 10,384,674
                Capital : Baku
                Currency : Azerbaijani Manat
                Language : Azerbaijani
                National Animal : Karabakh Horse
                National Bird : Caspian Snowcock
                National Flower : Ophrys Caucasia
                National Fruit : Pomegranate
                National Sport : Freestyle Wrestling''')
        elif library_code.lower() == "bahamas":
            info_text.set('''Country Name : Bahamas
                Land Mass : 13,880 sq km, 5,358 sq mi
                Population : 399,440
                Capital : Nassau
                Currency : Bahamian Dollar
                Language : English
                National Animal : Blue Marlin
                National Bird : Flamingo
                National Flower : Yellow Elder
                National Fruit : Pineapple
                National Sport : Sailing''')
        elif library_code.lower() == "bahrain":
            info_text.set('''Country Name : Bahrain
                Land Mass : 786.5 sq km, 588.7 sq mi
                Population : 11,635,753
                Capital : Manama
                Currency : Bahraini Dinar
                Language : Arabic
                National Animal : Arabian Oryx
                National Bird : White Eared Bulbul
                National Flower : N/A
                National Fruit : N/A
                National Sport : Football''')
        elif library_code.lower() == "bangladesh":
            info_text.set('''Country Name : Bangladesh
                Land Mass : 148,460 sq km, 57,320 sq mi
                Population : 175,286,414
                Capital : Dhaka
                Currency : Bangladesh Taka
                Language : Bengali
                National Animal : Bengal Tiger
                National Bird : Oriental Magpie-Robi
                National Flower : Water Lily
                National Fruit : Jackfruit
                National Sport : Kabaddi''')

root = tk.Tk()
root.title("GeoWiki")

# Set background color
root.configure(bg="#9099de")

# Define a custom font
custom_font = font.Font(family="verdana", size=12, weight="bold",slant='italic', underline=False, overstrike=False)

label = tk.Label(root, text="Enter the name of the country: ", bg="#9099de", font=custom_font)
label.pack(pady=10)  # Add vertical padding

entry = tk.Entry(root, font=custom_font, background="#adb2d9", width=25)
entry.pack(pady=10, padx=10)

# Style the button
button = tk.Button(root, text="Get Info", command=library, bg="#4CAF50", fg="white", font=custom_font)
button.pack(pady=2)

info_text = tk.StringVar()
info_label = tk.Label(root, textvariable=info_text, wraplength=400, justify=tk.LEFT, bg="#9099de", font=custom_font)
info_label.pack(pady=0)

root.mainloop()
