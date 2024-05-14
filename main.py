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

        # Identify major term (predicate) from major premise
        major_term = None
        found_nns = 0  # Counter to track the NNS tags encountered
        for word, tag in major_pos_tags:
            if tag == 'NNS':
                found_nns += 1
                if found_nns == 2:  # Select the second NNS encountered
                    major_term = word
                    break

        if major_term is None:
            print("Major term not identified.")
            return

        # Identify minor term (subject) from minor premise
        minor_subject = None
        for word, tag in minor_pos_tags:
            if tag == 'NNS':
                minor_subject = word
                break

        if minor_subject is None:
            print("Minor subject not identified.")
            return

        # Derive the conclusion
        self.conclusion = f"All {minor_subject} are {major_term}."

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
