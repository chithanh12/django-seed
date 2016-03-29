#!/bin/sh

set -e
echo -n "waiting for TCP connection to db:5432..."

while ! nc -w 1 db 5432 2>/dev/null
do
  echo -n .
  sleep 1
done
#start the script
exec $WAIT_START_CMD