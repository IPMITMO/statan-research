from timer import Timer
import os

time_sum = 0
count = 10

for i in range(0,count):
    with Timer() as t:
        os.system("pylama -i C0111 -l \"pylint,pyflakes\" ../../sources/requests-2.12.1 > /dev/null")
    print("=> elasped pylama: %s s" % t.secs)
    time_sum = time_sum + t.secs
print("Average: " + (time_sum / count) + " s")