from sqlalchemy import create_engine, text
from pprint import pprint
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
db_connection_string = os.getenv("DB_CONNECTION_STRING")

# Create a database engine
engine = create_engine(db_connection_string)


def load_jobs_from_db():
    try:
        # Connect to the database
        with engine.connect() as conn:
            # Execute a SQL query to select all records from the "jobs" table
            result = conn.execute(text("SELECT * FROM jobs"))
            
            jobs = []
            for row in result.all():
                jobs.append(row._asdict())
            
            return jobs
            
            # Fetch and print the query results
            # print("type(result): ", type(result))
            # result_all = result.all()
            # print("type(result.all()): ", type(result_all))
            # first_result=result_all[0]
            # print("type(first_result): ", type(first_result))
            
            # print("\n")
            # first_result_dict = first_result._asdict()
            # print("type(first_result_dict): ", type(first_result_dict))
            # print(first_result_dict)
            
    except Exception as e:
        # Handle any exceptions that may occur during the database interaction
        print("An error occurred:", e)
        

def load_specificjob_from_db(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE id = :val")
        result = conn.execute(query, 
                              {'val': id})
        row = result.first()
        if row is None:
            return None
        else:
            return row._asdict()

        

def add_application_to_db(job_id, application):
    try:
        with engine.connect() as conn:
            query = text(
                "INSERT INTO applications (job_id, full_name, email, linked_in_url, education, work_experience, resume_url)"
                "VALUES (:job_id, :full_name, :email, :linked_in_url, :education, :work_experience, :resume_url)"
            )
            conn.execute(
                query,
                {
                    'job_id': job_id,
                    'full_name': application['full_name'],
                    'email': application['email'],
                    'linked_in_url': application['linkedin_email'],
                    'education': application['education'],
                    'work_experience': application['work_exp'],
                    'resume_url': application['resume_url']
                }
            )
            # Commit the transaction to save changes to the database
            conn.commit()
    except Exception as e:
        # Log any exceptions that occur
        print(f"Error inserting data: {str(e)}")






