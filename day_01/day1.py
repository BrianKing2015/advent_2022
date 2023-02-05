# Day 1, calorie counting

def main():
	input_file = "real_input.txt"
	with open(input_file, "r", encoding="UTF-8") as file:
		per_elf = file.read().split("\n\n")
		most_calorie_elf = 0
		list_of_elf_calories = []
		
		for group in per_elf:
			group = group.split("\n")
			sum_of_calories = 0
			for line in group:
				sum_of_calories = sum_of_calories + int(line)

			list_of_elf_calories.append(sum_of_calories)

			if sum_of_calories > most_calorie_elf:
				most_calorie_elf = sum_of_calories

		print(f"This is solution one {most_calorie_elf}")
		list_of_elf_calories.sort(reverse=True)
		print(f"This is solution two {sum(list_of_elf_calories[:3])}")

if __name__ == '__main__':
	main()
