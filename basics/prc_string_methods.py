#string methods
st='he is Going to office NO:123'
sl=st.lower()
print(sl) #it prints all letters in lower case
su=st.upper()
print(su) #it prints all letters in lower case
ss=st.strip()
print(ss) # it removes white space both ends
s1=st.isalpha()
print(s1) # it is checking given charecters alpha or not
s2=st.isdigit()
print(s2)
s3=st.isnumeric()
print(s3)
s4=st.rjust(35,"*")
print(s4) #Returns a right justified version of the string
s5=st.capitalize()
print(s5) #Converts the first character to upper case
s6=st.casefold()
print(s6)
s7=st.ljust(35,"*")
print(s7) #Returns a left justified version of the string
s8=st.split()
print(s8) #Splits the string at the specified separator, and returns a list
s9=st.center(40,"*")
print(s9)  #Returns a centered string
s10=st.count("1")
print(s10)
s11=st.find("is")
print(s11) #Searches the string for a specified value and returns the position of where it was found
sformat='{} is going io office No:{}'
sf=sformat.format("venky","10")
print(sf)
s12=st.index("1")
print(s12)
st_num="venky"
print(st_num.isnumeric())
print(st_num.isalpha())
title_st=st.title() #Converts the first character of each word to upper case
print(title_st)
