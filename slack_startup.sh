#!/bin/bash

re='^[0-9]+$'
DIRECTORY=`dirname $0`

# Exit if /tmp/lock.file exists
if [ -f /tmp/web-console.lock.file ]
then
    pid=$(cat /tmp/web-console.lock.file)
    slack_pid=$(pgrep -P $pid)
    # If child PID doesn't exists
    if ! [[ $slack_pid =~ $re ]]
    then
        # Start slack service as it's not running
        # Create lock file, sleep 1 sec and verify lock
        echo $$ > /tmp/web-console.lock.file
        sleep 1
        [ "x$(cat /tmp/web-console.lock.file)" == "x"$$ ] || exit

        # Increase sleep time to allow network connection
        sleep 100

        python $DIRECTORY/app.py
        sleep 10
        # Remove lock file
        rm /tmp/web-console.lock.file
    fi
else
    # Start slack service as it's not running
    # Create lock file, sleep 1 sec and verify lock
    echo $$ > /tmp/web-console.lock.file
    sleep 1
    [ "x$(cat /tmp/web-console.lock.file)" == "x"$$ ] || exit
    sleep 10
    python $DIRECTORY/app.py
    sleep 10
    # Remove lock file
    rm /tmp/web-console.lock.file
fi