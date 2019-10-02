Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> filename = open("/Users/Maxim/Desktop/Apps/Work Apps/Python Prog/file.txt","r")
>>> with filename as f:
	text = f.read()

	
>>> print(text)
Hello World!
>>> def count_char(text, char):
	count = 0
	for c in text:
		if c == char:
			count+=1
	return count

>>> print(count_char(text, "e"))
1
>>> print(count_char(text, "H"))
1
>>> print(count_char(text, "L"))
0
>>> print(count_char(text, "l"))
3
>>> for char in "abcdefghijkmnopqrstuvwxyz":
	perc = 100* count_char(text, char) / len(text)
	print("{0} - {1}%".format(char,round(perc, 2)))

	
a - 0.0%
b - 0.0%
c - 0.0%
d - 8.33%
e - 8.33%
f - 0.0%
g - 0.0%
h - 0.0%
i - 0.0%
j - 0.0%
k - 0.0%
m - 0.0%
n - 0.0%
o - 16.67%
p - 0.0%
q - 0.0%
r - 8.33%
s - 0.0%
t - 0.0%
u - 0.0%
v - 0.0%
w - 0.0%
x - 0.0%
y - 0.0%
z - 0.0%
>>> for char in "abcdefghijklmnopqrstuvwxyz":
	perc = 100* count_char(text, char) / len(text)
	print("{0} - {1}%".format(char,round(perc, 2)))

	
a - 0.0%
b - 0.0%
c - 0.0%
d - 8.33%
e - 8.33%
f - 0.0%
g - 0.0%
h - 0.0%
i - 0.0%
j - 0.0%
k - 0.0%
l - 25.0%
m - 0.0%
n - 0.0%
o - 16.67%
p - 0.0%
q - 0.0%
r - 8.33%
s - 0.0%
t - 0.0%
u - 0.0%
v - 0.0%
w - 0.0%
x - 0.0%
y - 0.0%
z - 0.0%
>>> 
