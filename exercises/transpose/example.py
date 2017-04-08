def transpose(input_lines):
    lines = input_lines.split("\n")
    zipped = map(list,
                 [line.ljust(len(max(lines, key=len)))
                  for line in lines])
    return "\n".join("".join(line) for line in zip(*zipped)).strip()
