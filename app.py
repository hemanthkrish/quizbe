import os
import random
from flask import Flask, jsonify, render_template, request, abort
from questions_data import PREPOSITIONS_DATA, PHRASAL_VERBS_DATA, MM_IDIOMS_DATA, MM_OWS_DATA, generate_all_questions

# Initialize the Flask application
app = Flask(__name__)

# --- Configuration for different quiz topics ---
# This dictionary holds the settings for each quiz type.
TOPICS = {
    "prepositions": {
        "display_name": "Prepositions",
        "data": PREPOSITIONS_DATA,
        "slab_size": 30,
        "questions": [], # Will be populated at startup
    },
    "phrasal_verbs": {
        "display_name": "Phrasal Verbs",
        "data": PHRASAL_VERBS_DATA,
        "slab_size": 35,
        "questions": [], # Will be populated at startup
    },
    "idioms_mm": {
        "display_name": "Idioms-MM",
        "data": MM_IDIOMS_DATA,
        "slab_size": 60,
        "questions": [], # Will be populated at startup
    },
    "ows_mm": {
        "display_name": "Ows-MM",
        "data": MM_OWS_DATA,
        "slab_size": 60,
        "questions": [], # Will be populated at startup
    }
}

# --- Pre-load all questions for all topics on startup ---
def load_all_questions():
    """
    Generates and stores questions for each topic defined in the TOPICS config.
    This is done once at startup for efficiency.
    """
    print("Loading all question sets...")
    for topic_key, config in TOPICS.items():
        try:
            config["questions"] = generate_all_questions(config["data"])
            print(f"- Successfully loaded {len(config['questions'])} questions for '{topic_key}'.")
        except Exception as e:
            print(f"Error loading questions for '{topic_key}': {e}")

load_all_questions()


# --- Route to serve the main HTML page ---
@app.route('/')
def home():
    """
    Renders the main quiz page.
    It passes the topics configuration to the template to build the UI.
    """
    # Create a summary of topics to pass to the template
    topics_summary = {
        key: {
            "display_name": config["display_name"],
            "total_questions": len(config["questions"]),
            "slab_size": config["slab_size"]
        }
        for key, config in TOPICS.items()
    }
    return render_template('index.html', topics=topics_summary)

# --- API endpoint to get a slab of questions for a specific topic ---
@app.route('/api/questions')
def get_questions_slab():
    """
    Provides a 'slab' of questions for a given topic.
    The topic, start, and end indices are provided as query parameters.
    """
    topic = request.args.get('topic', 'prepositions')
    if topic not in TOPICS:
        return jsonify({"error": "Invalid topic requested."}), 400

    try:
        start = int(request.args.get('start', 0))
        end = int(request.args.get('end', TOPICS[topic]["slab_size"]))
    except ValueError:
        return jsonify({"error": "Invalid start/end parameters."}), 400

    all_questions_for_topic = TOPICS[topic]["questions"]
    total_questions = len(all_questions_for_topic)

    if not (0 <= start < end <= total_questions):
        return jsonify({"error": "Invalid question range."}), 400

    # Get the selected slab and shuffle it
    selected_questions = all_questions_for_topic[start:end]
    random.shuffle(selected_questions)
    
    # Renumber the questions for the current slab
    for i, question in enumerate(selected_questions):
        question['numb'] = i + 1

    return jsonify(selected_questions)

# # --- Main entry point for running the application ---
# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

