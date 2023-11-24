-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: FEETBOOKER
-- ------------------------------------------------------
-- Server version	8.0.31-google

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `FEETBOOKER`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `FEETBOOKER` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_hungarian_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `FEETBOOKER`;

--
-- Table structure for table `bookers`
--

DROP TABLE IF EXISTS `bookers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookers` (
  `nev` varchar(50) COLLATE utf8mb3_hungarian_ci DEFAULT NULL,
  `datum` date DEFAULT NULL,
  `ido` time DEFAULT NULL,
  `feet` tinyint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookers`
--

LOCK TABLES `bookers` WRITE;
/*!40000 ALTER TABLE `bookers` DISABLE KEYS */;
INSERT INTO `bookers` VALUES ('Poros Bence','2023-12-10','12:30:00',34),('Vivien Dusty','2023-12-12','18:30:00',43),('Poros Bence','2023-12-10','12:30:00',38),('Poros Vivien','2023-12-10','12:30:00',38),('Ted Smith','2023-12-10','12:30:00',38),('Coomer Boomer','2023-12-10','18:30:00',43),('Kele Péter Lajos','2023-12-13','18:30:00',43),('Smeg Ma','2023-12-12','15:30:00',42),('Egg Man','2023-12-10','18:30:00',45),('Krizsán Gergő','2023-12-14','15:30:00',45);
/*!40000 ALTER TABLE `bookers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storeroom`
--

DROP TABLE IF EXISTS `storeroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storeroom` (
  `bootsize` tinyint DEFAULT NULL,
  `amount` tinyint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_hungarian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storeroom`
--

LOCK TABLES `storeroom` WRITE;
/*!40000 ALTER TABLE `storeroom` DISABLE KEYS */;
INSERT INTO `storeroom` VALUES (34,3),(35,3),(36,3),(37,3),(38,3),(39,3),(40,3),(41,3),(42,4),(43,4),(44,4),(45,4);
/*!40000 ALTER TABLE `storeroom` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-20 10:06:56
