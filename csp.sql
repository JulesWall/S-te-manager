-- phpMyAdmin SQL Dump
-- version 5.2.1deb1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : lun. 07 août 2023 à 10:40
-- Version du serveur : 8.0.33-0ubuntu0.23.04.2
-- Version de PHP : 8.1.12-1ubuntu4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `csp`
--

-- --------------------------------------------------------

--
-- Structure de la table `bip`
--

CREATE TABLE `bip` (
  `id` mediumint NOT NULL,
  `id_owner` bigint NOT NULL,
  `expiration` bigint NOT NULL,
  `has_low_battery` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `House`
--

CREATE TABLE `House` (
  `id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  `last_message` bigint NOT NULL,
  `chan_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `profil`
--

CREATE TABLE `profil` (
  `id` mediumint NOT NULL,
  `idd` bigint NOT NULL,
  `name` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `grade` int NOT NULL,
  `hierarchie` int NOT NULL,
  `poste` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `money` int NOT NULL,
  `CP` int NOT NULL,
  `location` bigint NOT NULL,
  `service_time` bigint NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `service`
--

CREATE TABLE `service` (
  `id` int NOT NULL,
  `idd` bigint NOT NULL,
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `time` bigint NOT NULL,
  `cta` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `tph`
--

CREATE TABLE `tph` (
  `id` mediumint NOT NULL,
  `id_owner` bigint NOT NULL,
  `expiration` bigint NOT NULL,
  `Frequency` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Structure de la table `tph_frequency`
--

CREATE TABLE `tph_frequency` (
  `id` mediumint NOT NULL,
  `Frequency` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `channels` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

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

CREATE TABLE `vhl` (
  `id` int NOT NULL,
  `statut` int NOT NULL,
  `véhicule` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `cord` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `syno` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Déchargement des données de la table `vhl`
--

INSERT INTO `vhl` (`id`, `statut`, `véhicule`, `cord`, `syno`) VALUES
(1, 0, 'CCFM-601', '(32,275)', 1),
(2, 0, 'CCFM-602', '(508, 275)', 1),
(3, 0, 'CCGC-301', '(269,275)', 1),
(4, 0, 'EPA-001', '(33,186)', 1),
(5, 0, 'FPTL-121', '(269,186)', 1),
(6, 0, 'FPTSR-181', '(507,186)', 1),
(7, 0, 'VLM-131', '(258,61)', 2),
(8, 0, 'VLHR-104', '(259,169)', 2),
(9, 0, 'PCC-34-1', '(498,169)', 2),
(10, 0, 'VSAV-221', '(268,95)', 1),
(11, 0, 'VSAV-222', '(508,96)', 1),
(12, 0, 'VTU-TP-161', '(32,95)\r\n', 1),
(13, 0, 'VL-503', '(35,169)', 2),
(14, 0, 'VPMA-34-3', '(258,242)', 2);

-- --------------------------------------------------------

--
-- Structure de la table `wh`
--

CREATE TABLE `wh` (
  `id` mediumint NOT NULL,
  `alias` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `link` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `lastuse` bigint NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `bip`
--
ALTER TABLE `bip`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `House`
--
ALTER TABLE `House`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `profil`
--
ALTER TABLE `profil`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `service`
--
ALTER TABLE `service`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tph`
--
ALTER TABLE `tph`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tph_frequency`
--
ALTER TABLE `tph_frequency`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `vhl`
--
ALTER TABLE `vhl`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `wh`
--
ALTER TABLE `wh`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `bip`
--
ALTER TABLE `bip`
  MODIFY `id` mediumint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `House`
--
ALTER TABLE `House`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `profil`
--
ALTER TABLE `profil`
  MODIFY `id` mediumint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `service`
--
ALTER TABLE `service`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `tph`
--
ALTER TABLE `tph`
  MODIFY `id` mediumint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=180;

--
-- AUTO_INCREMENT pour la table `tph_frequency`
--
ALTER TABLE `tph_frequency`
  MODIFY `id` mediumint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `vhl`
--
ALTER TABLE `vhl`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT pour la table `wh`
--
ALTER TABLE `wh`
  MODIFY `id` mediumint NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
