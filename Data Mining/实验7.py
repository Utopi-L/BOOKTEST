# General
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    fbeta_score,
    make_scorer,
    recall_score,
)

# Model
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

plt.style.use("fivethirtyeight")
bmt_train = pd.read_csv("/archive/train.csv", sep=";")
bmt_test = pd.read_csv("/archive/test.csv", sep=";")
bmt_train.head()
bmt_train.info()
bmt_train.describe()
cols_to_category = [
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "poutcome",
]
bmt_train[cols_to_category] = bmt_train[cols_to_category].astype("category")
bmt_train["y"] = np.where(bmt_train["y"] == "no", 0, 1)
bmt_test["y"] = np.where(bmt_test["y"] == "no", 0, 1)
def counts_plot(y_var, col="w", ax=None):
    y_var_counts = (
        bmt_train.loc[:, y_var]
        .value_counts()
        .reset_index()
        .rename(columns={"index": y_var, y_var: "counts"})
        .assign(
            percent=lambda df_: (df_["counts"] / df_["counts"].sum()).round(2) * 100
        )
    )
    sns.set_context("paper")
    ax0 = sns.barplot(
        data=y_var_counts,
        x="percent",
        y=y_var,
        color=col,
        ax=ax,
        order=y_var_counts[y_var],
    )
    values1 = ax0.containers[0].datavalues
    labels = ["{:g}%".format(val) for val in values1]
    ax0.bar_label(ax0.containers[0], labels=labels, fontsize=9, color="#740405")
    ax0.set_ylabel("")
    ax0.set_xlabel("Percent", fontsize=10)
    ax0.set_title(str.title(y_var) + " | proportions ", fontsize=10)
    return
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(11, 6))
counts_plot("job", ax=ax1, col="#009688")
counts_plot("housing", ax=ax2, col="#35a79c")
counts_plot("marital", ax=ax3, col="#54b2a9")
counts_plot("education", ax=ax4, col="#83d0c9")
fig.tight_layout()
plt.show()

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(11, 6))
counts_plot("default", ax=ax1, col="#2e5090")
counts_plot("loan", ax=ax2, col="#5873a6")
counts_plot("contact", ax=ax3, col="#8296bc")
counts_plot("poutcome", ax=ax4, col="#abb9d3")
fig.tight_layout()
plt.show()

(
    bmt_train.loc[:, "y"]
    .value_counts()
    .reset_index()
    .rename(columns={"index": "y", "y": "counts"})
    .assign(percent=lambda df_: (df_["counts"] / df_["counts"].sum()).round(2) * 100)
)

y_var = (
    bmt_train.loc[:, "y"]
    .value_counts()
    .reset_index()
    .rename(columns={"index": "y", "y": "counts"})
    .assign(percent=lambda df_: (df_["counts"] / df_["counts"].sum()).round(2) * 100)
)

target_color = sns.color_palette(["#e42256", "#00b1b0"])

plt.pie(
    x=y_var["percent"],
    labels=["0 | Not subscribed", "1 | subscribed"],
    colors=target_color,
    autopct="%.0f%%",
    shadow=True,
    textprops={"fontsize": 10, "color": "#000000"},
    explode=[0.1, 0],
)
plt.title("Target Variable proportions", fontsize=14)
plt.text(
    x=-0.7,
    y=0.12,
    s="count: " + str(y_var.iloc[0, 1]) + "",
    color="black",
    ha="center",
    va="center",
)
plt.text(
    x=0.6,
    y=-0.31,
    s="count: " + str(y_var.iloc[1, 1]) + "",
    color="black",
    ha="center",
    va="center",
)
plt.show()


Num_feats = bmt_train.select_dtypes("integer").copy()

sample_for_pair_plot = Num_feats.groupby("y", group_keys=False).apply(
    lambda x: x.sample(frac=0.01)
)

