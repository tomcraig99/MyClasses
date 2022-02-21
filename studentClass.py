class Student:
    def __init__(self, studentID, name, birth, classification):
        self.studentID = studentID
        self.name = name
        self.birth = birth
        self.classification = classification

    def calc_age(self, birth_year, birth_month, birth_day):
        self.__year, self.__month, self.__day = 2022, 2, 21
        self.__age_year = 0
        self.__age_year = self.__year - birth_year
        if birth_month < self.__month:
            self.__age_year += 1
        elif birth_month == self.__month:
            if birth_day < self.__day:
                self.__age_year += 1

    def set_register(self, classification):
        if classification.lower() == "senior":
            self.__register = "4/1 through 4/3"
        elif classification.lower() == "junior":
            self.__register = "4/4 through 4/6"
        elif classification.lower() == "sophomore":
            self.__register = "4/7 through 4/9"
        elif classification == "freshman":
            self.__register = "4/10 through 4/12"
        else:
            self.__register = "Invalid class"

    def get_age(self):
        return self.__age_year

    def get_register(self):
        return self.__register
