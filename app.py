import os
from flask import Flask, render_template, json
from stats import ttest, mixedmodel, linearregression, avg_per_treatment

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

json_url1 = os.path.join(SITE_ROOT, "static/data", "pain_data.json")
json_url2 = os.path.join(SITE_ROOT, "static/data", "activity_data.json")
json_url3 = os.path.join(SITE_ROOT, "static/data", "stress_data.json")
json_url4 = os.path.join(SITE_ROOT, "static/data", "sleep_data.json")

paindata = json.load(open(json_url1))
activitydata = json.load(open(json_url2))
stressdata = json.load(open(json_url3))
sleepdata = json.load(open(json_url4))


@app.route('/')
def overview():
    return render_template('overview.html',
                           paindata=paindata,
                           activitydata=activitydata,
                           stressdata=stressdata,
                           sleepdata=sleepdata)


@app.route('/trends/<int:trendid>')
def trends(trendid):
    pain_per_treatment = avg_per_treatment(paindata["data"])
    activity_per_treatment = avg_per_treatment(activitydata["data"])
    stress_per_treatment = avg_per_treatment(stressdata["data"])
    sleep_per_treatment = avg_per_treatment(sleepdata["data"])

    return render_template('trends.html',
                           paindata=paindata,
                           activitydata=activitydata,
                           stressdata=stressdata,
                           sleepdata=sleepdata,
                           pain_per_treatment=pain_per_treatment,
                           activity_per_treatment=activity_per_treatment,
                           stress_per_treatment=stress_per_treatment,
                           sleep_per_treatment=sleep_per_treatment,
                           trendid=trendid)


@app.route('/details/<int:trendid>')
def details(trendid):
    if trendid == 1:
        my_data_arr = [d["value"] for d in activitydata["data"]]
        avg_data_arr = [d["avg"] for d in activitydata["data"]]
        lmm_res = mixedmodel(activitydata["data"])
        lin_res = linearregression(activitydata["data"])
    elif trendid == 2:
        my_data_arr = [d["value"] for d in paindata["data"]]
        avg_data_arr = [d["avg"] for d in paindata["data"]]
        lmm_res = mixedmodel(paindata["data"])
        lin_res = linearregression(paindata["data"])
    elif trendid == 3:
        my_data_arr = [d["value"] for d in stressdata["data"]]
        avg_data_arr = [d["avg"] for d in stressdata["data"]]
        lmm_res = mixedmodel(stressdata["data"])
        lin_res = linearregression(stressdata["data"])
    elif trendid == 4:
        my_data_arr = [d["value"] for d in sleepdata["data"]]
        avg_data_arr = [d["avg"] for d in sleepdata["data"]]
        lmm_res = mixedmodel(sleepdata["data"])
        lin_res = linearregression(sleepdata["data"])
    else:
        my_data_arr = [d["value"] for d in paindata["data"]]  # default case
        avg_data_arr = [d["avg"] for d in paindata["data"]]
        lmm_res = mixedmodel(paindata["data"])
        lin_res = linearregression(paindata["data"])

    ttest_res = ttest(my_data_arr, avg_data_arr)

    return render_template('details.html',
                           paindata=paindata,
                           activitydata=activitydata,
                           stressdata=stressdata,
                           sleepdata=sleepdata,
                           pvalue=ttest_res[1],
                           lin_pred_1=lin_res[3],
                           lmm_pred_a=lmm_res[0],
                           lmm_pred_b=lmm_res[1],
                           trendid=trendid)


@app.route('/info/<int:trendid>')
def info(trendid):
    return render_template('info.html',
                           paindata=paindata,
                           activitydata=activitydata,
                           stressdata=stressdata,
                           sleepdata=sleepdata,
                           trendid=trendid)


if __name__ == '__main__':
    app.run()
