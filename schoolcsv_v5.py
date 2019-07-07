#-------------------------------------------------------------------------------
# Name:        List of schools
# Purpose:     List of schools using OOP and lists to capture school data,
#              create instance objects, store in list and write to CSV file
#              Enhanced to include get methods for class School.
#              Enhanced to incorporate a GUI to collect input.
#              Enhanced to include a pull down menu for data entry and a heading
#
# Author:      Mr. Bruce
#
# Created:     15/06/2014
# Copyright:   (c) Playtech 2014
# Licence:     CC
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

#import GUI library
from tkinter import *

#for Python V3 you must explicitely load the messagebox
import tkinter.messagebox

class School:
    def __init__(self, school_name, roll_size, num_classrooms, max_students):
        self.school_name = school_name
        self.roll_size = roll_size
        self.num_classrooms = num_classrooms
        self.max_students = max_students

    def get_school_name(self):
        return self.school_name

    def get_roll_size(self):
        return self.roll_size

    def get_num_classrooms(self):
        return self.num_classrooms

    def get_max_students(self):
        return self.max_students

    def get_average(self):
        return int(self.roll_size) / int(self.num_classrooms)

    def show_info(self):
        print("{0} has {1:.2f} pupils per room".format(self.school_name, self.get_average()))
# end of indenting means end of class definition


#create the GUI interface
class GUI:
    def __init__(self):

        # similar to root in other texts
        window = Tk()
        window.title("Data Entry for schools data")
        #setting root window and size
        window.minsize(width=600, height=400)

        heading_label = Label(window, bg="black", fg="red", text="Classes", font=("Times","24"))
        heading_label.pack()

        #INITIALIZATION VARIABLES
        #this variable stores whether the data has been validated or not
        self.ready_to_write = False
        #this will contain the list of all schools entered via the gui
        self.recordlist = []

        #creating label and field variable in GUI for each entry field
        school_name_label = Label(window, text='Enter School Name:')
        school_name_label.pack(anchor="c") #.pack() places the component in the window
        self.school_name_field = Entry(window)
        self.school_name_field.pack(anchor="c")

        roll_size_label = Label(window, text='Enter roll size:')
        roll_size_label.pack()
        self.roll_size_field = Entry(window)
        self.roll_size_field.pack()

        num_classrooms_label = Label(window, text='Enter Number of Classrooms:')
        num_classrooms_label.pack()
        self.num_classrooms_field = Entry(window)
        self.num_classrooms_field.pack()

        #code for pulldown window
        MaxStudents_label = Label(window, text='Max students')
        MaxStudents_label.pack()
        self.max_students_field = StringVar()
        OptionMenu(window, self.max_students_field, "Less than 20", "25", "30").pack()


        #creates a button. The command function is run when the button is pressed
        #the 'command=self.doSubmit' is an example of a callback method
        button_label = Label(window, text='Press to validate:')
        button = Button(window, text='Submit', command=self.doSubmit)

        button_label1 = Label(window, text='Convert Record to csv')
        button1 = Button(window, text='write to csv', command=self.writetocsv)
        button_label.pack()
        button.pack()
        button_label1.pack()
        button1.pack()



        #waiting for user input - event driven program
        window.mainloop()


    def doSubmit(self):
        #this is the callback method for the 'Submit' button
        if len(self.school_name_field.get()) <1 or len(self.roll_size_field.get()) <1 or len(self.num_classrooms_field.get()) <1 or len(self.max_students_field.get()) <1:
            tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields')
        else:
            try:
                validated_roll_size = int(self.roll_size_field.get())
                validated_num_classrooms = int(self.num_classrooms_field.get())
                self.recordlist.append(School(self.school_name_field.get(),self.roll_size_field.get(), self.num_classrooms_field.get() , self.max_students_field.get()))
                self.ready_to_write= True
                tkinter.messagebox.showinfo('Notice','Submission Sucessful')

                self.school_name_field.delete(0, END) #command to clear field
                self.roll_size_field.delete(0, END)
                self.num_classrooms_field.delete(0, END)

            except:
                tkinter.messagebox.showwarning('Warning!','Please enter numeric roll and classroom size')
                print('Please enter numeric roll and classroom size')


    def writetocsv(self):
        #this is the callback method for the 'write to csv' button
        import csv
        file_name = 'schools_database.txt'

        if self.ready_to_write: #cheacks data has been previously validated
            ofile = open(file_name, 'a') #open with write('w') or append('a') privelages
            writer = csv.writer(ofile, delimiter=',')
            #cycles through list of records created by gui
            for record in self.recordlist:
                print(record.get_school_name())
                writer.writerow([record.get_school_name(),record.get_roll_size(), record.get_num_classrooms(), record.get_average(), record.get_max_students()])
            #explicitly closes the output file
            ofile.close()
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')

        self.ready_to_write= False
        tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')

#initialises the programme
GUI()




