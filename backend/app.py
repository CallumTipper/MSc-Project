from flask import Flask, render_template, json, request
from datetime import datetime
app = Flask(__name__)

time = datetime.now()
question_counter = 1

ans = [{  
"id": 99999,
"number": "2",
"section": "ii",
"question": "How should this work?",
"answer": False,
"student": 1,
"tutor": False,
"flag": 0,
"like": 0,
"query": 0
},
{  
"id": 8888888,
"number": "3",
"section": "ii",
"question": "test andwer",
"answer": "this question has been answered",
"student": 1,
"tutor": 5,
"flag": 1,
"like": 0,
"query": 0
}]


def sortQuestions(answers):
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
    global ans

    answers = sortQuestions(ans)
    return render_template("student.html", ans = ans, answers = answers)

@app.route('/tutor')
def tutor():
    global ans

    answers = sortQuestions(ans)
    return render_template("tutor.html", ans = ans, answers = answers)



# App routes for POST Requests

@app.route('/student', methods=['POST'])
def post_q():
    global ans
    global question_counter

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

        ans.append(q.copy())

        answers = sortQuestions(ans)
        return render_template("question_submitted.html", ans = ans, answers = answers)

    elif postOrigin == "flag":
        q_id = request.form.get("questionId")
        q_id = int(q_id)

        for i in ans:
            if i["id"] == q_id:
                i["flag"] += 1

        print(time, "Question {} Flagged".format(q_id)) # For log purposes

        answers = sortQuestions(ans)
        return render_template("student.html", ans = ans, answers = answers)

    elif postOrigin == "like":
        q_id = request.form.get("questionId")
        q_id = int(q_id)

        for i in ans:
            if i["id"] == q_id:
                i["like"] += 1
        
        print(time, "Answer {} Liked".format(q_id)) # For log purposes

        answers = sortQuestions(ans)
        return render_template("student.html", ans = ans, answers = answers)

    elif postOrigin == "query":
        q_id = request.form.get("questionId")
        q_id = int(q_id)

        for i in ans:
            if i["id"] == q_id:
                i["query"] += 1
        
        print(time, "Answer {} Queried".format(q_id)) # For log purposes

        answers = sortQuestions(ans)
        return render_template("student.html", ans = ans, answers = answers)


@app.route('/tutor', methods=['POST'])
def post_a():
    global ans
    answer = request.form.get('answer')
    tutor = request.form.get('tutor')
    q_id = request.form.get('id')
    q_id = int(q_id)
    
    for i in ans:
        if i['id'] == q_id:
            i['answer'] = answer
            i['tutor'] = tutor
    
    print(time, "Question {} Answered with '{}' by {}".format(q_id, answer, tutor)) # For log purposes

    answers = sortQuestions(ans)
    return render_template('tutor.html', ans = ans, answers = answers)


#  Run app
if __name__ == "__main__":
    app.run()