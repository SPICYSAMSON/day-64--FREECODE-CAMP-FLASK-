from flask import Flask, render_template, jsonify
from db import load_jobs_from_db, load_specificjob_from_db


app = Flask(__name__)

@app.route("/")
def hello_tres():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=jobs, 
                           company_name = "Spicysamson")

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
    specific_job = load_specificjob_from_db(id)         
    if not specific_job:
        return "Not found", 404
    
    return render_template('jobpage.html',
                           specific_job=specific_job)

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
    

