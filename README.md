![Who's Minecrafting?](assets/Whos-Minecraftinglg.png)

# mcDashboard - A Simple Minecraft Time Tracking Dashboard for Family & Friends Servers

## Overview

![Dashboard Screen Shot](assets/Minecraft_Dashboard1.png)

Minecraft has made a huge resurgence this year among my my friends and family. The renewed interest is due in no small part to our shelter-in-place practices during the COVID-19 Pandemic as we search for new ways to gather and to communicate with one another. I recently worked with my kids to set up a multiplayer server at home. Within a day we were all hooked. Within two days, none of us knew what day it was. We started spending so much time in Minecraft that I wanted to start tracking it.

My goal with this project is not to impose time limits (at least not yet). Instead, I wanted to use this dashboard as a reference, a tool, a teachable moment for my kids. Each morning the time clocks reset themselves. During the day, each player accumulates more time on the board. At the end of their play, they can compare how much time they perceived to have passed with how much time has actually passed. The goal of this dashboard is to help teach my kids how to regulate their online time by giving them a clock that doesn't lie.

Please keep in mind that this project is a proof of concept and a learning opportunity for me. It's not meant to be a turn-key solution. If you follow this guide, you should be able to implement it on your own Minecraft server. You are welcome to use any or all of this code to create your own awesome dashboard.

## Getting started

![Technical Diagram](assets/mcDashboardTechnicalDiagram.png)

There are several moving parts to this dashboard application. There's the logger script that polls the Minecraft server every minute. The Logger persists the logged in user information to a MySQL server. A Webserver then pulls the latest tally out of MySQL and displays it on a webpage. If you are using it as an information screen like me, you will also have a computer running this webpage in kiosk-mode. The good news is that you can probably fit all of these components onto one [Raspberry Pi](https://www.raspberrypi.org) System on a Chip (SoC) computer. That's what we're using at our house, but with one exception. We're using a NAS Appliance with a built-in MySQL server to host the database. Unfortunately the Achilles heal of the Raspberry Pi is that it uses an SD card for storage and there's a possibility for the card to become corrupted if the Pi loses power. If you are hosting the MySQL Server on your Pi, please attach a USB disk drive to use for the database, or at the very least make regular backups of your data.


## What You Will Need

1. A Raspberry Pi Computer or a spare PC that can run your favorite flavor of Linux. Yes, you can probably make all of this work on a Windows machine, but for this how-to, we're going to stick to Linux. Your Linux host will need:
    1. A web server installed and configured to serve the web application files in the mcDashboard directory. Apache or Nginx will do just fine. See the WebServer section below for important configuration tasks.
    1. Python3 should be installed
    1. Shell Access and the ability to configurate cront jobs. In Raspberry Pi, this is easy as you can open a terminal window when a keyboard and monitor are attached, or you can SSH into the Pi and configure everything through terminal.
    1. MySQL latest stable build.
1. Access to a Minecraft Server with the query service enabled and accessible to your Raspberry Pi device (make sure the [ports through any firewalls are opened correctly](https://portforward.com/minecraft/))


## Configuration

### Logger.py script

TO-DO

### MySQL Server

TO-DO

### Web Server

TO-DO
