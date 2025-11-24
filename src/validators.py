from typing import Dict, List

VALID_OUTCOMES = ('won', 'lost')


def validate_deal(deal: Dict) -> List[str]:
    errors = []
    if deal.get('outcome') not in VALID_OUTCOMES:
        errors.append(f'outcome must be one of {VALID_OUTCOMES}')
    try:
        v = float(deal.get('deal_value_usd', 0))
        if v < 0:
            errors.append('deal_value_usd must be >= 0')
    except (TypeError, ValueError):
        errors.append('deal_value_usd must be numeric')
    if not deal.get('close_month'):
        errors.append('close_month is required')
    return errors
