def run():
    path = input("Enter the path to the log file: ")
    try: 
        with open(path, 'r') as f:
            for line in f:
                if "Failed password" in line or "authenticaiton failure" in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found")