import hashlib
import zlib
from pathlib import Path
from typing import List


def ls_tree(sys_argv: List[str]) -> None:
    hex_digest = sys_argv[3]
    with open(Path('.git/objects') / hex_digest[:2] / hex_digest[2:], "rb") as f:
        content = zlib.decompress(f.read())  # clear text content
        segments = content.split(b'\0')
        for i, segment in enumerate(segments):
            if i and segment:
                print(segment)
                name = segment.split(b' ')[1]
                print(name.decode())
