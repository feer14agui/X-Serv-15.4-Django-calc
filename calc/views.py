from django.shortcuts import render

# Create your views here.

def suma (request, num1, num2):

	sum = int(num1) + int(num2)

	return HttpResponse ("El resultado es " + str(sum))

def resta (request, num1, num2):

	rest =  int(num1) - int(num2)

	return HttpResponse ("El resultado es " + str(rest)

def multiplicacion (request, num1, num2):

	mult =  int(num1) * int(num2)

	return HttpResponse ("El resultado es " + str(mult)

def division (request, num1, num2):

	div =  int(num1) / int(num2)

	return HttpResponse ("El resultado es " + str(div)
