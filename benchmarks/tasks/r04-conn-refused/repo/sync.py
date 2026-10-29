import json, pathlib, urllib.request

URL = "http://127.0.0.1:8765/v1/rates"


def main():
    with urllib.request.urlopen(URL, timeout=5) as r:
        rates = json.load(r)
    pathlib.Path(__file__).with_name("rates.json").write_text(json.dumps(rates, indent=1))
    print(f"synced {len(rates)} rates")


if __name__ == "__main__":
    main()
