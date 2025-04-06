a=1
print(f'We are in {__name__}.py')
if __name__=='__main__':
    while True:
        print('Enter your age:')
        age = input()
        try:
            age = int(age)
        except:
            print('Please use numeric digits.')
            continue
        if age < 1:
            print('Please enter a positive number.')
            continue

        print(f'Age={age}')
        break

