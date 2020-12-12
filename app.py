from flask import Flask, render_template,request, redirect,url_for
app = Flask(__name__)
import data

liste = data.data()

@app.route('/')
@app.route('/home')
def home():
    return render_template('news.html', news = liste)

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        data = list()
        searched = request.form.get('search')
        for i in liste:
            if searched in i[1]:
                data.append(i)
        return render_template('search.html',searched = searched, data = data)
    else:
        return redirect('/')



@app.route('/detail/<string:id>')
def detail(id):
    data = list()
    for i in liste:
        if i[0] == int(id):
            data = i
    return render_template('detail.html', data = data)

if __name__ == '__main__':
    app.run(debug = True)