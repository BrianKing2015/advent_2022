def calculate_priority(item_type):
    if "a" <= item_type <= "z":
        return ord(item_type) - ord("a") + 1
    elif "A" <= item_type <= "Z":
        return ord(item_type) - ord("A") + 27
    else:
        return 0


def find_common_items(input_file):
    total_priority = 0

    with open(input_file, "r") as file:
        rucksacks = file.readlines()

    for rucksack in rucksacks:
        rucksack = rucksack.strip()  # Remove leading/trailing whitespace
        first_compartment = rucksack[: len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2 :]

        common_items = set(first_compartment) & set(second_compartment)

        for item_type in common_items:
            total_priority += calculate_priority(item_type)

    return total_priority


if __name__ == "__main__":
    input_file = "rucksacks.txt"

    result = find_common_items(input_file)
    print("Sum of priorities of common items:", result)
