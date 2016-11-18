#coding:utf-8

def num(socre):
	if 90<= socre <= 100:
		print 'you socre is A!'
	elif 80<= socre <=89:
		print 'you socre is B!'
	elif 70<= socre <=79:
		print 'you socre is C!'
	elif 60<= socre <=69:
		print 'you socre is D!'
	else:
		print 'you socre is F!'
	

while 1:
	print '(1)Test socre(0~100).\n (2)qiut'
	choice = raw_input('enter you choice:')
	if choice == '1':
		socre = raw_input('enter you socre:')
		num(socre)
	elif choice == '2':
		print "qiut,Bye"
		break
	else:
		print "worry,enter again!"
		
