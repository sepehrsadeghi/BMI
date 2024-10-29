#BMI

print('Welcome to our program for counting your BMI')

name1 = input('Enter your name:')
last_name1 = input('Enter your last name:')

#Make better
name = name1.strip()
last_name = last_name1.strip()
name2 = name.capitalize()
last_name2 = last_name.capitalize()

print(f'Dear {name2} {last_name2} complete next procces for counting your BMI')

age = input('Enter your age:')
height = input('Enter your height according to cm:')
Weight = input('Enter your Weight according to kg:')

#Make better
age1 = age.strip()
height1 = height.strip()
Weight1 = Weight.strip()
height1 = float(height1)
Weight1 = float(Weight1)

#Counting
d = height1 ** 2
cnt = (Weight1 / d) * 10000
cnt = round(cnt,1)

#Finally result
print(f'Dear {name2} {last_name2} your BMI in {age1} years old is {cnt}.')
cnt = int(cnt)
if cnt < 18.5:
    print('Your are very thin,you should visit doctor.')
elif 20 < cnt < 23:
    print('Congratulations, you have an ideal weight, try to maintain this weight.')
elif 25 < cnt < 29.9:
    print('You are overweight, start exercising.')   
elif 30 < cnt < 34.9:
    print('You are in fat grade 1.')
elif 35 < cnt < 39.9:
    print('You are in fat grade 2.')
elif 40 < cnt:
    print('You are in fat grade 3.') 