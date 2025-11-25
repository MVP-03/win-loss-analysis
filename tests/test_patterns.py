import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from patterns import loss_by_deal_size, competitive_overlap, top_loss_reasons_by_segment

DEALS = [
    {'outcome': 'won',  'deal_value_usd': 10000, 'industry': 'saas', 'competitors_mentioned': ['CompA'], 'loss_reason': None},
    {'outcome': 'lost', 'deal_value_usd': 15000, 'industry': 'saas', 'competitors_mentioned': ['CompA', 'CompB'], 'loss_reason': 'price'},
    {'outcome': 'lost', 'deal_value_usd': 80000, 'industry': 'fin',  'competitors_mentioned': ['CompB'], 'loss_reason': 'features'},
    {'outcome': 'won',  'deal_value_usd': 200000,'industry': 'fin',  'competitors_mentioned': [], 'loss_reason': None},
    {'outcome': 'lost', 'deal_value_usd': 12000, 'industry': 'saas', 'competitors_mentioned': ['CompA'], 'loss_reason': 'price'},
]


def test_loss_by_deal_size_keys():
    result = loss_by_deal_size(DEALS)
    assert 'small' in result
    assert 'enterprise' in result


def test_competitive_overlap_total():
    result = competitive_overlap(DEALS)
    assert result['CompA']['total'] == 3
    assert result['CompB']['total'] == 2


def test_top_loss_reasons():
    result = top_loss_reasons_by_segment(DEALS, 'industry', top_n=2)
    assert 'saas' in result
    assert result['saas'][0][0] == 'price'
