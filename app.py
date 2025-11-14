import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

# Page configuration
st.set_page_config(
    page_title="CARE Journal Likert Survey - CHVs",
    page_icon="📋",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .survey-section {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stRadio > label {
        font-weight: 500;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Display logo and header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    st.markdown("""
        <div class="main-header">
            <h1>THE CARE JOURNAL LIKERT-SCALE SURVEY</h1>
            <h3>To be answered by Community Health Visitor</h3>
        </div>
    """, unsafe_allow_html=True)

# Introduction text
st.markdown("""
Thank you for taking part. This brief survey seeks to understand your experiences and reflections 
in supporting caregivers through the Anchor Programme. Your responses will help us improve reflective 
tools and supports for Community Health Visitors.

**This survey takes about 3-5 minutes to complete.** All responses will remain confidential and used 
only for programme's evaluation and improvement.

Please create a simple unique code (e.g., first letter of your birth month, last letter of your name 
and favourite two-digit number, "MN30") so your pre- and post- responses can be matched anonymously.
""")

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Survey type selection
st.markdown("---")
survey_type = st.radio(
    "**Select Survey Type:**",
    ["Pre-Care Journal Survey", "Post-Care Journal Survey"],
    horizontal=True
)

# Unique code and date
col1, col2 = st.columns(2)
with col1:
    unique_code = st.text_input(
        "**Unique Code:**",
        placeholder="e.g., MN30",
        help="Create a simple unique code to match your pre- and post- responses anonymously"
    )
with col2:
    survey_date = st.date_input("**Date:**", datetime.now())

st.markdown("---")

# Likert scale reference
st.markdown("""
### Rating Scale
| Strongly Disagree | Disagree | Neutral | Agree | Strongly Agree |
|-------------------|----------|---------|-------|----------------|
| 1 | 2 | 3 | 4 | 5 |
""")

# Pre-survey questions
pre_survey_questions = [
    "I feel confident facilitating reflective discussions with caregivers.",
    "I am comfortable helping caregivers explore their emotions.",
    "I regularly reflect on my own emotional responses to my work.",
    "I have strategies to manage secondary stress or fatigue.",
    "I feel supported by my team in practicing trauma-informed care.",
    "I believe a caregiver journal could support reflective work with families.",
    "I feel that reflective practice benefits both caregivers and practitioners."
]

# Post-survey questions
post_survey_questions = [
    "The journal supported caregivers' reflection and emotional awareness.",
    "It helped structured or deepen my reflective discussions with caregivers.",
    "Most caregivers were open to using the journal.",
    "Using the journal did not significantly add to my workload.",
    "The journal helped me stay attuned and reflective during visits.",
    "I observed improvements in caregiver-child interactions over time.",
    "Using the journal enhanced my sense of meaning and satisfaction in my work.",
    "I would continue using the journal with future families.",
    "Supporting caregivers through reflective work sometimes leaves me emotionally drained.",
    "Using the journal reminded me of the importance of caring for my own well-being."
]

# Select questions based on survey type
if survey_type == "Pre-Care Journal Survey":
    questions = pre_survey_questions
    open_question = "What supports or tools currently help you most in facilitating reflection with caregivers?"
else:
    questions = post_survey_questions
    open_question = "One thing that worked well or could be improved about the journal:"

# Display questions
st.markdown("### Survey Questions")
st.markdown("**Please rate the following statements:**")

responses = {}
for i, question in enumerate(questions, 1):
    st.markdown(f"**{i}. {question}**")
    response = st.radio(
        f"Select your response for question {i}:",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x} - {['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'][x-1]}",
        key=f"q{i}",
        horizontal=True,
        label_visibility="collapsed"
    )
    responses[f"Q{i}"] = response
    st.markdown("---")

# Open-ended question
st.markdown(f"### Open-Ended Question")
st.markdown(f"**{open_question}**")
open_response = st.text_area(
    "Your response:",
    height=150,
    key="open_response",
    label_visibility="collapsed"
)

# Submit button
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    submit_button = st.button("Submit Survey", type="primary", use_container_width=True)

# Handle submission
if submit_button:
    if not unique_code:
        st.error("⚠️ Please enter your unique code before submitting.")
    else:
        # Prepare data for saving
        survey_data = {
            "survey_type": survey_type,
            "unique_code": unique_code,
            "date": str(survey_date),
            "submission_timestamp": datetime.now().isoformat(),
            "responses": responses,
            "open_ended_response": open_response
        }
        
        # Save to JSON file
        filename = f"survey_responses_{unique_code}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(survey_data, f, indent=4)
        
        # Also append to a master CSV file
        csv_filename = "all_survey_responses.csv"
        
        # Prepare row for CSV
        csv_row = {
            "Survey_Type": survey_type,
            "Unique_Code": unique_code,
            "Date": str(survey_date),
            "Submission_Timestamp": datetime.now().isoformat(),
            "Open_Ended_Response": open_response
        }
        
        # Add all question responses
        for key, value in responses.items():
            csv_row[key] = value
        
        # Create or append to CSV
        df = pd.DataFrame([csv_row])
        if os.path.exists(csv_filename):
            df.to_csv(csv_filename, mode='a', header=False, index=False)
        else:
            df.to_csv(csv_filename, mode='w', header=True, index=False)
        
        st.success(f"✅ Survey submitted successfully! Your response has been saved as `{filename}`")
        st.balloons()
        
        # Show summary
        with st.expander("View Your Responses Summary"):
            st.json(survey_data)
        
        # Option to download
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="📥 Download Your Response (JSON)",
                data=json.dumps(survey_data, indent=4),
                file_name=filename,
                mime="application/json"
            )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><em>Thank you for your participation in the Anchor Programme evaluation.</em></p>
    <p><small>All responses are confidential and will be used only for programme evaluation and improvement.</small></p>
</div>
""", unsafe_allow_html=True)
