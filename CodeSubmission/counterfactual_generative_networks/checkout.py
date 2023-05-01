import numpy as np

#This function analyzed our randomized test/train split
def main():
	x = np.load('chinese_MNIST_data.npy', encoding='latin1', allow_pickle=True).item()
	testlabels = x.get('test_label')
	trainlabels = x.get('train_label')

	zerostest = 0
	onestest = 0
	twostest = 0
	threestest = 0
	fourstest = 0
	fivestest = 0
	sixstest = 0
	sevenstest = 0
	eightstest = 0
	ninestest = 0
	notnumero = 0
	for i in testlabels:
		if i == 0:
			zerostest +=1
		elif i == 1:
			onestest += 1
		elif i == 2:
			twostest += 1
		elif i == 3:
			threestest += 1
		elif i == 4:
			fourstest += 1
		elif i == 5:
			fivestest += 1
		elif i == 6:
			sixstest += 1
		elif i == 7:
			sevenstest += 1
		elif i == 8:
			eightstest += 1
		elif i == 9:
			ninestest += 1
		else:
			notnumero += 1
	print("testing")
	print("0:", zerostest, "1:", onestest, "2:", twostest, "3:", threestest, "4:", fourstest, "5:", fivestest, "6:", sixstest, "7:", sevenstest, "8:", eightstest, "9:", ninestest, "non-number", notnumero)


	zerostest = 0
	onestest = 0
	twostest = 0
	threestest = 0
	fourstest = 0
	fivestest = 0
	sixstest = 0
	sevenstest = 0
	eightstest = 0
	ninestest = 0
	notnumero = 0
	for i in trainlabels:
		if i == 0:
			zerostest +=1
		elif i == 1:
			onestest += 1
		elif i == 2:
			twostest += 1
		elif i == 3:
			threestest += 1
		elif i == 4:
			fourstest += 1
		elif i == 5:
			fivestest += 1
		elif i == 6:
			sixstest += 1
		elif i == 7:
			sevenstest += 1
		elif i == 8:
			eightstest += 1
		elif i == 9:
			ninestest += 1
		else:
			notnumer += 1
	print("training")
	print("0:", zerostest, "1:", onestest, "2:", twostest, "3:", threestest, "4:", fourstest, "5:", fivestest, "6:", sixstest, "7:", sevenstest, "8:", eightstest, "9:", ninestest, "non-number:", notnumero)
main()
