import argparse
import os
import sys
import zlib
from pathlib import Path

from app.command import ls_tree, hash_object


def main():
    parser = argparse.ArgumentParser(description='Git CLI')
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    command = sys.argv[1]
    print(f'{sys.argv}', file=sys.stderr)
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    elif command == "cat-file" and sys.argv[2] == '-p':
        with open(Path('.git/objects') / sys.argv[3][:2] / sys.argv[3][2:], "rb") as f:
            content = zlib.decompress(f.read())
            print(content.decode().split("\0")[1], end='')
    elif command == "hash-object" and sys.argv[2] == '-w':
        hash_object(sys.argv)
    elif command == "ls-tree" and sys.argv[2] == '--name-only':
        ls_tree(sys.argv)
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
