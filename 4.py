#!/usr/bin/env python3

from dateutil.parser import parse as parse_date
from collections import defaultdict
import itertools

log = []
with open("4.txt") as f:
    # lines look like
    # [1518-11-01 00:00] Guard #10 begins shift
    # [1518-11-01 00:05] falls asleep
    # [1518-11-01 00:25] wakes up

    for line in f:
        date, message = line.split("] ")

        date = parse_date(date.lstrip("["))
        message = message.rstrip()

        log.append((date, message))

log.sort()  # since messages are randomly ordered, we need to sort them by date first


def parse_guard_id(message):
    # Guard #10 begins shift
    # 10 begins shift
    # 10
    return int(message.split("#")[1].split()[0])


current_guard = parse_guard_id(log.pop(0)[1])
minute_guard_fell_asleep = -1  # -1 means guard is awake
sleep_times = []
guards = defaultdict(list)
for time, message in log:

    if message == "falls asleep":
        minute_guard_fell_asleep = time.minute
    elif message == "wakes up":
        # you could add a check here for minute_guard_fell_asleep == -1 but
        # if the guard fell asleep it means the next message must be about
        # him waking up, otherwise the problem would ask me to handle
        # the case where the guard sleeps past midnight, which would be trivial
        # but more code
        sleep_times.append((minute_guard_fell_asleep, time.minute))

        # this line isn't necessary if the input is well formed
        # minute_guard_fell_asleep = -1
    else:
        # if we got this far, it means the guard has changed
        guards[current_guard].append(sleep_times)
        current_guard = parse_guard_id(message)
        sleep_times = []


how_many_times_was_a_guard_asleep_on_a_given_minute = dict()
for guard, sleep_times in guards.items():
    minutes = [0] * 60
    for day in sleep_times:
        for sleep_range in day:
            for minute in range(*sleep_range):
                minutes[minute] += 1

    how_many_times_was_a_guard_asleep_on_a_given_minute[guard] = minutes


x = how_many_times_was_a_guard_asleep_on_a_given_minute  # shorten the line

# Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
# The answer is the minute the guard spent asleep the most, multiplied by his ID.
print(max((sum(minutes), guard_id * minutes.index(max(minutes))) for guard_id, minutes in x.items())[1])

# Of all guards, which guard is most frequently asleep on the same minute?
# The answer is the minute the guard spent asleep the most, multiplied by his ID.
print(max((max(minutes), guard_id * minutes.index(max(minutes))) for guard_id, minutes in x.items())[1])
