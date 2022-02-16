from typing import Tuple
import numpy as np
from sklearn.metrics import f1_score, matthews_corrcoef

def max_appr(y_pred: np.ndarray, y_true: np.ndarray, target_dr: float = 0.01) -> Tuple[str, Tuple[float, float], bool]:
    default_count: int = 0
    app_count: int = len(y_pred)
    threshold: float = 0.0
    for idx, tup in enumerate(sorted(zip(y_pred, y_true))):
        if tup[1]:
            default_count += 1
        if default_count / (idx + 1) > target_dr:
            app_count = idx
            threshold = tup[0]
            break
    return 'max_appr', app_count / len(y_pred), threshold, True


def mcc(y_true: np.ndarray, y_pred: np.ndarray) -> Tuple[str, float, bool]:
    y_pred = (y_pred > 0.5).astype(int)
    return 'MCC', matthews_corrcoef(y_pred, y_true), True


def macro_f1_score(y_true: np.ndarray, y_pred: np.ndarray) -> Tuple[str, float, bool]:
    y_pred = (y_pred > 0.5).astype(int)
    return 'macro_f1', f1_score(y_pred, y_true, average='macro'), True