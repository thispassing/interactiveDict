import time

print("hello")
# while 2 != 1:
time.sleep(1)
print("hello again")
time.sleep(1)


# need to find a way to break the loop, don't run it yet

def sleeper():
    while True:
        # Get user input
        num = input('How long to wait: ')
 
        # Try to convert it to a float
        try:
            num = float(num)
        except ValueError:
            print('Please enter in a number.\n')
            continue
 
        # Run our time.sleep() command,
        # and show the before and after time
        print('Before waiting: %s' % time.ctime())
        time.sleep(num)
        print('After waiting: %s\n' % time.ctime())
        exit()
 
try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()