from flask import Flask, render_template, jsonify
from db import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def hello_tres():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs, 
                           company_name = "Spicysamson")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(load_jobs_from_db())


if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
    

