## TODO: import all necessary packages and functions
# Since we are working with csv file and we need to read it, csv module is imported
# also in order to extract days,months,etc. from time object I used datetime module.
# Moreover, in order to understand elapsed time, i import time module

import csv
import datetime
import time

#Following code has two important parts: First one is ,of course, reading csv file as it is and naming it ..._file
#It is just string but in order to play with this data more efficiently I changed its type to dictionary. For example first row is like that:
#{'Start Time': '2017-01-01 00:00:36', 'End Time': '2017-01-01 00:06:32', 'Trip Duration': '356', 'Start Station': 'Canal St & Taylor St',
#'End Station': 'Canal St & Monroe St (*)', 'User Type': 'Customer', 'Gender': '', 'Birth Year': ''}

#This is where we read csv files
with open('chicago.csv','r') as chicago_file:
	chicago_reader= [{k: v for k,v in row.items()}
					  for row in csv.DictReader(chicago_file, skipinitialspace=True)]

with open('new_york_city.csv','r') as new_york_city_file:
	new_york_city_reader= [{k: v for k,v in row.items()}
					  for row in csv.DictReader(new_york_city_file, skipinitialspace=True)]

with open('washington.csv','r') as washington_file:
	washington_reader= [{k: v for k,v in row.items()}
					  for row in csv.DictReader(washington_file, skipinitialspace=True)]


def get_city():
	'''Asks the user for a city and returns the filename for that city's bike share data.
	Args:
	none.
	Returns:
	(str) Filename for a city's bikeshare data.
	'''
	while True:

		city_filter = input('\nHello! Let\'s explore some US bikeshare data!\n''Would you like to see data for Chicago, New York, or Washington?\n')

		city = city_filter.lower()

		if city=='chicago' or city=='new york' or city=='washington':
			return city
			break
		else:
			print("Please check your spelling. You should correctly writing one of the following:Chicago, New York, or Washington.\n")
			continue
    # I use lower method not only here but also in all input functions. Because I want to be consistent in my code.
	# It is easy to confuse about whether I use uppercase or lowercase in variables, so I make all variables lowercase, even user input ones.
	# Moreover, user needs to give right input otherwise code will keep asking the same question
def get_time_period():
	'''Asks the user for a time period and returns the specified filter.
	Args:
	none.
	Returns:
	(str) Filter parameter (in lower cases) for data analysis.
	'''
	while True:
		time_period_input = input('\nWould you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n')
		time_period = time_period_input
		if time_period == ('month') or time_period ==('day') or time_period ==('none'):
			return time_period.lower()
			break

		else:
			print("Please check your spelling\n")
			continue
	# I use lower method not only here but also in all input functions. Because I want to be consistent in my code.
	# It is easy to confuse about whether I use uppercase or lowercase in variables, so I make all variables lowercase, even user input ones.
	# Moreover, user needs to give right input otherwise code will keep asking the same question

def get_month():
	'''Asks the user for a month and returns the specified month.
	Args:
	none.
	Returns:
	(str) Specified month in lower cases.
	'''
	while True:
		month_input = input('\nWhich month? January, February, March, April, May, or June?\n')
		month = month_input.lower()
		if month=='january' or month=='february' or month=='march' or month=='april' or month=='may' or month=='june':
			return month.lower()
			break
		else:
			print("Please check your spelling\n")
			continue
	# I use lower method not only here but also in all input functions. Because I want to be consistent in my code.
	# It is easy to confuse about whether I use uppercase or lowercase in variables, so I make all variables lowercase, even user input ones.
	# Moreover, user needs to give right input otherwise code will keep asking the same question




def get_day():
	'''Asks the user for a day and returns the specified day.
	Args:
	none.
	Returns:
	(str) Specified day in lower cases.
	'''
	while True:

		day = input('\nWhich day? Please type your response as an integer. 0 is Sunday, 1 is Monday and so on.\n')
		if day=='0':
			return 'sunday'
			break
		elif day=='1':
			return 'monday'
			break
		elif day=='2':
			return 'tuesday'
			break
		elif day=='3':
			return 'wednesday'
			break
		elif day=='4':
			return 'thursday'
			break
		elif day=='5':
			return 'friday'
			break
		elif day=='6':
			return 'saturday'
			break
		else:
			print('You need to write a number between 0-6. 0 is Sunday, 1 is Monday and so on.\n ')
			continue


    # I use lower method not only here but also in all input functions. Because I want to be consistent in my code.
	# It is easy to confuse about whether I use uppercase or lowercase in variables, so I make all variables lowercase, even user input ones.
	# Moreover, user needs to give right input otherwise code will keep asking the same question

