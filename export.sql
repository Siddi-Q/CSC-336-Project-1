-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `doctor` (
  `SSN` varchar(11) NOT NULL,
  `fullName` varchar(255) DEFAULT NULL,
  `DoctorId` varchar(255) NOT NULL,
  PRIMARY KEY (`SSN`,`DoctorId`),
  CONSTRAINT `FK_D` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emergencycontact`
--

DROP TABLE IF EXISTS `emergencycontact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `emergencycontact` (
  `SSN` varchar(11) NOT NULL,
  `fullName` varchar(255) NOT NULL,
  `phoneNumber` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`SSN`,`fullName`),
  CONSTRAINT `FK_EC` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emergencycontact`
--

LOCK TABLES `emergencycontact` WRITE;
/*!40000 ALTER TABLE `emergencycontact` DISABLE KEYS */;
/*!40000 ALTER TABLE `emergencycontact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `patient` (
  `SSN` varchar(11) NOT NULL,
  `fullName` varchar(255) NOT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `dateOfBirth` date DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phoneNumber` varchar(20) DEFAULT NULL,
  `emergencyContactNumber` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientdiagnosis`
--

DROP TABLE IF EXISTS `patientdiagnosis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `patientdiagnosis` (
  `SSN` varchar(11) NOT NULL,
  `diagnosisID` varchar(255) NOT NULL,
  `diagnosisName` varchar(255) DEFAULT NULL,
  `dateOfDiagnosis` date DEFAULT NULL,
  PRIMARY KEY (`SSN`,`diagnosisID`),
  CONSTRAINT `FK_PD` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientdiagnosis`
--

LOCK TABLES `patientdiagnosis` WRITE;
/*!40000 ALTER TABLE `patientdiagnosis` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientdiagnosis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientdrugtreatment`
--

DROP TABLE IF EXISTS `patientdrugtreatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `patientdrugtreatment` (
  `SSN` varchar(11) NOT NULL,
  `diagnosisID` varchar(255) NOT NULL,
  `drugId` varchar(255) DEFAULT NULL,
  `drugName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SSN`,`diagnosisID`),
  CONSTRAINT `FK_PDT` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientdrugtreatment`
--

LOCK TABLES `patientdrugtreatment` WRITE;
/*!40000 ALTER TABLE `patientdrugtreatment` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientdrugtreatment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientrecord`
--

DROP TABLE IF EXISTS `patientrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `patientrecord` (
  `SSN` varchar(11) NOT NULL,
  `admissionDate` date NOT NULL,
  `releaseDate` date DEFAULT NULL,
  `fees` int(11) DEFAULT NULL,
  PRIMARY KEY (`SSN`,`admissionDate`),
  CONSTRAINT `FK_PR` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientrecord`
--

LOCK TABLES `patientrecord` WRITE;
/*!40000 ALTER TABLE `patientrecord` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patientsurgery`
--

DROP TABLE IF EXISTS `patientsurgery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `patientsurgery` (
  `SSN` varchar(11) NOT NULL,
  `surgeryID` varchar(255) NOT NULL,
  `surgeryName` varchar(255) DEFAULT NULL,
  `beginDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  `results` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SSN`,`surgeryID`),
  CONSTRAINT `FK_PS` FOREIGN KEY (`SSN`) REFERENCES `patient` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patientsurgery`
--

LOCK TABLES `patientsurgery` WRITE;
/*!40000 ALTER TABLE `patientsurgery` DISABLE KEYS */;
/*!40000 ALTER TABLE `patientsurgery` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-30 19:39:36
