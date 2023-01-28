import wrap, random

wrap.world.create_world(700, 600)
wrap.world.set_back_color(30, 25, 200)
wrap.add_sprite_dir("sprite")
snezhinki = []
text = wrap.sprite.add_text(str(len(snezhinki)), 40, 40, font_size=80)
s2 = None

@wrap.always(500)
def create_snezhinki():
    s1 = wrap.sprite.add("picture", random.randint(50, 650), -10)
    wrap.sprite.set_angle(s1, random.randint(1, 5))
    snezhinki.append(s1)
    wrap.sprite_text.set_text(text, str(len(snezhinki)))


@wrap.always(50)
def snezhinka(pos_x, pos_y):
    for s in snezhinki:
        cost = wrap.sprite.get_costume(s)
        if cost == "SNOWFLAKE":
            wrap.sprite.move(s, 0, wrap.sprite.get_angle(s))
        elif cost == "WATER":
            wrap.sprite.move(s, 0, 7)
        visota = wrap.sprite.get_top(s)
        if visota > 600:
            wrap.sprite.remove(s)
            snezhinki.remove(s)
            wrap.sprite_text.set_text(text, str(len(snezhinki)))


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def voda(pos_x, pos_y):
    for s in snezhinki:
        if wrap.sprite.is_collide_point(s, pos_x, pos_y, True):
            wrap.sprite.set_costume(s, "WATER")
            wrap.sprite.set_angle(s, 90)
            break

@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def peretaskivanie1(pos_x,pos_y):
    global s2
    for s in snezhinki:
        if wrap.sprite.is_collide_point(s, pos_x, pos_y, True):
            s2 = s

@wrap.on_mouse_move()
def peretaskivanie2(pos_x, pos_y):
    global s2
    if s2 != None:
        wrap.sprite.move_to(s2, pos_x, pos_y)

