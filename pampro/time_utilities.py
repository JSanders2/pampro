from datetime import datetime, date, time, timedelta

def start_of_day(datetimestamp):
	''' Trim the excess hours, minutes, seconds and microseconds off a datetime stamp '''
	start = datetimestamp - timedelta(hours=datetimestamp.hour, minutes=datetimestamp.minute, seconds=datetimestamp.second, microseconds=datetimestamp.microsecond)
	return start

def end_of_day(datetimestamp):
	''' Add the excess hours, minutes, seconds and microseconds onto a datetime stamp '''
	end = datetimestamp + timedelta(hours=23-datetimestamp.hour, minutes=59-datetimestamp.minute, seconds=59-datetimestamp.second, microseconds=999999-datetimestamp.microsecond)
	return end

def start_of_hour(datetimestamp):
	''' Trim the excess minutes, seconds and microseconds off a datetime stamp '''
	start = datetimestamp - timedelta(minutes=datetimestamp.minute, seconds=datetimestamp.second, microseconds=datetimestamp.microsecond)
	return start

def end_of_hour(datetimestamp):
	''' Add the excess minutes, seconds and microseconds onto a datetime stamp '''
	end = datetimestamp + timedelta(minutes=59-datetimestamp.minute, seconds=59-datetimestamp.second, microseconds=999999-datetimestamp.microsecond)
	return end