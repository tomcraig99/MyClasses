import studentClass as s


def main():
    student = s.Student(100, "Andrew Jackson", "2/01/2000", "Senior")

    birth_year = 2001
    birth_month = 12
    birth_day = 4

    student.calc_age(birth_year, birth_month, birth_day)

    print(student.get_age())

    classification = "Sophomore"
    student.set_register(classification)

    print(student.get_register())


main()
