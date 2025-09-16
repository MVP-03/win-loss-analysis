from typing import List, Dict


def win_rate_delta(trend: Dict[str, float]) -> Dict[str, float]:
    months = sorted(trend.keys())
    if len(months) < 2:
        return {}
    return {
        months[i]: round(trend[months[i]] - trend[months[i - 1]], 1)
        for i in range(1, len(months))
    }


def momentum_score(trend: Dict[str, float], lookback: int = 3) -> float:
    months = sorted(trend.keys())[-lookback:]
    if len(months) < 2:
        return 0.0
    deltas = [trend[months[i]] - trend[months[i - 1]] for i in range(1, len(months))]
    return round(sum(deltas) / len(deltas), 2)


def streak(trend: Dict[str, float]) -> int:
    months = sorted(trend.keys())
    if len(months) < 2:
        return 0
    direction = None
    count = 0
    for i in range(len(months) - 1, 0, -1):
        delta = trend[months[i]] - trend[months[i - 1]]
        curr  = 'up' if delta > 0 else ('down' if delta < 0 else 'flat')
        if direction is None:
            direction = curr
        if curr != direction:
            break
        count += 1
    return count if direction == 'up' else -count
