#!/usr/bin/python3
import mysql.connector
from mcstatus import JavaServer
import requests

def Getuuid(username):
    # Quick & Dirty REST Call to get the UUID for the requested user
    try:
        r = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'.format(username)).json()
        return r['id']
    except Exception as e:
        print(e)
        pass
    return

def AddPlayerAlias(username, _db):
    # If a record does not already exist, get the player's UUID from Mojang's API. If Mojang returns a UUID, then insert a PlayerAlias into the db
    _cursor = _db.cursor()
    _cursor.execute("SELECT player_name FROM PlayerAlias WHERE player_name = '{}'".format(username))
    _rows = _cursor.fetchall()
    if (len(_rows) == 0):
        uuid = Getuuid(username)
        if (uuid):
            _cursor.execute("INSERT INTO PlayerAlias (player_name, player_full_name, player_uuid) VALUES ('{}','{}','{}')".format(username, username, uuid))

###############################
#
#Main function
#
###############################

try:
    db = mysql.connector.connect(
        host='<CHANGEME-ip-address>',
        user='<CHANGEME-MySQL-Username>',
        passwd='<CHANGEME-MySQL-Password>',
        db='<CHANGEME-MySQL-Database>')
except mysql.connector.errors.InterfaceError:
    print ('MySQL Server is unreachable')
    exit()

try:
    mcServer = JavaServer.lookup('<CHANGEME-Minecraft-Server-Host>')
    mcQuery = mcServer.status()
except:
    print('Unable to connect to the Minecraft server or Query port. Make sure you have the correct address:port and that "query-enable=true" is set in your server.properties file')
    exit()

try:
    if (mcQuery.players.sample):
        for player in mcQuery.players.sample:
            cursor = db.cursor()
            cursor.execute(("INSERT INTO PlayerStats (timestamp, player_name) VALUES (CURRENT_TIMESTAMP, '{}')").format(player.name))
            AddPlayerAlias(player.name, db)
except mysql.connector.errors.ProgrammingError as e:
    print('MySQL returned the following error message on your last query: {}'.format(e))
finally:
    db.close()
