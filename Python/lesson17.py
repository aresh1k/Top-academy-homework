import re

telephone_numbers = ("+ 7 499 456-45-78", "+74994564578", "7 (499) 456 45 78", "7 (499) 456-45-78")

reg = "\+?\s?[78]\s?\(?\d+\)?\s?\d*[\s-]?\d*[\s-]?\d*"

for i in telephone_numbers:
    print(re.findall(reg, i))
