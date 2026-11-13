import streamlit as st
import streamlit_hotkeys as hotkeys
import pandas as pd
import random
import time

#-------------------
# Page Configuration
#-------------------
st.set_page_config(
    page_title = "Stroop Effect Experiment",
    page_icon = "🔬",
    layout = "centered"
)

# Keyboard controls for users
hotkeys.activate([
    hotkeys.hk("yes", "f"),
    hotkeys.hk("no", "j"),
])

#-----------------------------
# Experiment Settings (Colors)
#-----------------------------
COLORS = {
    "RED": "#FF0000",
    "BLUE": "#0000FF",
    "GREEN": "#008000",
    "YELLOW": "#D6A500"
}

#---------------
# Session state
#---------------
if "started" not in st.session_state:
    st.session_state.started = False
if "finished" not in st.session_state:
    st.session_state.finished = False
if "trials" not in st.session_state:
    st.session_state.trials = []
if "results" not in st.session_state:
    st.session_state.results = []
if "current_trial" not in st.session_state:
    st.session_state.current_trial = 0
if "trial_start" not in st.session_state:
    st.session_state.trial_start = None

#-------------------------
# Generator Random Trials
#-------------------------
def generate_trials():
    trials = []
    # Put 10 matching trials into trials
    for _ in range(10):
        color = random.choice(list(COLORS.keys()))
        trials.append({
            "word": color,
            "ink": color,
            "condition": "Matching",
            "correct_answer": "f"
        })

    # Put 10 non-matching trials into trials
    for _ in range(10):
        word = random.choice(list(COLORS.keys()))
        possible_inks = [
            color for color in COLORS.keys()
            if color != word
        ]
        ink = random.choice(possible_inks)
        trials.append({
            "word": word,
            "ink": ink,
            "condition": "Non-matching",
            "correct_answer": "j"
        })

    # Shuffle trials to randomize it
    random.shuffle(trials)
    return trials

#----------------
# Answer tracker
#----------------
def record_answer(answer):
    trial = st.session_state.trials[
        st.session_state.current_trial
    ]
    end_time = time.perf_counter()
    reaction_time = (
        end_time - st.session_state.trial_start
    )

    correct = answer == trial["correct_answer"]

    st.session_state.results.append({
        "Trial": st.session_state.current_trial + 1,
        "Condition": trial["condition"],
        "Word": trial["word"],
        "Ink Color": trial["ink"],
        "Response": answer.upper(),
        "Seconds": round(reaction_time, 3),
        "Correct": "Y" if correct else "N"
    })

    st.session_state.current_trial += 1

    if st.session_state.current_trial >= 20:
        st.session_state.finished = True
        st.session_state.started = False
    else:
        # Start the timer for the next trial
        st.session_state.trial_start = time.perf_counter()

#---------------------
# Introduction Screen
#---------------------
st.title("🔬 Stroop Effect Experiment")

if not st.session_state.started and not st.session_state.finished:
    st.write("""
        Welcome to the Stroop Effect experiment!

        You will see a series of color words displayed in different ink colors.

        Your job is to read the color in your head before
        determining whether the word matches the color of the ink!
    """)

    st.subheader("Instructions")

    st.markdown("""
        - Press **F** if the word matches the ink color.
        - Press **J** if the word does NOT match the ink color.
        - Respond as quickly and accurately as possible.
        - There will be 20 trials.
    """)

    st.info(
        """
        Example: BLUE written in blue ink - F (for word matches the ink color) \n
        BLUE written in red ink - J (for word that does NOT matches the ink color) \n
        PLEASE MAKE SURE TO READ THE COLOR FIRST BEFORE YOU INPUT F or J!
        """
    )

    if st.button("Start Experiment", type = "primary"):
        st.session_state.trials = generate_trials()
        st.session_state.results = []
        st.session_state.current_trial = 0
        st.session_state.finished = False
        st.session_state.started = True
        st.session_state.trial_start = time.perf_counter()
        st.rerun()

#-------------------
# Experiment Screen
#-------------------
if st.session_state.started:
    trial_number = st.session_state.current_trial
    trial = st.session_state.trials[trial_number]
    st.progress(trial_number / 20)

    st.subheader(
        f"Trial {trial_number + 1} of 20"
    )

    st.markdown(
        f"""
        <div style = "
            text-align:center;
            font-size:70px;
            font-weight:bold;
            color:{COLORS[trial['ink']]};
            padding:60px 0px;
        ">
            {trial['word']}
        </div>
        """,
        unsafe_allow_html = True
    )

    st.markdown(
        "<h3 style = 'text-align: center'>"
        "READ the color. Does the word match the ink color?"
        "</h3>",
        unsafe_allow_html = True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.button(
            "F - YES",
            disabled = True,
            use_container_width = True
        )
    with col2:
        st.button(
            "J - NO",
            disabled = True,
            use_container_width = True
        )

    st.caption(
        "Use your physical keyboard to answer."
    )

    # Read User's keyboard input
    if hotkeys.pressed("yes"):
        record_answer("f")
        st.rerun()
    elif hotkeys.pressed("no"):
        record_answer("j")
        st.rerun()

#--------------
# Result Screen
#--------------
if st.session_state.finished:
    st.success("Experiment completed! Thank you so much for time! All data is anonymous.")
    st.header("Your Results")
    df = pd.DataFrame(st.session_state.results)

    #Full trial table
    st.subheader("Individual Trial Results")
    st.dataframe(
        df,
        use_container_width = True,
        hide_index = True
    )
    # Separate matching and non-matchin results
    matching = df[
        df["Condition"] == "Matching"
    ]
    non_matching = df[
        df["Condition"] == "Non-matching"
    ]

    def calculate_stats(data):
        average_speed = data["Seconds"].mean()
        accuracy = ((data["Correct"] == "Y").sum() / len(data)) * 100
        return average_speed, accuracy

    matching_speed, matching_accuracy = calculate_stats(matching)
    nonmatching_speed, nonmatching_accuracy = calculate_stats(non_matching)

    # Summary Table
    summary = pd.DataFrame([
        {
            "Condition": "Matching",
            "Average Time (seconds)": round(matching_speed, 3),
            "Accuracy (%)": round(matching_accuracy, 1)
        },
        {
            "Condition": "Non-matching",
            "Average Time (seconds)": round(nonmatching_speed, 3),
            "Accuracy (%)": round(nonmatching_accuracy, 1)
        }
    ])
    st.table(summary)

    # Download results
    st.download_button(
        label="Download Results as CSV",
        data=df.to_csv(index=False),
        file_name="stroop_results.csv",
        mime="text/csv"
    )
    st.divider()

    # Google Docs submission link
    st.subheader("Submit Your Results")

    st.write(
        "https://docs.google.com/forms/d/e/1FAIpQLSeS5SqYjlZddqEslvT1Wo9GXhSsTlXDCho6-o91OrFf9g6gKQ/viewform?usp=dialog"
    )

    st.link_button(
        "Open Google Docs Submission",
        "https://docs.google.com/forms/d/e/1FAIpQLSeS5SqYjlZddqEslvT1Wo9GXhSsTlXDCho6-o91OrFf9g6gKQ/viewform?usp=dialog"
    )

    if st.button("Restart Experiment"):
        for key in [
            "started",
            "finished",
            "trials",
            "results",
            "current_trial",
            "trial_start"
        ]:
            del st.session_state[key]

        st.rerun()