`page=99` does not raise. `ITEMS[start:start + per_page]` past the end is `[]`, so a caller walking pages stops at the first empty page. Only `page < 1` or `per_page < 1` raise.

The cap is not arbitrary: 100 items keeps one page under the 64 KB response limit (see the comment on that line). We can raise it together with the limit; dropping it would let `per_page=500` send a 300 KB page.