sns.pairplot(
    sample_for_pair_plot,
    hue="y",
    kind="scatter",
    diag_kind="kde",
    palette=target_color,
    height=1.5,
    aspect=1,
    plot_kws=dict(s=10),
)
plt.show()
def num_distributions(var_1, var_2):

    age_dur = bmt_train[[var_1, var_2, "y"]]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

    ## HistPlot

    sns.histplot(
        data=age_dur,
        kde=True,
        line_kws={"lw": 1.5, "alpha": 0.6},
        x=var_1,
        bins=20,
        hue="y",
        palette=target_color,
        alpha=0.6,
        ax=ax1,
    )
    ax1.legend(
        title="Subscribed?",
        loc="upper right",
        labels=["YES", "NO"],
        ncol=2,
        frameon=True,
        shadow=True,
        title_fontsize=8,
        prop={"size": 7},
        bbox_to_anchor=(1.18, 1.25),
    )
    ax1.set_xlabel(str.title(var_1), fontsize=10)
    ax1.set_ylabel("Frequency", fontsize=10)
    ax1.set_title(str.title(var_1) + " distributions", fontsize=12)
    ax1.yaxis.set_major_formatter(ticker.EngFormatter())

    ## Ccatter plot

    sns.scatterplot(
        data=age_dur,
        x=var_1,
        y=var_2,
        hue="y",
        ax=ax2,
        palette=target_color,
        legend=False,
        alpha=0.6,
    )
    ax2.yaxis.set_major_formatter(ticker.EngFormatter())
    ax2.set_title(str.title(var_2) + " distributions", fontsize=12)
    ax2.set_ylabel(str.title(var_2), fontsize=10)
    ax2.set_xlabel(str.title(var_1), fontsize=10)

    return
num_distributions("age", "duration")
num_distributions("age", "balance")
num_distributions("balance", "duration")
num_distributions("balance", "campaign")
larg_dur = bmt_train["duration"].nlargest(10)
small_dur = bmt_train["duration"].nsmallest(5)
bmt_train.query("duration in @larg_dur | duration in @small_dur").sort_values(
    by="duration", ascending=False
).style.background_gradient()
(
    bmt_train[["default", "y"]]
    .value_counts()
    .reset_index()
    .rename(columns={0: "counts"})
    .style.background_gradient()
)
default_and_target = (
    bmt_train[["default", "y"]]
    .value_counts()
    .reset_index()
    .rename(columns={0: "counts"})
)

fig, ax = plt.subplots(1, 1)

sns.barplot(
    data=default_and_target,
    x="default",
    y="counts",
    hue="y",
    palette=target_color,
    alpha=0.8,
)
ax.set_title("Default distributions vs Target (y)", fontsize=12)
ax.set_ylabel("Counts")
ax.set_xlabel("Default", fontsize=10)
ax.yaxis.set_major_formatter(ticker.EngFormatter())
ax.legend(
    title="Subscribed?",
    loc="upper right",
    ncol=2,
    frameon=True,
    shadow=True,
    title_fontsize=8,
    prop={"size": 9},
)
plt.show()
(
    bmt_train[["balance", "default", "y"]]
    .groupby(["default", "y"])["balance"]
    .agg(["mean", "count"])
    .reset_index()
    .style.background_gradient()
)
rf_seed = 345
np.random.seed(rf_seed)
train_x = bmt_train.iloc[:, :-1]
train_x.head()
train_y = bmt_train[["y"]]

