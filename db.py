from sqlalchemy import create_engine, text

# Replace with your correct database connection string
db_connection_string = "mysql+pymysql://root:HAKDUGERZ69@127.0.0.1:3306/trescareers?charset=utf8mb4"

# Create a database engine
engine = create_engine(db_connection_string)

try:
    # Connect to the database
    with engine.connect() as conn:
        # Execute a SQL query to select all records from the "jobs" table
        result = conn.execute(text("SELECT * FROM jobs"))
        
        # Fetch and print the query results
        for row in result:
            print(row)
except Exception as e:
    # Handle any exceptions that may occur during the database interaction
    print("An error occurred:", e)




