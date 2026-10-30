import pathlib, tempfile
from report import totals


def test_quoted_fields():
    p = pathlib.Path(tempfile.mkdtemp(), "x.csv")
    p.write_text('region,customer,amount\neast,"A, B",7\neast,"say ""hi""",3\nwest,Q,1\n')
    assert totals(p) == {"east": 10, "west": 1}
