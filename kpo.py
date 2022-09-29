from random import randint

t = ["Kő", "Papír", "Olló"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Kő, Papír, Olló?")
    if player == computer:
        print("Döntetlen!")
    elif player == "Kő":
        if computer == "Papír":
            print("Vesztettél!", computer, "becsomagolja", player)
        else:
            print("Nyertél!", player, "üti", computer)
    elif player == "Papír":
        if computer == "Olló":
            print("Vesztettél!", computer, "vágja", player)
        else:
            print("Nyertél!", player, "becsomagolja", computer)
    elif player == "Olló":
        if computer == "Kő":
            print("Vesztettél...", computer, "üti", player)
        else:
            print("Nyertél !", player, "vágja", computer)
    else:
        print("Valami hiba történt. Ellenőrizze a helyesírást !")

    player = False
    computer = t[randint(0,2)]