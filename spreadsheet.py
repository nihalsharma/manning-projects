import csv
import sys

# Step 1: Read file path from command-line argument
if len(sys.argv) < 2:
    print("Please provide a file path as a command-line argument.")
    sys.exit(1)

file_path = sys.argv[1]

# Step 2: Open file handle with latin-1 encoding
try:
    with open(file_path, 'r', encoding='latin-1') as file:
        csv_reader = csv.reader(file)
        
        # Step 3: Skip over the first row (column names)
        next(csv_reader)
        
        # Step 4: Save contents into a two-dimensional list
        data = [row for row in csv_reader]

        # Print the two-dimensional list
        print(data)

except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
except csv.Error as e:
    print(f"CSV Error: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
