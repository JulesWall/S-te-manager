-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  jeu. 29 juin 2023 à 17:34
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
-- Base de données :  `csp`
--

-- --------------------------------------------------------

--
-- Structure de la table `bip`
--

DROP TABLE IF EXISTS `bip`;
CREATE TABLE IF NOT EXISTS `bip` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `id_owner` bigint(11) NOT NULL,
  `expiration` bigint(11) NOT NULL,
  `has_low_battery` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `profil`
--

DROP TABLE IF EXISTS `profil`;
CREATE TABLE IF NOT EXISTS `profil` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `idd` bigint(11) NOT NULL,
  `name` longtext COLLATE utf8mb4_bin NOT NULL,
  `grade` int(11) NOT NULL,
  `hierarchie` int(11) NOT NULL,
  `poste` text COLLATE utf8mb4_bin NOT NULL,
  `money` int(11) NOT NULL,
  `CP` int(11) NOT NULL,
  `location` bigint(20) NOT NULL,
  `service_time` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

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
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `tph`
--

DROP TABLE IF EXISTS `tph`;
CREATE TABLE IF NOT EXISTS `tph` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `id_owner` bigint(11) NOT NULL,
  `expiration` bigint(11) NOT NULL,
  `Frequency` text COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

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
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `vhl`
--

INSERT INTO `vhl` (`id`, `statut`, `véhicule`, `cord`, `syno`) VALUES
(1, 0, 'CCFM-601', '(32,275)', 1),
(2, 0, 'CCFM-602', '(508, 275)', 1),
(3, 1, 'CCGC-301', '(269,275)', 1),
(4, 1, 'EPA-001', '(33,186)', 1),
(5, 0, 'FPTL-121', '(269,186)', 1),
(6, 0, 'FPTSR-181', '(507,186)', 1),
(7, 1, 'VLM-131', '(258,61)', 2),
(8, 1, 'VLHR-104', '(259,169)', 2),
(9, 0, 'PCC-34-1', '(498,169)', 2),
(10, 6, 'VSAV-221', '(268,95)', 1),
(11, 4, 'VSAV-222', '(508,96)', 1),
(12, 1, 'VTU-TP-161', '(32,95)\r\n', 1),
(13, 6, 'VL-151', '(35,169)', 2),
(14, 1, 'VPMA-34-3', '(258,242)', 2);

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
  `lastuse` bigint(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