def popular_month(city_file):
	'''
	This function will first convert string to time object then will find the most dense month in terms of bikeshare usage.
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	Keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader.
	Returns:
	(str) Month corresponding to highest amount of bikeshare usage
	'''
	my_list=[]
	# Every row in city file (which is a dictionary)...
	for i in range(len(city_file)):
		# Take its 'Start Time' value...
		a=city_file[i]['Start Time']
		# Following method changes str to time object
		b=datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
		# Following method returns month of its time object and append it to list. Remember 1 is january, 2 is february and so on.
		my_list.append(b.month)
	# Count each months in the list by following method:
	number_jan=my_list.count(1)
	number_feb=my_list.count(2)
	number_mar=my_list.count(3)
	number_apr=my_list.count(4)
	number_may=my_list.count(5)
	number_jun=my_list.count(6)
	# Make a list containing each months count:
	list_of_usage_monthly=[number_jan,number_feb,number_mar,number_apr,number_may,number_jun]
	# Max value of the list:
	max_value=max(list_of_usage_monthly)
	if number_jan==max_value:
		return 'January'
	elif number_feb==max_value:
		return 'February'
	elif number_mar==max_value:
		return 'March'
	elif number_apr==max_value:
		return 'April'
	elif number_may==max_value:
		return 'May'
	elif number_jun==max_value:
		return 'June'
	#There is a shorter way of doing this which i figured out late and applied in other question.

def popular_day(city_file, time_period):
	'''
	This function will first convert str to object then will find the most
	dense day in terms of bikeshare usage.
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader.
	time_period: This is a str which indicates filter parameter. For this function it can either be
	a month or none.
	Returns:
	(str) Day of week corresponding to highest amount of bikeshare usage
	'''
    # The following code assigns filtered month (to be analyzed month) to number
	if time_period=='january':
		spec_month=1
	elif time_period=='february':
		spec_month=2
	elif time_period=='march':
		spec_month=3
	elif time_period=='april':
		spec_month=4
	elif time_period=='may':
		spec_month=5
	elif time_period=='june':
		spec_month=6
	# If the user didnt specify any time filter:
	if time_period=='none':
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			a=city_file[i]['Start Time']
			# Following method changes str to time object
			b=datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
			# Following method finds corresponding day of the above time object and appends it to list (Sunday is 0, Monday is 1, and so on.)
			my_list.append(b.weekday())
		# Count each months in the list by following method:
		number_mon=my_list.count(0)
		number_tue=my_list.count(1)
		number_wed=my_list.count(2)
		number_thu=my_list.count(3)
		number_fri=my_list.count(4)
		number_sat=my_list.count(5)
		number_sun=my_list.count(6)
		# Make a list containing each months count:
		list_of_usage_daily=[number_sun,number_mon,number_tue,number_wed,number_thu,number_fri,number_sat]
		# Max value of the list:
		max_value=max(list_of_usage_daily)

		if number_sun==max_value:
			return 'Sunday'
		elif number_mon==max_value:
			return 'Monday'
		elif number_tue==max_value:
			return'Tuesday'
		elif number_wed==max_value:
			return 'Wednesday'
		elif number_thu==max_value:
			return 'Thursday'
		elif number_fri==max_value:
			return 'Friday'
		elif number_sat==max_value:
			return 'Saturday'
	# If the user specify the month:
	else:
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			a=city_file[i]['Start Time']
			# Following method changes str to time object
			b=datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
			# Now, if the month of the above object is same as the specified month...
			if b.month==spec_month:
			# Append its day to list (Sunday is 0, Monday is 1, and so on.)
				my_list.append(b.weekday())
		# Count each months in the list by following method:
		number_mon=my_list.count(0)
		number_tue=my_list.count(1)
		number_wed=my_list.count(2)
		number_thu=my_list.count(3)
		number_fri=my_list.count(4)
		number_sat=my_list.count(5)
		number_sun=my_list.count(6)
		# Make a list containing each months count:
		list_of_usage_daily=[number_sun,number_mon,number_tue,number_wed,number_thu,number_fri,number_sat]
		# Max value of the list:
		max_value=max(list_of_usage_daily)

		if number_sun==max_value:
			return 'Sunday'
		elif number_mon==max_value:
			return 'Monday'
		elif number_tue==max_value:
			return 'Tuesday'
		elif number_wed==max_value:
			return 'Wednesday'
		elif number_thu==max_value:
			return 'Thursday'
		elif number_fri==max_value:
			return 'Friday'
		elif number_sat==max_value:
			return 'Saturday'



