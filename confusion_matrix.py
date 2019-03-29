import numpy as np

y_pred = []
y_label = []
# calculate the confusion matrix
def TP(y_pred, y_label, label=1):
    if label == 1:
        return np.sum(y_pred*y_label)
    else:
        neg_y_pred = 1 - y_pred
        neg_y_label = 1 - y_label
        return  np.sum(neg_y_pred*neg_y_label)

def TN(y_pred, y_label, label=1):
    if label == 1:
        neg_y_pred = 1 - y_pred
        neg_y_label = 1 - y_label
        return  np.sum(neg_y_pred*neg_y_label)  
    else:
        return np.sum(y_pred*y_label)

def FP(y_pred, y_label, label=1):
    if label == 1:
        neg_y_label = 1 - y_label
        return np.sum(neg_y_label*y_pred)
    else:
        neg_y_pred = 1 - y_pred
        return np.sum(neg_y_pred*y_label)

def FN(y_pred, y_label, label=1):
    if label == 1:
        neg_y_pred = 1 - y_pred
        return np.sum(neg_y_pred*y_label)
    else:
        neg_y_label = 1 - y_label
        return np.sum(neg_y_label*y_pred)

def confusion_matrix(y_pred, y_label, label=1):
    neg_y_pred = 1 - y_pred
    neg_y_label = 1 - y_label
    if label == 1:
        tp = np.sum(y_pred*y_label)
        tn = np.sum(neg_y_pred*neg_y_label)
        fp = np.sum(y_pred*neg_y_label)
        fn = np.sum(neg_y_pred*y_label)
        return (tp, tn, fp, fn)
    else:
        tp = np.sum(neg_y_pred*neg_y_label)
        tn = np.sum(y_pred*y_label)
        fp = np.sum(neg_y_pred*y_label)
        fn = np.sum(y_pred*neg_y_label)
        return (tp, tn, fp, fn)
