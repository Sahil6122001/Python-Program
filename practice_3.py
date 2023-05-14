# First Program 




name = input("Enter your Name - ")
greeting = "Good Afternoon"
print(greeting , name)
# Second Program
letter = '''Dear <|Name|>
you are Selected
date : <|Date|>'''
name = input("Enter Your Name")
date = input("Enter the Date")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)

#3 Double Spaces 
st = "you are a good  boy"
doublespaces = st.find("  ")
print(doublespaces)
#4 Replace Spaces
st = "you are a good  boy"
replace = st.replace("  ", " ")
print(st)
#4 Formateed
st = "you are a good boy "
print(st)
sb = "you are \n a good boy"
print (sb)
