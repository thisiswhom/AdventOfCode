import re

class Naughty_Or_Nice_Text():
    def __init__(self, text):
        self.text = text


    def three_vowel_check(self):
        vowel_count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for vowel in vowels:
            vowel_count += self.text.count(vowel)
        if vowel_count >= 3:
            return True
        else:
            return False

    def banned_combos_check(self):
        combo_count = 0
        banned_combos = ['ab', 'cd', 'pq', 'xy']
        for combo in banned_combos:
            combo_count += self.text.count(combo)
        if combo_count > 0:
            return False
        else:
            return True

    def consecutive_letters_check(self):
        index_tracker = 0
        length_of_text = len(self.text) -1
        for index in self.text:
            if index_tracker + 1 > length_of_text:
                return False
            if self.text[index_tracker] == self.text[index_tracker +1]:
                return True
            index_tracker += 1

    def passed_all_part_one_checks(self):
        """Returns bool if the checks for part one of the challege passes for each string"""
        if self.three_vowel_check() and self.banned_combos_check() and self.consecutive_letters_check():
            return True
        else:
            return False

    def double_consecutive_letters_check(self):
        """Looking for a double set of any letters with the count method"""
        pattern = r'([a-zA-Z]{2}).*?\1'
        return bool(re.search(pattern, self.text))

    def repeat_pattern_check(self):
        """Uses regex to find any one character, then any other character
        then it must find a chracter that matches the first

        Originally going to use a bunch of loops but learned that it could be
        done much simpler with a regex"""
        pattern = r'([a-zA-Z]).\1'
        return bool(re.search(pattern, self.text))

    def passed_all_part_two_checks(self):
        """Returns bool if the checks for part two of the challege passes for each string"""
        if self.double_consecutive_letters_check() and self.repeat_pattern_check():
            return True
        else:
            return False


def create_file_path(file_name):
    """This function creates the absolute path of the values file.

    This is to enable me to not worry about pushing my username/file structure gitHub
    Possible side benefit is others can run this on their system without worrying
    about differences in their environment and mine"""
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_dir, file_name)
    return file


def intake_values(file):
    """Opens a file then makes each line a string in list."""
    input_file = open(f"{file}")
    list_of_values = [line.strip() for line in input_file.readlines()]
    return list_of_values

def main():
    number_of_nice_part_1 = 0
    number_of_nice_part_2 = 0
    file = create_file_path("values")
    list_of_values = intake_values(file)
    for value in list_of_values:
        questionable_string = Naughty_Or_Nice_Text(value)
        if questionable_string.passed_all_part_one_checks():
            number_of_nice_part_1 += 1
        if questionable_string.passed_all_part_two_checks():
            number_of_nice_part_2 += 1
    print(f"There are {number_of_nice_part_1} nice strings in part one!")
    print(f"There are {number_of_nice_part_2} nice strings in part two!")
    return number_of_nice_part_1


if __name__ == "__main__":
    main()