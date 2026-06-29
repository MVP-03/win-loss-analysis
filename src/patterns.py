from typing import List, Dict, Tuple


def loss_by_deal_size(deals: List[Dict]) -> Dict[str, Dict]:
    buckets = {'small': [], 'mid': [], 'enterprise': []}
    for deal in deals:
        val = float(deal.get('deal_value_usd', 0) or 0)
        if val < 25_000:
            key = 'small'
        elif val < 100_000:
            key = 'mid'
        else:
            key = 'enterprise'
        buckets[key].append(deal)

    result = {}
    for bucket, items in buckets.items():
        if not items:
            continue
        won = sum(1 for d in items if d.get('outcome') == 'won')
        result[bucket] = {
            'total':    len(items),
            'won':      won,
            'lost':     len(items) - won,
            'win_rate': round(won / len(items) * 100, 1),
        }
    return result


def competitive_overlap(deals: List[Dict]) -> Dict[str, Dict]:
    comp_stats: Dict[str, Dict[str, int]] = {}
    for deal in deals:
        for comp in (deal.get('competitors_mentioned') or []):
            if comp not in comp_stats:
                comp_stats[comp] = {'won': 0, 'lost': 0}
            if deal.get('outcome') == 'won':
                comp_stats[comp]['won'] += 1
            else:
                comp_stats[comp]['lost'] += 1

    result = {}
    for comp, stats in comp_stats.items():
        total = stats['won'] + stats['lost']
        result[comp] = {
            **stats,
            'total':    total,
            'win_rate': round(stats['won'] / total * 100, 1) if total else 0.0,
        }
    return dict(sorted(result.items(), key=lambda x: x[1]['total'], reverse=True))


def top_loss_reasons_by_segment(deals: List[Dict], segment_key: str, top_n: int = 3) -> Dict[str, List[Tuple[str, int]]]:
    groups: Dict[str, Dict[str, int]] = {}
    for deal in deals:
        if deal.get('outcome') != 'lost':
            continue
        seg = deal.get(segment_key, 'unknown') or 'unknown'
        reason = deal.get('loss_reason') or 'unrecorded'
        groups.setdefault(seg, {})
        groups[seg][reason] = groups[seg].get(reason, 0) + 1

    return {
        seg: sorted(reasons.items(), key=lambda x: x[1], reverse=True)[:top_n]
        for seg, reasons in groups.items()
    }
