#!/bin/bash

function trigger_sigint_sigterm() {
  echo "cleanup...";
  exit 0
}

trap trigger_sigint_sigterm SIGINT
trap trigger_sigint_sigterm SIGTERM

count=1
while :; do
    echo "tick=$count"
    ((count++))
    sleep 1
done
