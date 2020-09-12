#from django.contrib.gis.measure import W, Weight
from measurement.measures import Weight, Volume

def kilograms():
	value = input('Enter your kilograms values: ')
	kg = Weight(kg=value)
	print(kg.kg,'Kilograms')
	print(kg.g,'Grams')
	print(kg.lb,'Pounds')
	print(kg.oz,'Ounces')
	print(kg.tonne,'Tons')
#Kilograms()
def grams():
	value = input('Enter your grams values: ')
	grams = Weight(g=value)
	print(grams.kg,'Kilograms')
	print(grams.g,'Grams')
	print(grams.lb,'Pounds')
	print(grams.oz,'Ounces')
	print(grams.tonne,'Tons')
#grams()
def ounces():
	value = input('Enter your ounces values: ')
	ounces = Weight(oz=value)
	print(ounces.kg,'Kilograms')
	print(ounces.g,'Grams')
	print(ounces.lb,'Pounds')
	print(ounces.oz,'Ounces')
	print(ounces.tonne,'Tons')
#ounces()
def pounds():
	value = input('Enter your pounds values: ')
	pounds = Weight(lb=value)
	print(pounds.kg,'Kilograms')
	print(pounds.g,'Grams')
	print(pounds.lb,'Pounds')
	print(pounds.oz,'Ounces')
	print(pounds.tonne,'Tons')
#pounds()
def tons():
	value = input('Enter your tons values: ')
	tons = Weight(tonne=value)
	print(tons.kg,'Kilograms')
	print(tons.g,'Grams')
	print(tons.lb,'Pounds')
	print(tons.oz,'Ounces')
	print(tons.tonne,'Tons')
tons()
'''
kilograms kg
grams g
ounces oz
pounds lb
tons tonne
'''