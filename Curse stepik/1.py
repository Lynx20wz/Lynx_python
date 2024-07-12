time = int(input())
hours_in_sleep = int(input())*60
minuts_in_sleep = int(input())
print((time + hours_in_sleep + minuts_in_sleep)//60)
print((time + hours_in_sleep + minuts_in_sleep)%60)