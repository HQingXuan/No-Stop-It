from collections import Counter
from datetime import datetime, timezone

import fmt


def day_of(ts):
    return fmt.day(datetime.fromtimestamp(ts, timezone.utc))


def per_day(timestamps):
    return dict(Counter(day_of(t) for t in timestamps))