def popular_hour(city_file, time_period):
	'''
	This function will first convert str to object then will find the most
	dense hours in terms of bikeshare usage.
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader.
	time_period: This is a str which indicates filter parameter. For this function it can be month, day, or none
	Returns:
	(str) Month corresponding to highest amount of bikeshare usage
	'''
    # The following code assigns filtered month (to be analyzed month) to number
	if time_period=='january':
		spec_month=1
	elif time_period=='february':
		spec_month=2
	elif time_period=='march':
		spec_month=3
	elif time_period=='april':
		spec_month=4
	elif time_period=='may':
		spec_month=5
	elif time_period=='june':
		spec_month=6
	# The following code assigns filtered day (to be analyzed day) to number
	if time_period=='sunday':
		spec_day=0
	if time_period=='monday':
		spec_day=1
	if time_period=='tuesday':
		spec_day=2
	elif time_period=='wednesday':
		spec_day=3
	elif time_period== 'thursday':
		spec_day=4
	elif time_period=='friday':
		spec_day=5
	elif time_period=='saturday':
		spec_day=6

	list_of_usage_hourly=[]
	# If the user didnt specify any time filter:
	if time_period=='none':
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			a=city_file[i]['Start Time']
			# Following method changes str to time object
			b=datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
			# Add it to list
			my_list.append(b.hour)
		# For every hour in a day...
		for i in range(24):
			# Count the number of appearance of this hour in my list and add this count to list_of_usage_hourly
			list_of_usage_hourly.append(my_list.count(i))
		# Find the maximum of this list (Remember this value is just the maximum value of appearance of every hour in the list,
		# But we are interested in which hour is peak hour for bikeshare.)
		m= max(list_of_usage_hourly)
		# Find the corresponding hour for maximum count.
		for i,value in enumerate(list_of_usage_hourly):
			if value==m:
				return i
	# If the user specify month filter:
	elif time_period==('january') or time_period==('february') or time_period==('march') or time_period==('april') or time_period==('may') or time_period==('june'):
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			a=city_file[i]['Start Time']
			# Following method changes str to time object
			b=datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
			# Now, if the month of the above object is same as the specified month...
			if b.month==spec_month:
				# Append its hour to my_list
				my_list.append(b.hour)
		# For every hour in a day..
		for i in range(24):
			# Count the number of appearance of this hour in my list and add this count to list_of_usage_hourly
			list_of_usage_hourly.append(my_list.count(i))
		# Find the maximum of this list (Remember this value is just the maximum value of appearance of every hour in the list,
		# But we are interested in which hour is peak hour for bikeshare.)
		m= max(list_of_usage_hourly)
		# Find the corresponding hour for maximum count.
		for i,value in enumerate(list_of_usage_hourly):
			if value==m:
				return i
	# If the user specify day filter:
	else:
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			a=city_file[i]['Start Time']
			# Following method changes str to time object
			b=datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
			# Now, if the day of the above object is same as the specified day...
			if b.weekday()==spec_day:
				# Append its hour to my_list
				my_list.append(b.hour)
		# For every hour in a day..
		for i in range(24):
			# Count the number of appearance of this hour in my list and add this count to list_of_usage_hourly
			list_of_usage_hourly.append(my_list.count(i))
		# Find the maximum of this list (Remember this value is just the maximum value of appearance of every hour in the list,
		# But we are interested in which hour is peak hour for bikeshare.)
		m= max(list_of_usage_hourly)
		# Find the corresponding hour for maximum count.
		for i,value in enumerate(list_of_usage_hourly):
			if value==m:
				return i


def trip_duration(city_file, time_period):
	'''
	This function will find the total trip duration and average trip duration
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader.
	time_period: This is a str which indicates filter parameter. For this function it can be month, day, or none
	Returns:
	(str) Total trip duration and average trip duration in edited format.
	'''
    # The following code assigns filtered month (to be analyzed month) to number
	if time_period=='january':
		spec_month=1
	elif time_period=='february':
		spec_month=2
	elif time_period=='march':
		spec_month=3
	elif time_period=='april':
		spec_month=4
	elif time_period=='may':
		spec_month=5
	elif time_period=='june':
		spec_month=6
	# The following code assigns filtered day (to be analyzed day) to number
	if time_period=='sunday':
		spec_day=0
	if time_period=='monday':
		spec_day=1
	if time_period=='tuesday':
		spec_day=2
	elif time_period=='wednesday':
		spec_day=3
	elif time_period== 'thursday':
		spec_day=4
	elif time_period=='friday':
		spec_day=5
	elif time_period=='saturday':
		spec_day=6
	list_of_usage_hourly=[]

	# If the user didnt specify any time filter:
	if time_period=='none':
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Trip Duration' value...
			a=city_file[i]['Trip Duration']
			# Make it float because we are going to do some basic math...
			b=float(a)
			# Append it to my list
			my_list.append(b)
		#Following variable (seconds) is total trip duration.
		seconds=sum(my_list)
		#Following variable (average_trip) is average trip duration.
		average_trip=(sum(my_list)/len(my_list))
		# Total trip duration is in seconds lets convert it more readable scale.
		# Divmod finds how many minutes are there in seconds variable (just divides seconds by 60), and remainder is now the new value of seconds.
		m, s= divmod(seconds,60)
		# Similarly find hour and new value of minutes
		h,m= divmod(m,60)
		# Similarly find day and new value of hours.
		g,h= divmod(h,24)
		# Result is given ...days and HH:MM:SS format.
		return ("Total trip duration is %g days and %d:%02d:%02d (or in other words %g seconds). Also average time is %02d" % (g,h, m, s,seconds,average_trip))
	# If the user specify month filter:
	elif time_period==('january') or time_period==('february') or time_period==('march') or time_period==('april') or time_period==('may') or time_period==('june'):
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# Now, if the month of the above object is same as the specified month...
			if  y.month==spec_month:
				# Take its 'Trip Duration' value...
				a=washington_reader[i]['Trip Duration']
				# Make it float because we are going to do some basic math...
				b=float(a)
				# Append it to my list
				my_list.append(b)
		#Following variable (seconds) is total trip duration.
		seconds=sum(my_list)
		#Following variable (average_trip) is average trip duration.
		average_trip=(sum(my_list)/len(my_list))
		# Total trip duration is in seconds lets convert it more readable scale.
		# Divmod finds how many minutes are there in seconds variable (just divides seconds by 60), and remainder is now the new value of seconds.
		m, s= divmod(seconds,60)
		# Similarly find hour and new value of minutes
		h,m= divmod(m,60)
		# Similarly find day and new value of hours.
		g,h= divmod(h,24)
		# Result is given ...days and HH:MM:SS format.
		return ("Total trip duration is %g days and %d:%02d:%02d (or in other words %g seconds). Also average time is %02d seconds" % (g,h, m, s,seconds,average_trip))
	# If the user specify day filter:
	else:
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# Now, if the day of the above object is same as the specified day...
			if y.weekday()==spec_day:
				# Take its 'Trip Duration' value...
				a=city_file[i]['Trip Duration']
				# Make it float because we are going to do some basic math...
				b=float(a)
				# Append it to my list
				my_list.append(b)
		#Following variable (seconds) is total trip duration.
		seconds=sum(my_list)
		#Following variable (average_trip) is average trip duration.
		average_trip=(sum(my_list)/len(my_list))
		# Total trip duration is in seconds lets convert it more readable scale.
		# Divmod finds how many minutes are there in seconds variable (just divides seconds by 60), and remainder is now the new value of seconds.
		m, s= divmod(seconds,60)
		# Similarly find hour and new value of minutes
		h,m= divmod(m,60)
		# Similarly find day and new value of hours.
		g,h= divmod(h,24)
		# Result is given ...days and HH:MM:SS format.
		return ("Total trip duration is %g days and %d:%02d:%02d (or in other words %g seconds). Also average time is %02d seconds" % (g,h, m, s,seconds,average_trip))


