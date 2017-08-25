-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--psql => \i tournament.sql

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE IF NOT EXISTS players (

id serial PRIMARY KEY,
name varchar(50)
);

-- CREATE TABLE IF NOT EXISTS tournament (

-- id serial PRIMARY KEY,
-- name varchar(200)
-- );

CREATE TABLE IF NOT EXISTS matches (

id serial PRIMARY KEY,
winner serial references players(id),
loser serial references players(id)
);

CREATE VIEW wins AS
SELECT players.id, COUNT(matches.winner) as wins
FROM players left join matches
ON players.id = matches.winner
GROUP BY players.id;

CREATE VIEW losses AS
SELECT players.id, COUNT(matches.loser) as losses
FROM players left join matches
ON players.id = matches.loser
GROUP BY players.id;

CREATE VIEW total_matches AS
SELECT players.id AS player_id, COUNT(matches.id) as num_of_matches
FROM players left join matches
ON players.id = matches.winner OR players.id = matches.loser
GROUP BY players.id;

CREATE VIEW player_standings AS
SELECT players.id, players.name, wins.wins, total_matches.num_of_matches
FROM players 
LEFT JOIN wins ON players.id = wins.id 
LEFT JOIN total_matches ON players.id = total_matches.player_id
ORDER BY wins.wins DESC;


-- INSERT INTO matches (winner, loser) VALUES (2, 3);
-- INSERT INTO matches (winner, loser) VALUES (1, 4);
-- INSERT INTO matches (winner, loser) VALUES (2, 1);
-- INSERT INTO matches (winner, loser) VALUES (4, 3);


-- drop view player_standings;
-- drop view total_matches;
-- drop view wins;
-- drop view losses;
-- drop table matches;
-- drop table players;
-- drop database tournament;

