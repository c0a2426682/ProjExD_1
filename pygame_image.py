import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kouka_img = pg.image.load("fig/3.png")
    kouka_img = pg.transform.flip(kouka_img,True,False)
    kouka_rct = kouka_img.get_rect()
    kouka_rct.center = 300,200
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kouka_x = -1
        kouka_y = 0
        x = tmr % 3200
        screen.blit(bg_img, [0-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kouka_img,kouka_rct)
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kouka_y -= 1
        if key_lst[pg.K_DOWN]:
            kouka_y += 1
        if key_lst[pg.K_LEFT]:
            kouka_x -= 1
        if key_lst[pg.K_RIGHT]:
            kouka_x += 2
        kouka_rct.move_ip((kouka_x,kouka_y))
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()