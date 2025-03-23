import json
import numpy as np
from collections import Counter

# Load survey data from x.json
with open('x.json', 'r') as file:
    survey_data = json.load(file)

# Open output file
with open('needfinding_results.txt', 'w') as output_file:
    def write_and_print(text):
        """Write to file and print to console."""
        print(text)
        output_file.write(text + '\n')


    def get_numeric_value(response):
        """Extract the numeric part from answers like '5 (Very Satisfied)'."""
        try:
            return int(response.split()[0])
        except (ValueError, IndexError):
            return None


    def analyze_question(question_text, responses):
        """Analyze responses for a single question and output stats."""
        write_and_print(f"Question: {question_text}\n")

        # Count response frequencies
        response_counts = Counter(responses)
        total_responses = sum(response_counts.values())

        write_and_print("Response Frequencies:")
        for resp, count in response_counts.items():
            percent = (count / total_responses) * 100
            write_and_print(f"  {resp}: {count} responses ({percent:.1f}%)")

        # Handle numeric ratings if present
        numeric_values = [get_numeric_value(r) for r in responses if get_numeric_value(r) is not None]
        if numeric_values:
            num_array = np.array(numeric_values)
            write_and_print("\nNumeric Summary:")
            write_and_print(f"  Mean: {num_array.mean():.2f}")
            write_and_print(f"  Median: {np.median(num_array):.2f}")
            write_and_print(f"  Std Dev: {num_array.std():.2f}")
            write_and_print(f"  Min: {num_array.min()}")
            write_and_print(f"  Max: {num_array.max()}")

        write_and_print("\n" + "-" * 50 + "\n")


    # Process each question in the survey
    for question in survey_data:
        analyze_question(question["text"], question["answers"])