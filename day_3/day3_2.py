def calculate_priority(item_type):
    if "a" <= item_type <= "z":
        return ord(item_type) - ord("a") + 1
    elif "A" <= item_type <= "Z":
        return ord(item_type) - ord("A") + 27
    else:
        return 0


def find_badge_items(input_file):
    total_priority = 0

    with open(input_file, "r") as file:
        rucksacks = file.read().splitlines()

    num_groups = len(rucksacks) // 3

    for group_index in range(num_groups):
        group_rucksacks = rucksacks[group_index * 3 : (group_index + 1) * 3]

        common_items = (
            set(group_rucksacks[0]) & set(group_rucksacks[1]) & set(group_rucksacks[2])
        )

        for item_type in common_items:
            total_priority += calculate_priority(item_type)

    return total_priority


if __name__ == "__main__":
    input_file = "rucksacks.txt"

    result = find_badge_items(input_file)
    print("Sum of priorities of badge items:", result)
