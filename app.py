
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("student.html")

@app.route("/student", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]
    student_class = request.form["class"]
    rollno = request.form["rollno"]
    

    db =pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="students",
        port=3306
    )
    cursor = db.cursor()
    sql = "INSERT INTO info (name, email, class, rollno) VALUES (%s, %s, %s, %s)"
    values=(name,email,student_class,rollno)

    cursor.execute(sql,values)
    db.commit()
    cursor.close()
    db.close()
    return "student information saved successfully"

   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

