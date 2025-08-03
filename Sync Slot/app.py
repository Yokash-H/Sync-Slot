from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Update with your DB credentials
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="syncfree"
)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    reg_number = request.form['reg_number']
    slot_string = request.form['slot_preference']
    slots = slot_string.split(',')

    cursor = db.cursor()

    cursor.execute("INSERT INTO students (name, reg_number, slot_preference) VALUES (%s, %s, %s)",
                   (name, reg_number, slot_string))
    db.commit()

    free_people = []
    for slot in slots:
        cursor.execute("SELECT name, reg_number FROM students WHERE slot_preference LIKE %s", (f"%{slot}%",))
        for row in cursor.fetchall():
            free_people.append({"name": row[0], "reg_number": row[1], "slot": slot})

    return render_template('form.html', free_people=free_people, selected_slots=slots)

if __name__ == '__main__':
    app.run(debug=True)
