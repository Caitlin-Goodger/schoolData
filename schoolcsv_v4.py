#-------------------------------------------------------------------------------
# Name:        List of schools
# Purpose:     List of schools using OOP and lists to capture school data,
#              create instance objects, store in list and write to CSV file
# History:     Enhanced to include get methods for class School.
#              Enhanced to incorporate a GUI to collect input.
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

from tkinter import *

#for Python V3 you must explicitely load the messagebox
import tkinter.messagebox


class School:
    def __init__(self, school_name, roll_size, num_classrooms, website):
        self.school_name = school_name
        self.roll_size = roll_size
        self.num_classrooms = num_classrooms
        self.website= website

    def get_school_name(self):
        return self.school_name

    def get_roll_size(self):
        return self.roll_size

    def get_num_classrooms(self):
        return self.num_classrooms

    def get_website(self):
        return self.website

    def get_average(self):
        return round(int(self.roll_size) / int(self.num_classrooms),2)

    def show_info(self):
        print("{0} has {1:.2f} pupils per room".format(self.school_name, self.get_average()))


class GUI:

    def __init__(self):

        window = Tk()
        window.title("Data Entry for public schoosl data")
        window.minsize(width=600, height=500)
        def mNew():
            mlabel3 = Label(window,text="You Clicked New").pack()
            return
        def mAbout():
            messagebox.showinfo(title="About",message="This is a program to enter infomation about schools and work out the number of student per classroom and then put it into a csv file.")
        def mQuit():
            mExit = messagebox.askokcancel(title="Quit", message="Do you want to quit?")
            if mExit > 0:
                window.destroy()
                return

        menubar = Menu (window)

        filemenu = Menu(menubar,tearoff = 0)
        filemenu.add_command(label="New", command = mNew)
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save as..")
        filemenu.add_command(label="Close", command = mQuit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar,tearoff = 0)
        helpmenu.add_command(label="Help Docs")
        helpmenu.add_command(label="About", command=mAbout)
        menubar.add_cascade(label="Help", menu=helpmenu)

        window.config(menu=menubar)

        #INITIALIZATION VARIABLES
        #this variable stores whether the data has been validated or not
        self.ready_to_write = False
        #this will contain the list of all schools entered via the gui
        self.recordlist = []
        tlabel = Label(window, text='Classes', fg = "blue")
        tlabel.config(font=("Courier", 30))
        tlabel.pack()
        #creating label and field variable in GUI for each entry field
        school_name_label = Label(window, text='Enter Public School Name:')
        school_name_label.pack() #.pack() places the component in the window
        self.school_name_field = Entry(window)
        self.school_name_field.pack()

        roll_size_label = Label(window, text='Enter roll size (number please):')
        roll_size_label.pack()
        self.roll_size_field = Entry(window)
        self.roll_size_field.pack()

        num_classrooms_label = Label(window, text='Enter Number of Classrooms:')
        num_classrooms_label.pack()
        self.num_classrooms_field = Entry(window)
        self.num_classrooms_field.pack()

        website_label = Label(window, text='School Website:')
        website_label.pack()
        self.website_field = Entry(window)
        self.website_field.pack()

        #I have decided not to validate this so I am assuming that the user puts in a valide file type. This means that it is easy for the user to change from a .csv file to a .py to a .txt
        file_label = Label(window, text='What do you want your CSV file to be called? Please include the file type eg .csv')
        file_label.pack()
        self.file_field = Entry(window)
        self.file_field.pack()

        wora_label = Label(window, text='w for Write or a for Append CSV file:')
        wora_label.pack()
        self.wora_field = Entry(window)
        self.wora_field.pack()


        #creates a button. The command function is run when the button is pressed
        #the 'command=self.doSubmit' is an example of a callback method
        button_label = Label(window, text='Press to validate:')
        button = Button(window, text='Submit', command=self.doSubmit)

        button_label1 = Label(window, text='Convert Record to csv')
        button1 = Button(window, text='Write to csv', command=self.writetocsv)

        button_label2 = Label(window, text='About This Program')
        button2 = Button(window, text='About', command=mAbout)

        button_label.pack()
        button.pack()
        button_label1.pack()
        button1.pack()
        button_label2.pack()
        button2.pack()

        #waiting for user input - event driven program
        window.mainloop()

    #Only checks in the list no the stuff that is already in the CSV file.
    def doSubmit(self):
        noduplicate = True;
        for record in self.recordlist:
            if self.school_name_field.get() == record.get_school_name():
                noduplicate= False
                tkinter.messagebox.showwarning('Warning!','Duplicate school name');
                print('Please enter school name again');

        #this is the callback method for the 'Submit' button
        if noduplicate == True:
            if len(self.school_name_field.get()) <1 or len(self.roll_size_field.get()) <1 or len(self.num_classrooms_field.get()) <1 or len(self.wora_field.get()) <1 or len(self.file_field.get()) <1 or len(self.website_field.get()) <1:
                tkinter.messagebox.showwarning('Warning!','Please enter a value for all fields')
            else:
                if self.wora_field.get() == "w" or self.wora_field.get() == "a":
                    try:
                        ##print(self.wora_field.get()) Used to make sure the right values are coming through
                        self.wora = self.wora_field.get()
                        self.file = self.file_field.get()
                        validated_roll_size = int(self.roll_size_field.get())
                        validated_num_classrooms = int(self.num_classrooms_field.get())
                        self.recordlist.append(School(self.school_name_field.get(),self.roll_size_field.get(), self.num_classrooms_field.get(), self.website_field.get()))
                        self.ready_to_write= True
                        tkinter.messagebox.showinfo('Notice','Submission Sucessful')

                        self.school_name_field.delete(0, END) #command to clear field
                        ##self.roll_size_field.delete(0, END) This is to delete what was in the roll size field
                        self.num_classrooms_field.delete(0, END)
                        self.website_field.delete(0, END)
                        self.file_field.delete(0, END)
                        self.wora_field.delete(0, END)

                    except:
                        tkinter.messagebox.showwarning('Warning!','Please enter numeric roll or classroom data')
                        print('Please enter numeric roll size or classroom data')
                else:
                    tkinter.messagebox.showwarning('Warning!','Please enter w for write or a for append for write to CSV')
                    print('Please enter w for write or a for append for write to CSV')






    def writetocsv(self):
        #this is the callback method for the 'write to csv' button
        import csv
        file_name = self.file
        ##print(self.wora) Used to check the right values are coming through
        if self.ready_to_write: #cheacks data has been previously validated
            ofile = open(file_name, self.wora) #open with write('w') or append('a') privelages
            writer = csv.writer(ofile, delimiter=',', lineterminator='\n')
            #Write in a new row and give it the heads for the info
            for record in self.recordlist:
                print(record.get_school_name())
                writer.writerow([record.get_school_name(),record.get_roll_size(), record.get_num_classrooms(), record.get_average(), record.get_website()])
            #explicitly closes the output file
            ofile.close()
            self.ready_to_write= False
            if self.wora == "a":
                tkinter.messagebox.showinfo('Notice',file_name+' Information Successfully Added')
            if self.wora == "w":
                tkinter.messagebox.showinfo('Notice',file_name+' File Successfully Generated')
        else:
            tkinter.messagebox.showwarning('Error!', 'You need to Validate your data')


#initialises the programme
GUI()