#!/usr/bin/env python3
#coding:utf-8

from bs4 import BeautifulSoup
import urllib.request
import sys


def banner():
	print(' _____ ______   ___   ___    _____  ___               ________  ________  ________  ___   ___  ________  ___  ___  ________  ________')     
	print('|\   _ \  _   \|\  \ |\  \  / __  \|\  \             |\   __  \|\   __  \|\_____  \|\  \ |\  \|\   ____\|\  \|\  \|\_____  \|\   __  \ ')    
	print('\ \  \\\__\ \  \ \  \\_\  \|\/_|\  \ \  \            \ \  \|\ /\ \  \|\  \|____|\ /\ \  \\_\  \ \  \___|\ \  \\\  \|____|\ /\ \  \|\  \ ')  
	print(' \ \  \\|__| \  \ \______  \|/ \ \  \ \  \            \ \   __  \ \   _  _\    \|\  \ \______  \ \  \    \ \   __  \    \|\  \ \   _  _\ ')
	print('  \ \  \    \ \  \|_____|\  \   \ \  \ \  \____        \ \  \|\  \ \  \\  \|  __\_\  \|_____|\  \ \  \____\ \  \ \  \  __\_\  \ \  \\  \|')
	print('   \ \__\    \ \__\     \ \__\   \ \__\ \_______\       \ \_______\ \__\\ _\ |\_______\     \ \__\ \_______\ \__\ \__\|\_______\ \__\\ _\ ')
	print('    \|__|     \|__|      \|__|    \|__|\|_______|        \|_______|\|__|\|__|\|_______|      \|__|\|_______|\|__|\|__|\|_______|\|__|\|__|')
	print('\n\n')


def main():
	email = sys.argv[1]

	if len(email) < 7:
		print('Please enter an email address')
		exit(1)

	hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

	req = urllib.request.Request(f'https://haveibeenpwned.com/account/{email}', headers=hdr)
	response = urllib.request.urlopen(req)

	page = response.read()
	html = BeautifulSoup(page,'html.parser')
	print(f'Looked for {email} and found this :')
	for pwnedCompanyHTML in html.find_all('span', {'class': 'pwnedCompanyTitle'}):
		print('\t [*] ' + pwnedCompanyHTML.getText()[0:-1:])

if __name__ == '__main__':
	banner()
	main()