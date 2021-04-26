#Task1 “Good day <name>! <day> is a perfect day to learn some python.”
name = 'Artur'
day = 'Monday'
s = 'Good day {}! {} is a perfect day to learn some python'
print(s.format(name,day))

#Task 2Manipulate strings.ask 2 anipulate strings.
first_name = 'Artur'
last_name = 'Novoskoltsev'
first_name = first_name.upper()
full_name = first_name + ' ' + last_name
print(f'Hello, {full_name}!')

#Task 3nUsing python as a calculator.
'''Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division'''

a=12
b=10
print('Subtraction', a+b)
print('Division', a-b)
print('Multiplication', a*b)
print('Exponent', a/b)
print('Modulus', a**b)
print('Floor division', a//b)

#"000012 Василий 110110 32.10"
print('{:0>6d} {} {:b} {:.2f}\n'.format(12,"Василий",54,32.1))

#Попробуйте взять какое то одно слово в переменную и "собрать" из него другие слова. Например взяли слово "Корован"
s= 'Корован'
print(s[4],s[3],s[2],s[1],s[6],s[5], sep='')
