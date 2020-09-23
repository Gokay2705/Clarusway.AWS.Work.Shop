# Import Flask modules
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# Create an object named app
app = Flask(__name__)
# Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./email.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
# Execute the code below only once.
# Write sql code for initializing users table..
drop_table= """
DROP TABLE IF EXISTS users;
"""
users_table = """    
CREATE TABLE users(
username VARCHAR NOT NULL PRIMARY KEY,
email VARCHAR);
"""
data = """
INSERT INTO users
VALUES
    ("Levent Akyuz", "levent.akyuz@gmail.com"),
    ("Mustafa Kanat", "mustafa.kanat@yahoo.com"),
    ("Hakan Sule", "hakan.sule@clarusway.com");
"""
db.session.execute(drop_table)
db.session.execute(users_table)
db.session.execute(data)
db.session.commit()

def find_emails(keyword):
    query=f"""
    SELECT * FROM users WHERE username like '%{keyword}%'
    """
    result = db.session.execute(query)
    user_emails = [(row[0], row[1]) for row in result]
    if not any(user_emails):
        user_emails = [('Not Found', 'Not Found')]
    return user_emails






