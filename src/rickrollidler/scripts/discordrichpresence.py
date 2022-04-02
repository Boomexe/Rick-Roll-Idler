from pypresence import Presence
from time import sleep

success = False
large_image = 'rick'
print('Started Discord Presence')

while success != True:
    try:
        rpc = Presence('959268149499408434')
        rpc.connect()
        success = True
    except:
        print('Could not connect to discord! Trying again in one minute...')
        sleep(60)

while True:
    try:
        rpc.update(
            details = '*Intensely clicking*',
            state = 'In development...',
            large_image=large_image
        )

    except:
        print('Could not update discord presence!')
    sleep(15)