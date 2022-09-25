-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: lego_items
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `lego-db-csv220910`
--

DROP TABLE IF EXISTS `lego-db-csv220910`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lego-db-csv220910` (
  `ky-lego-item` int DEFAULT NULL,
  `cat_number` int DEFAULT NULL,
  `owned_by` text,
  `first_year` text,
  `last_year` text,
  `category` text,
  `title` text,
  `original_price` text,
  `item_retired` text,
  `taobao_price` text,
  `item_image` text,
  `box_image` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lego-db-csv220910`
--

LOCK TABLES `lego-db-csv220910` WRITE;
/*!40000 ALTER TABLE `lego-db-csv220910` DISABLE KEYS */;
INSERT INTO `lego-db-csv220910` VALUES (1,7499,'Ken','2011-01','2018-06','Train','Flexible and Straight Tracks','19.99','Retired','115','',''),(2,10258,'Ken','2017-08','2021-12','Creator Expert','London Bus','139.99','Retired','850','',''),(3,10290,'','2021-10','','Icons','Pickup Truck','129.99','Available Now','780','',''),(4,21039,'Ken','2018-01','202-12','Architecture','Shanghai','59.99','Retired','850','',''),(5,21041,'Ken, James','2018-06','2019-12','Architecture','Great Wall of China','49.99','Retired','560','',''),(6,30349,'Ken','2016-01','2017-12','Polybag','Sports Car','3.99','Retired','38','',''),(8,40145,'Ken','2015-01','2021-12','Exclusive ','Grand Opening LEGO Brand Retail Store','','Retired','158','',''),(9,40220,'Ken','2016','','Creator Expert','London Bus','9.99','Available Now','75','',''),(10,40305,'Ken','2018-06','2021-12','Other','Microscale LEGO® Brand Store','24.99','Available Now','180','',''),(11,40338,'','2019-11','2019-12','Gift with purchase','Christmas Tree','19.99',' Retired',' 650','',''),(13,40519,'Ken','','','Postcard','New York Postcard','14.99','Available Now','','',''),(14,40558,'','','','Star Wars','Clone Trooper™ Command Station','14.99','Available Now','','',''),(15,40568,'','','','Postcard','Paris Postcard','14.99','Available Now','','',''),(16,40569,'','','','Postcard','London Postcard','14.99','Available Now','','',''),(17,40573,'','','','Other','Christmas Tree','44.99','Available Now','','',''),(18,40574,'Ken','2022-08','','Other','LEGO® Brand Store','36.00','Available Now','200','',''),(19,40654,'','','','Postcard','Beijing Postcard','14.99','Available Now','','',''),(20,42117,'Ken','2021-01','','Technic','Race Plane','9.99','Available Now','75','',''),(21,42126,'','2021-10','2022-12','Technic','Ford® F-150 Raptor','99.99','Available Now','800','',''),(22,42138,'','2022-01','','Technic','Ford Mustang Shelby® GT500®','49.99','Available Now','300','',''),(23,60098,'','2015-06','2017-12','City - Train','Heavy-Haul Train','199.99','Retired','3000','',''),(24,60197,'','','','City - Train','Passenger Train','159.99','Available Now','','',''),(25,60205,'Ken','','','City - Train','Tracks','19.99','Available Now','','',''),(26,60238,'Ken','','','City - Train','Switch Tracks','15.99','Available Now','','',''),(27,60335,'','','','City - Train','Train Station','99.99','Available Now','','',''),(28,60336,'','','','City - Train','Freight Train','199.99','Available Now','','',''),(29,60350,'','','','City - Space','Lunar Research Base','129.99','Available Now','','',''),(30,75074,'','','','Star Wars','Snowspeeder™','','Retired','','',''),(31,75100,'','2015-09','2016-12','Star Wars™','First Order Snowspeeder™','39.99','Retired','420','',''),(32,75126,'','','','Star Wars','First Order Snowspeeder™','','Retired','','',''),(33,75150,'','','','Star Wars','Vader\'s TIE Advanced vs. A-Wing Starfighter','','Retired','','',''),(34,75166,'','2017-01','2018-12','Star Wars™','First Order Transport Speeder Battle Pack','14.99','Retired','255','',''),(35,75167,'','','','Star Wars','Bounty Hunter Speeder Bike™ Battle Pack','','Retired','','',''),(36,75197,'','','','Star Wars','First Order Specialists Battle Pack','','Retired','','',''),(37,75198,'','','','Star Wars','Tatooine™ Battle Pack','','Retired','','',''),(38,75199,'','','','Star Wars','General Grievous\' Combat Speeder','','Retired','','',''),(39,75206,'','','','Star Wars','Jedi™ and Clone Troopers™ Battle Pack','','Retired','','',''),(40,75207,'','','','Star Wars','Imperial Patrol Battle Pack','','Retired','','',''),(41,75234,'','','','Star Wars','AT-AP™ Walker','','Retired','','',''),(42,75238,'','','','Star Wars','Action Battle Endor™ Assault','','Retired','','',''),(43,75239,'','','','Star Wars','Action Battle Hoth™ Generator Attack','','Retired','','',''),(44,75254,'','','','Star Wars','AT-ST™ Raider from The Mandalorian','','Retired','','',''),(45,75266,'','','','Star Wars','Sith Troopers™ Battle Pack','','Retired','','',''),(46,75267,'','','','Star Wars','Mandalorian™ Battle Pack','','Retired','','',''),(47,75268,'','','','Star Wars','Snowspeeder™','','Retired','','',''),(48,75271,'','','','Star Wars','Luke Skywalker\'s Landspeeder™','','Retired','','',''),(49,75280,'','','','Star Wars','501st Legion™ Clone Troopers','29.99','Available Now','','',''),(50,75295,'','','','Star Wars','Millennium Falcon™ Microfighter','9.99','Available Now','','',''),(51,75298,'','','','Star Wars','AT-AT™ vs. Tauntaun™ Microfighters','19.99','Available Now','','',''),(52,75299,'','','','Star Wars','Trouble on Tatooine™','29.99','Available Now','','',''),(53,75320,'','','','Star Wars','Snowtrooper™ Battle Pack','19.99','Available Now','','',''),(54,75321,'','','','Star Wars','The Razor Crest™ Microfighter','9.99','Available Now','','',''),(55,75340,'','','','Star Wars','LEGO® Star Wars™ Advent Calendar','44.99','Available Now','','',''),(56,75342,'','','','Star Wars','Republic Fighter Tank™','39.99','Available Now','','',''),(57,76905,'','2021','','Speed Champions','Ford GT Heritage Edition and Bronco R','49.99','Available Now','380','',''),(58,76911,'Ken','2022-08','','Speed Champions','007 Aston Martin DB5','19.99','Available Now','140','',''),(59,853600,'Ken','2016','','Magnet','Magnet Statue of Liberty 2016','5.99','Available Now','120','',''),(60,854088,'','','','Magnet','Forbidden City Magnet Build','9.99','Available Now','','',''),(61,5002938,'Ken','2015','','Star Wars','Stormtrooper™ Sergeant','','','55','',''),(62,5005233,'Ken','2018','','Mini Figure','Hamleys Royal Guard Minifigure','6.00?','','50','',''),(NULL,853914,'Ken','2019','','Magnet','London Bus Magnet','9.99','Available Now','75',NULL,NULL);
/*!40000 ALTER TABLE `lego-db-csv220910` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-25 18:12:44
