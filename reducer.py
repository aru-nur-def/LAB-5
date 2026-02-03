import sys

def main():
    current_word = None
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split("\t")
        if len(parts) != 2:
            continue

        word, count_str = parts
        try:
            count = int(count_str)
        except ValueError:
            continue

        if current_word is None:
            current_word = word
            current_count = count
        elif word == current_word:
            current_count += count
        else:
            print(f"{current_word}\t{current_count}")
            current_word = word
            current_count = count

    if current_word is not None:
        print(f"{current_word}\t{current_count}")

if __name__ == "__main__":
    main()
