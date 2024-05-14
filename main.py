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

        # Extract entities (nouns) from major premise
        major_entities = self.extract_entities(major_pos_tags)

        # Extract entities (nouns) from minor premise
        minor_entities = self.extract_entities(minor_pos_tags)

        # Debugging prints
        print("Major Premise:")
        print("Entities:", major_entities)

        print("\nMinor Premise:")
        print("Entities:", minor_entities)

        # Identify the middle term (shared entity)
        middle_term = None
        for entity in minor_entities:
            if entity in major_entities:
                middle_term = entity
                break

        if middle_term is None:
            print("Middle term does not match in premises.")
            return

        # Identify the subject and predicate for the conclusion
        minor_subject = None
        for entity in minor_entities:
            if entity != middle_term:
                minor_subject = entity
                break

        if minor_subject is None:
            print("Minor subject not identified.")
            return

        major_predicate = None
        for entity in major_entities:
            if entity != middle_term:
                major_predicate = entity
                break

        if major_predicate is None:
            print("Major predicate not identified.")
            return

        # Derive the conclusion
        self.conclusion = f"All {minor_subject} are {major_predicate}"

    def extract_entities(self, pos_tags):
        # Extract entities (nouns) from POS tags
        entities = []

        for token, pos_tag in pos_tags:
            if pos_tag.startswith('N'):
                entities.append(token)

        return entities

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
