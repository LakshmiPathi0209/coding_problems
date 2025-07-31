# You are given a chemical formula as a string. Your task is to write a program that parses the formula and returns a dictionary that maps each element to its total count.
# # The chemical formula:
# # May contain elements like "H", "O", "Mg", "Na", etc.
# # May include subscripts (like H2 or O2) which indicate the number of atoms.
# # May include parentheses () with subscripts to indicate grouping.
# # May include nested parentheses like Mg(OH(H2O)2)2
# # You must correctly evaluate the entire formula and return a mapping of each atom to its total count.




import re
from collections import defaultdict

def parse_formula(formula: str) -> dict:
    def multiply_counts(counts, multiplier):
        for elem in counts:
            counts[elem] *= multiplier
        return counts

    def merge_counts(main, to_add):
        for elem, count in to_add.items():
            main[elem] += count

    def parse():
        stack = []
        counts = defaultdict(int)
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(counts)
                counts = defaultdict(int)
                i += 1
            elif formula[i] == ')':
                i += 1
                num = 0
                while i < len(formula) and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1
                num = num if num > 0 else 1
                temp = multiply_counts(counts, num)
                counts = stack.pop()
                merge_counts(counts, temp)
            else:
                match = re.match(r'([A-Z][a-z]*)(\d*)', formula[i:])
                if not match:
                    raise ValueError(f"Invalid element at index {i}: {formula[i:]}")
                elem = match.group(1)
                count = int(match.group(2)) if match.group(2) else 1
                counts[elem] += count
                i += len(match.group(0))
        return counts

    return dict(parse())

# Example test cases
formulas = [
    "Mg(OH(H2O)2)2"
]

if __name__ == "__main__":
    for f in formulas:
        print(f"{f}: {parse_formula(f)}")


