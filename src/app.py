from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection, init_db

app = Flask(__name__)

# Table ensure karne ke liye
init_db()

# 1. READ: Sabhi students ki list dikhana
@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('index.html', students=students)

# 2. CREATE: Naya student record add karna
@app.route('/add', methods=['POST'])
def add_student():
    roll_no = request.form['roll_no']
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    phone = request.form['phone']

    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO students (roll_no, name, email, course, phone) VALUES (?, ?, ?, ?, ?)',
                     (roll_no, name, email, course, phone))
        conn.commit()
    except Exception as e:
        print(f"Error adding student: {e}")
    finally:
        conn.close()
    return redirect(url_for('index'))

# 3. UPDATE: Student details update karna
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    roll_no = request.form['roll_no']
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    phone = request.form['phone']

    conn = get_db_connection()
    conn.execute('UPDATE students SET roll_no = ?, name = ?, email = ?, course = ?, phone = ? WHERE id = ?',
                 (roll_no, name, email, course, phone, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# 4. DELETE: Student record delete karna
@app.route('/delete/<int:id>')
def delete_student(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)