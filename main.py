from os.path import dirname, join
from status_codes import fetch, transform
from json import dumps

with open(join(dirname(__file__), "URL")) as f:
    url = f.read()

csv = fetch(url)
data = transform(csv)

print(dumps(data, indent=4, sort_keys=True))
