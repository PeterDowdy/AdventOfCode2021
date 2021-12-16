data = []
with open("day16.txt") as f:
    for x in f.readlines():
        data.append(x.strip())
data = data[0]

bin_data = ""
for h in data:
    bin_data += bin(int(h, 16)).replace("0b", "").rjust(4, "0")

commands = []


def get_packet(sub_bin_data):
    commands = []
    ctr = 0
    while ctr < len(sub_bin_data):
        version = int(sub_bin_data[ctr : ctr + 3], 2)
        ctr += 3
        type = int(sub_bin_data[ctr : ctr + 3], 2)
        ctr += 3
        if type == 4:
            string_so_far = ""
            while True:
                next_chunk = sub_bin_data[ctr : ctr + 5]
                string_so_far += next_chunk[1:]
                ctr += 5
                if next_chunk[0] == "0":
                    break
            return (ctr, [(version, type, int(string_so_far, 2))])
        else:
            h = sub_bin_data[ctr]
            ctr += 1
            calculated_value = None
            if h == "0":
                bit_count = int(sub_bin_data[ctr : ctr + 15], 2)
                ctr += 15
                target_ctr = ctr + bit_count
                while ctr < target_ctr:
                    next_ctr, next_commands = get_packet(sub_bin_data[ctr:])
                    commands += next_commands
                    ctr += next_ctr
                calculated_value = (ctr, commands)
            elif h == "1":
                sub_packet_count = int(sub_bin_data[ctr : ctr + 11], 2)
                ctr += 11
                for _ in range(0, sub_packet_count):
                    next_ctr, next_commands = get_packet(sub_bin_data[ctr:])
                    commands += next_commands
                    ctr += next_ctr
                calculated_value = (ctr, commands)
            if type == 0:
                return (ctr, [(version, type, sum(c[2] for c in commands))])
            if type == 1:
                pdct = 1
                for c in commands:
                    pdct *= c[2]
                return (ctr, [(version, type, pdct)])
            if type == 2:
                return (ctr, [(version, type, min(c[2] for c in commands))])
            if type == 3:
                return (ctr, [(version, type, max(c[2] for c in commands))])
            if type == 5:
                if commands[0][2] > commands[1][2]:
                    return (ctr, [(version, type, 1)])
                else:
                    return (ctr, [(version, type, 0)])
            if type == 6:
                if commands[0][2] < commands[1][2]:
                    return (ctr, [(version, type, 1)])
                else:
                    return (ctr, [(version, type, 0)])
            if type == 7:
                if commands[0][2] == commands[1][2]:
                    return (ctr, [(version, type, 1)])
                else:
                    return (ctr, [(version, type, 0)])


total_ctr = 0
while total_ctr < len(bin_data):
    if all(x == "0" for x in bin_data[total_ctr:]):
        break
    next_ctr, next_commands = get_packet(bin_data[total_ctr:])
    commands += next_commands
    total_ctr = next_ctr
print(commands)
