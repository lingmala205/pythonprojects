def main():

    while True:
        try:
            x = float(input('Enter a number:'))
            break
        except ValueError:
            print('Oops! Invalid. Try again!')

main()
