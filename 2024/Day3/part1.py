"""
regex made with https://regex-generator.olafneumann.org/?sampleText=mul(2%2C4)&flags=im&selection=4%7CDigit,6%7CDigit



"""

import re

def use_regex(input_text):
    pattern = re.compile(r"mul\(\d,\d\)", re.IGNORECASE, re.MULTILINE)
    return pattern.match(input_text)
