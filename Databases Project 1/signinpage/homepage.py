import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def add_Patient(self):

        first_name = self.FirstNameText.get('1.0', 'end-1c')
        last_name = self.LastNameText.get('1.0', 'end-1c')
        dob = self.DOBText.get('1.0', 'end-1c')
        full_address = self.AddressText.get('1.0', 'end-1c')
        phone_number = self.PhoneNumberText.get('1.0', 'end-1c')
        e_contact_fn = self.EmergencyFirstNameText.get('1.0', 'end-1c')
        e_contact_ln = self.EmergencyContactLastNameText.get('1.0', 'end-1c')
        e_contact_num = self.EmergencyContactNumberText.get('1.0', 'end-1c')

        try:
            sql_insert = "INSERT INTO patient (firstname, lastname, dateofbirth, fulladdress, phonenumber,  emergencycontactfirstname, emergencycontactlastname,emergencycontactnumber) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            patient_info = (
            first_name, last_name, dob, full_address, phone_number, e_contact_fn, e_contact_ln, e_contact_num)
            self.my_cursor.execute(sql_insert, patient_info)
            self.my_db.commit()
        except:
            messagebox.showerror('Error', 'Error in insertion, please make sure you entered all values as indicated')

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        self.FirstNameLabel = tk.Label(top)
        self.FirstNameLabel.place(relx=0.22, rely=0.165, height=38, width=121)
        self.FirstNameLabel.configure(background="#d9d9d9")
        self.FirstNameLabel.configure(disabledforeground="#a3a3a3")
        self.FirstNameLabel.configure(foreground="#000000")
        self.FirstNameLabel.configure(text='''First Name''')

        self.LastNameLabel = tk.Label(top)
        self.LastNameLabel.place(relx=0.231, rely=0.227, height=38, width=118)
        self.LastNameLabel.configure(background="#d9d9d9")
        self.LastNameLabel.configure(disabledforeground="#a3a3a3")
        self.LastNameLabel.configure(foreground="#000000")
        self.LastNameLabel.configure(text='''Last Name''')

        self.DateofBirthLabel = tk.Label(top)
        self.DateofBirthLabel.place(relx=0.231, rely=0.282, height=38, width=142)

        self.DateofBirthLabel.configure(background="#d9d9d9")
        self.DateofBirthLabel.configure(disabledforeground="#a3a3a3")
        self.DateofBirthLabel.configure(foreground="#000000")
        self.DateofBirthLabel.configure(text='''Date of Birth''')

        self.FirstNameText = tk.Text(top)
        self.FirstNameText.place(relx=0.398, rely=0.173, relheight=0.025
                                 , relwidth=0.361)
        self.FirstNameText.configure(background="white")
        self.FirstNameText.configure(font=font9)
        self.FirstNameText.configure(foreground="black")
        self.FirstNameText.configure(highlightbackground="#d9d9d9")
        self.FirstNameText.configure(highlightcolor="black")
        self.FirstNameText.configure(insertbackground="black")
        self.FirstNameText.configure(selectbackground="#c4c4c4")
        self.FirstNameText.configure(selectforeground="black")
        self.FirstNameText.configure(width=344)
        self.FirstNameText.configure(wrap='word')

        self.LastNameText = tk.Text(top)
        self.LastNameText.place(relx=0.398, rely=0.227, relheight=0.025
                                , relwidth=0.361)
        self.LastNameText.configure(background="white")
        self.LastNameText.configure(cursor="fleur")
        self.LastNameText.configure(font=font9)
        self.LastNameText.configure(foreground="black")
        self.LastNameText.configure(highlightbackground="#d9d9d9")
        self.LastNameText.configure(highlightcolor="black")
        self.LastNameText.configure(insertbackground="black")
        self.LastNameText.configure(selectbackground="#c4c4c4")
        self.LastNameText.configure(selectforeground="black")
        self.LastNameText.configure(width=344)
        self.LastNameText.configure(wrap='word')

        self.DOBText = tk.Text(top)
        self.DOBText.place(relx=0.398, rely=0.282, relheight=0.025
                           , relwidth=0.361)
        self.DOBText.configure(background="white")
        self.DOBText.configure(font=font9)
        self.DOBText.configure(foreground="black")
        self.DOBText.configure(highlightbackground="#d9d9d9")
        self.DOBText.configure(highlightcolor="black")
        self.DOBText.configure(insertbackground="black")
        self.DOBText.configure(selectbackground="#c4c4c4")
        self.DOBText.configure(selectforeground="black")
        self.DOBText.configure(width=344)
        self.DOBText.configure(wrap='word')

        self.AddressText = tk.Text(top)
        self.AddressText.place(relx=0.398, rely=0.4, relheight=0.025
                               , relwidth=0.507)
        self.AddressText.configure(background="white")
        self.AddressText.configure(font=font9)
        self.AddressText.configure(foreground="black")
        self.AddressText.configure(highlightbackground="#d9d9d9")
        self.AddressText.configure(highlightcolor="black")
        self.AddressText.configure(insertbackground="black")
        self.AddressText.configure(selectbackground="#c4c4c4")
        self.AddressText.configure(selectforeground="black")
        self.AddressText.configure(width=484)
        self.AddressText.configure(wrap='word')

        self.PhoneNumberText = tk.Text(top)
        self.PhoneNumberText.place(relx=0.398, rely=0.455, relheight=0.025
                                   , relwidth=0.361)
        self.PhoneNumberText.configure(background="white")
        self.PhoneNumberText.configure(font=font9)
        self.PhoneNumberText.configure(foreground="black")
        self.PhoneNumberText.configure(highlightbackground="#d9d9d9")
        self.PhoneNumberText.configure(highlightcolor="black")
        self.PhoneNumberText.configure(insertbackground="black")
        self.PhoneNumberText.configure(selectbackground="#c4c4c4")
        self.PhoneNumberText.configure(selectforeground="black")
        self.PhoneNumberText.configure(width=344)
        self.PhoneNumberText.configure(wrap='word')

        self.MaleRadioButton = tk.Radiobutton(top)
        self.MaleRadioButton.place(relx=0.398, rely=0.337, relheight=0.036
                                   , relwidth=0.09)
        self.MaleRadioButton.configure(activebackground="#d9d9d9")
        self.MaleRadioButton.configure(activeforeground="#000000")
        self.MaleRadioButton.configure(background="#d9d9d9")
        self.MaleRadioButton.configure(disabledforeground="#a3a3a3")
        self.MaleRadioButton.configure(foreground="#000000")
        self.MaleRadioButton.configure(highlightbackground="#d9d9d9")
        self.MaleRadioButton.configure(highlightcolor="black")
        self.MaleRadioButton.configure(justify='left')
        self.MaleRadioButton.configure(text='''Male''')

        self.FemaleRadioButton = tk.Radiobutton(top)
        self.FemaleRadioButton.place(relx=0.545, rely=0.337, relheight=0.036
                                     , relwidth=0.115)
        self.FemaleRadioButton.configure(activebackground="#d9d9d9")
        self.FemaleRadioButton.configure(activeforeground="#000000")
        self.FemaleRadioButton.configure(background="#d9d9d9")
        self.FemaleRadioButton.configure(disabledforeground="#a3a3a3")
        self.FemaleRadioButton.configure(foreground="#000000")
        self.FemaleRadioButton.configure(highlightbackground="#d9d9d9")
        self.FemaleRadioButton.configure(highlightcolor="black")
        self.FemaleRadioButton.configure(justify='left')
        self.FemaleRadioButton.configure(text='''Female''')

        self.GenderLabel = tk.Label(top)
        self.GenderLabel.place(relx=0.262, rely=0.337, height=38, width=92)
        self.GenderLabel.configure(background="#d9d9d9")
        self.GenderLabel.configure(disabledforeground="#a3a3a3")
        self.GenderLabel.configure(foreground="#000000")
        self.GenderLabel.configure(text='''Gender''')
        self.GenderLabel.configure(width=92)

        self.AddressLabel = tk.Label(top)
        self.AddressLabel.place(relx=0.231, rely=0.392, height=38, width=135)
        self.AddressLabel.configure(background="#d9d9d9")
        self.AddressLabel.configure(disabledforeground="#a3a3a3")
        self.AddressLabel.configure(foreground="#000000")
        self.AddressLabel.configure(text='''Full Address''')

        self.PhoneNumberLabel = tk.Label(top)
        self.PhoneNumberLabel.place(relx=0.189, rely=0.455, height=38, width=169)

        self.PhoneNumberLabel.configure(background="#d9d9d9")
        self.PhoneNumberLabel.configure(disabledforeground="#a3a3a3")
        self.PhoneNumberLabel.configure(foreground="#000000")
        self.PhoneNumberLabel.configure(text='''Phone Number''')

        self.EmergencyFirstNameLabel = tk.Label(top)
        self.EmergencyFirstNameLabel.place(relx=0.031, rely=0.525, height=38
                                           , width=335)
        self.EmergencyFirstNameLabel.configure(background="#d9d9d9")
        self.EmergencyFirstNameLabel.configure(disabledforeground="#a3a3a3")
        self.EmergencyFirstNameLabel.configure(foreground="#000000")
        self.EmergencyFirstNameLabel.configure(text='''Emergency Contact First Name''')

        self.EmergencyFirstNameText = tk.Text(top)
        self.EmergencyFirstNameText.place(relx=0.398, rely=0.525, relheight=0.025
                                          , relwidth=0.361)
        self.EmergencyFirstNameText.configure(background="white")
        self.EmergencyFirstNameText.configure(font=font9)
        self.EmergencyFirstNameText.configure(foreground="black")
        self.EmergencyFirstNameText.configure(highlightbackground="#d9d9d9")
        self.EmergencyFirstNameText.configure(highlightcolor="black")
        self.EmergencyFirstNameText.configure(insertbackground="black")
        self.EmergencyFirstNameText.configure(selectbackground="#c4c4c4")
        self.EmergencyFirstNameText.configure(selectforeground="black")
        self.EmergencyFirstNameText.configure(width=344)
        self.EmergencyFirstNameText.configure(wrap='word')

        self.EmergencyContactLastNameText = tk.Text(top)
        self.EmergencyContactLastNameText.place(relx=0.398, rely=0.588
                                                , relheight=0.025, relwidth=0.371)
        self.EmergencyContactLastNameText.configure(background="white")
        self.EmergencyContactLastNameText.configure(font=font9)
        self.EmergencyContactLastNameText.configure(foreground="black")
        self.EmergencyContactLastNameText.configure(highlightbackground="#d9d9d9")
        self.EmergencyContactLastNameText.configure(highlightcolor="black")
        self.EmergencyContactLastNameText.configure(insertbackground="black")
        self.EmergencyContactLastNameText.configure(selectbackground="#c4c4c4")
        self.EmergencyContactLastNameText.configure(selectforeground="black")
        self.EmergencyContactLastNameText.configure(width=354)
        self.EmergencyContactLastNameText.configure(wrap='word')

        self.EmergencyContactNumberText = tk.Text(top)
        self.EmergencyContactNumberText.place(relx=0.409, rely=0.651
                                              , relheight=0.025, relwidth=0.361)
        self.EmergencyContactNumberText.configure(background="white")
        self.EmergencyContactNumberText.configure(font=font9)
        self.EmergencyContactNumberText.configure(foreground="black")
        self.EmergencyContactNumberText.configure(highlightbackground="#d9d9d9")
        self.EmergencyContactNumberText.configure(highlightcolor="black")
        self.EmergencyContactNumberText.configure(insertbackground="black")
        self.EmergencyContactNumberText.configure(selectbackground="#c4c4c4")
        self.EmergencyContactNumberText.configure(selectforeground="black")
        self.EmergencyContactNumberText.configure(width=344)
        self.EmergencyContactNumberText.configure(wrap='word')

        self.EmergencyLastNameLabel = tk.Label(top)
        self.EmergencyLastNameLabel.place(relx=0.031, rely=0.588, height=38
                                          , width=332)
        self.EmergencyLastNameLabel.configure(background="#d9d9d9")
        self.EmergencyLastNameLabel.configure(disabledforeground="#a3a3a3")
        self.EmergencyLastNameLabel.configure(foreground="#000000")
        self.EmergencyLastNameLabel.configure(text='''Emergency Contact Last Name''')

        self.EmergencyNumberLabel = tk.Label(top)
        self.EmergencyNumberLabel.place(relx=0.052, rely=0.651, height=38
                                        , width=308)
        self.EmergencyNumberLabel.configure(background="#d9d9d9")
        self.EmergencyNumberLabel.configure(disabledforeground="#a3a3a3")
        self.EmergencyNumberLabel.configure(foreground="#000000")
        self.EmergencyNumberLabel.configure(text='''Emergency Contact Number''')

        self.SubmitButton = tk.Button(top)
        self.SubmitButton.place(relx=0.325, rely=0.745, height=64, width=312)
        self.SubmitButton.configure(activebackground="#d9d9d9")
        self.SubmitButton.configure(activeforeground="#000000")
        self.SubmitButton.configure(background="#d9d9d9")
        self.SubmitButton.configure(disabledforeground="#a3a3a3")
        self.SubmitButton.configure(foreground="#000000")
        self.SubmitButton.configure(highlightbackground="#d9d9d9")
        self.SubmitButton.configure(highlightcolor="black")
        self.SubmitButton.configure(pady="0")
        self.SubmitButton.configure(text='''Submit''')
        self.SubmitButton.configure(width=312)
        self.SubmitButton.configure(command=self.add_Patient)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()