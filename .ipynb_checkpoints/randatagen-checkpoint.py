import random

# Define character groups with initial weights
vowel_weights = {'a': 0.3, 'e': 0.3, 'i': 0.2, 'o': 0.1, 'u': 0.1}
consonant_weights = {'b': 0.1, 'c': 0.1, 'd': 0.1, 'g': 0.1, 'h': 0.1,
                     'l': 0.1, 'm': 0.1, 'n': 0.1, 'r': 0.1, 's': 0.1}

# Helper function to pick a character based on weights
def weighted_choice(weights):
    letters, probabilities = zip(*weights.items())
    return random.choices(letters, weights=probabilities, k=1)[0]

# Generate a random name
def generate_name(length=3, syllable_structure="CVC"):
    name = []
    for _ in range(length):
        for char in syllable_structure:
            if char == 'C':
                name.append(weighted_choice(consonant_weights))
            elif char == 'V':
                name.append(weighted_choice(vowel_weights))
    return ''.join(name).capitalize()

# Adjust weights based on feedback
def adjust_weights(name, rating, is_vowel=True):
    weights = vowel_weights if is_vowel else consonant_weights
    for char in name.lower():
        if char in weights:
            # Adjust weight: higher rating increases weight, lower rating decreases it
            weights[char] += 0.01 * rating
    normalize_weights(weights)

# Normalize weights to ensure they sum to 1
def normalize_weights(weights):
    total = sum(weights.values())
    for key in weights:
        weights[key] /= total

# Rate names and adjust weights
def rate_and_adjust(names, ratings):
    for name, rating in zip(names, ratings):
        for char in name.lower():
            if char in vowel_weights:
                adjust_weights(char, rating, is_vowel=True)
            elif char in consonant_weights:
                adjust_weights(char, rating, is_vowel=False)

# Generate and rate names
def interactive_name_rating():
    names = [generate_name() for _ in range(3)]
    print("Generated Names:")
    for i, name in enumerate(names):
        print(f"{i + 1}. {name}")
    print("\nRate the names from most realistic (1) to least realistic (3):")
    ratings = [int(input(f"Rating for {name}: ")) for name in names]
    rate_and_adjust(names, [4 - r for r in ratings])  # Convert 1-3 to 3-1
    print("\nWeights updated! Generating new names...\n")

    
    