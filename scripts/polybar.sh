#!/bin/bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# polybar -rq dummy & 
#polybar -rq wm &


polybar -r main &
polybar -r main2 &

echo "Polybar launched..."
