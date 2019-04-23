#DayDayUpQ2.py
dayfactor = 0.005
dayup = 1

for i in range(365):
    if i % 7 in [0, 6]:
        dayup *= 1 - dayfactor
    else:
        dayup *= 1 +dayfactor 

print("工作日的力量：{:.2f}".format(dayup))