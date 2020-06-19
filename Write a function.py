def is_leap(year):
    leap = False
    leap1=True
    
    # Write your logic here
    if year%400==0:
        return leap1
    if year%100==0:
        return leap
    if year%4==0:
        return leap1
    else:
        return leap            
    
    return leap

year = int(input())
print(is_leap(year))