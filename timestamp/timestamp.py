import datetime

# Function to create a text file with the current timestamp
def create_timestamp_file():
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "timestamp.txt"
    with open(filename, "w") as file:
        file.write(current_timestamp)
    print(f"File '{filename}' created with timestamp: {current_timestamp}")

# Function to read from a text file and display its content
def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage
create_timestamp_file()
read_file("timestamp.txt")
