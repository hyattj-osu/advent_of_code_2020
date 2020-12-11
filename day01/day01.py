# Part 1: Find the two entries that sum to 2020; what do you get if you multiply them together?
# Part 2: In your expense report, what is the product of the three entries that sum to 2020?


# part 1
def find_two(numbers):
    for i, num in enumerate(numbers):
        target_spot = i - 1 # makes sure there are at least two values to work with
        while target_spot >= 0:
            sum = num + numbers[target_spot]
            if sum == 2020:
                product = num * numbers[target_spot]
                print(f'{num} + {numbers[target_spot]} = {sum}')
                print(f'{num} * {numbers[target_spot]} = {product}')
            target_spot -= 1
    return()



# part 2
def find_three(numbers):
    if len(numbers) < 3:
        return()
    for num1_index in range(0, len(numbers) - 2):
        for num2_index in range(num1_index + 1, len(numbers) - 1):
            for num3_index in range(num2_index + 1, len(numbers)):
                sum = numbers[num1_index] + numbers[num2_index] + numbers[num3_index]
                if sum == 2020:
                    product = numbers[num1_index] * numbers[num2_index] * numbers[num3_index]
                    print(f'{numbers[num1_index]} + {numbers[num2_index]} + {numbers[num3_index]} = {sum}')
                    print(f'{numbers[num1_index]} * {numbers[num2_index]} * {numbers[num3_index]} = {product}')
    return()



def main():
    numbers = []
    with open("./day01/input.txt", 'r') as infile:
        for line in infile:
            numbers.append(int(line))
    find_two(numbers)
    find_three(numbers)

    return()



if __name__ == "__main__":
    main()