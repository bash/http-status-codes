#
# (c) 2016 Ruben Schmidmeister
#

from urllib import request


def fetch(url):
    content = ''
    response = request.urlopen(url)

    while True:
        chunk = response.read().decode('utf8')

        if not chunk:
            break

        content = content + chunk

    return content
