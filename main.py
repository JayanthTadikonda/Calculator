import re
import string

print("My first project")
print("quit to exit")

previous = 0
run = True


def performcal():
    global run
    global previous
    if previous == 0:
        equation = input("Enter the equation:")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("See ya Human!")
        run = False
    else:
        equation = re.sub('[A-Za-z,.:" " ]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performcal()



