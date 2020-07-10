/* This is the table where the Player's screen name,
 * their unique ID, your friendly name wil be stored.
 * Logger.py inserts a new username into this table once when it
 * sees that user for the first time. You may updat this table at a
 * later time to add your friendly name to the player_full_name column.
 */
CREATE TABLE `PlayerAlias` (
 `player_name` varchar(100) COLLATE latin1_general_ci NOT NULL,
 `player_full_name` varchar(150) COLLATE latin1_general_ci NOT NULL,
 `player_uuid` varchar(100) COLLATE latin1_general_ci NOT NULL,
 PRIMARY KEY (`player_name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


/*
 * The PlayerStats table is where the logger.py script will insert a
 * timestamp every time it sees a player logged in.
 */
CREATE TABLE `PlayerStats` (
 `timestamp` datetime NOT NULL,
 `player_name` varchar(100) COLLATE latin1_general_ci NOT NULL,
 KEY `time` (`timestamp`),
 KEY `player_handle` (`player_name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci COMMENT='Time tally for Players Online';


/*
 * The TodayStats SQL View is server optimized join query that tally's
 * the total minutes per day the user has been seend online. This is
 * used by the dashboard web application mcstatus.cgi
 */
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `TodayStats`
AS
select `pa`.`player_full_name` AS `player_full_name`,`ps`.`player_name` AS `player_name`,`pa`.`player_uuid` AS `player_uuid`,count(0) AS `minutes_today`
from (`PlayerStats` `ps` join `PlayerAlias` `pa`
    on((`ps`.`player_name` = `pa`.`player_name`)))
where (`ps`.`timestamp` >= cast(now() as date))
group by `pa`.`player_full_name`,`ps`.`player_name`,`pa`.`player_uuid`
order by `pa`.`player_full_name`,`pa`.`player_name`;


/*
 * this is a sample create user script based on "mcDashboard" as the Username
 * for this application. You will want to edit this for your preferred Username
 *
 */
 GRANT ALL PRIVILEGES ON *.* TO 'mcDashboard'@'%' IDENTIFIED BY PASSWORD 'CHANGEME-PASSWORD' WITH GRANT OPTION;
 GRANT ALL PRIVILEGES ON `mcDashboard`.* TO 'mcDashboard'@'%';
 GRANT ALL PRIVILEGES ON `mcDashboard\_%`.* TO 'mcDashboard'@'%';
