from urllib.parse import *
parse_url=urlparse('https://www.geeksforgeeks.org/pprint-data-pretty-printer-python/')
print(parse_url)
print("++++++++++++++++++++++")
unparse_url=urlunparse(parse_url)
print(unparse_url)