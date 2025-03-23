## Hi there 👋

# iOS Settings Redesign Project

This repository contains data and analysis scripts for my CS6750 Individual Project, redesigning the iOS Settings app. Files are organized by appendices in the project PDF.

## Directory Structure

- **Appendix_B**: Needfinding survey data and analysis (Section 3)
  - `x.json`: Raw data (26 responses)
  - `analyze_needfinding.py`: Script for numeric analysis
  - `needfinding_results.txt`: Output file with stats

- **Appendix_G**: First evaluation data and analysis (Section 8)
  - `survey_data.json`: Primary survey data (15 responses)
  - `survey_2.json`: Secondary survey data (20 responses, 16 valid)
  - `analyze_first_evaluation.py`: Script for numeric, Yes/No, and preference analysis
  - `first_eval_results.txt`: Output file with results

- **Appendix_J**: Final evaluation instruments, data, and analysis (Sections 12-13)
  - `finalsurvey.json`: Raw data (15 responses)
  - `analyze_final_evaluation.py`: Script for numeric and qualitative analysis
  - `final_eval_results.txt`: Output file with results

## Usage
- Run scripts with Python 3.x (requires `numpy`).
- Outputs match appendix summaries (e.g., mean 4.67 for Q1 in Appendix J).
- Qualitative analysis requires manual theme identification (see script comments).

## Notes
- Appendix G reports 18 primary responses, but `survey_data.json` has 15 due to incomplete data.
- See the project PDF for detailed context and results.
