from flask import Flask, render_template
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

app = Flask(__name__)

# Database connection
username = "root"
password = quote_plus("razaqsvne@2003")
host = "localhost"
port = "3306"
database = "climate_db"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

@app.route("/")
def index():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM climate_data ORDER BY datetime DESC LIMIT 10")
        )
        rows = result.fetchall()

    return render_template("index.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
