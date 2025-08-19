import sys


def read_log_file(file_path):
    """Reads and prints the contents of the specified log file."""
    try:
        with open(file_path, 'r') as f:
            for line in f:
                print(line.rstrip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python log_reader.py <log_file_path>")
        sys.exit(1)
    log_file = sys.argv[1]
    read_log_file(log_file)


if __name__ == "__main__":
    main()
