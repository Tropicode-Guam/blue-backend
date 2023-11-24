-- MariaDB dump 10.19-11.1.2-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	11.1.2-MariaDB-1:11.1.2+maria~ubu2204

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `language`
--

DROP TABLE IF EXISTS `language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `language`
--

LOCK TABLES `language` WRITE;
/*!40000 ALTER TABLE `language` DISABLE KEYS */;
INSERT INTO `language` VALUES
(1,'aa'),
(2,'ab'),
(3,'af'),
(4,'ak'),
(5,'am'),
(6,'ar'),
(7,'an'),
(8,'as'),
(9,'av'),
(10,'ae'),
(11,'ay'),
(12,'az'),
(13,'ba'),
(14,'bm'),
(15,'be'),
(16,'bn'),
(17,'bi'),
(18,'bo'),
(19,'bs'),
(20,'br'),
(21,'bg'),
(22,'ca'),
(23,'cs'),
(24,'ch'),
(25,'ce'),
(26,'cu'),
(27,'cv'),
(28,'kw'),
(29,'co'),
(30,'cr'),
(31,'cy'),
(32,'da'),
(33,'de'),
(34,'dv'),
(35,'dz'),
(36,'el'),
(37,'en'),
(38,'eo'),
(39,'et'),
(40,'eu'),
(41,'ee'),
(42,'fo'),
(43,'fa'),
(44,'fj'),
(45,'fi'),
(46,'fr'),
(47,'fy'),
(48,'ff'),
(49,'gd'),
(50,'ga'),
(51,'gl'),
(52,'gv'),
(53,'gn'),
(54,'gu'),
(55,'ht'),
(56,'ha'),
(57,'he'),
(58,'hz'),
(59,'hi'),
(60,'ho'),
(61,'hr'),
(62,'hu'),
(63,'hy'),
(64,'ig'),
(65,'io'),
(66,'ii'),
(67,'iu'),
(68,'ie'),
(69,'ia'),
(70,'id'),
(71,'ik'),
(72,'is'),
(73,'it'),
(74,'jv'),
(75,'ja'),
(76,'kl'),
(77,'kn'),
(78,'ks'),
(79,'ka'),
(80,'kr'),
(81,'kk'),
(82,'km'),
(83,'ki'),
(84,'rw'),
(85,'ky'),
(86,'kv'),
(87,'kg'),
(88,'ko'),
(89,'kj'),
(90,'ku'),
(91,'lo'),
(92,'la'),
(93,'lv'),
(94,'li'),
(95,'ln'),
(96,'lt'),
(97,'lb'),
(98,'lu'),
(99,'lg'),
(100,'mh'),
(101,'ml'),
(102,'mr'),
(103,'mk'),
(104,'mg'),
(105,'mt'),
(106,'mn'),
(107,'mi'),
(108,'ms'),
(109,'my'),
(110,'na'),
(111,'nv'),
(112,'nr'),
(113,'nd'),
(114,'ng'),
(115,'ne'),
(116,'nl'),
(117,'nn'),
(118,'nb'),
(119,'no'),
(120,'ny'),
(121,'oc'),
(122,'oj'),
(123,'or'),
(124,'om'),
(125,'os'),
(126,'pa'),
(127,'pi'),
(128,'pl'),
(129,'pt'),
(130,'ps'),
(131,'qu'),
(132,'rm'),
(133,'ro'),
(134,'rn'),
(135,'ru'),
(136,'sg'),
(137,'sa'),
(138,'si'),
(139,'sk'),
(140,'sl'),
(141,'se'),
(142,'sm'),
(143,'sn'),
(144,'sd'),
(145,'so'),
(146,'st'),
(147,'es'),
(148,'sq'),
(149,'sc'),
(150,'sr'),
(151,'ss'),
(152,'su'),
(153,'sw'),
(154,'sv'),
(155,'ty'),
(156,'ta'),
(157,'tt'),
(158,'te'),
(159,'tg'),
(160,'tl'),
(161,'th'),
(162,'ti'),
(163,'to'),
(164,'tn'),
(165,'ts'),
(166,'tk'),
(167,'tr'),
(168,'tw'),
(169,'ug'),
(170,'uk'),
(171,'ur'),
(172,'uz'),
(173,'ve'),
(174,'vi'),
(175,'vo'),
(176,'wa'),
(177,'wo'),
(178,'xh'),
(179,'yi'),
(180,'yo'),
(181,'za'),
(182,'zh'),
(183,'zu'),
(184,'bh');
/*!40000 ALTER TABLE `language` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-17 14:02:05
