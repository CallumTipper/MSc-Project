from flask import Flask, render_template, json, request
from datetime import datetime


# Global variables
app = Flask(__name__)
time = datetime.now()
question_counter = 1



# Auxilliary functions
def loadData():
    with open('data.txt', 'r') as json_file:
        data = json.load(json_file)
    return data

def writeData(data):
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

def sortQuestions(ans):
    return sorted(ans, key=lambda k: k['flag', reverse=True])

def sortAnswers(answers):
    a = sorted(answers, key=lambda k: k['section'])
    b = sorted(answers, key=lambda k: k['number'])
    return b




# App routes for basic page loading on navigation
@app.route('/')
def index():
    lnk = ""
    return render_template("index.html", link=lnk)

@app.route('/student')
def student():
    ans = loadData()["ans"]
    ans = sortQuestions(ans)
    answers = sortAnswers(ans)
    return render_template("student.html", ans = ans, answers = answers)

@app.route('/tutor')
def tutor():
    ans = loadData()["ans"]
    ans = sortQuestions(ans)
    answers = sortAnswers(ans)
    return render_template("tutor.html", ans = ans, answers = answers)



# App routes for POST Requests
@app.route('/student', methods=['POST'])
def post_q():
    global question_counter
    data = loadData()
    postOrigin = request.form.get("post-origin")

    if postOrigin == "post_q":
        unique_id = question_counter + 1
        question_counter += 1
        number = request.form.get('number')
        section = request.form.get('section')
        question = request.form.get('question')
        answer = False
        student = request.form.get('student')
        tutor = False

        q = {
            "id": unique_id,
            "number": number,
            "section": section,
            "question": question,
            "answer": answer,
            "student": student,
            "tutor": tutor,
            "flag": 0,
            "like": 0,
            "query": 0
        }

        print(time, "Question Added {}-{}: '{}' ".format(q["number"], q["section"], q["question"])) # For log purposes
        
        data["ans"].append(q)
        writeData(data)
        ans = loadData()["ans"]

        ans = sortQuestions(ans)
        answers = sortAnswers(ans)
        return render_template("question_submitted.html", ans = ans, answers = answers)

    elif postOrigin == "flag":
        q_id = int(request.form.get("questionId"))

        ans = data["ans"]
        for i in ans:
            if i["id"] == q_id:
                i["flag"] += 1
        data["ans"] = ans
        writeData(data)

        print(time, "Question {} Flagged".format(q_id)) # For log purposes

        ans = sortQuestions(ans)
        answers = sortAnswers(ans)
        return render_template("student.html", ans = ans, answers = answers)

    elif postOrigin == "like":
        q_id = int(request.form.get("questionId"))

        ans = data["ans"]
        for i in ans:
            if i["id"] == q_id:
                i["like"] += 1
        data["ans"] = ans
        writeData(data)
        
        print(time, "Answer {} Liked".format(q_id)) # For log purposes

        ans = sortQuestions(ans)
        answers = sortAnswers(ans)
        return render_template("student.html", ans = ans, answers = answers)

    elif postOrigin == "query":
        q_id = int(request.form.get("questionId"))

        ans = data["ans"]
        for i in ans:
            if i["id"] == q_id:
                i["query"] += 1
        data["ans"] = ans
        writeData(data)
        
        print(time, "Answer {} Queried".format(q_id)) # For log purposes

        ans = sortQuestions(ans)
        answers = sortAnswers(ans)
        return render_template("student.html", ans = ans, answers = answers)


@app.route('/tutor', methods=['POST'])
def post_a():
    data = loadData()
    answer = request.form.get('answer')
    tutor = request.form.get('tutor')
    q_id = int(request.form.get('id'))
    
    ans = data["ans"]
    for i in ans:
        if i['id'] == q_id:
            i['answer'] = answer
            i['tutor'] = tutor
    data["ans"] = ans
    writeData(data)
    
    print(time, "Question {} Answered with '{}' by {}".format(q_id, answer, tutor)) # For log purposes

    ans = sortQuestions(ans)
    answers = sortAnswers(ans)
    return render_template('tutor.html', ans = ans, answers = answers)



#  Run app
if __name__ == "__main__":
    app.run()