#!/bin/sh
node /usr/src/server/src/server/Server.js & python3 /opt/notsendgrid/app/request_sender.py && fg