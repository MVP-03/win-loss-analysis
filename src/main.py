import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.loader import load_deals
from src.analyser import (
    win_rate_by_segment,
    avg_deal_size_by_segment,
    loss_reasons,
    win_rate_trend,
    cycle_length_by_segment,
)
from src.reporter import (
    print_win_rate_table,
    print_avg_deal_size,
    print_loss_reasons,
    print_trend,
    print_cycle_length,
)

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'deals.csv')


def main() -> None:
    deals = load_deals(DATA_PATH)
    print(f"\n  Loaded {len(deals)} deals\n")

    print_win_rate_table(win_rate_by_segment(deals, 'vertical'), 'Vertical')
    print_win_rate_table(win_rate_by_segment(deals, 'headcount_band'), 'Headcount Band')
    print_avg_deal_size(avg_deal_size_by_segment(deals, 'vertical'), 'Vertical')
    print_loss_reasons(loss_reasons(deals))
    print_trend(win_rate_trend(deals))
    print_cycle_length(cycle_length_by_segment(deals, 'vertical'), 'Vertical')
    print()


if __name__ == '__main__':
    main()
