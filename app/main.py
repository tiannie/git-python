import hashlib
import os
import sys
import zlib
from pathlib import Path


def main():
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
    elif command == "cat-file" and sys.argv[2] == 'p':
        with open(Path('.git/objects') / sys.argv[3][:2] / sys.argv[3][2:] , "rb") as f:
            content = zlib.decompress(f.read())
            print(content.decode().split("\0")[1], end='')
    elif command == "hash-object" and sys.argv[2] == '-w':
        with open(sys.argv[3] , "r") as f:
            content = f.read()  # clear text content
            obj_content = f'blob {len(content)}\0{content}'.encode()  # content with header in bytecode
            hex_digest = hashlib.sha1(obj_content).hexdigest()
            (Path('.git/objects') / hex_digest[:2]).mkdir(exist_ok=True)
            with open(Path('.git/objects') / hex_digest[:2] / hex_digest[2:] , "wb") as f_obj:
                f_obj.write(zlib.compress(obj_content))
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
