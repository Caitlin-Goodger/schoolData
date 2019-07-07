#-------------------------------------------------------------------------------
# Name:        List of schools
# Purpose:     List of schools using OOP and lists to capture school data,
#              create instance objects, store in list and write to CSV file
#              Enhanced to include get methods for class School.
#-------------------------------------------------------------------------------


import csv

class School:
    def __init__(self, school_name, roll_size, num_classrooms):
        self.school_name = school_name
        self.roll_size = roll_size
        self.num_classrooms = num_classrooms

    def get_school_name(self):
        return self.school_name

    def get_roll_size(self):
        return self.roll_size

    def get_num_classrooms(self):
        return self.num_classrooms

    def get_average(self):
        return self.roll_size/self.num_classrooms

    def show_info(self):
        print("{0} has {1:.2f} pupils per room".format(self.school_name, self.get_average()))
# end of indenting means end of class definition

# get_values is an ordinary function
def get_values():
    global school_name
    global roll_size
    global num_classrooms
    school_name = input("Name of school: ")
    roll_size = int(input("Size of school roll: "))
    num_classrooms = int(input("Number of classrooms: "))


schools = []
for i in range (2):
    get_values()
    #when we append School we are running the object init method hence the object is stored in the list
    schools.append(School(school_name,roll_size,num_classrooms))

for school in schools:
    school.show_info()


file_name = 'schoolsdb2.txt'

ofile = open(file_name, 'w') #open with write('w') or append('a') privelages
writer = csv.writer(ofile, delimiter=',',lineterminator='\n')
#cycles through list of records created by gui

for school in schools:
# the following code is used for debugging purposes
    print(schools[i].school_name)
    print(schools[i].roll_size)
    print(schools[i].num_classrooms)
    print(school.get_school_name())
    print(school.get_roll_size())
    print(school.get_num_classrooms())
#we write the object contents out as a list...
    writer.writerow([school.get_school_name(),school.get_roll_size(),school.get_num_classrooms()])

#explicitly closes the output file
ofile.close()







