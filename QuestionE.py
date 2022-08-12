import pandas as pd
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay

patient = pd.read_csv('patient.csv')
patient
y_train = patient['necessity']
y_scores = patient['prediction']

display = PrecisionRecallDisplay.from_predictions(y_train, y_scores, name="LinearSVC")
_ = display.ax_.set_title("2-class Precision-Recall curve")
plt.show()

precisions, recalls, thresholds = precision_recall_curve(y_train, y_scores)

def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
    plt.plot(thresholds, recalls[:-1], "r-", label="Recall")
    [...]

plot_precision_recall_vs_threshold(precisions, recalls, thresholds)
plt.show()

