

# Year    Leap?
# 1944    True
# 2011    False
# 1986    False
# 1800    False
# 1900    False
# 2000    True
# 2056    True

def isLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True 
    elif year % 400 != 0:
         return False
    else:
        return True

years = [1944, 2011, 1986, 1800, 1900, 2000, 2056]
for year in years:
    print(year, isLeap(year))
    