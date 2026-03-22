#!/bin/bash

echo "PPID: $PPID"
ps ax -o pid,ppid,stat,ni,comm
