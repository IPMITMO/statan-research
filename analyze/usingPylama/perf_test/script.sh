#!/bin/bash
pylama -l "pylint,pep8,pydocstyle,pyflakes" ../../../sources/perf_test/ > messages_3072.txt
