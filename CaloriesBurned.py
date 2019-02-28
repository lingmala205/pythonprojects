def main():

    print('Running on a particular treadmill you burn 4.2 calories per minute.')

    count = 10.0
    
    while count < 35.0:
        calories = count * 4.2
        print('After ', count,' minutes, you have burned ', calories,' calories.')
        count += 5


main()
