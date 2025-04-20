from flask import Flask,request,render_template,redirect

app = Flask(__name__)

todos = []

@app.route('/todo', methods=['GET','POST'])
def todo():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todos.append(task)
        return redirect('/todo')
    return render_template('todo.html',todos=todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
