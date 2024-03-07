from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")
    matches = re.findall(regex_pattern, test_string)
    return render_template("results.html", test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route("/validate_email", methods=["POST"])
def validate_email():
    email = request.form.get("email")
    regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = re.match(regex_pattern, email) is not None
    return render_template("validate_email.html", email=email, is_valid=is_valid)

if __name__ == "__main__":
    app.run(debug=True)
