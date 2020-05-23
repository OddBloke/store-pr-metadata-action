#!/bin/sh -leu
echo "Hello World:" "$@"
find / -xdev
/app/bin/gcli list
