while(True):

	time_str=str(input("Enter time in (hh:mm) format :"))
	hh,mm = time_str.split(':')
	#print(hh, ",", mm)

	if(hh==mm):
		print(hh+":"+mm)
	else:
		time_set = set()
		for s in hh:
			time_set.add(s)
		for s in mm:
			time_set.add(s)
		#print(time_set)
		loop=True
		min = int(mm)
		hr = int(hh)
		while(loop):
			min -= 1
			if (min == -1):
				hr -= 1
				min = 59
			cnt = 0	
			#print("Time reduce  ", hr ," : ", min)
			length = len(str(hr) + str(min))
			for s in str(min):
				if(s in time_set):
					cnt += 1
			for s in str(hr):
				if(s in time_set):
					cnt += 1
			if (cnt == length):
				if(len(str(hr)) != 2):
					res_hr = "0"+str(hr)
				else:
					res_hr = hr
				if(len(str(min)) != 2):
					res_min = "0"+str(min)
				else:
					res_min = min				
				print(res_hr,":",res_min)
				loop = False
				