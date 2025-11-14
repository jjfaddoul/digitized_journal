# CARE Journal Likert Survey - Digitized App

A Streamlit application that digitizes the Anchor Care Journal Likert-Scale Survey for Community Health Visitors.

## Features

- **Pre and Post Survey Support**: Choose between Pre-Care Journal Survey and Post-Care Journal Survey
- **Anonymous Tracking**: Uses unique codes to match pre- and post- responses anonymously
- **Interactive UI**: Clean, user-friendly interface with logo display
- **Data Export**: Responses saved as both JSON and CSV formats
- **Likert Scale**: 5-point scale from Strongly Disagree to Strongly Agree
- **Open-ended Questions**: Includes text areas for qualitative feedback

## Installation

1. Ensure you have Python installed (Python 3.7 or higher)

2. Install required packages:
```bash
pip install streamlit pandas python-docx
```

## Running the App

From the project directory, run:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Usage

1. **Select Survey Type**: Choose Pre-Care or Post-Care Journal Survey
2. **Enter Unique Code**: Create a simple anonymous code (e.g., "MN30")
3. **Select Date**: Choose the survey date
4. **Answer Questions**: Rate each statement using the 5-point Likert scale
5. **Provide Feedback**: Answer the open-ended question
6. **Submit**: Click the submit button to save your responses

## Data Storage

- Individual responses are saved as JSON files: `survey_responses_[CODE]_[TIMESTAMP].json`
- All responses are also compiled in: `all_survey_responses.csv`

## Files Included

- `app.py`: Main Streamlit application
- `logo.png`: Organization logo displayed in the app header
- `Anchor Care Journal Likert Survey_CHVs.docx`: Original survey document

## Survey Questions

### Pre-Care Journal Survey (7 questions)
Focuses on confidence, comfort levels, and beliefs about reflective practice before using the journal.

### Post-Care Journal Survey (10 questions)
Evaluates the effectiveness of the journal, its impact on practice, and practitioner well-being.

## Privacy & Confidentiality

All responses remain confidential and are used only for programme evaluation and improvement. The unique code system ensures anonymity while allowing matching of pre- and post- responses.
