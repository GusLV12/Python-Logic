from datetime import datetime

ageMain = datetime.now().year

def ageYear(calculateAge):
  age = ageMain - calculateAge
  return age

initAge = int(input("Enter your birth year: "))
print(f'Your age is: {ageYear(initAge)}')