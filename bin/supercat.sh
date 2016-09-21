#!/bin/bash

hash pygmentize 2>/dev/null || { echo >&2 "I require pygmentize but it's not installed.  Aborting."; exit 1; }

if [ ! -t 0 ];then
        file=/dev/stdin
elif [ -f $1 ];then
        file=$1
else
        echo "Usage: $0 code.c"
        echo "or e.g. head code.c|$0"
        exit 1
fi
pygmentize -f terminal -g $file
