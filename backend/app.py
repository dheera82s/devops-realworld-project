from flask import Flask
import mysql.connector
import os

app = Flask(__name__)


@app.route("/api/health")
def health():
    return "Backend is Healthy"


@app.route("/api/db-test")
def db_test():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "mysql"),
            user=os.getenv("MYSQL_USER", "appuser"),
            password=os.getenv("MYSQL_PASSWORD", "apppassword"),
            database=os.getenv("MYSQL_DATABASE", "devopsdb")
        )

        connection.close()

        return "MySQL connection successful"

    except Exception as e:
        return f"MySQL connection failed: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)