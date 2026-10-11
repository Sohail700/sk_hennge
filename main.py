import sys


def sum_negative_powers(values, index=0):
    if index == len(values):
        return 0

    value = values[index]

    if value < 0:
        return value ** 4 + sum_negative_powers(values, index + 1)

    return sum_negative_powers(values, index + 1)


def solve(lines, case_count, line_index, results):
    if case_count == 0:
        return

    x = int(lines[line_index])
    values = tuple(map(int, lines[line_index + 1].split()))

    if len(values) != x:
        results.append(-1)
    else:
        results.append(sum_negative_powers(values))

    solve(lines, case_count - 1, line_index + 2, results)


def main():
    lines = sys.stdin.read().splitlines()

    if not lines:
        return

    case_count = int(lines[0])
    results = []

    solve(lines, case_count, 1, results)

    sys.stdout.write("\n".join(map(str, results)) + "\n")


if __name__ == "__main__":
    main()
