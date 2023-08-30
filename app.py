from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[
    {
        'id': 1,
        'title': "Data Analyst",
        'location': "Manila, Philippines",
        'salary': "50,000 pesos"
    },
    {
        'id': 2,
        'title': "Data Scientist",
        'location': "Cebu, Philippines",
        'salary': "70,000 pesos"
    },
    {
        'id': 3,
        'title': "Frontend Engineer",
        'location': "Remote",
    },
    {
        'id': 4,
        'title': "Backend Engineer",
        'location': "LA, Albay",
        'salary': "80,000 pesos"
    },
]


@app.route("/")
def hello_tres():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name = "TRES")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)