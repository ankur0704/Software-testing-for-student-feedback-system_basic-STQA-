# flask Web Application Layer

from flask import Flask, request, jsonify
from models import init_db, add_feedback, get_all_feedback

app = Flask(__name__)
init_db()

@app.route('/') # default home route page
def home():
    return "Welcome to Student Feedback Management System"

@app.route('/add_feedback', methods=['POST'])  # add_feedback route 
def add_feedback_route():
    data = request.get_json()
    result = add_feedback(
        data['student_name'], data['subject'],
        data['rating'], data.get('comments', '')
    )
    return jsonify(result)

@app.route('/feedback', methods=['GET'])  # get all feedback route(GET method)
def get_feedback_route():
    return jsonify(get_all_feedback())

if __name__ == '__main__':
    app.run(debug=True)
