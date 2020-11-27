from tkinter import *
import sqlite3
class Database:
    com = sqlite3.connect('database')
    def __init__(self, master):
        self.master = master
        master.title('Records')
        master.geometry('400x600')
    def screen(self,disclose_label, error):
        self.disclose_label = disclose_label
        self.error = error
        self.fname = Entry(root, bg = 'white', fg = 'black', borderwidth = 10,width =40)
        self.lname = Entry(root, bg = 'white', fg = 'black', borderwidth = 10,width =40)
        self.age =  Entry(root, bg = 'white', fg = 'black', borderwidth = 10,width =40)
        self.gpa =   Entry(root, bg = 'white', fg = 'black', borderwidth = 10,width =40)
        self.depart =  Entry(root, bg = 'white', fg = 'black', borderwidth = 10,width =40)
        select_input_label = Entry(root,bg = 'white', fg = 'black', borderwidth = 10,width =10)
        
        
        self.label_fname = Label(root,font = ('new times roman', 13,'normal'),text ='First name',fg ='blue')
        self.label_lname =Label(root, font = ('verdana',13,''), text = 'Last name',fg ='blue')
        self.label_age =Label(root, font = ('verdana',13,'normal'), text = 'Age',fg ='blue')
        self.label_gpa =Label(root, font = ('verdana',13,'normal'), text = 'GPA',fg ='blue')
        self.label_depart =Label(root, font = ('verdana',13,'normal'), text = 'Department',fg ='blue')
        select_oid = Label(root, text = 'Select oid',pady = 35,font =('calibra', 13, 'bold italic'),fg ='blue')

        self.fname.grid(row = 0, column =1, columnspan =3)
        self.lname.grid(row = 1, column =1, columnspan =3)
        self.age.grid(row = 2, column =1, columnspan =3)
        self.gpa.grid(row = 3, column =1, columnspan =3)
        self.depart.grid(row = 4, column =1, columnspan =3)

        self.label_fname.grid(row =0, column = 0)
        self.label_lname.grid(row =1, column = 0)
        self.label_age.grid(row =2, column = 0)
        self.label_gpa.grid(row =3, column = 0)
        self.label_depart.grid(row =4, column = 0)
        select_oid.grid(row = 5, column = 0)
        select_input_label.grid(row =5,column = 1)
        def submit():
             #connecting to database
            com = sqlite3.connect('database')
            c = com.cursor()
            if list(self.fname.get())!= [] and list(self.lname.get()) != [] and list(self.age.get())!=[] and list(self.gpa.get()) != [] and list(self.depart.get()) != []:
                #c.execute('''CREATE TABLE records(fname text, lname text, age integer, gpa real, depart text)''')
                c.execute('''INSERT INTO records  VALUES(:fname, :lname, :age, :gpa, :depart)''',{'fname':self.fname.get(),
                                                                                                                                               'lname':self.lname.get(),
                                                                                                                                                'age':self.age.get(),
                                                                                                                                                 'gpa':self.gpa.get(),
                                                                                                                                                  'depart':self.depart.get()})
                com.commit()
            
            self.fname.delete(0,END)
            self.lname.delete(0,END)
            self.age.delete(0,END)
            self.gpa.delete(0,END)
            self.depart.delete(0,END)
            
                      
        def show_records():
            #connecting to database
            com = sqlite3.connect('database')
            c = com.cursor()
            c.execute('''SELECT *,oid FROM records''')
            v = c.fetchall()
            y = ' '
            for i in v:
                y = y + str(i[0]) +' ' + str(i[1])+ ' ' + str(i[5]) +'\n' #concatenating all the words and separating them with a new line
            self.disclose_label.configure( text =y, relief = SUNKEN)
            self.disclose_label.grid(row = 8, column = 0, columnspan = 3, sticky = W+E)
            com.commit()
        def delete_records():
            #connecting to database
            com = sqlite3.connect('database')
            c = com.cursor()
            c.execute('''DELETE FROM records WHERE oid = :num''', {'num' : select_input_label.get()})
            com.commit()

        def close_records():
            #Closing record
            self.disclose_label.grid_forget()
            
        def edit_records():
            #connecting to database
            com = sqlite3.connect('database')
            c = com.cursor()
            c.execute('''SELECT *,oid FROM records''')
            v = c.fetchall()
            for i in v:
                if select_input_label.get() == str(i[5]): #Checking if the oid_num exist
                    top = Toplevel() #Creating a second window for editing
                    top.geometry('400x400')
                    top.title('Update Records')
                    fname_edit = Entry(top, bg = 'white', fg = 'black', borderwidth = 10,width =40)
                    lname_edit = Entry(top, bg = 'white', fg = 'black', borderwidth = 10,width =40)
                    age_edit =  Entry(top, bg = 'white', fg = 'black', borderwidth = 10,width =40)
                    gpa_edit =   Entry(top, bg = 'white', fg = 'black', borderwidth = 10,width =40)
                    depart_edit =  Entry(top, bg = 'white', fg = 'black', borderwidth = 10,width =40)


                    label_fname_edit = Label(top,font = ('new times roman', 13,'normal'),text ='First name',fg ='blue')
                    label_lname_edit =Label(top, font = ('verdana',13,''), text = 'Last name',fg ='blue')
                    label_age_edit =Label(top, font = ('verdana',13,'normal'), text = 'Age',fg ='blue')
                    label_gpa_edit =Label(top, font = ('verdana',13,'normal'), text = 'GPA',fg ='blue')
                    label_depart_edit =Label(top, font = ('verdana',13,'normal'), text = 'Department',fg ='blue')


                    fname_edit.grid(row = 0, column =1, columnspan =3)
                    lname_edit.grid(row = 1, column =1, columnspan =3)
                    age_edit.grid(row = 2, column =1, columnspan =3)
                    gpa_edit.grid(row = 3, column =1, columnspan =3)
                    depart_edit.grid(row = 4, column =1, columnspan =3)

                    label_fname_edit.grid(row =0, column = 0)
                    label_lname_edit.grid(row =1, column = 0)
                    label_age_edit.grid(row =2, column = 0)
                    label_gpa_edit.grid(row =3, column = 0)
                    label_depart_edit.grid(row =4, column = 0)


                    fname_edit.insert(0, i[0])
                    lname_edit.insert(0, i[1])
                    age_edit.insert(0, i[2])
                    gpa_edit.insert(0, i[3])
                    depart_edit.insert(0, i[4])
                    self.error.grid_forget()
                    
                    def update_record():
                        #Updating record in the editing window
                        com = sqlite3.connect('database')
                        c = com.cursor()
                        c.execute('''UPDATE records SET fname=:fname, lname =:lname, age=:age, gpa=:gpa, depart=:depart WHERE oid = :oid''',{'fname':fname_edit.get(),
                                                                                                                                               'lname':lname_edit.get(),
                                                                                                                                                'age':age_edit.get(),
                                                                                                                                                 'gpa':gpa_edit.get(),
                                                                                                                                                   'depart':depart_edit.get(),
                                                                                                                                                    'oid' : select_input_label.get()
                                                                                                                                                                              })
                        com.commit()
                        top.destroy()
                    #creating update record button
                    update_record = Button(top, text  = 'update record', bg = 'white', fg = 'blue',font =('calibra', 10, 'bold'), command = update_record)
                    update_record.grid(row =10, column = 1,  pady = 10)
                    break
            else:
                self.error.configure(text = 'Invalid oid entered', bg = 'white', fg = 'red', font = ('arial', 8, 'italic bold'))
                self.error.grid(row = 11, column = 0, columnspan = 3, pady = 10, ipadx = 30)
                
        #creating submit button
        submit_button =Button(root, text = 'Submit record', bg = 'blue', fg = 'White',font =('calibra', 10, 'bold'),command = submit)
        submit_button.grid(row =6, column = 0, columnspan = 3, ipadx = 140, pady = 10)

        #creating show record button
        show_record = Button(root, text  = 'Show records', bg = 'blue', fg = 'white',font =('calibra', 10, 'bold'),command = show_records)
        show_record.grid(row =7, column = 0, ipadx = 10, pady = 10)

        #creating delete record button
        delete_record = Button(root, text  = 'Delete record', bg = 'blue',fg='white',font =('calibra', 10, 'bold'), command = delete_records)
        delete_record.grid(row =7, column = 2, pady = 10, ipadx = 10)
        
         #creating close record button
        delete_record = Button(root, text  = 'Close records', bg = 'blue', fg = 'white',font =('calibra', 10, 'bold'),command = close_records)
        delete_record.grid(row =9, column = 0,  pady = 10)

         #creating edit record button
        update_record = Button(root, text  = 'Edit record', bg = 'white', fg = 'blue',font =('calibra', 10, 'bold'),command = edit_records)
        update_record.grid(row =10, column = 1,  pady = 10)
        

        
#Calling the functions and class        
root =Tk()
gui = Database(root)
error = Label(root)
disclose_label = Label(root)
gui.screen(disclose_label,error)
root.mainloop()
