

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