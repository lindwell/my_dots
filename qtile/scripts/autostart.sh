#!/bin/sh


xinput set-prop 'ATML3000:00 03EB:2168 Touchpad' "libinput Tapping Enabled" 1
~/.fehbg &
nm-applet &
blueman-applet &
dunst &
mpd --no-daemon $HOME/.config/mpd/mpd.conf &
