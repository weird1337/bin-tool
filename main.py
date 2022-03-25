import random,requests,string, os, time
from colorama import init, Fore
init()

def checker(unchecked_bin):
	list = []
	r = requests.get(f"https://lookup.binlist.net/{unchecked_bin}").json().items()
	for item, key in r:
		try:
			list.append(f'{item} = {key}')
		except:
			pass
	return list

def Gen(first_number):
	gen = ''.join(random.choices(string.digits, k=4))
	unchecked_bin = str(first_number)+gen
	print("\n\nGenerated Bin:", unchecked_bin, '\n~~~~~~~~~~~~~~~~~~~~~\n')
	f = open('Generated.txt', 'a', encoding='utf-8')
	f.write(f"Bin:{unchecked_bin}\n")
	for item in checker(unchecked_bin):
		f.write(item + '\n')
	f.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	f.close()
	time.sleep(1.5)

def menu():
	print(f"""
						{Fore.YELLOW} 
						┌─┐┌─┐  ┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
                                                │  │    │ ┬├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
                                                └─┘└─┘  └─┘└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─
						weird#1337
						{Fore.GREEN}[1]Visa   [2]Mastercard{Fore.RESET} 
		""")

while True:
	os.system("cls")
	menu()
	choose_2 = int(input("\t[+]Your Choice :"))
	if choose_2 == 1:
		first_number = 42
		Gen(first_number)
	elif choose_2 == 2:
		first_number = 55
		Gen(first_number)
	else:
		print("Error Choose 1 or 2")
