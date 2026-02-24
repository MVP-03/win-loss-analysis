from typing import Dict, List, Tuple


def format_win_rate_table(rates: Dict[str, float], label: str = 'Segment') -> str:
    lines = [f'{label:<20}  Win Rate', '-' * 32]
    for seg, rate in sorted(rates.items(), key=lambda x: x[1], reverse=True):
        bar = '█' * int(rate / 5)
        lines.append(f'{seg:<20}  {rate:>5.1f}%  {bar}')
    return '\n'.join(lines)


def format_loss_reasons(reasons: Dict[str, int]) -> str:
    total = sum(reasons.values())
    lines = ['Loss Reasons', '-' * 28]
    for reason, count in reasons.items():
        pct = count / total * 100 if total else 0
        lines.append(f'{reason:<18} {count:>3}  ({pct:.0f}%)')
    return '\n'.join(lines)


def format_competitive_overlap(overlap: Dict[str, Dict]) -> str:
    lines = ['Competitive Overlap', '-' * 40]
    for comp, stats in overlap.items():
        lines.append(
            f'{comp:<16} won={stats["won"]}  lost={stats["lost"]}  '
            f'win_rate={stats["win_rate"]:.1f}%'
        )
    return '\n'.join(lines)