def popular_start_stations(city_file, time_period):
	'''
	This function will find the most popular start station.
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader.
	time_period: This is a str which indicates filter parameter. For this function it can be month, day, or none
	Returns:
	(str) The most popular start station.
	'''
	# The following code assigns filtered month (to be analyzed month) to number
	if time_period=='january':
		spec_month=1
	elif time_period=='february':
		spec_month=2
	elif time_period=='march':
		spec_month=3
	elif time_period=='april':
		spec_month=4
	elif time_period=='may':
		spec_month=5
	elif time_period=='june':
		spec_month=6
	# The following code assigns filtered day (to be analyzed day) to number
	if time_period=='sunday':
		spec_day=0
	if time_period=='monday':
		spec_day=1
	if time_period=='tuesday':
		spec_day=2
	elif time_period=='wednesday':
		spec_day=3
	elif time_period== 'thursday':
		spec_day=4
	elif time_period=='friday':
		spec_day=5
	elif time_period=='saturday':
		spec_day=6
	# If the user didnt specify any time filter:
	if time_period=='none':
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Station' value...
			a=city_file[i]['Start Station']
			# Append it
			my_list.append(a)
		# In order to count stations, we need to know unique elements in the list.
		my_set=set(my_list)
		# Also we need to know number of appearance of each unique stations in the list and assign them in corresponding station.
		# For example, X station: Y times. To do this, I make use of dictionary.
		my_dicts={}
		# This is the code for X station : Y times
		for element in my_set:
			my_dicts[element]=my_list.count(element)
		# Returns the most popular start station.
		return max(my_dicts, key=my_dicts.get)

	# If the user specify month time filter:
	elif time_period==('january') or time_period==('february') or time_period==('march') or time_period==('april') or time_period==('may') or time_period==('june'):
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# Now, if the month of the above object is same as the specified month...
			if  y.month==spec_month:
				# Take its 'Start Station' value...
				a=city_file[i]['Start Station']
				# Append it
				my_list.append(a)
		# In order to count stations, we need to know unique elements in the list.
		my_set=set(my_list)
		# Also we need to know number of appearance of each unique stations in the list and assign them in corresponding station.
		# For example, X station: Y times. To do this, I make use of dictionary.
		my_dicts={}

		# This is the code for X station : Y times
		for element in my_set:
			my_dicts[element]=my_list.count(element)
		# Returns the most popular start station.
		return max(my_dicts, key=my_dicts.get)

	# If the user specify day time filter:
	else:
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# Now, if the day of the above object is same as the specified day...
			if y.weekday()==spec_day:
				# Take its 'Start Station' value...
				a=city_file[i]['Start Station']
				# Append it
				my_list.append(a)
		# In order to count stations, we need to know unique elements in the list.
		my_set=set(my_list)
		# Also we need to know number of appearance of each unique stations in the list and assign them in corresponding station.
		# For example, X station: Y times. To do this, I make use of dictionary.
		my_dicts={}
		# This is the code for X station : Y times
		for element in my_set:
			my_dicts[element]=my_list.count(element)
		# Returns the most popular start station.
		return max(my_dicts, key=my_dicts.get)




