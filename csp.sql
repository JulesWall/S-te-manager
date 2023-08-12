-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  sam. 12 août 2023 à 21:56
-- Version du serveur :  10.4.10-MariaDB
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `csp2`
--

-- --------------------------------------------------------

--
-- Structure de la table `bip`
--

DROP TABLE IF EXISTS `bip`;
CREATE TABLE IF NOT EXISTS `bip` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `id_owner` bigint(20) NOT NULL,
  `expiration` bigint(20) NOT NULL,
  `has_low_battery` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `house`
--

DROP TABLE IF EXISTS `house`;
CREATE TABLE IF NOT EXISTS `house` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_id` bigint(20) NOT NULL,
  `last_message` bigint(20) NOT NULL,
  `chan_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `profil`
--

DROP TABLE IF EXISTS `profil`;
CREATE TABLE IF NOT EXISTS `profil` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `idd` bigint(20) NOT NULL,
  `name` longtext COLLATE utf8mb4_bin NOT NULL,
  `grade` int(11) NOT NULL,
  `hierarchie` int(11) NOT NULL,
  `poste` text COLLATE utf8mb4_bin NOT NULL,
  `money` int(11) NOT NULL,
  `CP` int(11) NOT NULL,
  `location` bigint(20) NOT NULL,
  `service_time` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `service`
--

DROP TABLE IF EXISTS `service`;
CREATE TABLE IF NOT EXISTS `service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idd` bigint(20) NOT NULL,
  `name` text COLLATE utf8mb4_bin NOT NULL,
  `time` bigint(20) NOT NULL,
  `cta` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `tph`
--

DROP TABLE IF EXISTS `tph`;
CREATE TABLE IF NOT EXISTS `tph` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `id_owner` bigint(20) NOT NULL,
  `expiration` bigint(20) NOT NULL,
  `Frequency` text COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=180 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `tph_frequency`
--

DROP TABLE IF EXISTS `tph_frequency`;
CREATE TABLE IF NOT EXISTS `tph_frequency` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `Frequency` text COLLATE utf8mb4_bin NOT NULL,
  `channels` longtext COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `tph_frequency`
--

INSERT INTO `tph_frequency` (`id`, `Frequency`, `channels`) VALUES
(1, 'off', '[]'),
(2, 'cta', '[705097188811735151]'),
(3, 'formation', '[842533103791898644]'),
(4, 'c15', '[706125118711267368]'),
(5, 'TAC-1', '[842533103791898644]'),
(6, 'TAC-2', '[842533103791898644]');

-- --------------------------------------------------------

--
-- Structure de la table `vhl`
--

DROP TABLE IF EXISTS `vhl`;
CREATE TABLE IF NOT EXISTS `vhl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `statut` int(11) NOT NULL,
  `véhicule` longtext COLLATE utf8mb4_bin NOT NULL,
  `cord` text COLLATE utf8mb4_bin NOT NULL,
  `syno` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `vhl`
--

INSERT INTO `vhl` (`id`, `statut`, `véhicule`, `cord`, `syno`) VALUES
(30, 0, 'VLCG-151', '(20,864)', 1),
(29, 0, 'VTP-29', '(20,717)', 1),
(28, 0, 'VTP-28', '(824,620)', 1),
(27, 0, 'VPMA-034-3', '(556,620)', 1),
(26, 0, 'VEMAH-341', '(288,620)', 1),
(7, 0, 'VLM-411', '(824,373)', 1),
(25, 0, 'VTUTP-355', '(20,620)', 1),
(24, 0, 'CCGC-311', '(288,225)', 1),
(10, 0, 'VSAV-432', '(288,373)', 1),
(11, 0, 'VSAV-431', '(20,373)', 1),
(23, 0, 'FPTL-GFOR', '(556,225)', 1),
(22, 0, 'EPA-325', '(20,225)', 1),
(21, 0, 'CCF-241', '(824,128)', 1),
(18, 0, 'FPTL-111', '(20,128)', 1),
(19, 0, 'FPTSR-121', '(288,128)', 1),
(20, 0, 'CCF-231', '(556,128)', 1),
(15, 0, 'VSAV-433', '(556,373)', 1),
(16, 0, 'VSAV-142R', '(288,470)', 1),
(17, 0, 'AR-1', '(20,470)', 1),
(31, 0, 'VLHR-104', '(288,864)', 1),
(32, 0, 'VPC-034-2', '(556,864)', 1),
(33, 0, 'VLCG-100', '(824,864)', 1),
(34, 0, 'VL-59', '(20,961)', 1),
(35, 0, 'VL-36', '(288,961)', 1),
(36, 0, 'VL-78', '(556,961)', 1),
(37, 0, 'VLTT-89', '(824,961)', 1),
(38, 0, 'VLTT-56', '(20,1055)', 1);

-- --------------------------------------------------------

--
-- Structure de la table `wh`
--

DROP TABLE IF EXISTS `wh`;
CREATE TABLE IF NOT EXISTS `wh` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `alias` tinytext COLLATE utf8mb4_bin NOT NULL,
  `name` text COLLATE utf8mb4_bin NOT NULL,
  `link` text COLLATE utf8mb4_bin NOT NULL,
  `lastuse` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
