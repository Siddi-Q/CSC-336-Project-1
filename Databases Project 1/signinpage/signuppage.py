import sys
import mysql.connector
from tkinter import messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import signuppage_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    signuppage_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    signuppage_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def add_Patient(self):

        patient_ssn = self.SSNText.get('1.0', 'end-1c')
        patient_name = self.FullNameText.get('1.0', 'end-1c')
        dob = self.DOBText.get('1.0', 'end-1c')
        full_address = self.AddressText.get('1.0', 'end-1c')
        phone_number = self.PhoneNumberText.get('1.0', 'end-1c')
        emergency_name = self.EmergencyContactNameText.get('1.0', 'end-1c')
        e_contact_num = self.EmergencyContactNumberText.get('1.0', 'end-1c')
        gender = self.GenderText.get('1.0', 'end-1c')

        insert_patient = "INSERT INTO patient (SSN, fullName, gender, dateOfBirth, address, phoneNumber, emergencyContactNumber) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        patient_info = (patient_ssn, patient_name, gender, dob, full_address, phone_number, e_contact_num)
        insert_emergency_contact = "INSERT INTO emergencycontact (SSN, fullName, phoneNumber) VALUES (%s,%s,%s)"
        emergency_contact_info = (patient_ssn, emergency_name, e_contact_num)
        try:
            self.my_cursor.execute(insert_patient, patient_info)
            self.my_db.commit()
            self.my_cursor.execute(insert_emergency_contact, emergency_contact_info)
            self.my_db.commit()
            messagebox.showinfo('Success', "You successfully inserted patient info & emergency contact")
        except Exception:
            messagebox.showerror('Error', 'Error entering patient info: please double check patient information')

    def __init__(self, top=None):
        try:
            self.my_db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="csc336",
                database="hospital")

            self.my_cursor = self.my_db.cursor()

        except Exception:
            messagebox.showerror('Error', 'Error while connecting to mysql database')

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        top.geometry("954x1275+791+150")
        top.title("Sign Up")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.FullNameLabel = tk.Label(top)
        self.FullNameLabel.place(relx=0.21, rely=0.165, height=38, width=115)
        self.FullNameLabel.configure(activebackground="#f9f9f9")
        self.FullNameLabel.configure(activeforeground="black")
        self.FullNameLabel.configure(background="#d9d9d9")
        self.FullNameLabel.configure(disabledforeground="#a3a3a3")
        self.FullNameLabel.configure(foreground="#000000")
        self.FullNameLabel.configure(highlightbackground="#d9d9d9")
        self.FullNameLabel.configure(highlightcolor="black")
        self.FullNameLabel.configure(text='''Full Name''')

        self.SSNLabel = tk.Label(top)
        self.SSNLabel.place(relx=0.073, rely=0.227, height=38, width=255)
        self.SSNLabel.configure(activebackground="#f9f9f9")
        self.SSNLabel.configure(activeforeground="black")
        self.SSNLabel.configure(background="#d9d9d9")
        self.SSNLabel.configure(disabledforeground="#a3a3a3")
        self.SSNLabel.configure(foreground="#000000")
        self.SSNLabel.configure(highlightbackground="#d9d9d9")
        self.SSNLabel.configure(highlightcolor="black")
        self.SSNLabel.configure(text='''Social Security Number''')

        self.DateofBirthLabel = tk.Label(top)
        self.DateofBirthLabel.place(relx=0.199, rely=0.282, height=38, width=142)

        self.DateofBirthLabel.configure(activebackground="#f9f9f9")
        self.DateofBirthLabel.configure(activeforeground="black")
        self.DateofBirthLabel.configure(background="#d9d9d9")
        self.DateofBirthLabel.configure(disabledforeground="#a3a3a3")
        self.DateofBirthLabel.configure(foreground="#000000")
        self.DateofBirthLabel.configure(highlightbackground="#d9d9d9")
        self.DateofBirthLabel.configure(highlightcolor="black")
        self.DateofBirthLabel.configure(text='''Date of Birth''')

        self.FullNameText = tk.Text(top)
        self.FullNameText.place(relx=0.398, rely=0.173, relheight=0.025
                                , relwidth=0.361)
        self.FullNameText.configure(background="white")
        self.FullNameText.configure(font=font9)
        self.FullNameText.configure(foreground="black")
        self.FullNameText.configure(highlightbackground="#d9d9d9")
        self.FullNameText.configure(highlightcolor="black")
        self.FullNameText.configure(insertbackground="black")
        self.FullNameText.configure(selectbackground="#c4c4c4")
        self.FullNameText.configure(selectforeground="black")
        self.FullNameText.configure(width=344)
        self.FullNameText.configure(wrap='word')

        self.SSNText = tk.Text(top)
        self.SSNText.place(relx=0.398, rely=0.227, relheight=0.025
                           , relwidth=0.361)
        self.SSNText.configure(background="white")
        self.SSNText.configure(font=font9)
        self.SSNText.configure(foreground="black")
        self.SSNText.configure(highlightbackground="#d9d9d9")
        self.SSNText.configure(highlightcolor="black")
        self.SSNText.configure(insertbackground="black")
        self.SSNText.configure(selectbackground="#c4c4c4")
        self.SSNText.configure(selectforeground="black")
        self.SSNText.configure(width=344)
        self.SSNText.configure(wrap='word')

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
        self.AddressText.place(relx=0.398, rely=0.439, relheight=0.025
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
        self.PhoneNumberText.place(relx=0.398, rely=0.518, relheight=0.025
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

        self.GenderLabel = tk.Label(top)
        self.GenderLabel.place(relx=0.241, rely=0.376, height=38, width=92)
        self.GenderLabel.configure(activebackground="#f9f9f9")
        self.GenderLabel.configure(activeforeground="black")
        self.GenderLabel.configure(background="#d9d9d9")
        self.GenderLabel.configure(disabledforeground="#a3a3a3")
        self.GenderLabel.configure(foreground="#000000")
        self.GenderLabel.configure(highlightbackground="#d9d9d9")
        self.GenderLabel.configure(highlightcolor="black")
        self.GenderLabel.configure(text='''Gender''')

        self.AddressLabel = tk.Label(top)
        self.AddressLabel.place(relx=0.199, rely=0.439, height=38, width=135)
        self.AddressLabel.configure(activebackground="#f9f9f9")
        self.AddressLabel.configure(activeforeground="black")
        self.AddressLabel.configure(background="#d9d9d9")
        self.AddressLabel.configure(disabledforeground="#a3a3a3")
        self.AddressLabel.configure(foreground="#000000")
        self.AddressLabel.configure(highlightbackground="#d9d9d9")
        self.AddressLabel.configure(highlightcolor="black")
        self.AddressLabel.configure(text='''Full Address''')

        self.PhoneNumberLabel = tk.Label(top)
        self.PhoneNumberLabel.place(relx=0.178, rely=0.518, height=38, width=169)

        self.PhoneNumberLabel.configure(activebackground="#f9f9f9")
        self.PhoneNumberLabel.configure(activeforeground="black")
        self.PhoneNumberLabel.configure(background="#d9d9d9")
        self.PhoneNumberLabel.configure(disabledforeground="#a3a3a3")
        self.PhoneNumberLabel.configure(foreground="#000000")
        self.PhoneNumberLabel.configure(highlightbackground="#d9d9d9")
        self.PhoneNumberLabel.configure(highlightcolor="black")
        self.PhoneNumberLabel.configure(text='''Phone Number''')

        self.EmergencyContactNameLabel = tk.Label(top)
        self.EmergencyContactNameLabel.place(relx=0.01, rely=0.573, height=38
                                             , width=329)
        self.EmergencyContactNameLabel.configure(activebackground="#f9f9f9")
        self.EmergencyContactNameLabel.configure(activeforeground="black")
        self.EmergencyContactNameLabel.configure(background="#d9d9d9")
        self.EmergencyContactNameLabel.configure(disabledforeground="#a3a3a3")
        self.EmergencyContactNameLabel.configure(foreground="#000000")
        self.EmergencyContactNameLabel.configure(highlightbackground="#d9d9d9")
        self.EmergencyContactNameLabel.configure(highlightcolor="black")
        self.EmergencyContactNameLabel.configure(text='''Emergency Contact Full Name''')

        self.EmergencyContactNameText = tk.Text(top)
        self.EmergencyContactNameText.place(relx=0.398, rely=0.573
                                            , relheight=0.025, relwidth=0.361)
        self.EmergencyContactNameText.configure(background="white")
        self.EmergencyContactNameText.configure(font=font9)
        self.EmergencyContactNameText.configure(foreground="black")
        self.EmergencyContactNameText.configure(highlightbackground="#d9d9d9")
        self.EmergencyContactNameText.configure(highlightcolor="black")
        self.EmergencyContactNameText.configure(insertbackground="black")
        self.EmergencyContactNameText.configure(selectbackground="#c4c4c4")
        self.EmergencyContactNameText.configure(selectforeground="black")
        self.EmergencyContactNameText.configure(width=344)
        self.EmergencyContactNameText.configure(wrap='word')

        self.EmergencyContactNumberText = tk.Text(top)
        self.EmergencyContactNumberText.place(relx=0.398, rely=0.651
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

        self.EmergencyNumberLabel = tk.Label(top)
        self.EmergencyNumberLabel.place(relx=0.031, rely=0.651, height=38
                                        , width=308)
        self.EmergencyNumberLabel.configure(activebackground="#f9f9f9")
        self.EmergencyNumberLabel.configure(activeforeground="black")
        self.EmergencyNumberLabel.configure(background="#d9d9d9")
        self.EmergencyNumberLabel.configure(disabledforeground="#a3a3a3")
        self.EmergencyNumberLabel.configure(foreground="#000000")
        self.EmergencyNumberLabel.configure(highlightbackground="#d9d9d9")
        self.EmergencyNumberLabel.configure(highlightcolor="black")
        self.EmergencyNumberLabel.configure(text='''Emergency Contact Number''')

        self.SubmitButton = tk.Button(top)
        self.SubmitButton.place(relx=0.325, rely=0.776, height=64, width=312)
        self.SubmitButton.configure(activebackground="#d9d9d9")
        self.SubmitButton.configure(activeforeground="#000000")
        self.SubmitButton.configure(background="#d9d9d9")
        self.SubmitButton.configure(disabledforeground="#a3a3a3")
        self.SubmitButton.configure(foreground="#000000")
        self.SubmitButton.configure(highlightbackground="#d9d9d9")
        self.SubmitButton.configure(highlightcolor="black")
        self.SubmitButton.configure(pady="0")
        self.SubmitButton.configure(text='''Submit''')
        self.SubmitButton.configure(command=self.add_Patient)

        self.GenderText = tk.Text(top)
        self.GenderText.place(relx=0.398, rely=0.376, relheight=0.025
                              , relwidth=0.361)
        self.GenderText.configure(background="white")
        self.GenderText.configure(font=font9)
        self.GenderText.configure(foreground="black")
        self.GenderText.configure(highlightbackground="#d9d9d9")
        self.GenderText.configure(highlightcolor="black")
        self.GenderText.configure(insertbackground="black")
        self.GenderText.configure(selectbackground="#c4c4c4")
        self.GenderText.configure(selectforeground="black")
        self.GenderText.configure(width=344)
        self.GenderText.configure(wrap='word')

        self.menubar = tk.Menu(top, font=font9, bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.DateFormatLabel = tk.Label(top)
        self.DateFormatLabel.place(relx=0.786, rely=0.282, height=38, width=142)
        self.DateFormatLabel.configure(activebackground="#f9f9f9")
        self.DateFormatLabel.configure(activeforeground="black")
        self.DateFormatLabel.configure(background="#d9d9d9")
        self.DateFormatLabel.configure(disabledforeground="#a3a3a3")
        self.DateFormatLabel.configure(foreground="#000000")
        self.DateFormatLabel.configure(highlightbackground="#d9d9d9")
        self.DateFormatLabel.configure(highlightcolor="black")
        self.DateFormatLabel.configure(text='''YYYYMMDD''')
        self.DateFormatLabel.configure(width=142)


if __name__ == '__main__':
    vp_start_gui()