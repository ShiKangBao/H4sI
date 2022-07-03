import gzip, base64, json
from urllib.parse import unquote

h4sI = "H4sIAKjkxlsC/8tIzcnJVyjPL0oBAPpDyiYKAAAA"
h4sI = unquote(h4sI)
b = base64.b64decode(h4sI)
g = gzip.decompress(b).decode("utf-8")
print(g)
# string to json
# print(json.loads(g))