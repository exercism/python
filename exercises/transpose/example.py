def transpose(input_lines):
    lines = [line.replace(' ', '_') for line in input_lines.splitlines()]
    lines = [line.ljust(len(max(lines, key=len))) for line in lines]
    lines = [''.join(line) for line in zip(*lines)]
    lines = [line.rstrip().replace('_', ' ') for line in lines]
    return '\n'.join(lines)
