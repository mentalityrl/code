#!/bin/bash

ordinal1='st'
ordinal2='nd'
ordinal3='rd'
ordinal4='th'

stMonth="January"
ndMonth="February"
rdMonth="March"
thMonth=("April" "May" "June" "July" "August" "September" "October" "November" "December")

read month

if [[ $month = $stMonth  ]]; then
	echo "$month is the $(grep $month ~/code/Learning-Bash/Assets/months | awk '{print $1}')$ordinal1 month of the year"
elif [[ $month = $ndMonth ]]; then
	echo "$month is the $(grep $month ~/code/Learning-Bash/Assets/months | awk '{print $1}')$ordinal2 month of the year"
elif [[ $month = $rdMonth ]]; then
	echo "$month is the $(grep $month ~/code/Learning-Bash/Assets/months | awk '{print $1}')$ordinal3 month of the year"
elif [[ $month = $thMonth  ]]; then
	echo "$month is the $(grep $month ~/code/Learning-Bash/Assets/months | awk '{print $1}')$ordinal4 month of the year"
else 
	echo "Incorrect"
fi

