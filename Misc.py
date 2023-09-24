def clamp(val, ll=0, ul=float("inf")):
    return max(ll, min(val, ul))
