import psycopg


USERNAME = "postgres"
PASSWORD = "17GIGSofcat"
PORT = "5432"


try:
    conn = psycopg.connect(
        f"dbname=A3_students user={USERNAME}"
        f" password={PASSWORD} host=localhost port={PORT}"
    )

except psycopg.OperationalError as e:
    print(f"Error: {e}")
    exit(1)
