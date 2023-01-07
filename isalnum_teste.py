


import re
app = "12/@@!~~ão//>dd"
cleanString = re.sub('\W+','', app )
print(cleanString)