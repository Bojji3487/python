a=1
if __name__=='_main_':
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

