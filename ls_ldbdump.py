import base64
import subprocess
import sys

if __name__ == '__main__':

    ldb_file = sys.argv[1]
    stdout = subprocess.getoutput("./ldbdump_base64 " + ldb_file)

    for row in stdout.splitlines()[1:]:
        row = row.replace('"', "").replace(',', "")
        k, v = row.split(": ")
        k_ = base64.b64decode(k)
        v_ = base64.b64decode(v)
        print("Key:", k_)

        print("Value bytes:", v_)
        if len(v_) < 2:
            print()
            print("=" * 10)
            continue

        flag = v_[0]
        value = v_[1:]
        if flag == 0:
            true_value = value.decode("utf_16_le")
        elif flag == 1:
            true_value = value.decode()
        else:
            print("Unknown Format")
            true_value = value

        print("Value:", true_value)

        print()
        print("=" * 10)
