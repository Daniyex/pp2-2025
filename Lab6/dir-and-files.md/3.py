import os

def test_path(path):
    if os.path.exists(path):
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")
s = input()
test_path(s)
