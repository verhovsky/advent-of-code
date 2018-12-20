from collections import Counter

with open("input") as f:
    letter_counts = [set(count for letter, count in Counter(line).most_common()) for line in f]

    print(sum(2 in counts for counts in letter_counts) * sum(3 in counts for counts in letter_counts))
# this is an inefficient, quadratic solution

with open("input") as f:
    box_ids = [line.strip() for line in f]

for i, box_id in enumerate(box_ids[:-1]):
    for other_box_id in box_ids[i + 1 :]:
        matching_characters = "".join(x for x, y in zip(box_id, other_box_id) if x == y)
        if len(box_id) - len(matching_characters) == 1:
            print(matching_characters)
