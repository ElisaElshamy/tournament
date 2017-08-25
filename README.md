# About

Tourament is a Python project that uses the PostgreSQL database
to track a Swiss style tournament.  Rules in a Swiss style 
tournament allow participants to keep playing until the end.  After
every round a player is matched with somone who ranked the same as they
did.  The loosers and winners are paired accordingly.

# Install

After ssh'ing into the Vagrant virtual machine, The first thing to do is 
```cd /vagrant/tournament``` and run the command ```psql```

That should take you into the psql prompt where you can now import the .sql file:
```\i tournament.sql```

Verify that the database and tables were created using the ```\dt``` command at the 
psql prompt, you should get something like this:
```
         List of relations
 Schema |  Name   | Type  |  Owner  
--------+---------+-------+---------
 public | matches | table | vagrant
 public | players | table | vagrant
 ```

Use the command ```\q``` to quit the psql prompt.

# How to use

You should be in the tournament directory.  
Run the command ```python tournament_test.py```.  This file uses the logic 
in tournament.py to run unit tests that simulate a new tournament every time.  If all
tests pass, you will see the following message:

```
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```

# Development

Tournament is a Python project that uses PostgreSQL to organize the data.  Data uses
views to organize the match records in a very concise way. 

## Libraries

- **Python 2.7.12** - https://www.python.org/
- **PostgreSQL** - https://www.postgresql.org/