def popular_end_stations(city_file,time_period):
	'''
	This function will find the most popular end station.
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader.
	time_period: This is a str which indicates filter parameter. For this function it can be month, day, or none
	Returns:
	(str) The most popular end station.
	'''
	# The following code assigns filtered month (to be analyzed month) to number
	if time_period=='january':
		spec_month=1
	elif time_period=='february':
		spec_month=2
	elif time_period=='march':
		spec_month=3
	elif time_period=='april':
		spec_month=4
	elif time_period=='may':
		spec_month=5
	elif time_period=='june':
		spec_month=6
	# The following code assigns filtered day (to be analyzed day) to number
	if time_period=='sunday':
		spec_day=0
	if time_period=='monday':
		spec_day=1
	if time_period=='tuesday':
		spec_day=2
	elif time_period=='wednesday':
		spec_day=3
	elif time_period== 'thursday':
		spec_day=4
	elif time_period=='friday':
		spec_day=5
	elif time_period=='saturday':
		spec_day=6
	# If the user didnt specify any time filter.
	if time_period=='none':
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'End Station' value...
			a=city_file[i]['End Station']
			# Append it
			my_list.append(a)
		# In order to count stations, we need to know unique elements in the list.
		my_set=set(my_list)
		# Also we need to know number of appearance of each unique stations in the list and assign them in corresponding station.
		# For example, X station: Y times. To do this, I make use of dictionary.
		my_dicts={}
		# This is the code for X station : Y times
		for element in my_set:
			my_dicts[element]=my_list.count(element)
		# Returns the most popular end station.
		return max(my_dicts, key=my_dicts.get)

	# If the user specify month time filter:
	elif time_period==('january') or time_period==('february') or time_period==('march') or time_period==('april') or time_period==('may') or time_period==('june'):
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# Now, if the month of the above object is same as the specified month...
			if  y.month==spec_month:
				# Take its 'End Station' value...
				a=city_file[i]['End Station']
				# Append it
				my_list.append(a)
		# In order to count stations, we need to know unique elements in the list.
		my_set=set(my_list)
		# Also we need to know number of appearance of each unique stations in the list and assign them in corresponding station.
		# For example, X station: Y times. To do this, I make use of dictionary.
		my_dicts={}
		# This is the code for X station : Y times
		for element in my_set:
			my_dicts[element]=my_list.count(element)
		# Returns the most popular end station.
		return max(my_dicts, key=my_dicts.get)

	# If the user specify day time filter:
	else:
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# Now, if the day of the above object is same as the specified day...
			if y.weekday()==spec_day:
				# Take its 'End Station' value...
				a=city_file[i]['End Station']
				# Append it
				my_list.append(a)
		# In order to count stations, we need to know unique elements in the list.
		my_set=set(my_list)
		# Also we need to know number of appearance of each unique stations in the list and assign them in corresponding station.
		# For example, X station: Y times. To do this, I make use of dictionary.
		my_dicts={}
		# This is the code for X station : Y times
		for element in my_set:
			my_dicts[element]=my_list.count(element)
		# Returns the most popular end station.
		return max(my_dicts, key=my_dicts.get)




def popular_trip(city_file, time_period):
	'''
	This function will find the most popular trip ( like X to Y station)
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader.
	time_period: This is a str which indicates filter parameter. For this function it can be month, day, or none
	Returns:
	(str) The most popular trip.
	'''
	# The following code assigns filtered month (to be analyzed month) to number
	if time_period=='january':
		spec_month=1
	elif time_period=='february':
		spec_month=2
	elif time_period=='march':
		spec_month=3
	elif time_period=='april':
		spec_month=4
	elif time_period=='may':
		spec_month=5
	elif time_period=='june':
		spec_month=6
	# The following code assigns filtered day (to be analyzed day) to number
	if time_period=='sunday':
		spec_day=0
	if time_period=='monday':
		spec_day=1
	if time_period=='tuesday':
		spec_day=2
	elif time_period=='wednesday':
		spec_day=3
	elif time_period== 'thursday':
		spec_day=4
	elif time_period=='friday':
		spec_day=5
	elif time_period=='saturday':
		spec_day=6

	# If the user didnt specify any time filter.
	if time_period=='none':
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Station' and 'End Station' and combine them...
			a=city_file[i]['Start Station']
			b=city_file[i]['End Station']
			my_list.append(a+" to "+b)
		# Same logic as in previous popular_start_stations/popular_end_stations function.
		my_set=set(my_list)
		my_dicts={}
		for element in my_set:
			my_dicts[element]=my_list.count(element)

		return max(my_dicts, key=my_dicts.get)
	# If the user specify month time filter.
	elif time_period==('january') or time_period==('february') or time_period==('march') or time_period==('april') or time_period==('may') or time_period==('june'):
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			if  y.month==spec_month:
				# Take its 'Start Station' and 'End Station' and combine them...
				a=city_file[i]['Start Station']
				b=city_file[i]['End Station']
				my_list.append(a+" to "+b)
		# Same logic as in previous popular_start_stations/popular_end_stations function.
		my_set=set(my_list)
		my_dicts={}

		for element in my_set:
			my_dicts[element]=my_list.count(element)
		return max(my_dicts, key=my_dicts.get)

	# If the user specify day time filter.
	else:
		my_list=[]
		# Every row in city file (which is a dictionary)..
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			if y.weekday()==spec_day:
				# Take its 'Start Station' and 'End Station' and combine them...
				a=city_file[i]['Start Station']
				b=city_file[i]['End Station']
				my_list.append(a+" to "+b)
		# Same logic as in previous popular_start_stations/popular_end_stations function.
		my_set=set(my_list)
		my_dicts={}
		for element in my_set:
			my_dicts[element]=my_list.count(element)
		return max(my_dicts, key=my_dicts.get)



