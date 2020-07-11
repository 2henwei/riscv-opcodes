import sys

inputs = []
inputs.append(sys.stdin)

insts = []
new_insts = []

for f in inputs:
    for line in f:
        if line[0] == '\n' or line[0] == '#': continue
        insts.append(line.strip())

for inst in insts:
    tokens = inst.split()

    # Find nf field
    if "nf" in tokens:
        name = tokens[0]

        # nf field
        tokens[1] = "31..29=0"

        for seg in range(2, 8 + 1):
            new_tokens = list(tokens)
            if name[2] == "s" or name[2] == "x":
                seg_name = "%sseg%d%s" % (name[:3], seg, name[3:])
            else:
                seg_name = "%sseg%d%s" % (name[:2], seg, name[2:])

            new_tokens[0] = seg_name
            new_tokens[1] = "31..29=%d" % (seg - 1)
            new_insts.append(" ".join(new_tokens))
        new_insts.append(" ".join(tokens))
    else:
        new_insts.append(inst)

for i in new_insts:
    print(i)
