#exception
import sys, traceback
sum = [00 , 22, 33]
try :
	print(sum[3])

except IndexError as e:
	print ( sys.exc_info())
	

else:
	print ("this is finally")