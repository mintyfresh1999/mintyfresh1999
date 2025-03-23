import json
import numpy as np
from collections import Counter
import re

# Load primary survey data
with open('survey_data.json', 'r') as f:
    primary_data = json.load(f)

# Load secondary survey data
with open('survey_2.json', 'r') as f:
    secondary_data = json.load(f)

# Open output file
with open('first_eval_results.txt', 'w') as output_file:
    def write_and_print(text):
        """Write to file and print to console."""
        print(text)
        output_file.write(text + '\n')


    def extract_number(answer):
        """Pull out numeric ratings from responses."""
        if isinstance(answer, (int, float)):
            return int(answer)
        elif isinstance(answer, str):
            numbers = re.findall(r'\d+', answer)
            return int(numbers[0]) if numbers else None
        return None


    def analyze_numeric(question, answers):
        """Calculate stats for numeric questions."""
        write_and_print(f"\nQuestion: {question}\n")
        numeric_answers = [extract_number(a) for a in answers if extract_number(a) is not None]

        counts = Counter(numeric_answers)
        total = len(numeric_answers)
        write_and_print("Frequencies:")
        for val, count in sorted(counts.items()):
            write_and_print(f"  {val}: {count} ({count / total * 100:.1f}%)")

        if numeric_answers:
            arr = np.array(numeric_answers)
            write_and_print("\nStats:")
            write_and_print(f"  Mean: {arr.mean():.2f}")
            write_and_print(f"  Median: {np.median(arr):.2f}")
            write_and_print(f"  Std Dev: {arr.std():.2f}")

        write_and_print("\n" + "-" * 50)


    def analyze_yes_no(question, answers):
        """Analyze Yes/No responses."""
        write_and_print(f"\nQuestion: {question}\n")
        counts = Counter(answers)
        total = sum(counts.values())
        write_and_print("Frequencies:")
        for resp, count in counts.items():
            write_and_print(f"  {resp}: {count} ({count / total * 100:.1f}%)")
        write_and_print("\n" + "-" * 50)


    def analyze_preferences(question, answers):
        """Count prototype preferences and list reasons."""
        write_and_print(f"\nQuestion: {question}\n")
        valid_answers = [a for a in answers if a not in ["N/A", "Filled out in the linked Google Forms"]]
        pref_counts = Counter(re.findall(r'\b[1-3]\b', " ".join(valid_answers)))

        total = sum(pref_counts.values())
        write_and_print("Preferences:")
        for pref, count in pref_counts.items():
            write_and_print(f"  Prototype {pref}: {count} ({count / total * 100:.1f}%)")

        write_and_print("\nManual Qualitative Analysis Required for 'Why' Responses:")
        write_and_print("  - Review responses for common themes (e.g., speed, ease of use).")
        write_and_print("\n" + "-" * 50)


    # Primary survey analysis
    questions = [
        "What are your thoughts on directly searching and changing the settings in the drop down menu?",
        "How clearly does the dynamic search interface convey its purpose?",
        "How do you feel about pinned connectivity icons at the top?",
        "Are ‚ÄúRecently Used‚Äù toggles helpful?",
        "How useful would you say this feature in the iOS settings app would be?"
    ]
    for q in questions:
        answers = [entry.get(q) for entry in primary_data]
        analyze_numeric(q, answers)

    # Yes/No question
    yes_no_q = "Does collapsing/expanding categories help you find things more easily?"
    yes_no_answers = [entry.get(yes_no_q) for entry in primary_data]
    analyze_yes_no(yes_no_q, yes_no_answers)

    # Secondary survey preferences
    pref_q = secondary_data[0]["text"]
    pref_answers = secondary_data[0]["answers"]
    analyze_preferences(pref_q, pref_answers)