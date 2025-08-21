import sys



def read_log_file(file_path):
    """Reads and prints the contents of the specified log file."""
    import re
    error_keywords = ["ERROR", "CRITICAL", "WARNING"]
    log_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|DEBUG|ERROR|CRITICAL|WARNING) (.+)$")
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line_stripped = line.rstrip()
                print(line_stripped)
                match = log_pattern.match(line_stripped)
                if match:
                    timestamp, level, message = match.groups()
                    if level in error_keywords:
                        print(f"[DETECTED] Time: {timestamp} | Level: {level} | Message: {message}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        pass

def read_log(file_path):
    """Reads the log file and returns its lines as a list."""
    try:
        with open(file_path, 'r') as f:
            return [line.rstrip() for line in f]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
        print(f"Error reading file: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python log_reader.py <log_file_path>")
        sys.exit(1)
    log_file = sys.argv[1]
    read_log_file(log_file)


if __name__ == "__main__":
    main()
