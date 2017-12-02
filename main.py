from insultName import insultName

def main():
    ready = False
    while ready == False:
        playerName = str(input('What is your name? '))
        insultName(playerName)
        ans = str(input('Are you sure about that? \nY or N: '))
        x = 0
        while x == 0:
            if ans.upper() == 'Y':
                ready = True
                x = 1
            elif ans.upper() == 'N':
                x = 1
                continue
            else:
                print('That wasn\'t one of the options. Try again.')
                ans = str(input('Y or N: '))
                continue


main()

