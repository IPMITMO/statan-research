#!/bin/bash

for i in "$@"
do
case $i in
    -s=*|--searchpath=*)
    SEARCHPATH="${i#*=}"
    shift # past argument=value
    ;;
    *)
            # unknown option
    ;;
esac
done

find "${SEARCHPATH}"/ -type f -name "*.py" -exec pyflakes '{}' \;