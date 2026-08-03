from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("LIBRARY.db")

    result = conn.execute("SELECT Member.FamilyName, Member.GivenName, Book.Title FROM Member, Book, Loan "+
                          "WHERE Member.MemberNumber = Loan.MemberNumber AND Book.BookID = Loan.BookID AND Loan.Returned = ?", ("FALSE",)).fetchall()
    conn.close()

    return render_template("TASK_4_4_xy_25S11.html", result = result)

if __name__ == '__main__':
    app.run(debug = True, port = 2567)
