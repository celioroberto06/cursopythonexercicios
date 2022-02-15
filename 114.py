import urllib
from urllib import request
from selenium import webdriver
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site pudim não está acessível no momento.[m')
else:
    print('Conseguir acessar o site pudim com sucesso')
    print(site.read())
    navegador = webdriver.Chrome()
    navegador.get('http://www.pudim.com.br/')