from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

y_train = [1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,1]
y_scores = [91,23,76,48,36,36,92,88,51,10,28,62,75,80,54,72,22,50,12,29,59,78,32,93]

precisions, recalls, thresholds = precision_recall_curve(y_train, y_scores)

def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
    plt.plot(thresholds, recalls[:-1], "g-", label="Recall")
    [...]

plot_precision_recall_vs_threshold(precisions, recalls, thresholds)
plt.show()