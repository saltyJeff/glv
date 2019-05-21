def clamp(val, minVal, maxVal) -> float:
    return max(minVal, min(val, maxVal))
def rescale(n, range1, range2):
    delta1 = range1[1] - range1[0]
    delta2 = range2[1] - range2[0]
    return (delta2 * (n - range1[0]) / delta1) + range2[0]