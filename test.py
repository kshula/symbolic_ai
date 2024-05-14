import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag


class AristotelianSyllogism:
    def __init__(self):
        self.major_premise = None
        self.minor_premise = None
        self.conclusion = None

    def set_major_premise(self, major_premise):
        self.major_premise = major_premise

    def set_minor_premise(self, minor_premise):
        self.minor_premise = minor_premise

    def derive_conclusion(self):
        if self.major_premise is None or self.minor_premise is None:
            print("Premises are not fully defined.")
            return

        # Tokenize and perform POS tagging on major premise
        major_tokens = word_tokenize(self.major_premise.lower())
        major_pos_tags = pos_tag(major_tokens)

        # Tokenize and perform POS tagging on minor premise
        minor_tokens = word_tokenize(self.minor_premise.lower())
        minor_pos_tags = pos_tag(minor_tokens)

        # Debugging prints for major premise POS tags
        print("Major Premise Full POS Tagging:")
        print(major_pos_tags)

        # Debugging prints for minor premise POS tags
        print("\nMinor Premise Full POS Tagging:")
        print(minor_pos_tags)

        # Identify first and second plural nouns (NNS) in major premise
        first_nns = None
        second_nns = None
        for word, tag in major_pos_tags:
            if tag == 'NNS':
                if first_nns is None:
                    first_nns = word
                else:
                    second_nns = word
                    break

        if first_nns is None or second_nns is None:
            print("Noun plurals not fully identified in major premise.")
            return

        # Identify plural noun (NNS) in minor premise
        minor_nns = None
        for word, tag in minor_pos_tags:
            if tag == 'NNS':
                minor_nns = word
                break

        if minor_nns is None:
            print("Plural noun not identified in minor premise.")
            return

        # Check if the minor premise subject is a subset of the second NNS in the major premise
        if first_nns == minor_nns:
            # Derive the conclusion
            self.conclusion = f"All {minor_nns} are {second_nns}."

        else:
            print("Minor premise subject is not a subset of the second noun in major premise.")
            return

    def get_conclusion(self):
        return self.conclusion


# Example usage
syllogism = AristotelianSyllogism()

# Prompt user to input major premise
major_input = input("Enter the major premise: ")
syllogism.set_major_premise(major_input)

# Prompt user to input minor premise
minor_input = input("Enter the minor premise: ")
syllogism.set_minor_premise(minor_input)

# Derive conclusion
syllogism.derive_conclusion()

# Get and print the conclusion
print("\nConclusion:", syllogism.get_conclusion())
