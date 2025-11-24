from subprocess import Popen

def ask(p):
	question = input("Restart Server (R), Stop Server (S)")
	if (question.lower() == "r"):
		p.communicate('stop')
		main()
	else:
		p.communicate('stop')
		

def main():
	p = Popen("serverStart.bat")
	stdout, stderr = p.communicate()
	
	ask(p)

main()