import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.analyser import (
    win_rate_by_segment,
    avg_deal_size_by_segment,
    loss_reasons,
    win_rate_trend,
)

DEALS = [
    {'vertical': 'saas',    'outcome': 'won',  'deal_value_usd': '50000', 'close_month': '2025-01', 'loss_reason': '',         'cycle_days': '45'},
    {'vertical': 'saas',    'outcome': 'lost', 'deal_value_usd': '0',     'close_month': '2025-01', 'loss_reason': 'pricing',  'cycle_days': '30'},
    {'vertical': 'fintech', 'outcome': 'won',  'deal_value_usd': '90000', 'close_month': '2025-01', 'loss_reason': '',         'cycle_days': '60'},
    {'vertical': 'fintech', 'outcome': 'won',  'deal_value_usd': '70000', 'close_month': '2025-02', 'loss_reason': '',         'cycle_days': '55'},
    {'vertical': 'other',   'outcome': 'lost', 'deal_value_usd': '0',     'close_month': '2025-02', 'loss_reason': 'no_budget','cycle_days': '20'},
]


def test_win_rate_by_segment_saas():
    rates = win_rate_by_segment(DEALS, 'vertical')
    assert rates['saas'] == 50.0


def test_win_rate_by_segment_fintech():
    rates = win_rate_by_segment(DEALS, 'vertical')
    assert rates['fintech'] == 100.0


def test_win_rate_zero_for_all_lost():
    rates = win_rate_by_segment(DEALS, 'vertical')
    assert rates['other'] == 0.0


def test_avg_deal_size_excludes_lost():
    sizes = avg_deal_size_by_segment(DEALS, 'vertical')
    assert sizes['saas'] == 50000.0


def test_avg_deal_size_fintech():
    sizes = avg_deal_size_by_segment(DEALS, 'vertical')
    assert sizes['fintech'] == 80000.0


def test_loss_reasons_counts():
    reasons = loss_reasons(DEALS)
    assert reasons['pricing'] == 1
    assert reasons['no_budget'] == 1


def test_loss_reasons_sorted_descending():
    deals = DEALS + [{'vertical': 'saas', 'outcome': 'lost', 'deal_value_usd': '0',
                      'close_month': '2025-01', 'loss_reason': 'pricing', 'cycle_days': '20'}]
    reasons = loss_reasons(deals)
    counts = list(reasons.values())
    assert counts == sorted(counts, reverse=True)


def test_win_rate_trend_months():
    trend = win_rate_trend(DEALS)
    assert '2025-01' in trend
    assert '2025-02' in trend


def test_win_rate_trend_sorted():
    trend = win_rate_trend(DEALS)
    keys = list(trend.keys())
    assert keys == sorted(keys)
