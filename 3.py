def parse_claim(line):
    # lines looks like this
    # #1 @ 1,3: 4x4
    # #2 @ 3,1: 4x4
    # #3 @ 5,5: 2x2
    claim_id, _, corner, area = line.strip().split(" ")

    claim_id = int(claim_id.replace("#", ""))

    starting_corner = tuple(int(x.strip(":")) for x in corner.split(","))

    area = tuple(int(x) for x in area.split("x"))
    ending_corner = starting_corner[0] + area[0], starting_corner[1] + area[1]

    return claim_id, starting_corner, ending_corner


with open("input") as f:
    claims = [parse_claim(line) for line in f]

# the highest coordinate we need to consider. I could set this programatically, but 2000 is good enough
max_value = 2000
fabric = [[0] * max_value for _ in range(max_value)]

for _, first_corner, second_corner in claims:
    for x in range(first_corner[0], second_corner[0]):
        for y in range(first_corner[1], second_corner[1]):
            fabric[x][y] += 1


print(sum(number_of_claims > 1 for row in fabric for number_of_claims in row))


def claim_is_not_overlapped(claim, solved_fabric):
    for x in range(first_corner[0], second_corner[0]):
        for y in range(first_corner[1], second_corner[1]):
            if fabric[x][y] != 1:
                return False
    return True


for claim_id, first_corner, second_corner in claims:
    if claim_is_not_overlapped(first_corner, second_corner):
        print(claim_id)
