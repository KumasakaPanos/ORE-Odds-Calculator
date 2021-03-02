import sys;

def gIn():
	try:
		return(int(input()))
	except ValueError:
		print("Whole numbers only, please. \n");

def oCalc(x):
	cm = .9;
	cTotal = 1;
	

	for j in range(x-1):
		cTotal *= cm;
		cm = cm - .1;

	return(round((1-cTotal)*100));
	
print(oCalc(gIn()));
input();
