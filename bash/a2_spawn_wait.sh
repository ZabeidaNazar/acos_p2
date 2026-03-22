#!/bin/bash

func() {
   sleep 2
   return 7
}

# sleep 2 &
# exit 7 &
echo "Основний процес $BASHPID"
func &
wait $! 
exit_code=$?

echo "Процес з pid=$! завершився з кодом виходу $exit_code"

