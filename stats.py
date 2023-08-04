import scipy.stats as stats
import pandas as pd
# import statsmodels.api as sm
import statsmodels.formula.api as smf
import json
from sklearn.linear_model import LinearRegression


def ttest(data_group1, data_group2):
    return stats.ttest_ind(a=data_group1, b=data_group2, equal_var=True)


def mixedmodel(dataset):
    dataset_string = json.dumps(dataset)
    df = pd.read_json(dataset_string, orient="records")

    df_treatmentA = df.loc[df['treatment'] == 'A']
    df_treatmentB = df.loc[df['treatment'] == 'B']

    x_a = df_treatmentA["id"].to_numpy().reshape((-1, 1))
    y_a = df_treatmentA["value"].to_numpy()
    model_a = LinearRegression(fit_intercept=True).fit(x_a, y_a)
    y_pred_a = model_a.predict([[20]])

    x_b = df_treatmentB["id"].to_numpy().reshape((-1, 1))
    y_b = df_treatmentB["value"].to_numpy()
    model_b = LinearRegression(fit_intercept=True).fit(x_b, y_b)
    y_pred_b = model_b.predict([[20]])

    md = smf.mixedlm("value ~ id", df, groups=df["treatment"])
    mdf = md.fit(method=["powell", "lbfgs"])  # currently not in use

    return y_pred_a[0], y_pred_b[0]


def linearregression(dataset):
    dataset_string = json.dumps(dataset)
    df = pd.read_json(dataset_string, orient="records")

    x = df["id"].to_numpy().reshape((-1, 1))
    y = df["value"].to_numpy()

    model = LinearRegression(fit_intercept=True).fit(x, y)

    y_pred_1 = model.predict([[20]])
    y_pred_2 = model.predict([[21]])
    y_pred_3 = model.predict([[22]])

    return model.score(x, y), model.intercept_, model.coef_, y_pred_1[0], y_pred_2[0], y_pred_3[0]


def avg_per_treatment(dataset):
    dataset_string = json.dumps(dataset)
    df = pd.read_json(dataset_string, orient="records")

    df_A = df[df["treatment"] == "A"]
    df_B = df[df["treatment"] == "B"]

    return df_A["value"].mean(), df_B["value"].mean()
