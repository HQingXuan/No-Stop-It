# store

## API

`list_items(page=1, per_page=20)` returns one page of items. per_page is capped at 100; page or per_page below 1 raises ValueError.
