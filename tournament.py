#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB_connection = connect()
    cursor = DB_connection.cursor()
    cursor.execute("DELETE FROM matches")
    DB_connection.commit()
    DB_connection.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB_connection = connect()
    cursor = DB_connection.cursor()
    cursor.execute("DELETE FROM players")
    DB_connection.commit()
    DB_connection.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB_connection = connect()
    cursor = DB_connection.cursor()
    cursor.execute("SELECT count(*) AS count FROM players")
    result = cursor.fetchone()
    number_of_players = result[0]
    DB_connection.close()

    return number_of_players


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB_connection = connect()
    cursor = DB_connection.cursor()
    cursor.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    DB_connection.commit()
    DB_connection.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    DB_connection = connect()
    cursor = DB_connection.cursor()
    cursor.execute("SELECT * FROM player_standings")
    result = cursor.fetchall()
    DB_connection.close()

    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    DB_connection = connect()
    cursor = DB_connection.cursor()
    cursor.execute(
        "INSERT INTO matches (winner, loser) VALUES (%s, %s)", (winner, loser,))
    DB_connection.commit()
    DB_connection.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    DB_connection = connect()
    cursor = DB_connection.cursor()
    cursor.execute("SELECT * FROM player_standings")
    standings = cursor.fetchall()
    DB_connection.close()

    swisspairings = []

    counter = 0
    # Loop to go through two records at a time and append to the swisspairing
    # variable
    while counter < len(standings):
        pair_list = [standings[counter][0], standings[counter][1],
                     standings[counter + 1][0], standings[counter + 1][1]]
        swisspairings.append(pair_list)
        counter += 2

    return swisspairings