def users(city_file, time_period):
	'''
	This function will find the amount of user types ( namely, subscriber and customer)
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader.
	time_period: This is a str which indicates filter parameter. For this function it can be month, day, or none
	Returns:
	(str) Number of user types in edited format.
	'''

	# The following code assigns filtered month (to be analyzed month) to number
	if time_period=='january':
		spec_month=1
	elif time_period=='february':
		spec_month=2
	elif time_period=='march':
		spec_month=3
	elif time_period=='april':
		spec_month=4
	elif time_period=='may':
		spec_month=5
	elif time_period=='june':
		spec_month=6
	# The following code assigns filtered day (to be analyzed day) to number
	if time_period=='sunday':
		spec_day=0
	if time_period=='monday':
		spec_day=1
	if time_period=='tuesday':
		spec_day=2
	elif time_period=='wednesday':
		spec_day=3
	elif time_period== 'thursday':
		spec_day=4
	elif time_period=='friday':
		spec_day=5
	elif time_period=='saturday':
		spec_day=6
	# If the user didnt specify any time filter...
	if time_period=='none':
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its User Type and append it to list
			a=city_file[i]['User Type']
			my_list.append(a)
		# Count how many time each type appear in the list.
		number_sub=my_list.count('Subscriber')
		number_cus=my_list.count('Customer')
		return "Number of customer is: {} , and number of subscriber is: {} ".format(number_cus,number_sub)
	# If the user specify month time filter... Be aware only chicago_reader's file have related information!
	elif time_period==('january') or time_period==('february') or time_period==('march') or time_period==('april') or time_period==('may') or time_period==('june'):
		my_list=[]
		# Every row in city file...
		for i in range(len(city_file)):
			#Take its start time value and make it time object
			x=city_file[i]['Start Time']
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# If the month of the above object is the same as specified one...
			if  y.month==spec_month:
				# Take its User Type and append it to list.
				a=city_file[i]['User Type']
				my_list.append(a)
		# Count how many time each type appear in the list.
		number_sub=my_list.count('Subscriber')
		number_cus=my_list.count('Customer')
		return "Number of customer is: {} , and number of subscriber is: {} ".format(number_cus,number_sub)
	# If the user specify day time filter...Be aware only chicago_reader's file have related information!
	else:
		my_list=[]
		#Take its start time value and make it time object
		for i in range(len(city_file)):
			x=city_file[i]['Start Time']
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# If the day of the above object is the same as specified one...
			if y.weekday()==spec_day:
				# Take its User Type and append it to list.
				a=city_file[i]['User Type']
				my_list.append(a)
		# Count how many time each type appear in the list.
		number_sub=my_list.count('Subscriber')
		number_cus=my_list.count('Customer')
		return "Number of customer is: {} , and number of subscriber is: {} ".format(number_cus,number_sub)

