import sqlite3
from flask import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Task4_1_xy.html")

@app.route('/round1', methods=['POST'])
def round1():
    conn = sqlite3.connect("Task4.db")
    round1 = conn.execute("SELECT competitor.name, scores.score FROM competitor, scores WHERE scores.id = competitor.id and scores.round = ? ORDER BY scores.score DESC",(1,)).fetchall()
    conn.close()
    return render_template("Task4_2_xy_1.html", round1 = round1)

@app.route('/round2', methods=['POST'])
def round2() :
    conn = sqlite3.connect("Task4.db")
    round2 = conn.execute("SELECT competitor.name, scores.score FROM competitor, scores WHERE scores.id = competitor.id and scores.round = ? ORDER BY scores.score DESC",(2,)).fetchall()
    conn.close()
    return render_template("Task4_2_xy_2.html", round2 = round2)

@app.route('/round3', methods=['POST'])
def round3():
    conn = sqlite3.connect("Task4.db")
    round3 = conn.execute("SELECT competitor.name, scores.score FROM competitor, scores WHERE scores.id = competitor.id and scores.round = ? ORDER BY scores.score DESC",(3,)).fetchall()
    conn.close()
    return render_template("Task4_2_xy_3.html", round3 = round3)

@app.route('/mean', methods=['POST'])
def mean():
    conn = sqlite3.connect("Task4.db")
    data = conn.execute("SELECT competitor.id, competitor.name, scores.score, scores.round FROM competitor, scores WHERE scores.id = competitor.id ORDER BY competitor.id ASC").fetchall()
    conn.close()
    person = []
    people = []
    count = 0
    result = 0
    for i in range(len(data)):
        if data[i][0] == data[i - 1][0]:
            count += 1
            result += data[i][2]
        elif i == 0 :
            result = data[i][2]
            count = 1
        else:
            person.append(data[i - 1][1])
            person.append(round(result / count, 2))
            people.append(person)
            person = []
            result = data[i][2]
            count = 1
    while True:
        swap = False
        for i in range(len(people)):
            if i == len(people) - 1:
                continue
            elif people[i][-1] < people[i + 1][-1]:
                people[i],people[i+1] = people[i+1],people[i]
                swap = True
        if swap == False:
            break
    return render_template("Task4_3_xy.html", people = people)

@app.route('/qualifiers', methods=['POST'])
def qualifiers():
    conn = sqlite3.connect("Task4.db")
    data = conn.execute("SELECT competitor.id, competitor.name, scores.score, scores.round FROM competitor, scores WHERE scores.id = competitor.id ORDER BY competitor.id ASC").fetchall()
    conn.close()
    person = []
    people = []
    result = 0
    for i in range(len(data)):
        if data[i][0] == data[i - 1][0]:
            result += data[i][2]
        elif i == 0 :
            result = data[i][2]
            count = 1
        else:
            person.append(data[i - 1][1])
            person.append(result)
            if result > 250:
                person.append("Qualified for finals")
            else:
                person.append("Not qualified for final round")
            people.append(person)
            person = []
            result = data[i][2]
    while True:
        swap = False
        for i in range(len(people)):
            if i == len(people) - 1:
                continue
            elif people[i][-2] < people[i + 1][-2]:
                people[i],people[i+1] = people[i+1],people[i]
                swap = True
        if swap == False:
            break
    return render_template("Task4_4_xy.html", people = people)

if __name__ == '__main__':
    app.run(debug = True, port = 1256)
