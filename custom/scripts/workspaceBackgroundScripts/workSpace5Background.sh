#!/bin/bash
desktops=$(wmctrl -d | awk '{print $2}')
thisDesktopLong=$(echo ${desktops:8:8})
thisDesktop=$(echo ${thisDesktopLong:0:1})
if [ $thisDesktop != "-" ];then
  echo "5"
fi
