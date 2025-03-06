def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        print("Number of lines:", sum(1 for _ in file))
s = input()
count_lines_in_file(s)
