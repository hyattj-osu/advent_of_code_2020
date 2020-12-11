from string import ascii_lowercase



def parse_questions_anwered_per_person(answer_list):

    group_answers = []
    group_string = ""
    for i, person_answers in enumerate(answer_list):
        group_string += person_answers.strip()
        if not person_answers.strip() or i == len(answer_list)-1:
            group_answers.append(group_string)
            group_string = ""

    group_answer_sets = {}
    for i, group_answer in enumerate(group_answers):    
        group_answer_sets[i] = set(group_answer)

    sum_of_counts = sum([len(x) for x in group_answer_sets.values()])
    print(f'Part 1: {sum_of_counts}')

    return()



def parse_questions_anwered_per_group(answer_list):

    group_answers = []
    group_strings = []
    for i, person_answers in enumerate(answer_list):
        if person_answers.strip():
            group_strings.append(person_answers.strip())
        if not person_answers.strip() or i == len(answer_list)-1:
            group_answers.append(group_strings)
            group_strings = []

    common_answer_counts = []
    for group_answer in group_answers:
        common_answer_count = 0
        for letter in ascii_lowercase:
            if all([letter in person_answer for person_answer in group_answer]):
                common_answer_count += 1
        common_answer_counts.append(common_answer_count)

    print(f'Part 2: {sum(common_answer_counts)}')

    return()



def main():

    # with open("./day06/example.txt") as infile:
    with open("./day06/input.txt") as infile:
        lines = infile.readlines()

    parse_questions_anwered_per_person(lines)
    parse_questions_anwered_per_group(lines)

    return()



if __name__ == "__main__":
    main()