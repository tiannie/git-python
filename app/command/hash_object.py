import hashlib
import zlib
from pathlib import Path
from typing import List


def hash_object(sys_argv: List[str]) -> None:
    with open(sys_argv[3], "r") as f:
        content = f.read()  # clear text content
        obj_content = f'blob {len(content)}\0{content}'.encode()  # content with header in bytecode
        hex_digest = hashlib.sha1(obj_content).hexdigest()
        (Path('.git/objects') / hex_digest[:2]).mkdir(exist_ok=True)
        with open(Path('.git/objects') / hex_digest[:2] / hex_digest[2:], "wb") as f_obj:
            f_obj.write(zlib.compress(obj_content))
        print(hex_digest, end='')
