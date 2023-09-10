from machine import Pin
import time
import random
                  
left = Pin(13, Pin.IN)
right = Pin(15 , Pin.IN)

road = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '0', '.'],
]

t0 = time.ticks_ms()
move_t0 = time.ticks_ms()
score = 0
time_interval = 1000

def move(direction:str) -> None:
    
    move = {'left':-1, 'right':1}.get(direction)
    boundary = {'left': 0, 'right':2}.get(direction)
    car_index = road[-1].index('0')
    global move_t0
    
    if time.ticks_diff(time.ticks_ms(), move_t0) > time_interval and car_index != boundary: 
        move_t0 = time.ticks_ms()
        road[-1][car_index] = '.'
        road[-1][car_index+move] = '0'

def display_road() -> None:
    for i in road:
        print(i)
    print()
    
    
while True:
    if not left.value():
         move('left')
    
    if not right.value():
        move('right')
        
    if time.ticks_diff(time.ticks_ms(), t0) > time_interval:
        t0 = time.ticks_ms()
        
        new_row = ['.', '.']
        new_row.insert(random.randint(0, 2), 'x')
        road.insert(0, new_row)
        
        if 'x' in road[-2]:
            enemy_index = road[-2].index('x')
            car_index = road[-1].index('0')
        
            if car_index == enemy_index:
                print(f'GAME OVER: score = {score}')
                break
            road[-1][enemy_index] = 'x'
        score += 1
        time_interval -= score
            
        del road[-2]
        display_road()