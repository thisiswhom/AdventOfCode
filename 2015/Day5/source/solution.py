

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

    def passed_all_part_one_tests(self):
        if self.three_vowel_check() and self.banned_combos_check() and self.consecutive_letters_check():
            return True
        else:
            return False

    def repeat_pattern_check(self):
        pass


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
    number_of_nice = 0
    file = create_file_path("values")
    list_of_values = intake_values(file)
    for value in list_of_values:
        questionable_string = Naughty_Or_Nice_Text(value)
        if questionable_string.passed_all_part_one_tests():
            number_of_nice += 1
    print(f"There are {number_of_nice} nice strings!")
    return number_of_nice


if __name__ == "__main__":
    main()