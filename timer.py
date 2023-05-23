import time
seconds=input("give the time in seconds ")

def countdown(s):
    min=int(s/60)
    sec=int(s%60)
    timer=f'{min}:{sec}'
    print(timer)
countdown(int(seconds))

