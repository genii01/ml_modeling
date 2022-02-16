from typing import Tuple

import numpy as np
from sklearn.metrics import f1_score, matthews_corrcoef

from css_bnpl.metrics.custom import max_appr


def max_apprate(y_true: np.ndarray, y_pred: np.ndarray) -> Tuple[str, float, bool]:
    return 'max_apprate', max_appr(y_pred, y_true)[0], True


def mcc(y_true: np.ndarray, y_pred: np.ndarray) -> Tuple[str, float, bool]:
    y_pred = (y_pred > 0.5).astype(int)
    return 'MCC', matthews_corrcoef(y_pred, y_true), True


def macro_f1_score(y_true: np.ndarray, y_pred: np.ndarray) -> Tuple[str, float, bool]:
    y_pred = (y_pred > 0.5).astype(int)
    return 'macro_f1', f1_score(y_pred, y_true, average='macro'), True