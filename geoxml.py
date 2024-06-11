import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

sum = 0
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment')

for item in results:
    sum = sum + int(item.find('count').text)
    count = count + 1

print("Count:", count)
print("Sum:", sum)