train_y = np.ravel(train_y)
train_y.shape
ohe_columns = list(train_x.select_dtypes(include="category").columns.values)
ohe_columns
ohe_columns.remove("education")
ohe_columns
train_x = pd.get_dummies(
    train_x, prefix=ohe_columns, columns=ohe_columns, drop_first=True
)
train_x.head()
recode_education_var = {"unknown": 0, "primary": 1, "secondary": 2, "tertiary": 3}
train_x["education"] = train_x["education"].replace(recode_education_var)
train_x["education"].value_counts(normalize=True)
train_y.shape
test_x = bmt_test.iloc[:, :-1]
test_x.shape
test_y = bmt_test[["y"]]
test_y = np.ravel(test_y)
test_y.shape
test_x = pd.get_dummies(
    test_x, prefix=ohe_columns, columns=ohe_columns, drop_first=True
)
test_x.shape
test_x["education"] = test_x["education"].replace(recode_education_var)
test_x.shape
test_y.shape
rf = RandomForestClassifier(
    n_jobs=-1, random_state=rf_seed, class_weight="balanced_subsample"
)
# recall_score
rs = make_scorer(recall_score)
# CV
cv = cross_val_score(rf, train_x, train_y, cv=10, n_jobs=-1, scoring=rs)
print("Cross validation scores: {}".format(cv))
print("%0.2f recall with a standard deviation of %0.2f" % (cv.mean(), cv.std()))
# Fit the model
rf.fit(train_x, train_y)
pred = rf.predict(train_x)
print("The train recall score is {}".format(np.round(recall_score(train_y, pred), 4)))
sns.heatmap(
    confusion_matrix(train_y, pred),
    annot=True,
    fmt="g",
    cbar=False,
    cmap="Reds",
    annot_kws={"size": 15},
)
plt.title("Confusion matrix (Train set)", fontsize=16)
plt.yticks(rotation=0)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
print(classification_report(train_y, pred))
pred = rf.predict(test_x)
print("The test recall score is {}".format(np.round(recall_score(test_y, pred), 4)))
sns.heatmap(
    confusion_matrix(test_y, pred),
    annot=True,
    fmt="g",
    cmap="Reds",
    cbar=False,
    annot_kws={"size": 15},
)
plt.title("Confusion matrix (Test set)", fontsize=16)
plt.yticks(rotation=0)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
print(classification_report(test_y, pred))
X = bmt_train.iloc[:, :-1]
X.head()
y = bmt_train[["y"]]

y = np.ravel(train_y)
y.shape
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,stratify= y, random_state=rf_seed)
X_train.shape
y_train.shape
X_test.shape
y_test.shape
ohe_columns = list(X_train.select_dtypes(include="category").columns.values)
ohe_columns.remove("education")
ohe_columns
X_train = pd.get_dummies(
    X_train, prefix=ohe_columns, columns=ohe_columns, drop_first=True
)
X_train.head()
recode_education_var = {"unknown": 0, "primary": 1, "secondary": 2, "tertiary": 3}
X_train["education"] = X_train["education"].replace(recode_education_var)
X_train["education"].value_counts(normalize=True)
y_train.shape
X_test = bmt_test.iloc[:, :-1]
X_test.shape
y_test = bmt_test[["y"]]
y_test = np.ravel(test_y)
y_test
X_test = pd.get_dummies(
    X_test, prefix=ohe_columns, columns=ohe_columns, drop_first=True
)
X_test.shape
X_test["education"] = test_x["education"].replace(recode_education_var)
X_test.shape
y_test.shape
rf2 = RandomForestClassifier(
    n_jobs=-1, random_state=rf_seed, class_weight="balanced_subsample"
)
# recall_score
rs2 = make_scorer(recall_score)

# CV
cv = cross_val_score(rf2, train_x, train_y, cv=10, n_jobs=-1, scoring=rs2)
print("Cross validation scores: {}".format(cv))
print("%0.2f recall with a standard deviation of %0.2f" % (cv.mean(), cv.std()))

# Fit the model
rf2.fit(X_train, y_train)

# Get predictions Train set
pred = rf2.predict(X_train)
print("The train recall score is {}".format(np.round(recall_score(y_train, pred), 2)))
#pred
#np.unique(pred)

sns.heatmap(
    confusion_matrix(y_train, pred),
    annot=True,
    fmt="g",
    cbar=False,
    cmap="Greens",
    annot_kws={"size": 15},
)
plt.title("Confusion matrix (y_train)", fontsize=16)
plt.yticks(rotation=0)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
print(classification_report(y_train, pred))


# Get predictions test set
pred = rf2.predict(X_test)
print("The test recall score is {}".format(np.round(recall_score(y_test, pred), 2)))

sns.heatmap(
    confusion_matrix(y_test, pred),
    annot=True,
    fmt="g",
    cmap="Greens",
    cbar=False,
    annot_kws={"size": 15},
)
plt.title("Confusion matrix (y_test)", fontsize=16)
plt.yticks(rotation=0)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
print(classification_report(y_test, pred))