from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r'C:\Users\navna\OneDrive\Documents\Group_Project')
db_name = "my_database.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    movies = cursor.execute("SELECT * FROM movies_data limit 15").fetchall()
    con.close()

    return render_template("data_table.html", movies=movies)

if __name__=="__main__":
    app.run(debug=True)
