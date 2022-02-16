import InsectClass as i


def main():
    myInsect = i.Insect()

    print(
        "This insect has",
        myInsect.get_wings(),
        "wings and",
        myInsect.get_legs(),
        "legs",
    )
    myInsect.fly()
    print("The insect flew", myInsect.get_distance(), "miles")


main()
