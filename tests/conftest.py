import pytest


@pytest.fixture
def sample_deals():
    return [
        {'outcome': 'won',  'deal_value_usd': 50000, 'industry': 'saas', 'close_month': '2025-10',
         'cycle_days': 30, 'competitors_mentioned': ['CompA'], 'loss_reason': None},
        {'outcome': 'lost', 'deal_value_usd': 20000, 'industry': 'saas', 'close_month': '2025-10',
         'cycle_days': 45, 'competitors_mentioned': ['CompB'], 'loss_reason': 'price'},
        {'outcome': 'won',  'deal_value_usd': 150000,'industry': 'fin',  'close_month': '2025-11',
         'cycle_days': 60, 'competitors_mentioned': [], 'loss_reason': None},
        {'outcome': 'lost', 'deal_value_usd': 80000, 'industry': 'fin',  'close_month': '2025-11',
         'cycle_days': 90, 'competitors_mentioned': ['CompA'], 'loss_reason': 'features'},
    ]
