import json
import numpy as np
from collections import Counter

# Load final survey data
with open('finalsurvey.json', 'r') as f:
    data = json.load(f)

# Open output file
with open('final_eval_results.txt', 'w') as output_file:
    def write_and_print(text):
        """Write to file and print to console."""
        print(text)
        output_file.write(text + '\n')


    def extract_rating(answer):
        """Convert answer to integer if possible."""
        if isinstance(answer, (int, float)):
            return int(answer)
        return None


    def analyze_numeric_question(question, responses):
        """Compute stats for numeric questions."""
        write_and_print(f"\nQuestion: {question}\n")
        ratings = [extract_rating(r) for r in responses if extract_rating(r) is not None]

        counts = Counter(ratings)
        total = len(ratings)
        write_and_print("Frequencies:")
        for rating, count in sorted(counts.items()):
            write_and_print(f"  {rating}: {count} ({count / total * 100:.1f}%)")

        if ratings:
            arr = np.array(ratings)
            write_and_print("\nStats:")
            write_and_print(f"  Mean: {arr.mean():.2f}")
            write_and_print(f"  Median: {np.median(arr):.2f}")
            write_and_print(f"  Std Dev: {arr.std():.2f}")

        write_and_print("\n" + "-" * 50)


    # Define survey questions
    numeric_qs = [
        "The search bar makes finding settings quick and easy.",
        "The pinned settings section is useful for frequent tasks.",
        "Collapsible categories help me focus on relevant settings.",
        "The interface feels intuitive overall."
    ]
    qualitative_qs = [
        "What do you like most about the prototype compared to the current iOS Settings app?",
        "What could be improved in the search, pinned settings, or collapsible categories?",
        "Any other comments or suggestions?"
    ]

    # Analyze numeric questions
    for q in numeric_qs:
        answers = [entry.get(q) for entry in data]
        analyze_numeric_question(q, answers)

    # Placeholder for qualitative analysis
    for q in qualitative_qs:
        write_and_print(f"\nQuestion: {q}\n")
        responses = [entry.get(q) for entry in data if entry.get(q)]
        write_and_print("Responses:")
        for r in responses:
            write_and_print(f"  - {r}")
        write_and_print("\nManual Analysis Needed:")
        write_and_print("  - Identify 3-5 themes (e.g., speed, customization) and count mentions.")
        write_and_print("\n" + "-" * 50)