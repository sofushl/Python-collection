

def horse(speed, jump, health, m=None):
    return (speed/14.23) + (jump/5.25) + (health/(20 if m else 30))

while True:
    speed = input("speed: ")
    jump = input("jump: ")
    health = input("health: ")

    print(horse(speed,jump,health)/3)