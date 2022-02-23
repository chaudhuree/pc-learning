# age = int(input('enter your age:'))
age=26
age > 18 and print('adult')

if age > 18 and age < 21:
    print('you can play')
else:
    print('you can not play')

# logical or
# day = input('enter day:')
day="saturday"
if day == 'friday' or day == 'saturday':
    print('it is weekend')
else:
    print('it is not weekend')
# logical Not
year = input('enter your birth year:')
if not year.isnumeric():
    year=input('enter a year in the form of number:')

print(f"your birth year is: {year}, your age is: {2022-int(year)}")