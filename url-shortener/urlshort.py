import pyshorteners

long_url = input("Enter URL you wish to shorten: ")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("Your shortened URL is: " + short_url)