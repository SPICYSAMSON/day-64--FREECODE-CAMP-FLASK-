from sqlalchemy import create_engine, text
from pprint import pprint
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
db_connection_string = os.getenv("DB_CONNECTION_STRING")

# Replace with your correct database connection string


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




