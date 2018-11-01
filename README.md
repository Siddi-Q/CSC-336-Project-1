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
* Have the same hospital database tables (schemas)
* Make necessary database configurations in the code (more info below) 

Recommended steps to take to using the software:
* run the signuppage.py file, fill in all textboxes and submit, if you want to signin multiple patients be sure to change the SSN (see below for further info on the functions)
* run admin_doctor_window.py
* press the Show Information button in the Patient information frame
* Before you can show/update info in the other frames, you need to submit (insert) the necessary values (see below for further info on the functions)
* have fun playing around with the software!
* report any bugs/issues/needed improvements etc. 

Significant Project Files:
* export.sql

Note: Use this file to recreate our hospital database onto your local machine
  
* signuppage.py

Path: CSC-336-Project-1\Databases Project 1\signinpage\signuppage.py
  
Description: This file will open a Desktop GUI that a patient will use to signin.
  
Necesary Program Changes needed to be made by programmer:

  * In def __init__(self, top=None):, in the first try block adjust the host, user, and password fields to your preferred settings.

Function Name: def add_Patient(self)

Description: After inputing the values, this function will store them in the hospital database

Constraints: Need to input values into all textboxes.

* admin_doctor_window.py

Path: CSC-336-Project-1\Databases Project 1\admin-doctor-window\admin_doctor_window.py
  
Description: This file will open a Desktop GUI that an admin/hospital persoanel can use to show, add and update patient information.
  
Necesary Program Changes needed to be made by programmer:

  * In def __init__(self, top=None):, in the first try block adjust the host, user, and password fields to your preferred settings.

Function Name: def show_contact_info(self)

Description: This function will be executed once the Show Contact Information button, which is in the Emergency Contact Information  frame, is pressed. Given an ssn, this function will list a pateint's SSN and fullName. Aswell as the patients' emergency contact's  fullName and phoneNumber.

Button, Frame: Show Contact Information, Emergency Contact Information

Constraints: Need to input a SSN in the patient SSN text box. To get a result, that patient's SSN must exist in the patient table and emergencycontact table.

Output Format: (patient.SSN, patient.fullName, emergencycontact.fullName, emergencycontact.phoneNumber)

Function Name: def show_diagnosis(self)

Button, Frame: Show Diagnosis, Patient Diagnosis

Description: This function will be executed once the Show Diagnosis button, which is in the Patient Diagnosis frame, is pressed. Given an SSN, this function will list a pateint's SSN, fullName, diagnosisID, diagnosisName, and dateOfDiagnosis.

Constraints: Need to input a SSN in the patient SSN box. To get a result, that patient's SSN must exist in the patient table and patientdiagnosis table.

Output Format: (patient.SSN, patient.fullName, patientdiagnosis.diagnosisID, patientdiagnosis.diagnosisName, patientdiagnosis.dateOfDiagnosis)

Function Name: def update_diagnosis(self)

Button, Frame: Update, Patient Diagnosis

Description: This function will be executed once the Update button, which is in the Patient Diagnosis frame, is pressed. This function will update a patients diagnosis info.

Constraints: Need to input a patients SSN and diagnosisId, both of which need to already exist in the table. You can't update either attribute with this function.
 
Function Name: def submit_diagnosis(self)

Button, Frame: Submit, Patient Diagnosis

Description: This function will be executed once the Submit button, which is in the Patient Diagnosis frame, is pressed. This function will insert a patient's diagnosis information into the patientdiagnosis table.

Constraints: Need to fill in all fields.

Function Name: def show_drug_treatment(self)

Button, Frame: Show Drug Treatments, Patient Drug Treatment

Description: This function will be executed once the Show Drug Treatments button, which is in the Patient Drug Treatment frame, is pressed. Given an SSN, this function will list a pateint's SSN, fullName and the diagnosisID, drugId, and drugName.

Constraints: Need to input a SSN in the patient SSN box. To get a result, that patient's SSN must exist in the patient table and the patientdrugtreatment table.

Output Format: (patient.SSN, patient.fullName, patientdrugtreatment.diagnosisID, patientdrugtreatment.drugId, patientdrugtreatment.drugName)

