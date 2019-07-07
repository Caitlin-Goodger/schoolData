#schoolv0,.py
#note use of doctest and testmode
#created a class for school with two instances



import doctest

class School:
    def __init__(self, school_name, roll_size, num_classrooms):
        self.school_name = school_name
        self.roll_size = roll_size
        self.num_classrooms = num_classrooms

    def get_average(self):
        return self.roll_size/self.num_classrooms

    def show_info(self):
        """
            >>> s = School("Eveyln Intermediate", 1500, 96)
            >>> s.show_info()
            Eveyln Intermediate has 15.62 pupils per room
        """
        print("{0} has {1:.2f} pupils per room".format(self.school_name, self.get_average()))

def get_values():
    global school_name
    global roll_size
    global num_classrooms
    school_name = input("Name of school: ")
    roll_size = int(input("Size of school roll: "))
    num_classrooms = int(input("Number of classrooms: "))

if __name__== "__main__":
    school_name = ""; roll_size = 0; num_classrooms = 0;
    doctest.testmod(verbose = True)
    get_values()
    school1 = School(school_name,roll_size,num_classrooms)
    get_values()
    school2 = School(school_name,roll_size,num_classrooms)
    school1.show_info()
    school2.show_info()
