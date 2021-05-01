-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 27, 2021 at 03:55 PM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `austruck`
--

-- --------------------------------------------------------

--
-- Table structure for table `fatiguestatic`
--

DROP TABLE IF EXISTS `fatiguestatic`;
CREATE TABLE IF NOT EXISTS `fatiguestatic` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `SessionID` text NOT NULL,
  `SessionStart` datetime NOT NULL,
  `SessionEND` datetime NOT NULL,
  `BlinkCount` int(11) NOT NULL,
  `AlarmCount` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `licensetype`
--

DROP TABLE IF EXISTS `licensetype`;
CREATE TABLE IF NOT EXISTS `licensetype` (
  `LicenseTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `LicenseTypeName` varchar(40) NOT NULL,
  `Description` text,
  PRIMARY KEY (`LicenseTypeID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `licensetype`
--

INSERT INTO `licensetype` (`LicenseTypeID`, `LicenseTypeName`, `Description`) VALUES
(1, 'car license', NULL),
(2, 'Medium or Heavy rigid vehicle', NULL),
(3, ' Heavy combination', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `roadsdef`
--

DROP TABLE IF EXISTS `roadsdef`;
CREATE TABLE IF NOT EXISTS `roadsdef` (
  `RoadTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `SpeedLimit` int(11) DEFAULT NULL,
  `RoadSize` int(11) DEFAULT NULL,
  PRIMARY KEY (`RoadTypeID`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `roadsdef`
--

INSERT INTO `roadsdef` (`RoadTypeID`, `SpeedLimit`, `RoadSize`) VALUES
(1, 40, NULL),
(2, 70, NULL),
(3, 80, NULL),
(4, 100, NULL),
(5, 120, NULL),
(6, 200, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ruleandregulation`
--

DROP TABLE IF EXISTS `ruleandregulation`;
CREATE TABLE IF NOT EXISTS `ruleandregulation` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `RuleText` text NOT NULL,
  `Truck` int(11) DEFAULT NULL,
  `License` int(11) DEFAULT NULL,
  `Road` varchar(20) DEFAULT NULL,
  `RuleCondition` text,
  `SignPictureURL` text,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ruleandregulation`
--

INSERT INTO `ruleandregulation` (`ID`, `RuleText`, `Truck`, `License`, `Road`, `RuleCondition`, `SignPictureURL`) VALUES
(1, 'Must hold at least 1 year of Australian car license.', 1, 1, NULL, '', ''),
(2, 'Must travel at speeds no greater than the speed displayed on a speed limit sign as well as complying with the following conditions: \r\n» 40 km/h in a local traffic zone signed 40 km/h \r\n» 50 km/h in a built-up area not otherwise signed \r\n» 100 km/h in a 100 km/h zone \r\n» 100 km/h in a 110 km/h zone.', 1, 1, NULL, 'pneumatic tyres', '\\static\\img\\RuleSigns\\70Speed.png'),
(3, 'Must wear a properly adjusted and fastened seatbelt where one is fitted, or is required by law to be fitted to the vehicle.( As part of managing fatigue there is an exemption from wearing seatbelts for two-up drivers in sleeping compartments)', 1, 1, NULL, NULL, '\\static\\img\\RuleSigns\\fastenedseatbelt.jpg'),
(4, 'You must carry three approved portable warning triangles in your vehicle at all times.', 3, 3, NULL, NULL, '\\static\\img\\RuleSigns\\WorningTriangle.jpg'),
(5, 'If you have to stop your vehicle or if any part of your load falls onto the road (including the shoulder), three portable warning triangles must be placed on the road', 3, 3, NULL, '', ''),
(6, 'On roads with a speed limit of 80km/h or more, if the vehicle is not visible for 300 metres in all directions: \r\n» one triangle must be placed 200-250 metres behind the vehicle or fallen load, \r\n» one triangle must be placed 200-250 metres in front of the vehicle or fallen load, and \r\n» one triangle must be placed by the side of the vehicle or fallen load. ', 3, 3, '80', NULL, '\\static\\img\\RuleSigns\\80Speed.png'),
(7, 'On roads with a speed limit of 80km/h or more, if the vehicle is not visible for 200 metres in all directions: \r\n» one triangle must be placed 50-150 metres behind the vehicle or fallen load, \r\n» one triangle must be placed 50-150 metres in front of the vehicle or fallen load, and \r\n» one triangle must be placed by the side of the vehicle or fallen load.', 3, 3, '70', NULL, ''),
(8, 'Drivers of fatigue-regulated heavy vehicles must work to standard hours if the operator they work for does not hold BFM or AFM accreditation.', 1, 1, NULL, NULL, ''),
(9, 'A pre-trip inspection should be done by the driver which includes external check, vehicle tilt, load and load security, vehicle damage, leaks, area check, wheels and rims, check wheel nuts, tyres, engine checks and driver controls check.', 1, 1, NULL, NULL, ''),
(10, 'The sign “DO NOT OVERTAKE TURNING VEHICLE” may be attached to the rear of heavy vehicles over 7.5 metres long. Traffic following behind you must be able to see it clearly. The sign allows the driver to occupy space outside an assigned lane when turning so long as: » the vehicle is within 50 metres from the corner » the move can be made safely » wherever possible, you should set up the back of your vehicle so that traffic behind you cannot overtake your vehicle on the side you are turning to.', 3, 3, NULL, NULL, '\\static\\img\\RuleSigns\\DO_NOT_OVERTAKE_TURNING.jpg'),
(11, 'This sign has been introduced on some three-lane and four -lane freeways in Victoria. It prohibits all heavy vehicles over 4.5 tonnes, except buses and caravans, from travelling in the right lane wherever it is displayed. The restriction applies 24 hours a day.', 2, 2, NULL, NULL, '\\static\\img\\RuleSigns\\notrucks.png'),
(12, 'Load limit signs may apply to bridges or sections of road. You must not pass this sign if axle group mass of your vehicle is more than that allowed by the sign. Fines are heavy and you might have to pay for damage caused to roads that cannot take the weight of your vehicle.', 2, 2, NULL, NULL, '\\static\\img\\RuleSigns\\BridgeLimit.png'),
(14, 'If the driver of a truck drives past a trucks must enter sign, the driver must enter the area indicated by information on or with the sign.', 2, 2, NULL, NULL, '\\static\\img\\RuleSigns\\trucksmustenter.png'),
(15, 'No goods-carrying vehicle over 4.5 tonnes GVM can pass this sign without a permit from VicRoads or from the local council, unless the following exemptions apply: \r\n» the driver travels beyond the sign in any other lane, or \r\n» the driver of the truck is loading or unloading at a location beyond the no truck sign and no suitable alternative route to the location exists \r\n» the driver is escorted by a police officer or an authorised officer of the corporation.', 2, 2, NULL, NULL, '\\static\\img\\RuleSigns\\notrucks.png'),
(16, 'This sign will tell you the clearance under the bridge and may indicate a detour to avoid the obstruction. Check that your vehicle will fit under the bridge. You must know your maximum vehicle height.', 3, 3, NULL, NULL, '\\static\\img\\RuleSigns\\lowbridge.png'),
(17, 'A low clearance sign will tell you the clearance under the obstruction. If your vehicle is the height shown on the sign or higher, you must not drive under it. ', 1, 1, NULL, NULL, '\\static\\img\\RuleSigns\\lowclearance.png'),
(18, 'Clearance signs will tell you the clearance under an obstruction. These signs are only used where the clearance is at least 4 metres. If your vehicle is the height on the sign or higher, you must not drive under it.', 1, 1, NULL, NULL, '\\static\\img\\RuleSigns\\clearance.png'),
(19, 'Perform coupling of trailers by inspecting the area, inspect or check coupling devices, check trailer height, back the prime mover, check the connection, secure the vehicle, visually inspect, connect the electrical cable, raise the trailer supports and remove trailer wheel chocks.', 1, 1, NULL, NULL, NULL),
(20, 'Perform uncoupling of trailers by positioning the vehicle, apply the trailer brakes, secure the vehicle, lower the landing gear, disconnect air lines, release the turntable latch, pull the prime mover partially clear, secure the prime mover again, inspect the semi-trailer support and release the parking brake.', 1, 1, NULL, NULL, NULL),
(22, 'Must hold at least 2 years and successfully completing an approved training course', 6, 6, NULL, NULL, ''),
(26, 'Must hold at least 1 year and successfully completing an approved training course', 8, 8, NULL, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `truckstype`
--

DROP TABLE IF EXISTS `truckstype`;
CREATE TABLE IF NOT EXISTS `truckstype` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TypeName` varchar(40) NOT NULL,
  `MinWight` float NOT NULL DEFAULT '0',
  `MaxWight` float NOT NULL DEFAULT '0',
  `axles` text,
  `MaxLength` float NOT NULL DEFAULT '0',
  `MinLength` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `truckstype`
--

INSERT INTO `truckstype` (`ID`, `TypeName`, `MinWight`, `MaxWight`, `axles`, `MaxLength`, `MinLength`) VALUES
(2, 'Light Rigid', 4.5, 8, '1', 0, 0),
(1, 'General (car)', 1, 4.5, '1', 0, 0),
(3, 'Medium Rigid', 8, 100, '2', 0, 0),
(4, 'Heavy Rigid', 9, 100, '3 ', 0, 0),
(5, 'Heavy combination', 9, 100, '3', 0, 0),
(6, 'Multi combination', 9, 100, '3', 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
