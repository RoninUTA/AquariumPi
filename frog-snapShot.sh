#!/bin/bash

dateStamp=$(date +"%d-%b-%Y@%R")

#get sensor overlay information
overlay=$(python tempy.py)
echo $overlay

#take snapshot of the frogs for use on twitter
#overlay temperature information from sensor
fswebcam -r 640x480  --title "Froggy Cam" --subtitle "${overlay}" --info "yourwebsite.com" frogPics/$dateStamp.jpg


#removes previous twitter upload
rm -rf frogPics/webcam.jpg
cp frogPics/$dateStamp.jpg frogPics/webcam.jpg

exit 0


