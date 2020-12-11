import re

def process_bag_rules(rules):

    to_remove = re.compile(r"(bag)(s{0,1})|\.") # removes bag, bags, and '.'

    rule_dict = {}
    for rule in rules:
        stripped_rule = to_remove.sub('', rule)
        outer_bag, inner_bags_string = stripped_rule.split("contain")
        outer_bag = outer_bag.strip()

        inner_bag_list = [inner_bag.strip() for inner_bag in inner_bags_string.split(",")]
        inner_bag_dict = {}
        for inner_bag in inner_bag_list:
            bag_count = inner_bag.split()[0]
            bag_type = inner_bag.split(bag_count)[1].strip()

            if bag_count == "no":
                bag_count = '0'
                
            inner_bag_dict.update({bag_type: int(bag_count)})

        rule_dict.update({outer_bag: inner_bag_dict})
    return(rule_dict)


def check_inner_bags(rule_dict, outer_bag):
    shiny_gold_bag_count = 0
    for inner_bag in rule_dict[outer_bag].keys():
        if inner_bag == "shiny gold":
            shiny_gold_bag_count += 1
            return(shiny_gold_bag_count)
        elif inner_bag == "other":
            continue
        else:
            shiny_gold_bag_count += check_inner_bags(rule_dict, inner_bag)

    # we only care about whether the outermost bags can EVENTUALLY get a shiny gold, not how many variations of shiny 
    # gold there are in total
    if shiny_gold_bag_count > 1: 
        shiny_gold_bag_count = 1
    return(shiny_gold_bag_count)



def count_shiny_gold_bag_options(rule_dict):
    shiny_gold_options_count = 0

    for outer_bag in rule_dict.keys():
        shiny_gold_options_count += check_inner_bags(rule_dict, outer_bag)

    print(f'Part 1: {shiny_gold_options_count}')

    return()



def count_inner_bags(rule_dict, outer_bag):
    internal_bag_count = 0

    for inner_bag_type, bag_count in rule_dict[outer_bag].items():
        if inner_bag_type == "other":
            continue
        else:
            # print(f'{inner_bag_type}: {bag_count}')

            # we need to add the bag itself plus all internal bags
            internal_bag_count += bag_count + (bag_count * count_inner_bags(rule_dict, inner_bag_type))
    return(internal_bag_count)



def count_bags_in_shiny_bag(rule_dict):

    internal_bag_count = 0
    if "shiny gold" in rule_dict.keys():
        internal_bag_count = count_inner_bags(rule_dict, "shiny gold")


    print(f'Part 2: {internal_bag_count}')
    return()



def main():

    lines = []
    # with open("./day07/example.txt", 'r') as infile:
    with open("./day07/input.txt", 'r') as infile:
        lines = infile.read().splitlines()

    rule_dict = process_bag_rules(lines)
    count_shiny_gold_bag_options(rule_dict)

    count_bags_in_shiny_bag(rule_dict)

    return()



if __name__ == "__main__":
    main()