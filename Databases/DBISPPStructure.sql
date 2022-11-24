create schema dbispp;
use dbispp;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: dbispp
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumno` (
  `AlumnoID` int NOT NULL AUTO_INCREMENT,
  `UsuarioPerfilID` int NOT NULL,
  PRIMARY KEY (`AlumnoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `alumnocarpo`
--

DROP TABLE IF EXISTS `alumnocarpo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnocarpo` (
  `AlumnoCarpoID` int NOT NULL AUTO_INCREMENT,
  `CarpoID` int NOT NULL,
  `AlumnoID` int NOT NULL,
  `AlumnoCarpoActivo` tinyint DEFAULT '0',
  PRIMARY KEY (`AlumnoCarpoID`),
  KEY `fk_carpo_has_Alumno_Alumno1_idx` (`AlumnoID`),
  KEY `fk_carpo_has_Alumno_carpo1_idx` (`CarpoID`),
  CONSTRAINT `fk_carpo_has_Alumno_Alumno1` FOREIGN KEY (`AlumnoID`) REFERENCES `alumno` (`AlumnoID`),
  CONSTRAINT `fk_carpo_has_Alumno_carpo1` FOREIGN KEY (`CarpoID`) REFERENCES `carpo` (`CARPOID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `alumnocarpomateria`
--

DROP TABLE IF EXISTS `alumnocarpomateria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnocarpomateria` (
  `AlumnoCarpoMateriaID` int NOT NULL AUTO_INCREMENT,
  `AlumnoCarpoID` int NOT NULL,
  `MateriaID` int NOT NULL,
  PRIMARY KEY (`AlumnoCarpoMateriaID`),
  KEY `AlumnoCarpoID_idx` (`AlumnoCarpoID`),
  KEY `AlumnoCarpoMateriaID_idx` (`MateriaID`),
  CONSTRAINT `AlumnoCarpoID` FOREIGN KEY (`AlumnoCarpoID`) REFERENCES `alumnocarpo` (`AlumnoCarpoID`),
  CONSTRAINT `AlumnoCarpoMateriaID` FOREIGN KEY (`MateriaID`) REFERENCES `materia` (`MateriaID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `alumnodatos`
--

DROP TABLE IF EXISTS `alumnodatos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnodatos` (
  `AlumnoDatosID` int NOT NULL,
  PRIMARY KEY (`AlumnoDatosID`),
  CONSTRAINT `AlumnoID` FOREIGN KEY (`AlumnoDatosID`) REFERENCES `alumno` (`AlumnoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `carpo`
--

DROP TABLE IF EXISTS `carpo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carpo` (
  `CARPOID` int NOT NULL AUTO_INCREMENT,
  `CarreraID` int NOT NULL,
  `PlanDeEstudioID` int NOT NULL,
  `OrientacionID` int DEFAULT NULL,
  `CarpoPrograma` varchar(255) DEFAULT NULL,
  `estado` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`CARPOID`),
  KEY `CARPOCarreraID_idx` (`CarreraID`),
  KEY `CARPOOrientacionID_idx` (`OrientacionID`),
  KEY `CARPOPlanID_idx` (`PlanDeEstudioID`),
  CONSTRAINT `CARPOCarreraID` FOREIGN KEY (`CarreraID`) REFERENCES `carrera` (`CarreraID`),
  CONSTRAINT `CARPOOrientacionID` FOREIGN KEY (`OrientacionID`) REFERENCES `orientacion` (`OrientacionID`),
  CONSTRAINT `CARPOPlanID` FOREIGN KEY (`PlanDeEstudioID`) REFERENCES `plandeestudio` (`PlanID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='Combinacion de Carrera/Plan de estudio/Orientacion. Esta relación permite que se pueda diferenciar carreras únicas según su plan y orientación';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `carrera`
--

DROP TABLE IF EXISTS `carrera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrera` (
  `CarreraID` int NOT NULL AUTO_INCREMENT,
  `CarreraNombre` varchar(255) NOT NULL,
  PRIMARY KEY (`CarreraID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='En esta tabla se representan todas las carreras del instituto';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `materia`
--

DROP TABLE IF EXISTS `materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materia` (
  `MateriaID` int NOT NULL AUTO_INCREMENT,
  `MateriaNombre` varchar(100) NOT NULL,
  `CarpoIDMat` int NOT NULL,
  `MateriaAño` int DEFAULT NULL,
  `MateriaTipo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`MateriaID`),
  KEY `idcarpomat_idx` (`CarpoIDMat`),
  CONSTRAINT `idcarpomat` FOREIGN KEY (`CarpoIDMat`) REFERENCES `carpo` (`CARPOID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `orientacion`
--

DROP TABLE IF EXISTS `orientacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orientacion` (
  `OrientacionID` int NOT NULL AUTO_INCREMENT,
  `OrientacionNombre` varchar(255) NOT NULL,
  PRIMARY KEY (`OrientacionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='En esta tabla se representan tres orientaciones que corresponden a una carrera';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `perfil`
--

DROP TABLE IF EXISTS `perfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perfil` (
  `PerfilID` int NOT NULL AUTO_INCREMENT,
  `Perfil` varchar(45) NOT NULL,
  PRIMARY KEY (`PerfilID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `personal`
--

DROP TABLE IF EXISTS `personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal` (
  `PersonalID` int NOT NULL AUTO_INCREMENT,
  `UsuarioPerfilID` int NOT NULL,
  PRIMARY KEY (`PersonalID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `personalcarpo`
--

DROP TABLE IF EXISTS `personalcarpo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personalcarpo` (
  `PersonalCarpoID` int NOT NULL AUTO_INCREMENT,
  `PersonalID` int NOT NULL,
  `CarpoID` int NOT NULL,
  `PersonalCarpoActivo` tinyint DEFAULT NULL,
  PRIMARY KEY (`PersonalCarpoID`),
  KEY `fk_Personal_has_carpo_carpo1_idx` (`CarpoID`),
  KEY `fk_Personal_has_carpo_Personal1_idx` (`PersonalID`),
  CONSTRAINT `fk_Personal_has_carpo_carpo1` FOREIGN KEY (`CarpoID`) REFERENCES `carpo` (`CARPOID`),
  CONSTRAINT `fk_Personal_has_carpo_Personal1` FOREIGN KEY (`PersonalID`) REFERENCES `personal` (`PersonalID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `personalcarpomateria`
--

DROP TABLE IF EXISTS `personalcarpomateria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personalcarpomateria` (
  `PersonalCarpoMateriaID` int NOT NULL AUTO_INCREMENT,
  `PersonalCarpoID` int NOT NULL,
  `MateriaID` int NOT NULL,
  PRIMARY KEY (`PersonalCarpoMateriaID`),
  KEY `fk_PersonalCarpo_has_materia_materia1_idx` (`MateriaID`),
  KEY `PersonalCarpoID_idx` (`PersonalCarpoID`),
  CONSTRAINT `MateriaID` FOREIGN KEY (`MateriaID`) REFERENCES `materia` (`MateriaID`),
  CONSTRAINT `PersonalCarpoID` FOREIGN KEY (`PersonalCarpoID`) REFERENCES `personalcarpo` (`PersonalCarpoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `personaldatos`
--

DROP TABLE IF EXISTS `personaldatos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personaldatos` (
  `PersonalID` int NOT NULL,
  PRIMARY KEY (`PersonalID`),
  CONSTRAINT `PersonalID` FOREIGN KEY (`PersonalID`) REFERENCES `personal` (`PersonalID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `plandeestudio`
--

DROP TABLE IF EXISTS `plandeestudio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plandeestudio` (
  `PlanID` int NOT NULL AUTO_INCREMENT,
  `PlanNombre` varchar(255) NOT NULL,
  PRIMARY KEY (`PlanID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='En esta tabla se representan los diferentes planes de estudio';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `UsuarioID` int NOT NULL AUTO_INCREMENT,
  `Usuario` varchar(45) NOT NULL,
  `UsuarioCorreo` varchar(45) DEFAULT NULL,
  `UsuarioContraseña` varchar(120) DEFAULT NULL,
  `UsuarioContraseñaTemp` varchar(120) DEFAULT NULL,
  `UsuarioActivo` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`UsuarioID`),
  UNIQUE KEY `Usuario_UNIQUE` (`Usuario`),
  UNIQUE KEY `UsuarioCorreo_UNIQUE` (`UsuarioCorreo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `InsertTempPassword` BEFORE INSERT ON `usuario` FOR EACH ROW BEGIN
	IF (NEW.UsuarioContraseñaTemp IS NULL) THEN
		SET NEW.UsuarioContraseñaTemp := NEW.Usuario;
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `usuariodatos`
--

DROP TABLE IF EXISTS `usuariodatos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuariodatos` (
  `UsuarioID` int NOT NULL,
  `UsuarioNombre` varchar(45) DEFAULT NULL,
  `UsuarioApellido` varchar(45) DEFAULT NULL,
  `UsuarioCUIL` int DEFAULT NULL,
  `UsuarioFechaNac` varchar(45) DEFAULT NULL,
  `UsuarioSexoDNI` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`UsuarioID`),
  CONSTRAINT `UsuarioIDDatos` FOREIGN KEY (`UsuarioID`) REFERENCES `usuario` (`UsuarioID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuariodomicilio`
--

DROP TABLE IF EXISTS `usuariodomicilio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuariodomicilio` (
  `UsuarioID` int NOT NULL,
  `UsuarioNacionalidad` varchar(45) DEFAULT NULL,
  `UsuarioProvincia` varchar(45) DEFAULT NULL,
  `UsuarioDepartamento` varchar(45) DEFAULT NULL,
  `UsuarioLocalidad` varchar(45) DEFAULT NULL,
  `UsuarioCiudad` varchar(45) DEFAULT NULL,
  `UsuarioBarrio` varchar(45) DEFAULT NULL,
  `UsuarioCalle` varchar(45) DEFAULT NULL,
  `UsuarioAltura` varchar(45) DEFAULT NULL,
  `UsuarioPiso` varchar(45) DEFAULT NULL,
  `UsuarioNumDep` varchar(45) DEFAULT NULL,
  `UsuarioManzana` varchar(45) DEFAULT NULL,
  `UsuarioCP` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`UsuarioID`),
  CONSTRAINT `UsuarioIDDomicilio` FOREIGN KEY (`UsuarioID`) REFERENCES `usuario` (`UsuarioID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuarioperfil`
--

DROP TABLE IF EXISTS `usuarioperfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarioperfil` (
  `UsuarioPerfilID` int NOT NULL AUTO_INCREMENT,
  `UsuarioID` int NOT NULL,
  `PerfilID` int NOT NULL,
  `UsuarioPerfilActivo` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`UsuarioPerfilID`),
  KEY `UsuarioPerfilUsuarioID_idx` (`UsuarioID`),
  KEY `UsuarioPerfilPerfilID_idx` (`PerfilID`),
  CONSTRAINT `UsuarioPerfilPerfilID` FOREIGN KEY (`PerfilID`) REFERENCES `perfil` (`PerfilID`),
  CONSTRAINT `UsuarioPerfilUsuarioID` FOREIGN KEY (`UsuarioID`) REFERENCES `usuario` (`UsuarioID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `PerfilInsertUsuario` AFTER INSERT ON `usuarioperfil` FOR EACH ROW BEGIN
	IF ((SELECT perfilID FROM usuarioperfil WHERE usuarioperfilid = new.usuarioperfilid) = 7) THEN 
	  INSERT INTO alumno(UsuarioPerfilID) VALUES(new.usuarioperfilid);
	end if;
	IF ((SELECT perfilID FROM usuarioperfil WHERE usuarioperfilid = new.usuarioperfilid) = 2) THEN 
	  INSERT INTO Personal(UsuarioPerfilID) VALUES(new.UsuarioPerfilID);
	end if;
	IF ((SELECT perfilID FROM usuarioperfil WHERE usuarioperfilid = new.usuarioperfilid) = 3) THEN 
	  INSERT INTO Personal(UsuarioPerfilID) VALUES(new.UsuarioPerfilID);
	end if;
	IF ((SELECT perfilID FROM usuarioperfil WHERE usuarioperfilid = new.usuarioperfilid) = 4) THEN 
	  INSERT INTO Personal(UsuarioPerfilID) VALUES(new.UsuarioPerfilID);
	end if;
	IF ((SELECT perfilID FROM usuarioperfil WHERE usuarioperfilid = new.usuarioperfilid) = 5) THEN 
	  INSERT INTO Personal(UsuarioPerfilID) VALUES(new.UsuarioPerfilID);
	end if;
	IF ((SELECT perfilID FROM usuarioperfil WHERE usuarioperfilid = new.usuarioperfilid) = 6) THEN 
	  INSERT INTO Personal(UsuarioPerfilID) VALUES(new.UsuarioPerfilID);
	end if;
	IF ((SELECT perfilID FROM usuarioperfil WHERE usuarioperfilid = new.usuarioperfilid) = 8) THEN 
	  INSERT INTO Personal(UsuarioPerfilID) VALUES(new.UsuarioPerfilID);
	end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-23 20:54:22
