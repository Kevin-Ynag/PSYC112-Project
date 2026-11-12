# 🔬 Stroop Effect Experiment

An interactive, web-based cognitive psychology experiment developed using Python and Streamlit to investigate how mental interference affects processing speed and reaction time.

## 📚 About the Project

This project was developed for **PSYC112** course.

The experiment investigates the Stroop Effect, a psychological phenomenon in which conflicting information can interfere with cognitive processing and affect reaction time.

Participants are presented with color words displayed in different ink colors and must determine whether the word matches the ink color.

The experiment uses four colors:

- 🔴 Red
- 🔵 Blue
- 🟢 Green
- 🟡 Yellow

## 🧪 Experiment Methodology

Unlike the original method, which separates participants into two independent groups, this experiment allows each participant to complete both experimental conditions.

Each participant completes **20 randomized trials**:

### 1. Matching Condition

The color word and the ink color are the same.

Example:
- BLUE displayed in blue ink.
- RED displayed in red ink.

### 2. Non-Matching Condition

The color word and the ink color are different.

Example:
- BLUE displayed in red ink.
- GREEN displayed in yellow ink.

Each participant completes:
- 10 matching trials.
- 10 non-matching trials.

The trials are shuffled to randomize their presentation.

## ⌨️ Participant Instructions

Participants must determine whether the color word matches the ink color.

| Keyboard Input | Response |
|---|---|
| F | Yes – The word matches the ink color |
| J | No – The word does not match the ink color |

Participants are instructed to respond as quickly and accurately as possible.

## 📊 Data Collection and Results

The application automatically records the following information for each trial:

- Trial number
- Experimental condition
- Color word
- Ink color
- Participant response
- Reaction time (seconds)
- Response accuracy

After completing all 20 trials, participants can view their individual results.

The application also calculates:

- Average reaction time for matching trials.
- Average reaction time for non-matching trials.
- Accuracy percentage for matching trials.
- Accuracy percentage for non-matching trials.

Participants can download their individual experimental results as a CSV file for submission and further analysis.

## 🛠️ Technologies and Libraries Used

This experiment was developed using Python and the following libraries and modules:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Creates the interactive web application and participant interface |
| Pandas | Organizes experimental data, calculates averages, and exports CSV files |
| Random | Generates and shuffles randomized experimental trials |
| Time | Measures participants' reaction times using `time.perf_counter()` |
| Streamlit Hotkeys | Captures keyboard responses using the F and J keys |

## 💻 Installation and Setup

### Prerequisites

- Python 3.9 or later.
- pip (Python package installer).

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd stroop-effect-experiment
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your default web browser.

## 📁 Project Structure

```text
stroop-effect-experiment/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎯 Research Question

**How does mental interference affect processing speed?**

The experiment aims to investigate whether participants take longer to respond to non-matching color-word combinations compared to matching combinations.

The collected results will be used to compare average reaction times and accuracy across both experimental conditions.

## 👥 Participants and Data Submission

Each participant completes both experimental conditions independently.

After completing the experiment, participants download their individual results as a CSV file and submit their data through the designated Google Docs submission link.

The collected participant data will be used for the overall analysis of the Stroop Effect.

---

**Course:** PSYC112
**Project:** Stroop Effect Experiment  
**Programming Language:** Python  
**Framework:** Streamlit
