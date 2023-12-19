import operator
from collections import OrderedDict

from utils import parse_input


OPS = {
    "<": operator.lt,
    ">": operator.gt,
}


def process_workflow(
    workflow_map: dict[str, list],
    rating_by_category: OrderedDict[str, int],
    workflow_name: str,
) -> str:
    workflow_list = workflow_map[workflow_name]

    for item in workflow_list[:-1]:
        category = item[0]
        oper = OPS[item[1]]
        rating_to_compare = item[2]
        rating_input = rating_by_category.get(category)
        if rating_to_compare is not None:
            condition = oper(rating_input, rating_to_compare)
            if condition:
                # Return output which is either "A", "R", or the name of another workflow
                return item[-1]
    else:
        # If no other rules match, return the last workflow which is either "A", "R", or the name of another workflow.
        return workflow_list[-1]


def part_one():
    workflow_part, rating_part = parse_input("day_19.txt", "\n\n")
    total = 0

    workflow_map = dict()
    rating_map = dict()

    workflows = workflow_part.strip().split("\n")
    ratings = rating_part.strip().split("\n")

    # Construct a dictionary for the unique workflows (some conditions may contain the same category more than once!)
    for workflow in workflows:
        name, rules = workflow.split("{")
        rule_map = list()
        rules = rules.replace("}", "").split(",")

        # Order adding rules is important here
        for rule in rules[:-1]:
            condition, output = rule.split(":")
            category = condition[0]
            oper = condition[1]
            value = int(condition[2:])
            rule_map.append([category, oper, value, output])

        # Add the final fallback rule last
        rule_map.append(rules[-1])
        workflow_map[name] = rule_map

    # Construct a dictionary of part ratings.
    for index, rating in enumerate(ratings):
        parts = rating.replace("{", "").replace("}", "").split(",")
        rating_by_category = OrderedDict({item[0]: int(item[2:]) for item in parts})
        rating_map[index] = rating_by_category

    # Go through each part ratings entry and process the workflow
    for r_b_c in rating_map.values():
        # Start at "in" workflow
        output = process_workflow(workflow_map, r_b_c, "in")
        test = ["in", output]

        while output not in ("A", "R"):
            output = process_workflow(workflow_map, r_b_c, output)
            test.append(output)

        if output == "A":
            total += sum(r_b_c.values())

    print("Part 1: ", total)


def part_two():
    lines = parse_input("test.txt")
    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_one()
    # part_two()
