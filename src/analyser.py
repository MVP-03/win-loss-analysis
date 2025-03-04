from typing import List, Dict


def win_rate_by_segment(deals: List[Dict], segment_key: str) -> Dict[str, float]:
    groups: Dict[str, Dict[str, int]] = {}
    for deal in deals:
        seg = deal.get(segment_key, 'unknown') or 'unknown'
        if seg not in groups:
            groups[seg] = {'won': 0, 'total': 0}
        groups[seg]['total'] += 1
        if deal.get('outcome') == 'won':
            groups[seg]['won'] += 1
    return {
        seg: round(v['won'] / v['total'] * 100, 1) if v['total'] else 0.0
        for seg, v in groups.items()
    }


def avg_deal_size_by_segment(deals: List[Dict], segment_key: str) -> Dict[str, float]:
    groups: Dict[str, List[float]] = {}
    for deal in deals:
        if deal.get('outcome') != 'won':
            continue
        seg = deal.get(segment_key, 'unknown') or 'unknown'
        val = float(deal.get('deal_value_usd', 0) or 0)
        groups.setdefault(seg, []).append(val)
    return {
        seg: round(sum(vals) / len(vals), 0) if vals else 0.0
        for seg, vals in groups.items()
    }


def loss_reasons(deals: List[Dict]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for deal in deals:
        if deal.get('outcome') == 'lost':
            reason = deal.get('loss_reason') or 'unrecorded'
            counts[reason] = counts.get(reason, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))


def win_rate_trend(deals: List[Dict]) -> Dict[str, float]:
    groups: Dict[str, Dict[str, int]] = {}
    for deal in deals:
        month = deal.get('close_month', 'unknown') or 'unknown'
        if month not in groups:
            groups[month] = {'won': 0, 'total': 0}
        groups[month]['total'] += 1
        if deal.get('outcome') == 'won':
            groups[month]['won'] += 1
    return {
        m: round(v['won'] / v['total'] * 100, 1) if v['total'] else 0.0
        for m, v in sorted(groups.items())
    }


def cycle_length_by_segment(deals: List[Dict], segment_key: str) -> Dict[str, float]:
    groups: Dict[str, List[int]] = {}
    for deal in deals:
        if deal.get('outcome') != 'won':
            continue
        seg = deal.get(segment_key, 'unknown') or 'unknown'
        days = int(deal.get('cycle_days', 0) or 0)
        groups.setdefault(seg, []).append(days)
    return {
        seg: round(sum(vals) / len(vals), 1) if vals else 0.0
        for seg, vals in groups.items()
    }
