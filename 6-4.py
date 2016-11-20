def scoreCalculate(score):
	if 90<= score <= 100:
		print 'you score is A!'
	elif 80<= score <=89:
		print 'you score is B!'
	elif 70<= score <=79:
		print 'you score is C!'
	elif 60<= score <=69:
		print 'you score is D!'
	else:
		print 'you score is F!'
while 1:
	choice = ("1.Grade level \n 2.average:")
	if choice == "1":
		while 1:
			score= raw_input('enter you socre(q is qiut):')
			scoreCalculate(socre)
			if score == "q":
				break
	elif choice == "2":
		yourscore = []
		while True:
			score = raw_input("Enter your score (q for quit)-->")
			if score == 'q':
				break
			else:
				yourscore.append(int(score))
		average = float(sum(yourscore)) / len(yourscore)
		print average
	else:
		print "worry enter!"
		break