def gender(city_file, time_period):
	'''
	This function will find the amount of gender types ( namely, female and male)
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader. Warning: only chicago file includes this information
	time_period: This is a str which indicates filter parameter. For this function it can be month, day, or none
	Returns:
	(str) Amount of user in terms of gender types in edited format.
	'''
    # The following code assigns filtered month (to be analyzed month) to number
	if time_period=='january':
		spec_month=1
	elif time_period=='february':
		spec_month=2
	elif time_period=='march':
		spec_month=3
	elif time_period=='april':
		spec_month=4
	elif time_period=='may':
		spec_month=5
	elif time_period=='june':
		spec_month=6
	# The following code assigns filtered day (to be analyzed day) to number
	if time_period=='sunday':
		spec_day=0
	if time_period=='monday':
		spec_day=1
	if time_period=='tuesday':
		spec_day=2
	elif time_period=='wednesday':
		spec_day=3
	elif time_period== 'thursday':
		spec_day=4
	elif time_period=='friday':
		spec_day=5
	elif time_period=='saturday':
		spec_day=6
	# If the user didnt specify any time filter...Beware only chicago file includes this information.
	if time_period=='none' and city_file==chicago_reader:
		my_list=[]
		# For every row ...
		for i in range(len(city_file)):
			# Take its gender value
			a=city_file[i]['Gender']
			# Append it to list
			my_list.append(a)
			# Count how many time each type appear in the list.
		number_male=my_list.count('Male')
		number_female=my_list.count('Female')
		return "Number of female user is {}, number of male user is {}".format(number_female,number_male)
	# If the user specify month time filter. Similar logic is applied. Only chicago file includes this information.
	elif (time_period==('january') or time_period==('february') or time_period==('march') or time_period==('april') or time_period==('may') or time_period==('june')) and city_file==chicago_reader:
		my_list=[]
		for i in range(len(city_file)):
			x=city_file[i]['Start Time']
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			if  y.month==spec_month:
				a=city_file[i]['Gender']
				my_list.append(a)
		number_male=my_list.count('Male')
		number_female=my_list.count('Female')
		return "Number of female user is {}, number of male user is {}".format(number_female,number_male)
	# If the user specify day time filter. Similar logic is applied. Only chicago file includes this information.
	elif (time_period==('sunday') or time_period==('monday') or time_period==('tuesday') or time_period==('wednesday') or time_period==('thursday') or time_period==('friday') or time_period==('saturday')) and city_file==chicago_reader:
		my_list=[]
		for i in range(len(city_file)):
			x=city_file[i]['Start Time']
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			if y.weekday()==spec_day:
				a=city_file[i]['Gender']
				my_list.append(a)
		number_male=my_list.count('Male')
		number_female=my_list.count('Female')
		return "Number of female user is {}, number of male user is {}".format(number_female,number_male)
	else:
		return 'No information available about gender'


def birth_years(city_file, time_period):
	'''
	This function will find the youngest person, oldest person and popular birth years
	Args:
	city_file: This is a list in which elements are dictionary. Actually each row of csv is a dictionary with
	keys are just corresponding column name (str), and values are corresponding values in cell (str)
	Input will be among chicago_reader,new_york_city_reader,washington_reader. Warning: only chicago file includes this information
	time_period: This is a str which indicates filter parameter. For this function it can be month, day, or none
	Returns:
	(str) Birth year of youngest person, oldest person and most popular year in edited format.
	'''

	# The following code assigns filtered month (to be analyzed month) to number
	if time_period=='january':
		spec_month=1
	elif time_period=='february':
		spec_month=2
	elif time_period=='march':
		spec_month=3
	elif time_period=='april':
		spec_month=4
	elif time_period=='may':
		spec_month=5
	elif time_period=='june':
		spec_month=6
	# The following code assigns filtered day (to be analyzed day) to number
	if time_period=='sunday':
		spec_day=0
	if time_period=='monday':
		spec_day=1
	if time_period=='tuesday':
		spec_day=2
	elif time_period=='wednesday':
		spec_day=3
	elif time_period== 'thursday':
		spec_day=4
	elif time_period=='friday':
		spec_day=5
	elif time_period=='saturday':
		spec_day=6
	# If the user didnt specify any time filter. Only chicago file includes this information.
	if time_period=='none' and city_file==chicago_reader:
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Birth Year' value...
			a=city_file[i]['Birth Year']
			# Append it
			my_list.append(a)
		#Delete NaN values (namely '')
		cleaned_list = [x for x in my_list if x != '']
		# Find unique elements of cleaned list
		my_set=set(cleaned_list)
		# Find minimum of this set namely oldest person
		oldest=min(my_set)
		# Find maximum of this set namely youngest person
		youngest=max(my_set)
		# Find popular birth years
		my_dicts={}
		for i in my_set:
			my_dicts[i]=my_list.count(i)
		return "Oldest person born in {}, youngest person born in {}, most frequent users are born in {}".format(oldest,youngest,max(my_dicts, key=my_dicts.get))
	# If the user specify month time filter. Similar logic is applied. Only chicago file includes this information.
	elif (time_period==('january') or time_period==('february') or time_period==('march') or time_period==('april') or time_period==('may') or time_period==('june')) and city_file==chicago_reader:
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# Now, if the month of the above object is same as the specified month...
			if  y.month==spec_month:
				# Take its 'Birth Year' value...
				a=city_file[i]['Birth Year']
				# Append it
				my_list.append(a)
		#Delete NaN values (namely '')
		cleaned_list = [x for x in my_list if x != '']
		# Find unique elements of cleaned list
		my_set=set(cleaned_list)
		# Find minimum of this set namely oldest person
		oldest=min(my_set)
		# Find maximum of this set namely youngest person
		youngest=max(my_set)
		# Find popular birth years
		my_dicts={}
		for i in my_set:
			my_dicts[i]=my_list.count(i)
		return "Oldest person born in {}, youngest person born in {}, most frequent users are born in {}".format(oldest,youngest,max(my_dicts, key=my_dicts.get))
	# If the user specify day time filter. Similar logic is applied. Only chicago file includes this information.
	elif (time_period==('sunday') or time_period==('monday') or time_period==('tuesday') or time_period==('wednesday') or time_period==('thursday') or time_period==('friday') or time_period==('saturday')) and city_file==chicago_reader:
		my_list=[]
		# Every row in city file (which is a dictionary)...
		for i in range(len(city_file)):
			# Take its 'Start Time' value...
			x=city_file[i]['Start Time']
			# Following method changes str to time object
			y=datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
			# Now, if the day of the above object is same as the specified day...
			if y.weekday()==spec_day:
				# Take its 'Birth Year' value...
				a=city_file[i]['Birth Year']
				# Append it
				my_list.append(a)
		#Delete NaN values (namely '')
		cleaned_list = [x for x in my_list if x != '']
		# Find unique elements of cleaned list
		my_set=set(cleaned_list)
		# Find minimum of this set namely oldest person
		oldest=min(my_set)
		# Find maximum of this set namely youngest person
		youngest=max(my_set)
		# Find popular birth years
		my_dicts={}
		for i in my_set:
			my_dicts[i]=my_list.count(i)
		return "Oldest person born in {}, youngest person born in {}, most frequent users are born in {}".format(oldest,youngest,max(my_dicts, key=my_dicts.get))
	else:
		return 'No information available about gender'


