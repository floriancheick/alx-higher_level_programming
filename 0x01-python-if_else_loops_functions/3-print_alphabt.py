#!/usr/bin/python3
for item in range(ord('a'), ord('z') + 1):
    if item == ord('e') or item == ord('q'):
        continue
    print('{}'.format(chr(item)), end='')
