import base64
import subprocess
import sys

from ls_decode import ls_decode

if __name__ == '__main__':

    ldb_file = sys.argv[1]
    stdout = subprocess.getoutput("./ldbdump_base64 " + ldb_file)

    for row in stdout.splitlines()[1:]:
        row = row.replace('"', "").replace(',', "")
        k, v = row.split(": ")
        k_ = base64.b64decode(k)
        v_ = base64.b64decode(v)
        print("Key:", k_)
        true_value = ls_decode(v_[1:])
        print("Value:", true_value)
        print()
