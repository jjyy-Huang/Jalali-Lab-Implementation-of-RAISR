import numpy as np
import numba as nb
from math import floor

def _getEdgePixel(patch):
    up = patch[0, :]
    down = np.flipud(patch[-1, 1:])
    left = np.flipud(patch[1:, 0])
    right = patch[1:-1,-1]
    return np.hstack((up, right, down, left))

def _checkFlip(seq):
    res = 0
    for i in range(-1, len(seq) - 1):
        res += seq[i] ^ seq[i + 1]
    return res

def _getAngle(seq):
    for i in range(len(seq) - 1):
        if (seq[i] ^ seq[i + 1] == 1) & (seq[i] == 1):
            return i

    return len(seq) - 1


def ute(patch):
    p = patch.shape[0] * 4 - 4
    r = floor(patch.shape[0] / 2)
    edge = _getEdgePixel(patch)
    u = _checkFlip(edge)
    c = patch[r][r]
    if u == 2:
        riu = np.sum(edge)
        angle = _getAngle(edge)
        t = 4 + angle + riu * p + c * p * p
    elif u == 0:
        riu = 0
        t = 2 * c + riu
    else:
        riu = 1
        t = 2 * c + riu

    return t

mat = np.array(
    [[1, 1, 1, 1, 1],
    [1, 6, 7, 8, 0],
    [1, 10, 11, 12, 1],
    [1, 14, 15, 16, 1],
    [1, 1, 1, 1, 1]]
)
ute(mat)