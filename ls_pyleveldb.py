import sys
import leveldb

from ls_decode import ls_decode

if __name__ == '__main__':

    db = leveldb.LevelDB(sys.argv[1])
    rows = list(db.RangeIter())

    for k, v in rows:
        v = v[1:]
        key_bytes = list(c for c in list(k))
        value_bytes = list(c for c in list(v))

        print(key_bytes)
        print(ls_decode(value_bytes))
        print()
