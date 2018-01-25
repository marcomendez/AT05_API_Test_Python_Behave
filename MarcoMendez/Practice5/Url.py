#verify if a Url is correct
def isUrl (url):
    cmd1 ="https://www"
    words = url.split(".")
    print(f"{url} is url"  if len(url) == 3 and words[0] == cmd1 else f"{url} is not url")

isUrl("https://www.google.com")
isUrl("https://faceboo.com")