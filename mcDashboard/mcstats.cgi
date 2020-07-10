#!/usr/bin/python3
import mysql.connector
from mcstatus import MinecraftServer

def errorResponse(sError):
    print('Content-Type: application/json\n')
    print('{{"error":"{}"}}'.format(sError))


try:
    db = mysql.connector.connect(
          host='<CHANGEME-ip-address>',
          user='<CHANGEME-MySQL-Username>',
          passwd='<CHANGEME-MySQL-Password>',
          db='<CHANGEME-MySQL-Database>')
except mysql.connector.errors.InterfaceError:
    errorResponse('MySQL Server is unreachable')
    exit()

try:
    mcServer = MinecraftServer.lookup('<CHANGEME-Minecraft-Server-Hostname>')
    mcQuery = mcServer.query()
except:
    errorResponse('Unable to reach the Minecraft server. It may be down for maintenance')
    exit()

try:
    cursor = db.cursor()
    cursor.execute("SELECT player_name, player_full_name, minutes_today, player_uuid FROM TodayStats")
    rows = cursor.fetchall()
except mysql.connector.errors.ProgrammingError as e:
    errorResponse('There was an error while retrieving stats from the MySQL server: {}'.format(e))
    exit()

#We got this far without an exception. Below is the normal JSON response

print('Content-Type: application:json\n')
print('{"stats":[', end = '')
i=0

for row in rows:
    loggedIn = "false"
    for user in mcQuery.players.names:
        if user == row[0]:
            loggedIn = "true"
    timeFormatted = '{:02d}:{:02d}'.format(*divmod(row[2],60))
    print(('{{"player_name":"{}", "player_full_name":"{}", "time_today":"{}", "currently_logged_in":"{}", "player_uuid":"{}"}}').format(row[0],row[1],timeFormatted,loggedIn, row[3]), end = '')
    i += 1
    if i < len(rows):
        print(',', end = '')

print(']}');

db.close()
