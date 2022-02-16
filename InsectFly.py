import InsectClass as i


def main():
    mosquito = i.Insect(2, 2)
    housefly = i.Insect(6, 10)

    print(
        "This mosquito has",
        mosquito.get_wings(),
        "wings and",
        mosquito.get_legs(),
        "legs",
    )

    print(
        "This housefly has",
        housefly.get_wings(),
        "wings and",
        housefly.get_legs(),
        "legs",
    )

    mosquito.fly()
    print("The mosquito flew", mosquito.get_distance(), "mile(s)")

    housefly.fly()
    print("The housefly flew", housefly.get_distance(), "mile(s)")


main()
