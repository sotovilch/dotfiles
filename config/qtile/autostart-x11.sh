#!/bin/bash

hdmi=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

if [[ $hdmi != '' ]; then
  xrandr --output DP-3 --mode 2560x1440 --pos 0x0 --rotate normal --output $hdmi --mode 1280x720 --pos 2560x0 --rotate normal &
fi
