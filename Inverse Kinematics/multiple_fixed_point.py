from Vector_Lib import Vec2
import pygame
import inverse_kinematics as ik
import tentacle

#colors
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

fixed_point = Vec2(width/2, height)

def main():

    num_segments = 4
    length = 40

    tentacle_list = [
        tentacle.tentacle(Vec2(width/2, 0), num_segments, length),
        tentacle.tentacle(Vec2(width, height/2), num_segments, length),
        tentacle.tentacle(Vec2(width/2, height), num_segments, length),
        tentacle.tentacle(Vec2(0, height/2), num_segments, length),
    ]

    target = Vec2(0,0)
    velocity = Vec2(0.8,0.5)
    gravity = Vec2(0, 0.2)

    run = True
    while run:

        target = target.add(velocity)
        velocity = velocity.add(gravity)

        if target.y > height:
            target.y = height
            velocity.y = velocity.y * -1
            velocity.y *= 0.95

        if target.x < 0 or target.x > width:
            velocity.x *= -1

        run = handle_events(pygame.event.get())
        screen.fill(black)
        render(tentacle_list, target)
        pygame.display.update()



def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            return False
    return True


def render(arr, target):
    #x,y = pygame.mouse.get_pos()
    for tentacle in arr:
        tentacle.update(target)

    for tentacle in arr:

        for segment in tentacle.segments:
            pygame.draw.line(screen, white, [segment.a.x, segment.a.y],[segment.b.x, segment.b.y], 5)

    pygame.draw.circle(screen, red, [target.x, target.y], 10)



main()