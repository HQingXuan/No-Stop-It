from collections import Counter
from datetime import datetime

import fmt


def day_of(ts):
    return fmt.day(datetime.fromtimestamp(ts))


def per_day(timestamps):
    return dict(Counter(day_of(t) for t in timestamps))
