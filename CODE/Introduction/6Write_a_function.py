def is_leap(year):
    leap = False
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    return False

year = int(input())
print(is_leap(year))

#Otro code 
def is_leap(year):
    leap = False
    if (year%4==0) and (year%100!=0)or year%400=0):
        leap=True

year = int(input())
print(is_leap(year))

#Otro code 
def is_leap(year):
    leap = False
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False
        leap=True

year = int(input())
print(is_leap(year))
