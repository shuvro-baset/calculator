from django.contrib.gis.measure import D, Distance

def inches():
	value = input('Enter your inches values: ')
	inch = D(inch=value)
	#feet = inch.ft
	print(inch.ft,'Foot')
	print(inch.km,'Kilometre')
	print(inch.mi,'Mile')
	print(inch.cm,'Centimeter')
	print(inch.m,'Meter')
	print(inch.yd,'Yard')
	print(inch.inch,'Inches')
#inches()
def centimeter():
	value = input('Enter your centimeter values: ')
	centimeter = D(cm=value)
	print(centimeter.ft,'Foot')
	print(centimeter.km,'Kilometre')
	print(centimeter.mi,'Mile')
	print(centimeter.cm,'Centimeter')
	print(centimeter.m,'Meter')
	print(centimeter.yd,'Yard')
	print(centimeter.inch,'Inches')
#centimeter()
def feet():
	value = input('Enter your feet values: ')
	feet = D(ft=value)
	print(feet.ft,'Foot')
	print(feet.km,'Kilometre')
	print(feet.mi,'Mile')
	print(feet.cm,'Centimeter')
	print(feet.m,'Meter')
	print(feet.yd,'Yard')
	print(feet.inch,'Inches')
#feet()
def meters():
	value = input('Enter your meters values: ')
	meters = D(m=value)
	print(meters.ft,'Foot')
	print(meters.km,'Kilometre')
	print(meters.mi,'Mile')
	print(meters.cm,'Centimeter')
	print(meters.m,'Meter')
	print(meters.yd,'Yard')
	print(meters.inch,'Inches')
#meters()
def kilometers():
	value = input('Enter your kilometers values: ')
	kilometers = D(km=value)
	print(kilometers.ft,'Foot')
	print(kilometers.km,'Kilometre')
	print(kilometers.mi,'Mile')
	print(kilometers.cm,'Centimeter')
	print(kilometers.m,'Meter')
	print(kilometers.yd,'Yard')
	print(kilometers.inch,'Inches')
#kilometers()
def yards():
	value = input('Enter your yards values: ')
	yards = D(yd=value)
	print(yards.ft,'Foot')
	print(yards.km,'Kilometre')
	print(yards.mi,'Mile')
	print(yards.cm,'Centimeter')
	print(yards.m,'Meter')
	print(yards.yd,'Yard')
	print(yards.inch,'Inches')
#yards()
def miles():
	value = input('Enter your miles values: ')
	miles = D(mi=value)
	print(miles.ft,'Foot')
	print(miles.km,'Kilometre')
	print(miles.mi,'Mile')
	print(miles.cm,'Centimeter')
	print(miles.m,'Meter')
	print(miles.yd,'Yard')
	print(miles.inch,'Inches')
miles()

'''
km	Kilometre, Kilometer
mi	Mile
m	Meter, Metre
yd	Yard
ft	Foot, Foot (International)
survey_ft	U.S. Foot, US survey foot
inch	Inches
cm	Centimeter
mm	Millimetre, Millimeter
um	Micrometer, Micrometre
'''
#centimeter
#feet
#meters
#kilometers
#inches
#yards
#miles