def display_data():
	'''Displays five lines of data if the user specifies that they would like to.
	After displaying five lines, ask the user if they would like to see five more,
	continuing asking until they say stop.
	Args:
	none.
	Returns:
	(str) Five rows of chicago.csv
	'''
	# User input and assign it to display variable
	display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')

	# Since there is no specific limitation for city, I choose chicago for specimen.
	chicago_read=open('chicago.csv', newline='')
	chicago_file= csv.reader(chicago_read)
	while display=='yes':
		# While user type yes following code shows next five row of chicago file.
		row1 = next(chicago_file)
		row2=next(chicago_file)
		row3=next(chicago_file)
		row4=next(chicago_file)
		row5=next(chicago_file)
		print(row1)
		print(row2)
		print(row3)
		print(row4)
		print(row5)
		display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')

	chicago_read.close()


def statistics():
	'''Calculates and prints out the descriptive statistics about a city and time period
	specified by the user via raw input.
	Args:
	none.
	Returns:
	none.
	'''
	# Filter by city (Chicago, New York, Washington)
	city = get_city()
	# Remember city variable is just a string, by using if conditions
	# we will find corresponding city file. Between lines 12-22 we read
	# csv file and make it dictionary.
	if city=='chicago':
		city_file=chicago_reader
	elif city=='washington':
		city_file=washington_reader
	elif city=='new york':
		city_file=new_york_city_reader

	# Filter by time period (month, day, none)
	time_period_filter = get_time_period()
	if time_period_filter=='none':
		time_period='none'
	# If it is month, which month?
	if time_period_filter=='month':
		time_period=get_month()
	# If it is day, which day?
	elif time_period_filter=='day':
		time_period=get_day()

	#Up to now, City filter: city_file, Time filter: time_period

	print('Calculating the first statistic...')

	# What is the most popular month for start time?
	if time_period_filter == 'none':
		start_time = time.time()

		result_popular_month=popular_month(city_file)
		print("The most popular month is: {}".format(result_popular_month))

		print("That took %s seconds." % (time.time() - start_time))
		print("Calculating the next statistic...")

	# What is the most popular day of week (Monday, Tuesday, etc.) for start time?
	if time_period_filter == 'none' or time_period_filter == 'month':
		start_time = time.time()

		result_popular_day=popular_day(city_file,time_period)
		print("The most popular day is: {}".format(result_popular_day))

		print("That took %s seconds." % (time.time() - start_time))
		print("Calculating the next statistic...")

	start_time = time.time()
	# What is the most popular hour of day for start time?
	result_popular_hour=popular_hour(city_file,time_period)
	print("The most popular hour is: {}".format(result_popular_hour))

	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	start_time = time.time()

    # What is the total trip duration and average trip duration?
	result_total_trip=trip_duration(city_file,time_period)
	print(result_total_trip)

	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	start_time = time.time()

	# What is the most popular start station and most popular end station?
	result_start_station=popular_start_stations(city_file,time_period)
	result_end_station=popular_end_stations(city_file,time_period)
	print("The most popular start station is: {}".format(result_start_station))
	print("The most popular end station is: {}".format(result_end_station))


	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	start_time = time.time()

	# What is the most popular trip?
	result_popular_trip=popular_trip(city_file,time_period)
	print("The most popular trip is: {}". format(result_popular_trip))


	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	start_time = time.time()

	# What are the counts of each user type?
	result_type=users(city_file,time_period)
	print(result_type)



	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	start_time = time.time()

	# What are the counts of gender?
	result_gender=gender(city_file,time_period)
	print(result_gender)

	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	start_time = time.time()
	# What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
	# most popular birth years?
	result_birth_year=birth_years(city_file,time_period)
	print(result_birth_year)

	print("That took %s seconds." % (time.time() - start_time))

	# Display five lines of data at a time if user specifies that they would like to
	display_data()

	# Restart?
	restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
	if restart.lower() == 'yes':
		statistics()


if __name__ == "__main__":
	statistics()
