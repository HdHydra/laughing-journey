import re

string = "Tiger is the national animal of India"
pattern = "Tiger"
result = re.match(pattern, string).group(0)
print(result)

string = "Tiger born in 12-04-2003 is the 04-06-2000 national animal of India at 04-08-2010"
pattern = r'\d{2}-\d{2}-\d{4}'
result = re.findall(pattern, string)
print(result)

string = "Tiger born in,12-04-2003;is the,04-06-2000,national animal of India at 04-08-2010"
pattern = r'[;,\s]'
result = re.split(pattern, string)
print(result)

string = "Tiger born in 12-04-2003 is the 04-06-2000 national animal of India at 04-08-2010"
pattern = 'India'
replacement = 'England'
result = re.sub(pattern, replacement, string)
print(result)