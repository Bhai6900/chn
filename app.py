from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to create the Item table
def create_item_table():
    conn = sqlite3.connect('market.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS item (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            price INTEGER NOT NULL,
            barcode TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Call the function to create the Item table
create_item_table()

# Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('market.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query all items from the database
    cursor.execute('SELECT * FROM item')
    items = cursor.fetchall()

    # Close the connection
    conn.close()

    # Pass data to HTML template and render the page
    return render_template('market.html', items=items)


if __name__ == '__main__':
    app.run( host= '0.0.0.0', debug=True)
