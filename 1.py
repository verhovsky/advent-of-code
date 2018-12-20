print(sum(map(int, open("input").readlines())))


from itertools import cycle

with open("input") as f:
    frequency_changes = [int(line) for line in f]

frequency = 0
seen_frequencies = {frequency}
for frequency_change in cycle(frequency_changes):
    frequency += int(frequency_change)

    if frequency in seen_frequencies:
        print(frequency)
        break

    seen_frequencies.add(frequency)
