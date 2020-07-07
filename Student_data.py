class Student_Data:

    def __init__(self, first_name, last_name, age, nationality, bank_sort_code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.bank_sort_code = bank_sort_code

    def email(self):
        print("{}{}@spartaglobal.com".format(self.first_name[0], self.last_name))

    # def change_bank_details(self, bank_sort_code):
    #      self.bank_sort_code = bank_sort_code

    def __change_bank_details(self, bank_sort_code):
        self.bank_sort_code = bank_sort_code

"""
Here I am creating an object, an object is an instance of a class
"""
Andrew = Student_Data("Andrew", "Osborne", 21, "British/Caribbean", 21_23_46)


# Andrew.email()

# Andrew.change_bank_details(30_44_21)

"""
This name mangling allows you to access the private method within the class
"""
#
# Andrew._Student_Data__change_bank_details(33_45_29)


# print(Andrew.bank_sort_code)

# print(Andrew.bank_sort_code)
# Andrew.change_bank_details(33_45_29)
# print(Andrew.bank_sort_code)









