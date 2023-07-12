import os
from flask import Flask, render_template, url_for, json

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

@app.route('/')
def overview():
    return render_template('overview.html')


@app.route('/trends/<int:trendid>')
def trends(trendid):

    pain_json = ""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "pain_data.json")
    data = json.load(open(json_url))
    print(data)

    return render_template('trends.html', data=data, trendid=trendid)


if __name__ == '__main__':
    app.run()
