import sys
import re

WORD_RE = re.compile(r"[A-Za-z']+")

def main():
    for line in sys.stdin:
        line = line.strip().lower()
        for w in WORD_RE.findall(line):
            if w:
                print(f"{w}\t1")

if __name__ == "__main__":
    main()
