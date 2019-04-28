#!/bin/sh

PID=$(pgrep -o "cinnamon-sess|gnome-sess|mate-sess")
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

cd CHANGEME
venv/bin/python main.py