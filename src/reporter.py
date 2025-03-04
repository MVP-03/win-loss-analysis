from typing import Dict


def print_win_rate_table(rates: Dict[str, float], label: str) -> None:
    print(f"\n  Win Rate by {label}")
    print(f"  {'Segment':<26} {'Win %':>7}")
    print(f"  {'-' * 26} {'-' * 7}")
    for seg, rate in sorted(rates.items(), key=lambda x: x[1], reverse=True):
        bar = '#' * int(rate / 5)
        print(f"  {seg:<26} {rate:>6.1f}%  {bar}")


def print_avg_deal_size(sizes: Dict[str, float], label: str) -> None:
    print(f"\n  Avg Won Deal Size by {label}")
    print(f"  {'Segment':<26} {'Avg USD':>10}")
    print(f"  {'-' * 26} {'-' * 10}")
    for seg, size in sorted(sizes.items(), key=lambda x: x[1], reverse=True):
        print(f"  {seg:<26} {size:>10,.0f}")


def print_loss_reasons(reasons: Dict[str, int]) -> None:
    total = sum(reasons.values())
    print(f"\n  Loss Reasons  (n={total})")
    print(f"  {'Reason':<28} {'Count':>6}  {'Share':>6}")
    print(f"  {'-' * 28} {'-' * 6}  {'-' * 6}")
    for reason, count in reasons.items():
        share = round(count / total * 100, 1) if total else 0.0
        print(f"  {reason:<28} {count:>6}  {share:>5.1f}%")


def print_trend(trend: Dict[str, float]) -> None:
    print(f"\n  Monthly Win Rate Trend")
    print(f"  {'Month':<12} {'Win %':>7}")
    print(f"  {'-' * 12} {'-' * 7}")
    for month, rate in trend.items():
        bar = '#' * int(rate / 5)
        print(f"  {month:<12} {rate:>6.1f}%  {bar}")


def print_cycle_length(lengths: Dict[str, float], label: str) -> None:
    print(f"\n  Avg Sales Cycle (days) by {label}")
    print(f"  {'Segment':<26} {'Days':>6}")
    print(f"  {'-' * 26} {'-' * 6}")
    for seg, days in sorted(lengths.items(), key=lambda x: x[1]):
        print(f"  {seg:<26} {days:>6.1f}")
