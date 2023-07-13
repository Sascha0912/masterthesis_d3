import os
from flask import Flask, render_template, url_for, json

app = Flask(__name__)

@app.route('/')
def overview():
    return render_template('overview.html')


@app.route('/trends/<int:trendid>')
def trends(trendid):

    pain_json = ""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

    json_url1 = os.path.join(SITE_ROOT, "static/data", "pain_data.json")
    json_url2 = os.path.join(SITE_ROOT, "static/data", "activity_data.json")
    json_url3 = os.path.join(SITE_ROOT, "static/data", "stress_data.json")
    json_url4 = os.path.join(SITE_ROOT, "static/data", "sleep_data.json")

    paindata = json.load(open(json_url1))
    activitydata = json.load(open(json_url2))
    stressdata = json.load(open(json_url3))
    sleepdata = json.load(open(json_url4))

    print(paindata)

    return render_template('trends.html',
                           paindata=paindata,
                           activitydata=activitydata,
                           stressdata=stressdata,
                           sleepdata=sleepdata,
                           trendid=trendid)


@app.route('/details/<int:trendid>')
def details(trendid):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

    json_url1 = os.path.join(SITE_ROOT, "static/data", "pain_data.json")
    json_url2 = os.path.join(SITE_ROOT, "static/data", "activity_data.json")
    json_url3 = os.path.join(SITE_ROOT, "static/data", "stress_data.json")
    json_url4 = os.path.join(SITE_ROOT, "static/data", "sleep_data.json")

    paindata = json.load(open(json_url1))
    activitydata = json.load(open(json_url2))
    stressdata = json.load(open(json_url3))
    sleepdata = json.load(open(json_url4))

    return render_template('details.html',
                           paindata=paindata,
                           activitydata=activitydata,
                           stressdata=stressdata,
                           sleepdata=sleepdata,
                           trendid=trendid)


if __name__ == '__main__':
    app.run()
