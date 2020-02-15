import sys
import leveldb

db = leveldb.LevelDB(sys.argv[1])
rows = list(db.RangeIter())

for row in rows:
    print(row)

    value_bytes = list(c for c in list(row[1]))[1:]

    hex_list = []
    for i in range(0, len(value_bytes), 2):
        char = value_bytes[i]
        char_next = value_bytes[i + 1]

        new_hex = (char_next << 8) + char  # 倒序组合
        hex_list.append(new_hex)
    try:
        print([hex(x) for x in hex_list])
        print("".join([chr(x) for x in hex_list]))
    except Exception as e:
        print(e)

    print()
