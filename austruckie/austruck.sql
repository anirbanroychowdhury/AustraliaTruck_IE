-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 15, 2021 at 02:27 AM
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
-- Table structure for table `roadsrule`
--

DROP TABLE IF EXISTS `roadsrule`;
CREATE TABLE IF NOT EXISTS `roadsrule` (
  `RoadTypeID` int(11) NOT NULL,
  `RuleID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

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
(1, 'Must hold at least 1 year of Australian car license.', 2, NULL, NULL, '', ''),
(2, 'must travel at speeds no greater than the speed displayed on a speed limit sign as well as complying with the following conditions: \r\n» 40 km/h in a local traffic zone signed 40 km/h \r\n» 50 km/h in a built-up area not otherwise signed \r\n» 100 km/h in a 100 km/h zone \r\n» 100 km/h in a 110 km/h zone.', 2, NULL, NULL, 'pneumatic tyres', ''),
(3, ' drivers of heavy vehicles must wear a properly adjusted and fastened seatbelt where one is fitted, or is required by law to be fitted to the vehicle.( As part of managing fatigue there is an exemption from wearing seatbelts for two-up drivers in sleeping compartments)', 2, NULL, NULL, NULL, ''),
(4, 'You must carry three approved portable warning triangles in your vehicle at all times.', 3, NULL, NULL, NULL, ''),
(5, 'If you have to stop your vehicle or if any part of your load falls onto the road (including the shoulder), three portable warning triangles must be placed on the road', 3, NULL, NULL, '', ''),
(6, 'if the vehicle is not visible for 300 metres in all directions: \r\n» one triangle must be placed 200-250 metres behind the vehicle or fallen load, \r\n» one triangle must be placed 200-250 metres in front of the vehicle or fallen load, and \r\n» one triangle must be placed by the side of the vehicle or fallen load. ', 3, NULL, '80', NULL, ''),
(7, ' if the vehicle is not visible for 200 metres in all directions: \r\n» one triangle must be placed 50-150 metres behind the vehicle or fallen load, \r\n» one triangle must be placed 50-150 metres in front of the vehicle or fallen load, and \r\n» one triangle must be placed by the side of the vehicle or fallen load. \r\n', 3, NULL, '70', NULL, ''),
(8, 'Drivers of fatigue-regulated heavy vehicles must work to standard hours if the operator they work for does not hold BFM or AFM accreditation.', 2, NULL, NULL, NULL, ''),
(9, 'A pre-trip inspection should be done by the driver which includes external check, vehicle tilt, load and load security, vehicle damage, leaks, area check, wheels and rims, check wheel nuts, tyres, engine checks and driver controls check.', 2, NULL, NULL, NULL, ''),
(10, ' Traffic following behind you must be able to see it clearly. The sign allows the driver to occupy space outside an assigned lane when turning so long as: » the vehicle is within 50 metres from the corner » the move can be made safely » wherever possible, you should set up the back of your vehicle so that traffic behind you cannot overtake your vehicle on the side you are turning to.', 4, NULL, NULL, NULL, ''),
(11, 'This sign has been introduced on some three-lane and four -lane freeways in Victoria. It prohibits all heavy vehicles over 4.5 tonnes, except buses and caravans, from travelling in the right lane wherever it is displayed. The restriction applies 24 hours a day.\r\n', 1, NULL, NULL, NULL, NULL),
(12, 'Load limit signs may apply to bridges or sections of road. You must not pass this sign if axle group mass of your vehicle is more than that allowed by the sign. Fines are heavy and you might have to pay for damage caused to roads that cannot take the weight of your vehicle.\r\n', 2, NULL, NULL, NULL, NULL),
(13, 'Load limit signs may apply to bridges or sections of road. You must not pass this sign. Fines are heavy and you might have to pay for damage caused to roads that cannot take the weight of your vehicle.\r\n', 3, NULL, NULL, NULL, NULL),
(14, 'if the driver of a truck drives past a trucks must enter sign, the driver must enter the area indicated by information on or with the sign. \r\n', 2, NULL, NULL, NULL, NULL),
(15, 'No goods-carrying vehicle over 4.5 tonnes GVM can pass this sign without a permit from VicRoads or from the local council, unless the following exemptions apply: \r\n» the driver travels beyond the sign in any other lane, or \r\n» the driver of the truck is loading or unloading at a location beyond the no truck sign and no suitable alternative route to the location exists \r\n» the driver is escorted by a police officer or an authorised officer of the corporation. \r\n', 2, NULL, NULL, NULL, NULL),
(16, 'This sign will tell you the clearance under the bridge and may indicate a detour to avoid the obstruction. Check that your vehicle will fit under the bridge. You must know your maximum vehicle height. \r\n', 2, NULL, NULL, NULL, NULL),
(17, 'A low clearance sign will tell you the clearance under the obstruction. If your vehicle is the height shown on the sign or higher, you must not drive under it. ', 2, NULL, NULL, NULL, NULL),
(18, 'Clearance signs will tell you the clearance under an obstruction. These signs are only used where the clearance is at least 4 metres. If your vehicle is the height on the sign or higher, you must not drive under it.\r\n', 2, NULL, NULL, NULL, NULL),
(19, 'Perform coupling of trailers by inspecting the area, inspect or check coupling devices, check trailer height, back the prime mover, check the connection, secure the vehicle, visually inspect, connect the electrical cable, raise the trailer supports and remove trailer wheel chocks.', 2, NULL, NULL, NULL, NULL),
(20, 'Perform uncoupling of trailers by positioning the vehicle, apply the trailer brakes, secure the vehicle, lower the landing gear, disconnect air lines, release the turntable latch, pull the prime mover partially clear, secure the prime mover again, inspect the semi-trailer support and release the parking brake.', 2, NULL, NULL, NULL, NULL),
(21, 'Must hold at least 1 year', 5, 1, NULL, NULL, NULL),
(22, 'Must hold at least 2 years', 6, 1, NULL, NULL, 'successfully completing an approved training course'),
(23, 'Must hold at least 1 year', 6, 2, NULL, NULL, 'successfully completing an approved training course'),
(24, 'Must hold at least 1 year', 6, 3, NULL, NULL, 'successfully completing an approved training course'),
(25, 'Must hold at least 1 year ', 8, 2, NULL, NULL, 'successfully completing an approved training course'),
(26, 'Must hold at least 1 year ', 8, 3, NULL, NULL, 'successfully completing an approved training course');

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
  `OtherInfo` text,
  `MaxLength` float NOT NULL DEFAULT '0',
  `MinLength` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `truckstype`
--

INSERT INTO `truckstype` (`ID`, `TypeName`, `MinWight`, `MaxWight`, `OtherInfo`, `MaxLength`, `MinLength`) VALUES
(1, 'Light Rigid', 4.5, 12, NULL, 0, 0),
(2, 'General', 1, 1, 'All Heavy Vehicle ', 0, 0),
(3, 'Gross Vehicle Mass (GVM)', 12, 100, NULL, 0, 0),
(4, 'Long', 0, 0, NULL, 100, 7.5),
(5, 'Medium Rigid', 8, 100, '2 axle', 0, 0),
(6, 'Heavy Rigid', 8, 100, '3 axle', 0, 0),
(7, 'Heavy combination', 9, 100, 'unladen converter dolly or trailer', 0, 0),
(8, 'Multi combination', 0, 0, 'HC with more than one trailer', 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;