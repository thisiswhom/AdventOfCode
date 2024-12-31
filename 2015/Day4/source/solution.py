import hashlib, re

def get_md5_of_string(input_string):
    """
    Generates the MD5 hash of a given string

    :param input_string: the string to hash
    :type input_string: str
    :return: The MD5 hash of the input string
    :rtype: str
    """
    return hashlib.md5(input_string.encode()).hexdigest()

def use_regex(input_text):
    """
    Checks if the passed string matches the regex. for part 1 i had it
    run with five zeroes and just upped it to 6 for the second half

    :param input_text: the string to check
    :type input_text: str
    :return: Whether the regex is matched
    :rtype Bool
    """
    match = re.match(r"000000.*\d", input_text)
    return bool(match)

def find_lowest_number(secret_key):
    """
    Goes through every number from 1 to 10 million until one of them
    combines with the secrect key to create an md5 hash that matches the regex

    :param secret_key: the seed to start the hashing
    :type secret_key: str
    :return: what number was found to be the first to match the pattern
    :rtype int
    """
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
