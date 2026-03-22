#!/bin/bash

function trigger_sigint_sigterm() {
  echo "cleanup...";
  exit 0
}

trap trigger_sigint_sigterm SIGINT
trap trigger_sigint_sigterm SIGTERM


while :; do
    echo "Натисніть [CTRL+C] щоб зупинити..."
    sleep 1
done
