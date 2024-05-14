import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag


class Symbolic:
    def __init__(self):
        self.relationships = {}

    def extract_meaning(self, premise):
        # Tokenize and perform POS tagging on the premise
        tokens = word_tokenize(premise.lower())
        pos_tags = pos_tag(tokens)

        # Extract entities (nouns) and attributes (verbs/adjectives/nouns) from the POS tags
        nouns = [word for word, tag in pos_tags if tag.startswith('N')]
        attributes = [word for word, tag in pos_tags if tag.startswith('V') or tag.startswith('JJ') or tag.startswith('N')]

        # Store the relationships in the dictionary
        self.relationships[premise] = (nouns, attributes)
        print("Meaning of '{}':".format(premise))
        print("Entities:", nouns)
        print("Attributes:", attributes)

    def combine_premises(self, premise1, premise2):
        if premise1 in self.relationships and premise2 in self.relationships:
            nouns1, attributes1 = self.relationships[premise1]
            nouns2, attributes2 = self.relationships[premise2]

            # Find common entities between both premises
            common_entities = set(nouns1).intersection(nouns2)

            if common_entities:
                # Initialize a list to collect inherited qualities
                inherited_qualities = []

                # Iterate over attributes of premise2 to inherit relevant qualities to premise1
                for attr in attributes2:
                    if attr not in common_entities:  # Exclude attributes corresponding to common entities
                        inherited_qualities.append(attr)

                if inherited_qualities:
                    # Construct the conclusion based on inherited qualities
                    conclusion = "{} {}".format(', '.join(nouns1), ' '.join(inherited_qualities))
                    print("Conclusion based on inheritance:")
                    print(conclusion)
                else:
                    print("No inherited qualities found for common entities.")
            else:
                print("No common entities found between the premises.")
        else:
            print("Invalid premises. Please provide valid statements.")

    def language(self):
        premise1 = input("Enter premise 1: ")
        premise2 = input("Enter premise 2: ")

        self.extract_meaning(premise1)
        self.extract_meaning(premise2)

        # Combine premises and derive conclusions based on inheritance
        self.combine_premises(premise1, premise2)

# Example usage
symbolic_engine = Symbolic()
symbolic_engine.language()
