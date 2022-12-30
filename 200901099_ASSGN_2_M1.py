import re
Regular_exp =input ("INPUT A VALID REGEX\n")
expression = re.split('\s|(\w)',Regular_exp)
print ("\n OUTPUT TAGS : \n",list(filter(None, expression)))