from flask import Flask, render_template, jsonify, request
from db import load_jobs_from_db, load_specificjob_from_db, add_application_to_db


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
    
@app.route('/job/<id>/apply', methods = ['post'])
def apply_to_job(id):
    data = request.form
    job = load_specificjob_from_db(id)   #$ahhhh okay db call to get the current job (kung sain siya nag apply)
    #store in db
    #send an email
    #display an acknowledgement
    add_application_to_db(id,data)
    return render_template("application_submitted.html", 
                           application_data = data, specific_job = job)

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
    

