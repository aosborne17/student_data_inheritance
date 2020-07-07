import random
from Student_data import *

class DevOps_Student(Student_Data):

    """
    Using the super () function allows for initilization of the attributes from the parent class
    without having to manually do so.
    """
    def __init__(self, first_name, last_name, age, nationality, bank_sort_code, stream, sparta_rank):
        super().__init__(first_name, last_name, age, nationality, bank_sort_code)
        self.stream = stream
        self.sparta_rank = sparta_rank

    def study(self):
            sparta_rank = 0
            num_1 = random.randint(1, 10)
            num_2 = random.randint(1, 10)
            answer = num_1 * num_2
            guess = int(input("What is {} * {}: ".format(num_1, num_2)))
            if guess == answer:
                self.sparta_rank += 1
                print("Correct!")
            elif guess != answer:
                print("Incorrect!")
            print("Sparta rank is now --> {}".format(self.sparta_rank))


Andrew = DevOps_Student("Andrew", "Osborne", 21, "British/Caribbean", 21_23_46, "DevOps", 0)

# Andrew.study()

Andrew.email()