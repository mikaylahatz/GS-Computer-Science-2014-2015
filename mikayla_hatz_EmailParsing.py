hosts = open("./host.txt","r")
emails = open("./emailList.txt","r")

output = open("./output.txt","wb")
output.write("The following list will show a count of how many emails from each host :\n")
hostsList = []
emailList = []

for host in hosts: 
	host = host.rstrip()
	hostsList.append(host)

for email in emails:
	email = email.rstrip()
	email_parts = email.split("@")
	emailList.append(email_parts[1])

for host in hostsList:
	counter = 0
	for email in emailList:
		if email == host:
			counter +=1
	output.write("%s count is %s" %(host, counter) + " ")

hosts.close() 
emails.close() 
output.close()


