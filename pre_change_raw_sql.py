from sys import argv


def pre_change(read_f, write_f):

    with open(read_f, "r") as f:
        raw_sql_lines = f.readlines()
        filtered_sql_lines = [raw_sql_line.replace("000Z", "000").replace("T", " ") for raw_sql_line in raw_sql_lines]
        result = "".join(filtered_sql_lines)

    with open(write_f, "w") as f:
        f.write(result)

try:
    pre_change(*argv[1:])
    print("====================")
    print("successed pre_change")
    print("====================")
except:
    print("====================")
    print("  some thing wrong  ")
    print("====================")
