import hashlib, re

def get_md5_of_string(input_string):
    """

    :param input_string:
    :return:
    """
    return hashlib.md5(input_string.encode()).hexdigest()

def use_regex(input_text):
    """

    :param input_text:
    :return:
    """
    match = re.match(r"00000.*\d", input_text)
    return bool(match)

def find_lowest_number(secret_key):
    for i in range(10000000):
        print(f"here's i: {i}")
        full_secret_key = secret_key + str(i)
        print(f"here's full secrect key: {full_secret_key}")
        hash = get_md5_of_string(full_secret_key)
        print(f"here's hash key: {hash}")
        if use_regex(hash):
            return i



def main():
    puzzle_input = "yzbqklnj"
    answer = find_lowest_number(puzzle_input)
    print(f"the answer is {answer}")


if __name__ == "__main__":
    main()
