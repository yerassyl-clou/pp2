import re

def find_sequences(text):
    pattern = r'\b[a-z]+(?:_[a-z]+)*\b'  # Regular expression pattern for sequences of lowercase letters joined with underscores
    matches = re.findall(pattern, text)
    return matches

# Test string
text = ""

# Find sequences
sequences = find_sequences(text)

# Print the found sequences
if sequences:
    print("Sequences found:")
    for seq in sequences:
        print(seq)
else:
    print("No sequences found")
