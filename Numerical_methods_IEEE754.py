import re

def factorization(number):
	i = 0
	container = []
	result = abs(number) / (2**i)

	if(number == 0):
		print('No possible results. End of task.')
		exit()
	else:
		while(result > 2.0):
			i += 1
			result = abs(number) / (2**i)
			if(number > 0):
				container = [result, i]
			else:
				container = [result*(-1), i]
	return container

def mantissa(number):
    mantissa = []
    while(number != 0):
        if(number % 2 == 0):
            mantissa.append(0)
        else:
            mantissa.append(1)
        number = int(number / 2.0)
    return mantissa

def characteristic(number):
    final_characteristic = []
    n = 23 # characteristic's lenght, can be chosen

    while(len(final_characteristic) < n):
        container = re.split(r'[,|;.""]', str(number))
        final_characteristic.append(int(re.split(r'[,|;.""]', str(int(container[1]) / (10**len(str(container[1]))) * 2))[0]))
        number = int(container[1]) / (10**len(str(container[1])))*2

    return final_characteristic

number_str = input("Enter a float number: ")

# sign verification ------------------------
sign = int('-' in number_str)

number = float(number_str.replace(',','.'))
container = factorization(number)
sum_ = 127 + container[1]

# mantissa ---------------------------------------
mantissa_txt = (''.join(str(i) for i in mantissa(sum_)))[::-1]

# characteristic -----------------------------------------
characteristic = characteristic(container)
characteristic_txt = ''.join(str(i) for i in characteristic)

# result -----------------------------------------
print('sign\t mantissa\t characteristic')
print(sign,'\t',mantissa_txt,'\t',characteristic_txt)
