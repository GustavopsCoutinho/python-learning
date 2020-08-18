import time
import sys
indent = 0
try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.
except KeyboardInterrupt:
    sys.exit()