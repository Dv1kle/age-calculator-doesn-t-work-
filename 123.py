import datetime
# Step 2
birth_day = int(input("Day of birth: "))
birth_month = int(input("Month of birth: "))
birth_year = int(input("Year of birth: "))
day = int(datetime.date.today().day)
month = int(datetime.date.today().month)
year = int(datetime.date.today().year)
# Step 3
if birth_month > month  :
 age = (year - birth_year) - 1
else :
    age = year - birth_year 
# Step 4
month1 = abs(month - birth_month)
if birth_month > 9 :
 month1 = abs(birth_month / month)
day1 = (day - birth_day)
print("Your age: {0} years, {1} months, {2} days".format(age,month1,day1))