import traceback


def ls_decode(byte_array):
    return_str = []
    hex_list = []
    for i in range(0, len(byte_array), 2):

        char = byte_array[i]
        try:
            char_next = byte_array[i + 1]
        except:
            continue
        new_hex = (char_next << 8) + char  # 倒序组合
        hex_list.append(new_hex)
    # print([hex(x) for x in hex_list])

    for x in hex_list:
        try:
            chr(x).encode()
            return_str.append(chr(x))
        except Exception as e:
            print("[ERROR: %s]" % e)
            print(traceback.format_exc())
    return "".join(return_str)

