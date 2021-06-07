# James Choe
# miles.py
# 12/17/2020

def km_to_mi(km):
    mi = int(km) / 1.609
    return mi

def mi_to_km(mi):
    km = int(mi) * 1.609
    return km

version = input("Enter mi to convert miles to kilometers or enter km to convert kilometers to miles: ")

if version == "mi":
    mi = int(input("Enter the number of miles to convert into kilometers: "))
    km = mi_to_km(mi)
    print(f"{mi} mi is {km} km")
elif version == "km":
    km = int(input("Enter the number of kilometers to convert into miles: "))
    mi = km_to_mi(km)
    print(f"{km} km is {mi} mi")
else:
    print("Improper input.")