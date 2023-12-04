


def write_file(file_name="test_file.txt", file_content="Log 1: We are adding five bananas to our file."):
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)
    pass

def append_file(file_name="test_file", append_content="We are adding five more potatoes and yams to the lgofile."):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)
    pass

def read_file(file_name="test_file"):
    with open(f'{file_name}.txt', 'r') as f:
        return f.read()
    pass
