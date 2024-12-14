a="hello \nworld"
print(a)
print(type(a),id(a))

b='''hello 
python'''
print(b)
print(a,end="****\n")
# string methods

s="Python's world"
s1=s.upper() #print all letters in upr case
print(s1)
s2=s.lower() #print all letters in lower case
print(s2)
s3=s.title() #print every word starting letter upr case
print(s3)
print(s.upper())

a=True
b=False
print(type(a),type(b), sep="\n")
print(s.isalpha())
print(s.isalnum())
print(s.isdecimal())
print(s[-1:0])gi