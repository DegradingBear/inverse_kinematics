from Vector_Lib import Vec2
import pygame
import inverse_kinematics as ik

#colors
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

def main():

    segment_list = []
    for i in range(10):
        segment_list.append(ik.segment(Vec2(0,0), 90, 30))

    run = True
    while run:
        run = handle_events(pygame.event.get())
        screen.fill(black)
        render(segment_list)
        pygame.display.update()


def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            return False
    return True


def render(arr):
    x,y = pygame.mouse.get_pos()
    arr[-1].follow(Vec2(x,y))

    length = len(arr)
    i = length-2
    while i >= 0:
        arr[i].follow(arr[i+1].a)
        i -= 1

    for segment in arr:
        pygame.draw.line(screen, white, [segment.a.x, segment.a.y],[segment.b.x, segment.b.y], 5)


if __name__ == "__main__":
    main()