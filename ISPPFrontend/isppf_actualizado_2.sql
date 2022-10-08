-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-10-2022 a las 15:58:17
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `isppf_actualizado`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calendario`
--

CREATE TABLE `calendario` (
  `idcalendario` int(11) NOT NULL,
  `fecha_desde` datetime DEFAULT NULL,
  `fecha_hasta` datetime DEFAULT NULL,
  `fechaInsc_desde` datetime DEFAULT NULL,
  `fechaInsc_hasta` datetime DEFAULT NULL,
  `calendariovigencia` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `calendario`
--

INSERT INTO `calendario` (`idcalendario`, `fecha_desde`, `fecha_hasta`, `fechaInsc_desde`, `fechaInsc_hasta`, `calendariovigencia`) VALUES
(1, '2022-07-01 00:00:00', '2022-08-01 00:00:00', '2022-06-25 00:00:00', '2022-06-30 00:00:00', 1),
(2, '2022-08-01 00:00:00', '2022-09-01 00:00:00', '2022-07-25 00:00:00', '2022-07-30 00:00:00', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carpestmateria`
--

CREATE TABLE `carpestmateria` (
  `idcarpestMateria` int(11) NOT NULL,
  `idMateria` int(11) NOT NULL,
  `idCarpoEstudiante` int(11) NOT NULL,
  `Condicion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carpestmateria`
--

INSERT INTO `carpestmateria` (`idcarpestMateria`, `idMateria`, `idCarpoEstudiante`, `Condicion`) VALUES
(1, 1, 1, 'Regular'),
(2, 4, 1, NULL),
(3, 7, 1, NULL),
(4, 3, 2, 'Regular'),
(5, 6, 2, NULL),
(6, 2, 2, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carpo`
--

CREATE TABLE `carpo` (
  `CARPOID` int(11) NOT NULL,
  `CarreraID` int(11) NOT NULL,
  `PlanDeEstudioID` int(11) NOT NULL,
  `OrientacionID` int(11) DEFAULT NULL,
  `CarpoPrograma` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Combinacion de Carrera/Plan de estudio/Orientacion. Esta relación permite que se pueda diferenciar carreras únicas según su plan y orientación';

--
-- Volcado de datos para la tabla `carpo`
--

INSERT INTO `carpo` (`CARPOID`, `CarreraID`, `PlanDeEstudioID`, `OrientacionID`, `CarpoPrograma`) VALUES
(1, 1, 1, NULL, 'Educación Fisica 2012'),
(2, 1, 2, NULL, 'Educación Fisica 2016'),
(3, 2, 1, NULL, 'Biologia 2012'),
(4, 2, 2, NULL, 'Biologia 2016'),
(5, 3, 1, NULL, 'Química '),
(6, 4, 4, NULL, 'Filosofía'),
(7, 5, 5, NULL, 'Historia'),
(8, 6, 1, NULL, 'Ciencias de la Educación'),
(9, 7, 5, 1, 'Educación Especial'),
(10, 8, 4, NULL, 'Técnico Superior en Act. Física, Org. y Gestión Deportiva'),
(11, 1, 4, NULL, 'Educacion Fisica 2021'),
(12, 7, 5, 2, 'Educación Especial'),
(13, 6, 6, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carpoestudiante`
--

CREATE TABLE `carpoestudiante` (
  `idCARPOEstudiante` int(11) NOT NULL,
  `idCARPO` int(11) NOT NULL,
  `idEstudiante` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carpoestudiante`
--

INSERT INTO `carpoestudiante` (`idCARPOEstudiante`, `idCARPO`, `idEstudiante`) VALUES
(1, 3, 1),
(2, 3, 2),
(3, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

CREATE TABLE `carrera` (
  `CarreraID` int(11) NOT NULL,
  `CarreraNombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='En esta tabla se representan todas las carreras del instituto';

--
-- Volcado de datos para la tabla `carrera`
--

INSERT INTO `carrera` (`CarreraID`, `CarreraNombre`) VALUES
(1, 'Educación Fisica'),
(2, 'Biologia'),
(3, 'Química'),
(4, 'Filosofia'),
(5, 'Historia'),
(6, 'Ciencias de la Educación'),
(7, 'Educación Especial'),
(8, 'Técnico Superior en Act. Física, Org. y Gestión Deportiva');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `idestudiante` int(11) NOT NULL,
  `NombreAlumno` varchar(45) NOT NULL,
  `ApellidoAlumno` varchar(45) NOT NULL,
  `DNI` varchar(45) NOT NULL,
  `IDusuariosPerfiles` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`idestudiante`, `NombreAlumno`, `ApellidoAlumno`, `DNI`, `IDusuariosPerfiles`) VALUES
(1, 'Nicolas', 'Calderon', '41299019', 1),
(2, 'Exequiel', 'Barco', '42698355', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripcionexamencarpestmat`
--

CREATE TABLE `inscripcionexamencarpestmat` (
  `idInscripcionExamenCarpestMat` int(11) NOT NULL,
  `idCarpestMateria` int(11) NOT NULL,
  `idMesaExamenes` int(11) NOT NULL,
  `Aceptado` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `inscripcionexamencarpestmat`
--

INSERT INTO `inscripcionexamencarpestmat` (`idInscripcionExamenCarpestMat`, `idCarpestMateria`, `idMesaExamenes`, `Aceptado`) VALUES
(1, 4, 1, 0),
(2, 5, 4, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mandarcorreo`
--

CREATE TABLE `mandarcorreo` (
  `idmandarcorreo` int(11) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `contraseña` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `mandarcorreo`
--

INSERT INTO `mandarcorreo` (`idmandarcorreo`, `correo`, `contraseña`) VALUES
(1, 'preuebaspython@gmail.com', 'xscvodrwfqutoswh');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materia`
--

CREATE TABLE `materia` (
  `idmateria` int(11) NOT NULL,
  `nombremateria` varchar(100) NOT NULL,
  `idcarpo` int(11) NOT NULL,
  `año` int(11) DEFAULT NULL,
  `Tipo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `materia`
--

INSERT INTO `materia` (`idmateria`, `nombremateria`, `idcarpo`, `año`, `Tipo`) VALUES
(1, 'Pedagogia I', 3, '1', 'Cuatrimestral Primero'),
(2, 'Historia Argentina y LatinoAmericana', 3, '1', 'Cuatrimestral Primero'),
(3, 'Alfabetización Academica', 3, '1', 'Anual'),
(4, 'Matematica I', 3, '1', 'Cuatrimestral Primero'),
(5, 'Ciencias de la Tierra', 3, '1', 'Cuatrimestral Primero'),
(6, 'Biologia I', 3, '1', 'Anual'),
(7, 'Quimica General', 3, '1', 'Anual'),
(8, 'Practica 1', 3, '1', 'Anual'),
(9, 'Sociologia de la Educación', 3, '2', 'Cuatrimestral Primero'),
(10, 'Fisica Biologica II', 3, '2', 'Cuatrimestral Primero'),
(12, 'Psicología Educacional', 3, '1', 'Cuatrimestral Segundo'),
(13, 'Historia de la Educacion y Politica Educacion', 3, '1', 'Cuatrimestral Segundo'),
(14, 'Fisica Biologica I', 3, '1', 'Cuatrimestral Segundo'),
(15, 'Epistemologia e Historia de las Ciencias', 3, '1', 'Cuatrimestral Segundo'),
(16, 'Biologia Humana I', 3, '2', 'Cuatrimestral Primero'),
(17, 'Tecnologia de la Informaciony la Comunicación', 3, '2', 'Cuatrimestral Segundo'),
(18, 'Biologia de os Microorganismos', 3, '2', 'Cuatrimestral Segundo'),
(19, 'EDI', 3, '2', 'Cuatrimestral Segundo'),
(20, 'Didactica General', 3, '2', 'Anual'),
(21, 'Sujetos de la Educacion', 3, '2', 'Anual'),
(22, 'Biologia Celular y Molecular', 3, '2', 'Anual'),
(23, 'Quimica Organica y Biologica', 3, '2', 'Anual'),
(24, 'Practica II', 3, '2', 'Anual'),
(25, 'Filosofia de la Educacion', 3, '3', 'Cuatrimestral Primero'),
(26, 'Integracion e Inclusion Educativa', 3, '3', 'Cuatrimestral Segundo'),
(27, 'Didactica de la Biologia', 3, '3', 'Anual'),
(28, 'Morfofisiologia Animal', 3, '3', 'Anual'),
(29, 'Biologia Humana II', 3, '3', 'Anual'),
(30, 'Genetica', 3, '3', 'Anual'),
(31, 'EDI', 3, '3', 'Anual'),
(32, 'Practica III', 3, '3', 'Anual'),
(33, 'Educacion Sexual Integral', 3, '4', 'Cuatrimestral Primero'),
(34, 'Formacion Etica y Ciudadana', 3, '4', 'Cuatrimestral Primero'),
(35, 'Ecologia', 3, '4', 'Cuatrimestral Primero'),
(36, 'Biodiversidad Vegetal', 3, '4', 'Cuatrimestral Primero'),
(37, 'Salud y Ambiente', 3, '4', 'Cuatrimestral Segundo'),
(38, 'Biotecnologia', 3, '4', 'Cuatrimestral Segundo'),
(39, 'Evolucion', 3, '4', 'Cuatrimestral Segundo'),
(40, 'Biodiversidad Animal', 3, '4', 'Cuatrimestral Segundo'),
(41, 'EDI', 3, '4', 'Anual'),
(42, 'Residencia y sistematizacion de Experiencias', 3, '4', 'Anual'),
(47, 'Historia Social Argentina y Latinoamericana', 9, '1', 'Anual'),
(48, 'Psicología General', 9, '1', 'Anual'),
(49, 'Alfabetización Académica', 9, '1', 'Anual'),
(50, 'Sociología', 9, '1', '1°Cuatrimestre'),
(51, 'Práctica docente I: La Institución Educativa.', 9, '1', 'Anual'),
(52, 'Pedagogía General', 9, '1', 'Anual'),
(53, 'Didáctica General ', 9, '1', 'Anual'),
(54, 'Problemática del Nivel Superior', 9, '1', '1°Cuatrimestre'),
(55, 'Historia General de la Educación', 9, '1', '2°Cuatrimestre'),
(56, 'Sociología de la Educación', 9, '1', '2°Cuatrimestre'),
(57, 'Antropología ', 9, '2', '1°Cuatrimestre'),
(58, 'Tecnologías de la información y la comunicaci', 9, '2', 'Anual'),
(59, 'Filosofía', 9, '2', 'Anual'),
(60, 'Práctica docente II: Currículum,  sujetos y c', 9, '2', 'Anual'),
(61, 'Sujeto de la Educación I', 9, '2', 'Anual'),
(62, 'Psicología de la Educación', 9, '2', 'Anual'),
(63, ' Teoría y Política Curricular', 9, '2', 'Anual'),
(64, 'Didáctica I: Nivel Inicial', 9, '2', '1°Cuatrimestre'),
(65, 'Didáctica II: Nivel Primario', 9, '2', '2°Cuatrimestre'),
(66, 'Lengua extranjera: Inglés', 9, '3', 'Anual'),
(67, 'Educación sexual integral', 9, '3', '2°Cuatrimestre'),
(68, 'Epistemología de las Ciencias Sociales', 9, '3', '1°Cuatrimestre'),
(69, 'Práctica docente III: Programación  Didáctica', 9, '3', 'Anual'),
(70, 'Historia de la Educación Argentina', 9, '3', '2°Cuatrimestre'),
(71, 'Sujeto de la Educación II: pubertad y adolesc', 9, '3', 'Anual'),
(72, 'Filosofía de la Educación ', 9, '3', '1°Cuatrimestre'),
(73, 'Didáctica III: Nivel Secundario', 9, '3', 'Anual'),
(74, 'Educación y TIC I ', 9, '3', 'Anual'),
(75, 'Pedagogia', 12, '1', '1°Cuatrimestre'),
(76, 'Psicología Educacional', 12, '1', '2°Cuatrimestre'),
(77, 'Didáctica General', 12, '1', 'Anual'),
(78, 'Alfabetización Academica', 12, '1', 'Anual'),
(79, 'Practica I', 12, '1', 'Anual'),
(80, 'Problemática Contemporanea', 12, '1', '2°Cuatrimestre'),
(81, 'Sujeto de la educación especial', 12, '1', 'Anual'),
(82, 'Bases Neuropsicologicas', 12, '1', 'Anual'),
(83, 'Lengua y su Didactica', 12, '1', 'Anual'),
(84, 'Matemática y su Didáctica', 12, '1', 'Anual'),
(85, 'El arte en la educación especial', 12, '1', '2°Cuatrimestre'),
(86, 'Historia Argentina y Latinoamericana', 12, '2', '1°Cuatrimestre'),
(87, 'Historia de la educ. y politic. educ. Argenti', 12, '2', '2°Cuatrimestre'),
(88, 'Sociología de le educación', 12, '2', '1°Cuatrimestre'),
(89, 'Filosofía ', 12, '2', '2°Cuatrimestre'),
(90, 'Practica II', 12, '2', 'Anual'),
(91, 'Cs. Naturales y su Didactica', 12, '2', 'Anual'),
(92, 'Cs. Sociales y su Didactica', 12, '2', 'Anual'),
(93, 'Trastornos del desarrollo en suj. con disc. n', 12, '2', 'Anual'),
(94, 'Comunicación, lenguaje y sus alter. en suj. c', 12, '2', 'Anual'),
(95, 'Pedagogía', 13, '1', '1°Cuatrimestre'),
(96, 'Historia Argentina y Latinoamericana', 13, '1', '1°Cuatrimestre'),
(97, 'Matemática', 13, '1', '1°Cuatrimestre'),
(98, 'Ciencias de la Tierra', 13, '1', '1°Cuatrimestre'),
(99, 'Psicología Educacional', 13, '1', '2°Cuatrimestre'),
(100, 'Historia de la Educación y Política Educacion', 13, '1', '2°Cuatrimestre'),
(101, 'Física Biológica I', 13, '1', '2°Cuatrimestre'),
(102, 'Tecnología de la Información y la Comunicació', 13, '1', '2°Cuatrimestre'),
(103, 'Alfabetización Académica', 13, '1', 'Anual'),
(104, 'Practica I : La Institución Educativa', 13, '1', 'Anual'),
(105, 'Biología', 13, '1', 'Anual'),
(106, 'Química General', 13, '1', 'Anual'),
(107, 'Didáctica General', 13, '2', 'Anual'),
(108, 'Practica II', 13, '2', 'Anual'),
(109, 'Sujeto de la Educación', 13, '2', 'Anual'),
(110, 'Química Orgánica y Biológica', 13, '2', 'Anual'),
(111, 'Biología Humana I', 13, '2', 'Anual'),
(112, 'Trabajo Experimental en Biología', 13, '2', 'Anual'),
(113, 'Sociología de la Educación', 13, '2', '1°Cuatrimestre'),
(114, 'Física Biológica II', 13, '2', '1°Cuatrimestre'),
(115, 'Filosofía de la Educación', 13, '2', '2°Cuatrimestre'),
(116, 'Biología de los Microorganismos', 13, '2', '2°Cuatrimestre'),
(117, 'Epistemología e Historia de las Ciencias', 13, '3', '1°Cuatrimestre'),
(118, 'Integración e Inclusión Educativa', 13, '3', '2°Cuatrimestre'),
(119, 'Biología Humana', 13, '3', 'Anual'),
(120, 'Biología Celular y Molecular', 13, '3', 'Anual'),
(121, 'Didáctica de la Biología', 13, '3', 'Anual'),
(122, 'Morfofisiologia Vegetal', 13, '3', 'Anual'),
(123, 'Morfofisiologia Animal', 13, '3', 'Anual'),
(124, 'Practica III : Programación Didáctica y Gesti', 13, '3', 'Anual'),
(136, 'Pedagogía', 11, '1', '1°Cuatrimestre'),
(137, 'Psicología Educacional', 11, '1', '2°Cuatrimestre'),
(138, 'Alfabetización Académica', 11, '1', 'Anual'),
(139, 'Educación Sexual Integral', 11, '1', '1°Cuatrimestre'),
(140, 'Practica Docente I: La Institución Educativa', 11, '1', 'Anual'),
(141, 'Sujeto de la Educación I', 11, '1', 'Anual'),
(142, 'Biología del Movimiento I', 11, '1', 'Anual'),
(143, 'Practicas Motrices Integradas ', 11, '1', 'Anual'),
(144, 'Practicas Acuaticas', 11, '1', 'Anual'),
(145, 'Deportes individuales y su enseñanza I: Atletismo', 11, '1', 'Anual'),
(146, 'Deportes Colectivos y su enseñanza I: Basquet', 11, '1', 'Anual'),
(220, 'Juego y Educación Física ', 11, '2', 'Anual'),
(221, 'Didáctica de la Educación: Física I', 11, '2', '2°Cuatrimestre'),
(222, 'Didáctica General', 11, '2', '1°Cuatrimestre'),
(223, 'Practica docente II: Curriculum, Sujetos y Contextos', 11, '2', 'Anual'),
(224, 'Sujeto de la Educación II', 11, '2', 'Anual'),
(225, 'Biología del Movimiento ', 11, '2', 'Anual'),
(226, 'Gimnasia y su Enseñanza', 11, '2', 'Anual'),
(227, 'Deportes individuales y su enseñanza II: Natación', 11, '2', 'Anual'),
(228, 'Deportes colectivos y su enseñanza II: Voleibol ', 11, '2', 'Anual'),
(229, 'Sociología de la Educación', 11, '2', '1°Cuatrimestre'),
(230, 'Filosofía de la Educación', 11, '3', '1°Cuatrimestre'),
(231, 'Educación y Nuevas Tecnologías I ', 11, '3', 'Anual'),
(232, 'Historia de la Educación y Política Educacional Argentina', 11, '3', 'Anual'),
(233, 'Animación Sociocultural y Dinámica de Grupos ', 11, '3', '1°Cuatrimestre'),
(234, 'Practica docente III: Programación Didáctica, Gestión de micro experiencias de Enseñanza', 11, '3', 'Anual'),
(235, 'Teoría y epistemología de la Educación Física', 11, '3', '2°Cuatrimestre'),
(236, 'Practicas gimnasticas actuales y su enseñanza', 11, '3', 'Anual'),
(237, 'Deportes colectivos y su enseñanza III: Cestobol', 11, '3', 'Anual'),
(238, 'Deportes colectivos y su enseñanza III: Handbol ', 11, '3', 'Anual'),
(239, 'Practicas en la Naturaleza y Educación Ambiental', 11, '3', 'Anual'),
(240, 'Didáctica de la Educación Física II ', 11, '3', 'Anual'),
(241, 'Formación Ética y Ciudadana ', 11, '4', '1°Cuatrimestre'),
(242, 'Educación y Nuevas tecnologías II', 11, '4', 'Anual'),
(243, 'Inclusión e integración educativa ', 11, '4', '2°Cuatrimestre'),
(244, 'Residencia y Sistematización de experiencias I', 11, '4', 'Anual'),
(245, 'Practicas Corporales y Necesidades Educativas Especiales', 11, '4', '1°Cuatrimestre'),
(246, 'Deportes colectivos y su enseñanza IV: Hockey  ', 11, '4', 'Anual'),
(247, 'Deportes colectivos y su enseñanza IV: Softbol', 11, '4', 'Anual'),
(248, 'Entrenamiento Deportivo', 11, '4', '2°Cuatrimestre'),
(249, 'Didáctica de la Educación Física III ', 11, '4', 'Anual'),
(250, 'Taller de Evaluación Educativa Áulica ', 11, '5', '1°Cuatrimestre'),
(251, 'Taller de Investigación Educativa ', 11, '5', 'Anual'),
(252, 'Residencia y sistematización de experiencias II ', 11, '5', 'Anual'),
(253, 'Política, Legislación y Gestiones Deportivas', 11, '5', '1°Cuatrimestre'),
(254, 'Problemática de la Educación Superior', 11, '5', '2°Cuatrimestre'),
(255, 'Pedagogía', 2, '1', '1°Cuatrimestre'),
(256, 'Psicología Educacional ', 2, '1', '2°Cuatrimestre'),
(257, 'Alfabetización Académica', 2, '1', 'Anual'),
(258, 'Educación Sexual Integral', 2, '1', '1°Cuatrimestre'),
(259, 'Practica Docente I: La Institución Educativa ', 2, '1', 'Anual'),
(260, 'Sujeto de la Educación I', 2, '1', '2°Cuatrimestre'),
(261, 'Biología del Movimiento I', 2, '1', 'Anual'),
(262, 'Practicas Motrices Integradas', 2, '1', 'Anual'),
(263, 'Practicas Acuáticas', 2, '1', 'Anual'),
(264, 'Deportes Individuales y su Enseñanza I: Atletismo', 2, '1', 'Anual'),
(265, 'Deportes colectivos y su enseñanza I:Basquetbol', 2, '1', 'Anual'),
(266, 'Tecnología de la Información y la Comunicación ', 2, '2', '2°Cuatrimestre'),
(267, 'Sociología de la Educación', 2, '2', '1°Cuatrimestre'),
(268, 'Didáctica General  ', 2, '2', '1°Cuatrimestre'),
(269, 'Practica docente II: Curriculum, Sujetos y Contextos', 2, '2', 'Anual'),
(270, 'Sujeto de la Educación II ', 2, '2', 'Anual'),
(271, 'Biología del Movimiento II', 2, '2', '1°Cuatrimestre'),
(272, 'Gimnasia y su Enseñanza ', 2, '2', 'Anual'),
(273, 'Deportes Individuales y su Enseñanza II: Natación', 2, '2', 'Anual'),
(274, 'Deportes Colectivos y su Enseñanza II: Voleibol', 2, '2', 'Anual'),
(275, 'Juego y Educación Física ', 2, '2', 'Anual'),
(276, 'Didáctica de la Educación: Física I', 2, '2', '2°Cuatrimestre'),
(277, 'Filosofía de la Educación ', 2, '3', '1°Cuatrimestre'),
(278, 'Historia de la Educación y Política Educacional Argentina', 2, '3', 'Anual'),
(279, 'Animación Sociocultural y Dinámica de Grupos', 2, '3', '1°Cuatrimestre'),
(280, 'Practica docente III: Programación Didáctica, Gestión de micro experiencias de Enseñanza', 2, '3', 'Anual'),
(281, 'Teoría y Epistemología de la Educación Física', 2, '3', '2°Cuatrimestre'),
(282, 'Practicas Gimnasticas Actuales y su Enseñanza', 2, '3', 'Anual'),
(283, 'Deportes Colectivos y su Enseñanza III: Cestobol', 2, '3', 'Anual'),
(284, 'Deportes Colectivos y su Enseñanza III: Handbol', 2, '3', 'Anual'),
(285, 'Practicas en la Naturaleza y Educación Ambiental', 2, '3', 'Anual'),
(286, 'Didáctica de la Educación Física II', 2, '3', 'Anual'),
(287, 'EDI: Primeros Auxilios ', 2, '3', '2°Cuatrimestre'),
(288, 'Formación Ética y Ciudadana   ', 2, '4', '1°Cuatrimestre'),
(289, 'Inclusión e Integración Educativa ', 2, '4', '2°Cuatrimestre'),
(290, 'Residencia y Sistematización de Experiencias I ', 2, '4', 'Anual'),
(291, 'Política, Legislación y Gestión Deportiva', 2, '4', '2°Cuatrimestre'),
(292, 'Practicas Corporales y Necesidades Educativas Especiales', 2, '4', '1°Cuatrimestre'),
(293, 'Deportes Colectivos y su Enseñanza IV: Hockey ', 2, '4', 'Anual'),
(294, 'Deportes colectivos y su enseñanza IV: Softbol ', 2, '4', 'Anual'),
(295, 'Entrenamiento Deportivo', 2, '4', '2°Cuatrimestre'),
(296, 'Didáctica de la Educación Física III', 2, '4', 'Anual'),
(297, 'EDI: Técnico Deportivo  ', 2, '4', '1°Cuatrimestre'),
(298, 'EDI: Actividad Física y Salud', 2, '4', '1°Cuatrimestre'),
(299, 'Pedagogía ', 5, '1', '1°Cuatrimestre'),
(300, 'Pedagogía Educacional ', 5, '1', '2°Cuatrimestre'),
(301, 'Alfabetización Académica', 5, '1', 'Anual'),
(302, 'Historia de la Educación y Política Educacional Argentina', 5, '1', 'Anual'),
(303, 'Tecnología de la Información y de la Comunicación', 5, '1', '1°Cuatrimestre'),
(304, 'Practica Docente I: La Institución Educativa', 5, '1', 'Anual'),
(305, 'Matemática', 5, '1', 'Anual'),
(306, 'Química General', 5, '1', 'Anual'),
(307, 'Laboratorio I', 5, '1', 'Anual'),
(308, 'Física I', 5, '1', '2°Cuatrimestre'),
(309, 'Pedagogía ', 5, '1', '1°Cuatrimestre'),
(310, 'Pedagogía Educacional ', 5, '1', '2°Cuatrimestre'),
(311, 'Alfabetización Académica', 5, '1', 'Anual'),
(312, 'Historia de la Educación y Política Educacional Argentina', 5, '1', 'Anual'),
(313, 'Tecnología de la Información y de la Comunicación', 5, '1', '1°Cuatrimestre'),
(314, 'Practica Docente I: La Institución Educativa', 5, '1', 'Anual'),
(315, 'Matemática', 5, '1', 'Anual'),
(316, 'Química General', 5, '1', 'Anual'),
(317, 'Laboratorio I', 5, '1', 'Anual'),
(318, 'Física I', 5, '1', '2°Cuatrimestre'),
(319, 'Didáctica General', 5, '2', 'Anual'),
(320, 'Sociología de la Educación ', 5, '2', 'Anual'),
(321, 'Practica Docente II: Curriculum, Sujetos y Contextos', 5, '2', 'Anual'),
(322, 'Física II', 5, '2', '1°Cuatrimestre'),
(323, 'Epistemología e Historia de la Química', 5, '2', '2°Cuatrimestre'),
(324, 'Sujeto de la Educación', 5, '2', 'Anual'),
(325, 'Química Inorgánica', 5, '2', 'Anual'),
(326, 'Química Orgánica ', 5, '2', 'Anual'),
(327, 'Laboratorio II', 5, '2', 'Anual'),
(328, 'Didáctica General', 5, '2', 'Anual'),
(329, 'Sociología de la Educación ', 5, '2', 'Anual'),
(330, 'Practica Docente II: Curriculum, Sujetos y Contextos', 5, '2', 'Anual'),
(331, 'Física II', 5, '2', '1°Cuatrimestre'),
(332, 'Epistemología e Historia de la Química', 5, '2', '2°Cuatrimestre'),
(333, 'Sujeto de la Educación', 5, '2', 'Anual'),
(334, 'Química Inorgánica', 5, '2', 'Anual'),
(335, 'Química Orgánica ', 5, '2', 'Anual'),
(336, 'Laboratorio II', 5, '2', 'Anual'),
(337, 'Filosofía de la Educación', 5, '3', '1°Cuatrimestre'),
(338, 'Ética y Construcción de la Ciudadanía', 5, '3', '2°Cuatrimestre'),
(339, 'Practica III: Programación Didáctica y Gestión de Micro-experiencias de enseñanza', 5, '3', 'Anual'),
(340, 'Biología', 5, '3', 'Anual'),
(341, 'Didáctica de la Química', 5, '3', 'Anual'),
(342, 'Química Analítica ', 5, '3', 'Anual'),
(343, 'Fisicoquímica ', 5, '3', 'Anual'),
(344, 'Laboratorio III', 5, '3', 'Anual'),
(345, 'Filosofía de la Educación', 5, '3', '1°Cuatrimestre'),
(346, 'Ética y Construcción de la Ciudadanía', 5, '3', '2°Cuatrimestre'),
(347, 'Practica III: Programación Didáctica y Gestión de Micro-experiencias de enseñanza', 5, '3', 'Anual'),
(348, 'Biología', 5, '3', 'Anual'),
(349, 'Didáctica de la Química', 5, '3', 'Anual'),
(350, 'Química Analítica ', 5, '3', 'Anual'),
(351, 'Fisicoquímica ', 5, '3', 'Anual'),
(352, 'Laboratorio III', 5, '3', 'Anual'),
(353, 'Educación Sexual Integral', 5, '4', '1°Cuatrimestre'),
(354, 'Integración e Inclusión Educativa', 5, '4', '2°Cuatrimestre'),
(355, 'Residencia y sistematización de experiencias: Diseño, enseñanza y evaluación ', 5, '4', 'Anual'),
(356, 'Ciencias de la Tierra ', 5, '4', 'Anual'),
(357, 'Química Biológica ', 5, '4', 'Anual'),
(358, 'Química Ambiental y Salud', 5, '4', '1°Cuatrimestre'),
(359, 'Química Aplicada e Industrial', 5, '4', '2°Cuatrimestre'),
(360, 'Laboratorio IV', 5, '4', 'Anual'),
(361, 'Educación Sexual Integral', 5, '4', '1°Cuatrimestre'),
(362, 'Integración e Inclusión Educativa', 5, '4', '2°Cuatrimestre'),
(363, 'Residencia y sistematización de experiencias: Diseño, enseñanza y evaluación ', 5, '4', 'Anual'),
(364, 'Ciencias de la Tierra ', 5, '4', 'Anual'),
(365, 'Química Biológica ', 5, '4', 'Anual'),
(366, 'Química Ambiental y Salud', 5, '4', '1°Cuatrimestre'),
(367, 'Química Aplicada e Industrial', 5, '4', '2°Cuatrimestre'),
(368, 'Laboratorio IV', 5, '4', 'Anual'),
(369, 'Pedagogía', 1, '1', '1°Cuatrimestre'),
(370, 'Psicología Educacional ', 1, '1', '2°Cuatrimestre'),
(371, 'Educación Sexual Integral ', 1, '1', '2°Cuatrimestre'),
(372, 'Alfabetización Académica', 1, '1', 'Anual'),
(373, 'Historia de la Educación y Política Educacional Argentina', 1, '1', '1°Cuatrimestre'),
(374, 'Practica I', 1, '1', 'Anual'),
(375, 'Biología del Movimiento ', 1, '1', 'Anual'),
(376, 'Formación Físico-motriz', 1, '1', 'Anual'),
(377, 'Deportes individuales y su enseñanza I: Atletismo', 1, '1', '1°Cuatrimestre'),
(378, 'Deportes colectivos y su enseñanza I: Basquet', 1, '1', '2°Cuatrimestre'),
(379, 'Juegos motores y deportivos', 1, '1', 'Anual'),
(380, 'Historia de la Educación Física Argentina y Latinoamericana', 1, '1', '2°Cuatrimestre'),
(381, 'Formación Ética y Ciudadana ', 1, '2', '2°Cuatrimestre'),
(382, 'Formación Ética y Ciudadana ', 1, '1', '1°Cuatrimestre'),
(383, 'Sociología de la Educación', 1, '2', '2°Cuatrimestre'),
(384, 'Practica II', 1, '2', 'Anual'),
(385, 'Sujeto de la Educación I', 1, '2', '1°Cuatrimestre'),
(386, 'Biología del movimiento II', 1, '2', '1°Cuatrimestre'),
(387, 'Gimnasia y su enseñanza', 1, '2', 'Anual'),
(388, 'Deportes Individuales y su Enseñanza II: Judo', 1, '2', '1°Cuatrimestre'),
(389, 'Deportes individuales y su enseñanza III: Atletismo', 1, '2', '2°Cuatrimestre'),
(390, 'Deportes colectivos y su enseñanza II: Futbol', 1, '2', '1°Cuatrimestre'),
(391, 'Deportes colectivos y su enseñanza III: Cestobol', 1, '2', '2°Cuatrimestre'),
(392, 'Deportes colectivos y su enseñanza III: Handbol', 1, '2', '2°Cuatrimestre'),
(393, 'Practicas Acuáticas I', 1, '2', '2°Cuatrimestre'),
(394, 'Juego y Educación Física', 1, '2', 'Anual'),
(395, 'Desarrollo Motor y Practicas Corporales', 1, '2', '1°Cuatrimestre'),
(396, 'Didáctica de la educación física I ', 1, '2', '2°C'),
(397, 'Filosofía ', 1, '3', '1°Cuatrimestre'),
(398, 'Tecnología de la Información y de la Comunicación', 1, '3', '1°Cuatrimestre'),
(399, 'Practica III', 1, '3', 'Anual'),
(400, 'Sujeto de la Educación II ', 1, '3', '1°Cuatrimestre'),
(401, 'Sujeto de la Educación Especial', 1, '3', '2°Cuatrimestre'),
(402, 'Teoría y Epistemología de la Educación Física ', 1, '3', '2°Cuatrimestre'),
(403, 'Técnicas Gimnasticas Actuales y su Enseñanza', 1, '3', 'Anual'),
(404, 'Deportes Colectivos y su Enseñanza IV', 1, '3', '1°Cuatrimestre'),
(405, 'Deportes Colectivos y su Enseñanza V', 1, '3', '2°Cuatrimestre'),
(406, 'Practicas Acuáticas II', 1, '3', '2°Cuatrimestre'),
(407, 'Practicas en la Naturaleza y Educación Ambiental I', 1, '3', '2°Cuatrimestre'),
(408, 'Practicas corporales y aprendizaje ', 1, '3', '1°Cuatrimestre'),
(409, 'Didáctica de la Educación Física II ', 1, '3', 'Anual'),
(410, 'Animación Sociocultural y Dinámica de Grupos', 1, '4', '2°Cuatrimestre'),
(411, 'Inclusión e Integración Escolar', 1, '4', '1°Cuatrimestre'),
(412, 'Practica IV  ', 1, '4', 'Anual'),
(413, 'Deportes colectivos y su enseñanza VI: Vóley', 1, '4', '1°Cuatrimestre'),
(414, 'Entrenamiento  ', 1, '4', '2°Cuatrimestre'),
(415, 'Practicas Corporales para Necesidades Educativas Especiales', 1, '4', '1°Cuatrimestre'),
(416, 'Practicas Corporales del Adulto Mayor', 1, '4', '2°Cuatrimestre'),
(417, 'Política, Legislación y Gestión Deportiva', 1, '4', '2°Cuatrimestre'),
(418, 'Tiempo Libre y Problemáticas Recreativas', 1, '4', '1°Cuatrimestre'),
(419, 'Practicas en la Naturaleza II', 1, '4', '2°Cuatrimestre'),
(420, 'EDI: Actividad Física', 1, '4', 'Anual'),
(421, 'Sociología', 8, '1', '1 Cuatrimestre'),
(422, 'Problemática del Nivel Superior', 8, '1', '1 Cuatrimestre'),
(423, 'Historia General de la Educación', 8, '1', '2 Cuatrimestre'),
(424, 'Sociología de la Educación', 8, '1', '2 Cuatrimestre'),
(425, 'Historia Social Argentina y Latinoamericana', 8, '1', 'Anual'),
(426, 'Psicología General', 8, '1', 'Anual'),
(427, 'Alfabetización Académica', 8, '1', 'Anual'),
(428, 'Practica docente I: La Institución Educativa', 8, '1', 'Anual'),
(429, 'Pedagogia General', 8, '1', 'Anual'),
(430, 'Didactica General', 8, '1', 'Anual'),
(431, 'Antropología', 8, '2', '1 Cuatrimestre'),
(432, 'Didáctica I: Nivel Inicial', 8, '2', '1 Cuatrimestre'),
(433, 'Didáctica II: Nivel Primario', 8, '2', '2 Cuatrimestre'),
(434, 'Tecnologías de la información y la comunicación', 8, '2', 'Anual'),
(435, 'Filosofía', 8, '2', 'Anual'),
(436, 'Practica Docente II: Curriculum, sujetos y contextos', 8, '2', 'Anual'),
(437, 'Sujetos de la Educación I', 8, '2', 'Anual'),
(438, 'Psicología de la Educación', 8, '2', 'Anual'),
(439, 'Teoría y Política Curricular', 8, '2', 'Anual'),
(440, 'Epistemología de las Ciencias Sociales', 8, '3', '1 Cuatrimestre'),
(441, 'Filosofía de la Educación', 8, '3', '1 Cuatrimestre'),
(442, 'Educación Sexual Integral', 8, '3', '2 Cuatrimestre'),
(443, 'Historia de la Educación Argentina', 8, '3', '2 Cuatrimestre'),
(444, 'Lengua Extranjera: Ingles', 8, '3', 'Anual'),
(445, 'Practica Docente III: Programación, Didáctica, Gestión de Micro-experiencias de enseñanzas', 8, '3', 'Anual'),
(446, 'Sujeto de la Educación II: pubertad y adolescencia', 8, '3', 'Anual'),
(447, 'Didáctica III: Nivel Secundario', 8, '3', 'Anual'),
(448, 'Educación y TIC I', 8, '3', 'Anual'),
(449, 'Formación Ética y Ciudadana', 8, '4', '1 Cuatrimestre'),
(450, 'Educación Comparada', 8, '4', '1 Cuatrimestre'),
(451, 'Política Educacional Argentina', 8, '4', '2 Cuatrimestre'),
(452, 'Pensamiento Pedagógico Latinoamericano', 8, '4', '2 Cuatrimestre'),
(453, 'Residencia y Sistematización de experiencias: Diseño, enseñanzas y evaluación en los Niveles Inicial', 8, '4', 'Anual'),
(454, 'Didáctica IV: Nivel  Superior', 8, '4', 'Anual'),
(455, 'Metodología de Investigación Educativa', 8, '4', 'Anual'),
(456, 'Educación y TIC II', 8, '4', 'Anual'),
(457, 'Integración y Inclusión Educativa', 8, '5', '1 Cuatrimestre'),
(458, 'Evaluación educativa I: Áulica', 8, '5', '1 Cuatrimestre'),
(459, 'Educación en Contextos Diversos', 8, '5', '1 Cuatrimestre'),
(460, 'Evaluación Educativa II: Institucional', 8, '5', '2 Cuatrimestre'),
(461, 'Administración y Gestión Educativa', 8, '5', '2 Cuatrimestre'),
(462, 'Residencia y Sistematización de Experiencias en el Nivel Superior ', 8, '5', 'Anual'),
(463, 'Planeamiento Educativo', 8, '5', 'Anual'),
(464, 'Comprensión y Producción de Textos', 10, '1', '1 Cuatrimestre'),
(465, 'Historia y Sociología del Deporte', 10, '1', '1 Cuatrimestre'),
(466, 'TIC Aplicada a la Gestión Deportiva', 10, '1', '1 Cuatrimestre'),
(467, 'Marketing Deportivo', 10, '1', '1 Cuatrimestre'),
(468, 'Gestión del Talento Humano en el Deporte', 10, '1', '1 Cuatrimestre'),
(469, 'Psicología del Desarrollo Humano', 10, '1', '2 Cuatrimestre'),
(470, 'Estadística Aplicada al Deporte', 10, '1', '2 Cuatrimestre'),
(471, 'Planificación y Gestión de Proyectos Deportivos', 10, '1', '2 Cuatrimestre'),
(472, 'Publicidad, Promoción y Patrocinio de Eventos Deportivos', 10, '1', '2 Cuatrimestre'),
(473, 'Protocolo Ceremonial en Eventos Deportivos', 10, '1', '2 Cuatrimestre'),
(474, 'Ingles', 10, '1', 'Anual'),
(475, 'Anatomía Humana', 10, '1', 'Anual'),
(476, 'Deporte I', 10, '1', 'Anual'),
(477, 'Practica Profesional', 10, '1', 'Anual'),
(478, 'Problemática Socio-Contemporánea', 10, '2', '1 Cuatrimestre'),
(479, 'Ética del Deporte', 10, '2', '1 Cuatrimestre'),
(480, 'Psicología de la Act. Física y el Deporte', 10, '2', '2 Cuatrimestre'),
(481, 'Economía y Finanzas Deportivas', 10, '2', '2 Cuatrimestre'),
(482, 'Organización, Administración y Legislación Deportiva', 10, '2', 'Anual'),
(483, 'Análisis del Movimiento Humano', 10, '2', 'Anual'),
(484, 'Deporte II', 10, '2', 'Anual'),
(485, 'Act. Físicas, Recreativas y Sociales para Adultos Mayores', 10, '2', 'Anual'),
(486, 'Fisiología del Ejercicio', 10, '2', 'Anual'),
(487, 'Política, Organización y Gestión de Torneos y Competencias', 10, '2', 'Anual'),
(488, 'Practicas Profesionalizantes', 10, '2', 'Anual'),
(489, 'Pedagogía', 6, '1', '1 Cuatrimestre'),
(490, 'Historia Argentina y Latinoamericana', 6, '1', '1 Cuatrimestre'),
(491, 'Sociología de la Educación', 6, '1', '1 Cuatrimestre'),
(492, 'Psicología Educacional', 6, '1', '2 Cuatrimestre'),
(493, 'Historia de la Educación y Política Educacional Argentina', 6, '1', '2 Cuatrimestre'),
(494, 'Alfabetización Académica', 6, '1', 'Anual'),
(495, 'Practica I: La Institución Educación, aproximaciones desde un enfoque investigativo', 6, '1', 'Anual'),
(496, 'Historia de la Filosofía Antigua', 6, '1', 'Anual'),
(497, 'Introducción a la Filosofía', 6, '1', 'Anual'),
(498, 'Lógica y Argumentación', 6, '1', 'Anual'),
(499, 'Epistemología e Historia de la Ciencia', 6, '2', '1 Cuatrimestre'),
(500, 'Tecnología de la Información y la Comunicación', 6, '2', '2 Cuatrimestre'),
(501, 'Didáctica General', 6, '2', 'Anual'),
(502, 'Practica II: Curriculum, Sujetos y Contextos, Aproximaciones desde un enfoque investigativo', 6, '2', 'Anual'),
(503, 'Sujeto de la Educacion Secundaria', 6, '2', 'Anual'),
(504, 'Antropología Filosofía', 6, '2', 'Anual'),
(505, 'Historia de la Filosofía Medieval', 6, '2', 'Anual'),
(506, 'Etica', 6, '2', 'Anual'),
(507, 'Teoría del Conocimiento', 6, '2', 'Anual'),
(508, 'Filosofía de la Educación', 6, '3', '1 Cuatrimestre'),
(509, 'Filosofía del Lenguaje', 6, '3', '1 Cuatrimestre'),
(510, 'Filosofía Social y DDHH', 6, '3', '1 Cuatrimestre'),
(511, 'Formación Ética y Ciudadana', 6, '3', '2 Cuatrimestre'),
(512, 'Filosofía Practica', 6, '3', '2 Cuatrimestre'),
(513, 'Filosofía y Arte', 6, '3', '2 Cuatrimestre'),
(514, 'Practica III: Programación Didáctica y Gestión de Micro-experiencias de enseñanzas para Nivel Primar', 6, '3', 'Anual'),
(515, 'Didáctica de la Filosofía', 6, '3', 'Anual'),
(516, 'Historia de la Filosofía Moderna', 6, '3', 'Anual'),
(517, 'Educación Sexual Integral', 6, '4', '1 Cuatrimestre'),
(518, 'Filosofía de la Comunicación y TICS', 6, '4', '1 Cuatrimestre'),
(519, 'Política y Ciudadanía', 6, '4', '2 Cuatrimestre'),
(520, 'Filosofía Latinoamericana e Intercultural', 6, '4', '2 Cuatrimestre'),
(521, 'Residencia y Sistematización de Exp. Diseño, Enseñanza y Evaluación', 6, '4', 'Anual'),
(522, 'Filosofía Contemporánea', 6, '4', 'Anual'),
(523, 'Metafisica', 6, '4', 'Anual'),
(524, 'Pedagogía', 7, '1', '1 Cuatrimestre'),
(525, 'Psicología Educacional', 7, '1', '2 Cuatrimestre'),
(526, 'Alfabetización Académica', 7, '1', 'Anual'),
(527, 'Filosofía', 7, '1', '1 Cuatrimestre'),
(528, 'Hist.de la Educ. Polit. Educ. Arg.', 7, '1', '2 Cuatrimestre'),
(529, 'Practica I', 7, '1', 'Anual'),
(530, 'Introducción a la Historia', 7, '1', '1 Cuatrimestre'),
(531, 'Historia de América I', 7, '1', '2 Cuatrimestre'),
(532, 'Culturas Orig. Americ. y Arg.', 7, '1', 'Anual'),
(533, 'Historia Antigua', 7, '1', 'Anual'),
(534, 'Epistemología de la Ciencia', 7, '2', '1 Cuatrimestre'),
(535, 'Problemática Socio-antropológica Educativa', 7, '2', '2 Cuatrimestre'),
(536, 'Didáctica General', 7, '2', 'Anual'),
(537, 'Practica II', 7, '2', 'Anual'),
(538, 'Sujeto de la Educación', 7, '2', 'Anual'),
(539, 'Historia Medieval', 7, '2', '1 Cuatrimestre'),
(540, 'Historia Moderna', 7, '2', '2 Cuatrimestre'),
(541, 'Historia de América II', 7, '2', 'Anual'),
(542, 'Historia de Argentina I', 7, '2', 'Anual'),
(543, 'EDI: Espacio y Soledad', 7, '2', '1 Cuatrimestre'),
(544, 'EDI: Producciones Historiograficas', 7, '2', '2 Cuatrimestre'),
(545, 'Sociología de la Educación', 7, '3', '1 Cuatrimestre'),
(546, 'Tecnología de la Información y la Comunicación', 7, '3', '2 Cuatrimestre'),
(547, 'Practica III', 7, '3', 'Anual'),
(548, 'Didáctica de la Historia', 7, '3', 'Anual'),
(549, 'Historia de América III', 7, '3', 'Anual'),
(550, 'Historia de Sgo y del NOA I', 7, '3', 'Anual'),
(551, 'Historia de Argentina II', 7, '3', 'Anual'),
(552, 'Corrientes Historiográficas Contemporáneas', 7, '3', '1 Cuatrimestre'),
(553, 'EDI: Ideas Políticas', 7, '3', '2 Cuatrimestre'),
(554, 'Educación Sexual Integral', 7, '4', '1 Cuatrimestre'),
(555, 'Formación Ética y Ciudadana', 7, '4', '1 Cuatrimestre'),
(556, 'Residencia y Sistematización de Experiencias', 7, '4', 'Anual'),
(557, 'Historia Arg. Reciente', 7, '4', 'Anual'),
(558, 'Historia de Sgo y del NOA II', 7, '4', 'Anual'),
(559, 'Historia Contemporanea', 7, '4', 'Anual'),
(560, 'EDI: Metodología de la Investigación', 7, '4', 'Anual');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mesaexamenes`
--

CREATE TABLE `mesaexamenes` (
  `idMesaExamenes` int(11) NOT NULL,
  `idmateria` int(11) NOT NULL,
  `fechaExamen` datetime DEFAULT NULL,
  `lugarExamen` varchar(45) DEFAULT NULL,
  `modoExamen` varchar(45) DEFAULT NULL,
  `idcalendario` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `mesaexamenes`
--

INSERT INTO `mesaexamenes` (`idMesaExamenes`, `idmateria`, `fechaExamen`, `lugarExamen`, `modoExamen`, `idcalendario`) VALUES
(1, 3, '2022-07-20 18:00:00', 'Aula 8', 'Presencial', 1),
(2, 7, '2022-07-21 08:00:00', 'Aula 3', 'Presencial', 1),
(3, 9, '2021-07-21 08:00:00', 'Aasd', 'Asd', 1),
(4, 6, '2022-07-21 08:00:00', 'asd', 'asd', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `orientacion`
--

CREATE TABLE `orientacion` (
  `OrientacionID` int(11) NOT NULL,
  `OrientacionNombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='En esta tabla se representan tres orientaciones que corresponden a una carrera';

--
-- Volcado de datos para la tabla `orientacion`
--

INSERT INTO `orientacion` (`OrientacionID`, `OrientacionNombre`) VALUES
(1, 'Sordos e Hipoacusticos'),
(2, 'Neuromotor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfiles`
--

CREATE TABLE `perfiles` (
  `idperfiles` int(11) NOT NULL,
  `perfil` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `perfiles`
--

INSERT INTO `perfiles` (`idperfiles`, `perfil`) VALUES
(1, 'Bedel'),
(2, 'Docente'),
(3, 'Alumno');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plandeestudio`
--

CREATE TABLE `plandeestudio` (
  `PlanID` int(11) NOT NULL,
  `PlanNombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='En esta tabla se representan los diferentes planes de estudio';

--
-- Volcado de datos para la tabla `plandeestudio`
--

INSERT INTO `plandeestudio` (`PlanID`, `PlanNombre`) VALUES
(1, '2012'),
(2, '2016'),
(3, '2018'),
(4, '2021'),
(5, '2015'),
(6, '2017'),
(7, '2014'),
(8, '2022');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idusuario` int(11) NOT NULL,
  `usuario` varchar(250) NOT NULL,
  `contraseña` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `contraseñatemp` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idusuario`, `usuario`, `contraseña`, `email`, `contraseñatemp`) VALUES
(1, 'nicocalde', 'pbkdf2:sha256:260000$pOB67GOTBZfODDOq$d3243bb82aca93fd197b81b5858683074793a49cf090408e886f46354eed407c', 'nicocalderon9818@gmail.com', NULL),
(2, 'exequiel', 'pbkdf2:sha256:260000$z8pN6PPD5GZBnhyj$495f9c42ee98926d37290cdba7fd462a74e5eb8370972f04350c383ca783ef46', 'fateofkiel2000@gmail.com', NULL),
(4, 'Mjsn98', 'pbkdf2:sha256:260000$5Q00hi9g8gCSlMtF$63499e381389168eddc66cb92257c2060c8584f83fffe70c53ac216faff0e99d', 'mjsn98@gmail.com', NULL),
(5, 'niconico', 'pbkdf2:sha256:260000$2zpWBIdXnfBuW76l$97f70eb1ec33cde3caab99265df8689c6cb002b39461c6579ec3ba5cff306b34', 'nico9823@gmail.com', NULL),
(6, 'ejemplo123', 'pbkdf2:sha256:260000$WtiWuYxfRbLBTZZR$edd1e1ea7737e05499b273abf002dedabab477dd3d131459d28ac43aedb0dec9', 'ejemplo123', NULL),
(7, 'holaprueba123', 'pbkdf2:sha256:260000$3rlIlgLptYjLxfbe$0f0383f2f786a5f53cd3b61af001bf60736dcdd3c1a2b5b330615cdbffedeb64', 'holaprueba123@gmail.com', NULL),
(8, 'honguillo', 'pbkdf2:sha256:260000$Wvb6vu2HVjjMKwyy$355cb5602a1cd01e3b8db2aeb3266805369830c9a2b9d6ced2574b03cd58a680', 'nacosta722@gmail.com', NULL),
(9, 'bedel', 'pbkdf2:sha256:260000$w6E01rXfn6tt4Jd2$c2502911753b2beaa6a7f52034b2155e0332abb668ea93647236c4b5c4df6a73', 'agustin9812@gmail.com', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuariosperfiles`
--

CREATE TABLE `usuariosperfiles` (
  `idusuarioperfil` int(11) NOT NULL,
  `idusuario` int(11) NOT NULL,
  `idperfil` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuariosperfiles`
--

INSERT INTO `usuariosperfiles` (`idusuarioperfil`, `idusuario`, `idperfil`) VALUES
(1, 1, 3),
(2, 2, 3),
(4, 9, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `calendario`
--
ALTER TABLE `calendario`
  ADD PRIMARY KEY (`idcalendario`);

--
-- Indices de la tabla `carpestmateria`
--
ALTER TABLE `carpestmateria`
  ADD PRIMARY KEY (`idcarpestMateria`),
  ADD KEY `idMateria_idx` (`idMateria`),
  ADD KEY `idCarpoEstudiante_idx` (`idCarpoEstudiante`);

--
-- Indices de la tabla `carpo`
--
ALTER TABLE `carpo`
  ADD PRIMARY KEY (`CARPOID`),
  ADD KEY `CARPOCarreraID_idx` (`CarreraID`),
  ADD KEY `CARPOPlanID_idx` (`PlanDeEstudioID`),
  ADD KEY `CARPOOrientacionID_idx` (`OrientacionID`);

--
-- Indices de la tabla `carpoestudiante`
--
ALTER TABLE `carpoestudiante`
  ADD PRIMARY KEY (`idCARPOEstudiante`),
  ADD KEY `idCARPO_idx` (`idCARPO`),
  ADD KEY `idEstudiante_idx` (`idEstudiante`);

--
-- Indices de la tabla `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`CarreraID`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`idestudiante`),
  ADD KEY `estudianteusuariosperfiles_idx` (`IDusuariosPerfiles`);

--
-- Indices de la tabla `inscripcionexamencarpestmat`
--
ALTER TABLE `inscripcionexamencarpestmat`
  ADD PRIMARY KEY (`idInscripcionExamenCarpestMat`),
  ADD KEY `idCarpestMateria_idx` (`idCarpestMateria`),
  ADD KEY `idMesaExamenes_idx` (`idMesaExamenes`);

--
-- Indices de la tabla `mandarcorreo`
--
ALTER TABLE `mandarcorreo`
  ADD PRIMARY KEY (`idmandarcorreo`);

--
-- Indices de la tabla `materia`
--
ALTER TABLE `materia`
  ADD PRIMARY KEY (`idmateria`),
  ADD KEY `idcarpomat_idx` (`idcarpo`);

--
-- Indices de la tabla `mesaexamenes`
--
ALTER TABLE `mesaexamenes`
  ADD PRIMARY KEY (`idMesaExamenes`),
  ADD KEY `mesamateria_idx` (`idmateria`),
  ADD KEY `calendariomesa_idx` (`idcalendario`);

--
-- Indices de la tabla `orientacion`
--
ALTER TABLE `orientacion`
  ADD PRIMARY KEY (`OrientacionID`);

--
-- Indices de la tabla `perfiles`
--
ALTER TABLE `perfiles`
  ADD PRIMARY KEY (`idperfiles`);

--
-- Indices de la tabla `plandeestudio`
--
ALTER TABLE `plandeestudio`
  ADD PRIMARY KEY (`PlanID`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idusuario`),
  ADD UNIQUE KEY `usuario_UNIQUE` (`usuario`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`);

--
-- Indices de la tabla `usuariosperfiles`
--
ALTER TABLE `usuariosperfiles`
  ADD PRIMARY KEY (`idusuarioperfil`),
  ADD KEY `idus_idx` (`idusuario`),
  ADD KEY `idpef_idx` (`idperfil`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `calendario`
--
ALTER TABLE `calendario`
  MODIFY `idcalendario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `carpestmateria`
--
ALTER TABLE `carpestmateria`
  MODIFY `idcarpestMateria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `carpo`
--
ALTER TABLE `carpo`
  MODIFY `CARPOID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `carpoestudiante`
--
ALTER TABLE `carpoestudiante`
  MODIFY `idCARPOEstudiante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `carrera`
--
ALTER TABLE `carrera`
  MODIFY `CarreraID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `orientacion`
--
ALTER TABLE `orientacion`
  MODIFY `OrientacionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `materia`
--
ALTER TABLE `materia`
  MODIFY `idmateria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=561;

--
-- AUTO_INCREMENT de la tabla `perfiles`
--
ALTER TABLE `perfiles`
  MODIFY `idperfiles` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `plandeestudio`
--
ALTER TABLE `plandeestudio`
  MODIFY `PlanID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuariosperfiles`
--
ALTER TABLE `usuariosperfiles`
  MODIFY `idusuarioperfil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carpestmateria`
--
ALTER TABLE `carpestmateria`
  ADD CONSTRAINT `idCarpoEstudiante` FOREIGN KEY (`idCarpoEstudiante`) REFERENCES `carpoestudiante` (`idCARPOEstudiante`),
  ADD CONSTRAINT `idMateria` FOREIGN KEY (`idMateria`) REFERENCES `materia` (`idmateria`);

--
-- Filtros para la tabla `carpo`
--
ALTER TABLE `carpo`
  ADD CONSTRAINT `CARPOCarreraID` FOREIGN KEY (`CarreraID`) REFERENCES `carrera` (`CarreraID`),
  ADD CONSTRAINT `CARPOOrientacionID` FOREIGN KEY (`OrientacionID`) REFERENCES `orientacion` (`OrientacionID`),
  ADD CONSTRAINT `CARPOPlanID` FOREIGN KEY (`PlanDeEstudioID`) REFERENCES `plandeestudio` (`PlanID`);

--
-- Filtros para la tabla `carpoestudiante`
--
ALTER TABLE `carpoestudiante`
  ADD CONSTRAINT `idCARPO` FOREIGN KEY (`idCARPO`) REFERENCES `carpo` (`CARPOID`),
  ADD CONSTRAINT `idEstudiante` FOREIGN KEY (`idEstudiante`) REFERENCES `estudiante` (`idestudiante`);

--
-- Filtros para la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD CONSTRAINT `estudianteusuariosperfiles` FOREIGN KEY (`IDusuariosPerfiles`) REFERENCES `usuariosperfiles` (`idusuarioperfil`);

--
-- Filtros para la tabla `inscripcionexamencarpestmat`
--
ALTER TABLE `inscripcionexamencarpestmat`
  ADD CONSTRAINT `idCarpestMateria` FOREIGN KEY (`idCarpestMateria`) REFERENCES `carpestmateria` (`idcarpestMateria`),
  ADD CONSTRAINT `idMesaExamenes` FOREIGN KEY (`idMesaExamenes`) REFERENCES `mesaexamenes` (`idMesaExamenes`);

--
-- Filtros para la tabla `materia`
--
ALTER TABLE `materia`
  ADD CONSTRAINT `idcarpomat` FOREIGN KEY (`idcarpo`) REFERENCES `carpo` (`CARPOID`);

--
-- Filtros para la tabla `mesaexamenes`
--
ALTER TABLE `mesaexamenes`
  ADD CONSTRAINT `calendariomesa` FOREIGN KEY (`idcalendario`) REFERENCES `calendario` (`idcalendario`),
  ADD CONSTRAINT `mesamateria` FOREIGN KEY (`idmateria`) REFERENCES `materia` (`idmateria`);

--
-- Filtros para la tabla `usuariosperfiles`
--
ALTER TABLE `usuariosperfiles`
  ADD CONSTRAINT `idpef` FOREIGN KEY (`idperfil`) REFERENCES `perfiles` (`idperfiles`),
  ADD CONSTRAINT `idus` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`idusuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
