from sklearn.metrics import matthews_corrcoef, f1_score
import numpy as np
y = np.array([1, 1, 1, 0])
pred = np.array([1, 1, 0, 0])
res = matthews_corrcoef(y,pred)
# res = f1_score(y,pred)
print(res)

from metrics import *
y = np.array([1,0,0,1])
pred = np.array([0.7,0.6,0.2,0.8])
metric_name, performance, _ = mcc(y, pred)
print(metric_name)
print(performance)

metric_name, performance, _ = macro_f1_score(y, pred)
print(metric_name)
print(performance)