

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
        consecutive_count = 0
        index_tracker = 0
        length_of_text = len(self.text) -1
        for index in self.text:
            if index_tracker + 1 > length_of_text:
                return False
            if self.text[index_tracker] == self.text[index_tracker +1]:
                return True
            index_tracker += 1

    def passed_all_tests(self):
        if self.three_vowel_check() and self.banned_combos_check() and self.consecutive_letters_check():
            return True
        else:
            return False


