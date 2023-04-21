import ast
import os
import sys
import time
import redis
from pathlib import Path

if __name__ == '__main__':

    FILE = Path(__file__).resolve()
    ROOT = FILE.parents[1]  # YOLOv5 root directory
    if str(ROOT) not in sys.path:
        sys.path.append(str(ROOT))  # add ROOT to PATH
    ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
    for i in FILE.parents:
        print(i)
