from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    try:
        # Intentar la conexión
        conn = mysql.connector.connect(
            host='mysql',  # El nombre del host del contenedor
            user='root',    #contrase puesta de docker-compose.yml
            password='root',
            database='db'
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        students = []
        print(f"Error: {e}")
    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
