from flask import Flask, render_template, request
import fake_news
import graph
import pandas as pd

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        pred_news = fake_news.fake_result(message)
        print(pred_news)
        return render_template('index.html',prediction = pred_news)
    else:
        return render_template('index.html',prediction = "Oops! Something went wrong!")


@app.route('/sub')
def sub():

    case_table = graph.datafilter()
    pred_table = graph.filter()
    return render_template('sub.html', table1=[case_table.to_html(classes='mytab', index = True, header = "true")],table2 = [pred_table.to_html(classes='mytab', index = True, header = True)])


if(__name__) == "__main__":
    app.run(debug=True, port = 2000 )