Function Name: def update_drug_treatment(self)

Button, Frame: Update, Patient Drug Treatment

Description: This function will be executed once the Update button, which is in the Patient Drug Treatment frame, is pressed. This function will update a patients drug treatment info.

Constraints: Need to input a patients SSN and diagnosisId, both of which need to already exist in the table. You can't update either attribute with this function.

Function Name: def submit_drug_treatment(self)

Button, Frame: Submit, Patient Drug Treatment

Description: This function will be executed once the Submit button, which is in the Patient Drug Treatment frame, is pressed. This function will insert a patient's diagnosis information into the patientdrugtreatemnt table.

Constraints: Need to fill in all fields.

Function Name: def show_patient_info(self)

Button, Frame: Show Information, Patient Information

Description: Takes patient SSN and displays full name, gender, dat of birth, address, phone number, and emergency contact phone number (all of which are in the 'patient' table)

Output Format: (patient.SSN, patient.fullName, patient.gender, patient.dateOfBirth, patient.address, patient.phoneNumber, patient.emergencyContactNumber)

Function Name: def update_patient_info(self)

Button, Frame: Update, Patient Information

Description: Takes input from user (patient name, gender, dob, address, phone number, and emergency phone number) stores each value into its own variable, and updates the patient whose ssn matches the one input by user in the patient table. Furthermore, emergency contact number is updated in the emergency contact table

Constraints: Need to input a patients SSN, it needs to already exist in the table. You can't update this attribute.

Function Name: def insert_patient_records(self)

Button, Frame: Submit, Patient Records

Description: Takes input from user (as update_patient does) and inserts these values as a new member of the patient table, with the exception of emergency contact

Constraints: Need to fill in all fields

Function Name: def show_patient_records(self)

Button, Frame: Show Records, Patient Records

Description: Takes patient SSN and displays full name, admission date, release date, and hospital fees 

Constraints: Need to input a SSN in the patient SSN box. To get a result, that patient's SSN must exist in the patient table and the patientrecord table.

Output Format: (patientrecord.SSN, patient.fullName, patientrecord.admissionDate, patientrecord.releaseDate, patientrecord.fees)

Function Name: def update_patient_records(self)

Button, Frame: Update, Patient Records

Description: Takes input from user (patient full name, admission date, release date, and hospital fees) stores each value into its own variable, and updates the patient whose ssn matches the one input by user in the patient records table.

Constraints: Need to input a patients SSN and admissionDate, both of which need to already exist in the table. You can't update either attribute with this function.

Function Name: def insert_patient_surgery(self)

Button, Frame: Submit, Patient Surgeries

Description: Takes patients ssn, a unique surgery id, surgery name, surgery start date, end date, & results and adds it to the patient surgeries table 

Constraints: Need to fill in all fields

Function Name: def show_surgery(self)

Button, Frame: Show Surgeries, Patient Surgeries

Description: Takes patient SSN, and displays full name, surgery id, surgery name, begin date, end date, and results from the patient surgeries table 

Constraints: Need to input a SSN in the patient SSN box. To get a result, that patient's SSN must exist in the patient table and the patientsurgery table.

Output Format: (patientsurgery.SSN, patient.fullName, patientsurgery.surgeryID, patientsurgery.surgeryName, patientsurgery.beginDate, patientsurgery.endDate, patientsurgery.results)

Function Name: def update_surgery(self)

Button, Frame: Update, Patient Surgeries

Description: takes input from user (patient ssn, surgery id, surgery name, begin date, end date, and results) and makes changes to the inputted attributes (besides ssn), if there are any to be made

Constraints: Need to fill in all fields.

* app.py

  Path: CSC-336-Project-1\Databases Project 1\app.py
  
  Description: This is the signin page that can be accessed on a webbrowser.
  
  Necesary Program Changes needed to be made by programmer:

  * Adjust the app.config['MYSQL_DATABASE_USER'], app.config['MYSQL_DATABASE_PASSWORD'] etc. to your preferred settings/values.
   
