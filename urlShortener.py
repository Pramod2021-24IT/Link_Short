import pyshorteners

url = input("Enter url :\n")

print("URL after shorting :-", pyshorteners.Shortener().tinyurl.short(url))