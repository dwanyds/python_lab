print("print leap years between two given years")
start_year=int(input("Enter the start year"))
end_year=int(input("enter the last year"))
print("list of leap years")
for year in range(start_year,end_year):
    if(0==year%4)and(0!=year%100)or(0==year%400):
        print(year)
