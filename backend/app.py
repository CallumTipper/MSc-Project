from flask import Flask, render_template, json, request
from datetime import datetime
app = Flask(__name__)

time = datetime.now()


question_counter = 1
# y = json.dumps(x) 
ans = [{  
"id": 99999,
"number": "2",
"section": "ii",
"question": "How should this work?",
"answer": False,
"student": 1,
"tutor": False,
"votes": 0
},
{  
"id": 8888888,
"number": "3",
"section": "ii",
"question": "test andwer",
"answer": "this question has been answered",
"student": 1,
"tutor": 5,
"votes": 1

}]

# App routes for basic page loading on navigation

@app.route('/')
def index():
    lnk = ""
    return render_template("index.html", link=lnk)

@app.route('/student')
def student():
    global ans
    
    ans = sorted(ans, key=lambda k: k['section'])
    ans = sorted(ans, key=lambda k: k['number'])
    ans = sorted(ans, key=lambda k: k['votes'], reverse=True)
    return render_template("student.html", ans = ans)

@app.route('/tutor')
def tutor():
    global ans
    
    ans = sorted(ans, key=lambda k: k['section'])
    ans = sorted(ans, key=lambda k: k['number'])
    ans = sorted(ans, key=lambda k: k['votes'], reverse=True)
    return render_template("tutor.html", ans = ans)



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
            "votes": 0
        }

        print(time, "Question Added {}-{}: '{}' ".format(q["number"], q["section"], q["question"])) # For log purposes

        ans.append(q.copy())
        
        ans = sorted(ans, key=lambda k: k['section'])
        ans = sorted(ans, key=lambda k: k['number'])
        ans = sorted(ans, key=lambda k: k['votes'], reverse=True)
        return render_template("question_submitted.html", ans = ans)

    elif postOrigin == "flag":
        q_id = request.form.get("questionId")
        q_id = int(q_id)

        for i in ans:
            if i["id"] == q_id:
                i["votes"] += 1

        print(time, "Question {} Flagged".format(q_id)) # For log purposes

        ans = sorted(ans, key=lambda k: k['section']) 
        ans = sorted(ans, key=lambda k: k['number'])
        ans = sorted(ans, key=lambda k: k['votes'], reverse=True)
        return render_template("student.html", ans = ans)

    else:
        print(333)
        return render_template("student.html", ans = ans)


@app.route('/tutor', methods=['POST'])
def post_a():
    global ans
    answer = request.form.get('answer')
    q_id = request.form.get('id')
    q_id = int(q_id)

    for i in ans:
        if i['id'] == q_id:
            i['answer'] = answer
    
    print(time, "Question {} Answered with '{}'".format(q_id, answer)) # For log purposes
    
    ans = sorted(ans, key=lambda k: k['section'])
    ans = sorted(ans, key=lambda k: k['number'])
    ans = sorted(ans, key=lambda k: k['votes'], reverse=True)
    return render_template('tutor.html', ans = ans)


#  Run app
if __name__ == "__main__":
    app.run()