from sklearn.metrics import matthews_corrcoef, f1_score
import numpy as np
y = np.array([1, 1, 1, 0])
pred = np.array([1, 1, 0, 0])
res = matthews_corrcoef(y,pred)
# res = f1_score(y,pred)
print(res)