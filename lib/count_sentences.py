#!/usr/bin/env python3
import re  # Import the 're' module for regular expressions

class MyString:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self._value:
            words = self._value.split()
            last_word = words[-1] if words else ""
            if last_word == ".":
                return True
        return False

    def is_question(self):
        if self._value and self._value.endswith("?"):
            return True
        return False

    def is_exclamation(self):
        if self._value and self._value.endswith("!"):
            return True
        return False

    def count_sentences(self):
        if not self._value:
            return 0

        # Use a regular expression to split the string into sentences
        sentences = re.split(r'[.!?]', self._value)

        # Remove empty and whitespace-only strings from the list of sentences
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

        return len(sentences)


# Create an instance of MyString
string = MyString()

# Assign a value to the instance
string.value = "This is a string! It has three sentences. Right?"

# Call the methods on the instance
print(string.is_sentence())  # True
print(string.is_question())  # False
print(string.is_exclamation())  # True
print(string.count_sentences())  # 3
