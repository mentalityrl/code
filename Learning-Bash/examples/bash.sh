#! /bin/bash
STRING="What is your name?"
echo $STRING
read name

if [ $name = "Bryan" ]; then
   echo "Wow, we have the same name!"
else
   echo "Your name sucks"
fi
