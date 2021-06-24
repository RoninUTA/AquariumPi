#!/bin/bash
echo "Checking to see if process is already running"
if ps -ef | grep -v grep | grep  mjpg_streamer > /dev/null; then
        exit 0
else
        echo "Starting Twitter Morning Update"
        sleep 3
        echo "Starting Camera on Device /dev/video0"
        sleep 3
        mjpg_streamer -i "/usr/local/lib/input_uvc.so -y YUYV" -o "/usr/local/lib/output_http.so" &
        sleep 3
        exit 0
fi
