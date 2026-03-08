import os
import sys
import zlib
from pathlib import Path


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    command = sys.argv[1]
    print(f'{sys.argv}')
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    elif command == "cat-file":
        with open(Path('.git/objects') / sys.argv[3][:2] / sys.argv[3][2:] , "rb") as f:
            content = zlib.decompress(f.read())
            print(content.decode().split("\0")[1], end='')
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
