#!/bin/bash

rm /tmp/fifo
mkfifo /tmp/fifo
netcat -l -k -v -p 4002 < /tmp/fifo | netcat -v -u localhost 5001 > /tmp/fifo
