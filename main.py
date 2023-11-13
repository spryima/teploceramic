import os
import requests

from xml.etree import ElementTree as ET

url = 'https://teploceramic.com.ua/tstore/yml/0c27a1c7f14adcdbcc9b5fc249bdb410.yml'
response = requests.get(url)
xml_data = response.content

tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

for offer in root.findall('.//offer'):
  offer.set('available', 'true')

tree.write('modified_file.yml')
os.system('git add modified_file.yml')
os.system('git commit -m "Оновлено файл"')
os.system('git push')
