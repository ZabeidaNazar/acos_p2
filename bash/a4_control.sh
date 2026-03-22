#!/bin/bash

sleep 100 &
pid=$!
echo "Процес розпочато"
ps -o pid,ppid,stat,ni,comm $pid
sleep 2

kill -SIGSTOP $pid
echo "Процес зупинено"
ps -o pid,ppid,stat,ni,comm $pid
sleep 2

kill -SIGCONT $pid
echo "Процес продовжено"
ps -o pid,ppid,stat,ni,comm $pid
sleep 2


kill -SIGTERM $pid
echo "Процес завершено"
ps -o pid,ppid,stat,ni,comm $pid

wait $pid

# echo "Процес з pid=$! завершився з кодом виходу $exit_code"

