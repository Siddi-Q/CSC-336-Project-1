# CSC-336-Project-1
<hr></hr>

Team Name: Team Seek Well

Project: Patient Management System (PMS)

By:
* Satesh Ramnath
* Saddique Shafi
* Kareem Soliman
* Hamza Shahzad

Prerequisites:
* Have Python 3 installed
* Have Oracle MySQL installed
* Have Python/MySQL connector installed

Significant Project Files:
* signuppage.py

  Path: CSC-336-Project-1\Databases Project 1\signinpage\signuppage.py
  
  Description: This file will open a Desktop GUI that a patient will use to signin.
  
  Necesary Program Changes needed to be made by programmer:

  * 

Function Name: def add_Patient(self)

Descriptions: After inputing the values, this function will store them in the hospital database

Constraints: Need to input values into all textboxes.

* admin_doctor_window.py

  Path: CSC-336-Project-1\Databases Project 1\admin-doctor-window\admin_doctor_window.py
  
  Description: This file will open a Desktop GUI that an admin/hospital persoanel can use to show, add and update patient information.
  
  Necesary Program Changes needed to be made by programmer:

  * 

Function Name: def show_contact_info(self)

Descriptions: This function will be executed once the Show Contact Information button, which is in the Emergency Contact Information frame, is pressed. This will list a pateints SSN and fullName. Aswell as the patients emergency contacts fullName and phoneNumber.

Constraints: Need to input a SSN in the patient SSN text box. To get a result that persons SSN must exist in the patient table and emergencycontact table

Function Name: def show_diagnosis(self)

Descriptions: 

Constraints:

Function Name: def update_diagnosis(self)

Descriptions: 

Constraints:

Function Name: def submit_diagnosis(self)

Descriptions: 

Constraints:

Function Name: def show_drug_treatment(self)

Descriptions: 

Constraints:

Function Name: def update_drug_treatment(self)

Descriptions: 

Constraints:

Function Name: def submit_drug_treatment(self)

Descriptions: 

Constraints:

Function Name: def show_patient_info(self)

Descriptions: Descriptions: Takes patient SSN and displays full name, gender, dat of birth, address, phone number, and emergency contact phone number (all of which are in the 'patient' table)

Constraints: User needs to enter a valid social security number

Function Name: def update_patient_info(self)

Descriptions: Takes input from user (patient name, gender, dob, address, phone number, and emergency phone number) stores each value into its own variable, and updates the patient whose ssn matches the one input by user in the patient table. Furthermore, emergency contact number is updated in the emergency contact table

Constraints: All fields in the patient info frame must be filled out to successfully update a patients information

Function Name: def insert_patient_records(self)

Descriptions: Takes input from user (as update_patient does) and inserts these values as a new member of the patient table, with the exception of emergency contact

Constraints: Must fill all values to create a new patient

Function Name: def show_patient_records(self)

Descriptions: Takes patient SSN and displays full name, admission date, release date, and hospital fees 

Constraints: User needs to enter a valid social security number

Function Name: def update_patient_records(self)

Descriptions: Takes input from user (patient full name, admission date, release date, and hospital fees) stores each value into its own variable, and updates the patient whose ssn matches the one input by user in the patient records table.

Constraints: All fields in the patient records frame must be filled out to successfully update a patients information

Function Name: def insert_patient_surgery(self)

Descriptions: Takes patients ssn, a unique surgery id, surgery name, surgery start date, end date, & results and adds it to the patient surgeries table 

Constraints: All fields in patient surgery frame must be filled out to insert a new patient into patient surgeries table

Function Name: def show_surgery(self)

Descriptions: Takes patient SSN, and displays full name, surgery id, surgery name, begin date, end date, and results from the patient surgeries table 

Constraints: Requires patient ssn 

Function Name: def update_surgery(self)

Descriptions: takes input from user (patient ssn, surgery id, surgery name, begin date, end date, and results) and makes changes to the inputted attributes (besides ssn), if there are any to be made

Constraints: Required all fields in the patient surgery frame to be filled out

* app.py

  Path: CSC-336-Project-1\Databases Project 1\
  
  Description: 
  
  Necesary Program Changes needed to be made by programmer:

  * 

Function Name: 

Descriptions: 

Constraints:
