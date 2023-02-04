import wrap, random, time

wrap.world.create_world(700, 600)
wrap.world.set_back_color(30, 25, 200)
wrap.add_sprite_dir("sprite")
snezhinki = []
text = wrap.sprite.add_text(str(len(snezhinki)), 40, 40, font_size=80)
s2 = None
a = time.time()


@wrap.always(1000)
def create_snezhinki():
    s1 = wrap.sprite.add("picture", random.randint(50, 650), -10)
    wrap.sprite.set_angle(s1, random.randint(1, 5))
    snezhinki.append(s1)
    wrap.sprite_text.set_text(text, str(len(snezhinki)))


@wrap.always(50)
def snezhinka():
    for s in snezhinki:
        cost = wrap.sprite.get_costume(s)
        if cost == "SNOWFLAKE" and s != s2:
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
        if wrap.sprite.is_collide_point(s, pos_x, pos_y, True):  # and s != s2:
            wrap.sprite.set_costume(s, "WATER")
            wrap.sprite.set_angle(s, 90)
            break


@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def peretaskivanie1(pos_x, pos_y):
    global s2
    if s2 != None:
        if wrap.sprite.get_costume(s2) == "snowflake_fioletovay":
            wrap.sprite.set_costume(s2,"SNOWFLAKE")
        s2 = None
        return
    for s in snezhinki:
        if wrap.sprite.is_collide_point(s, pos_x, pos_y, True) and wrap.sprite.get_costume(s) != "WATER":
            s2 = s
            wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)
            return


@wrap.on_mouse_move()
def peretaskivanie2(pos_x, pos_y):
    if s2 != None:
        wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)


@wrap.always()
def morganie():
    global a
    # if s2 != None and time.time() - a > 1:
    #     wrap.sprite.set_costume(s2, "snowflake_fioletovay")
    if s2 != None and time.time() - a > wrap.sprite.get_angle(s2)/3:
        a = time.time()
        if wrap.sprite.get_costume(s2) == "SNOWFLAKE":
            wrap.sprite.set_costume(s2, "snowflake_fioletovay")
            return
        if wrap.sprite.get_costume(s2) == "snowflake_fioletovay":
            wrap.sprite.set_costume(s2, "SNOWFLAKE")
