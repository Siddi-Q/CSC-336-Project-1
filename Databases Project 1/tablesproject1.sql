CREATE TABLE `patient` (
  `SSN` varchar(11) NOT NULL,
  `fullName` varchar(255) NOT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `dateOfBirth` date DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phoneNumber` varchar(20) DEFAULT NULL,
  `emergencyContactNumber` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`SSN`));
  
  CREATE TABLE `emergencycontact` (
  `SSN` varchar(11) NOT NULL,
  `fullName` varchar(255) NOT NULL,
  `phoneNumber` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`SSN`,`fullName`),
  CONSTRAINT `FK_EC` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`));
  
  CREATE TABLE `doctor` (
  `SSN` varchar(11) NOT NULL,
  `fullName` varchar(255) DEFAULT NULL,
  `DoctorId` varchar(255) NOT NULL,
  PRIMARY KEY (`SSN`,`DoctorId`),
  CONSTRAINT `FK_D` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`));
  
  CREATE TABLE `patientdiagnosis` (
  `SSN` varchar(11) NOT NULL,
  `diagnosisID` varchar(255) NOT NULL,
  `diagnosisName` varchar(255) DEFAULT NULL,
  `dateOfDiagnosis` date DEFAULT NULL,
  PRIMARY KEY (`SSN`,`diagnosisID`),
  CONSTRAINT `FK_PD` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`));
  
  CREATE TABLE `patientdrugtreatment` (
  `SSN` varchar(11) NOT NULL,
  `diagnosisID` varchar(255) NOT NULL,
  `drugId` varchar(255) DEFAULT NULL,
  `drugName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SSN`,`diagnosisID`),
  CONSTRAINT `FK_PDT` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`));
  
  CREATE TABLE `patientrecord` (
  `SSN` varchar(11) NOT NULL,
  `admissionDate` date NOT NULL,
  `releaseDate` date DEFAULT NULL,
  `fees` int DEFAULT NULL,
  PRIMARY KEY (`SSN`,`admissionDate`),
  CONSTRAINT `FK_PR` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`));
  
  CREATE TABLE `patientsurgery` (
  `SSN` varchar(11) NOT NULL,
  `surgeryID` varchar(255) NOT NULL,
  `surgeryName` varchar(255) DEFAULT NULL,
  `beginDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  `results` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SSN`,`surgeryID`),
  CONSTRAINT `FK_PS` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`));
  
  
  