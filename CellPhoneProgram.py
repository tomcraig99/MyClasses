import CellPhoneClass as c


def main():

    cell = c.CellPhone("verizeon", "iphone 12", 799)
    print("Manufacturer:", cell.get_manufact())
    print("Model Number:", cell.get_model())
    print("Retail Price:", cell.get_retail_price())

    cell.set_manufact("Apple")
    cell.set_model("iPhone 13")
    cell.set_retail_price(1000)

    print("Manufacturer:", cell.get_manufact())
    print("Model Number:", cell.get_model())
    print("Retail Price:", cell.get_retail_price())


main()
