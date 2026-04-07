DEAL_SIZE_BUCKETS = {
    'small':      (0,       25_000),
    'mid':        (25_000, 100_000),
    'enterprise': (100_000, None),
}

WIN_RATE_TARGETS = {
    'small':      40.0,
    'mid':        30.0,
    'enterprise': 20.0,
}

UNRECORDED_REASON = 'unrecorded'

MOMENTUM_LOOKBACK_MONTHS = 3
