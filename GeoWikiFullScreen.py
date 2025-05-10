import tkinter as tk
from tkinter import font

def library():
    country_list = entry.get()
    if country_list.lower() == "afghanistan":
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
    elif country_list.lower() == "albania":
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
    elif country_list.lower() == "algeria":
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
    elif country_list.lower() == "andorra":
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
    elif country_list.lower() == "angola":
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
    elif country_list.lower() == "antigua and barbuda":
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
    elif country_list.lower() == "argentina":
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
    elif country_list.lower() == "armenia":
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
    elif country_list.lower() == "australia":
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
    elif country_list.lower() == "austria":
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
    elif country_list.lower() == "azerbaijan":
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
    elif country_list.lower() == "bahamas":
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
    elif country_list.lower() == "bahrain":
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
    elif country_list.lower() == "bangladesh":
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

root.geometry("1920x1080")

root.resizable(True, True)

root.configure(bg="#9099de")

font_style = font.Font(family="verdana", size=12, weight="bold",slant='italic', underline=False, overstrike=False)
labelfont = font.Font(family="verdana", size=30, weight="bold",slant='italic', underline=False, overstrike=False)

label = tk.Label(root, text="Enter the name of the country: ", bg="#9099de", font=labelfont)
label.pack(pady=120)

entry = tk.Entry(root, font=font_style, background="#adb2d9", width=70)
entry.pack(pady=70)

button = tk.Button(root, text="Get Info", command=library, bg="#4CAF50", fg="black", font=font_style, width=20, height=2)
button.pack(pady=10)

info_text = tk.StringVar()
info_label = tk.Label(root, textvariable=info_text, wraplength=400, justify=tk.LEFT, bg="#9099de", font=font_style)
info_label.pack(pady=10)

root.mainloop()
