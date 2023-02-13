import wrap, random, time

wrap.world.create_world(700, 600)
wrap.world.set_back_color(30, 25, 200)
wrap.add_sprite_dir("sprite")
snezhinki = []
text = wrap.sprite.add_text(str(len(snezhinki)), 40, 40, font_size=80)
text1 = wrap.sprite.add_text("0", 30, 90, font_size=30)
player_coin = 0
s2 = None
a = time.time()
coins = 0
click = 0
click_sprite = 15
msn1 = wrap.sprite.add("picture", 590, 50, "SNOWFLAKE")
msn2 = wrap.sprite.add("picture", 650, 50, "WATER")
msn3 = wrap.sprite.add("picture", 525, 50, "fire")
msn4 = wrap.sprite.add("picture", 457, 50, "super_knopka")
msn5 = wrap.sprite.add("picture", 385, 50, "knopka")
msn6 = wrap.sprite.add("picture", 305, 50, "veter")
text_coin1 = wrap.sprite.add("picture", 55, 93, "coin")
fire_coin1 = wrap.sprite.add("picture", 515, 100, "coin")
fire_coin2 = wrap.sprite.add("picture", 525, 100, "coin")
fire_coin3 = wrap.sprite.add("picture", 535, 100, "coin")
veter_coin1 = wrap.sprite.add("picture", 313, 100, "coin")
snowflake_coin1 = wrap.sprite.add("picture", 590, 100, "coin")
water_coin1 = wrap.sprite.add("picture", 645, 100, "coin")
water_coin2 = wrap.sprite.add("picture", 655, 100, "coin")
super_knopka_coin1 = wrap.sprite.add("picture", 470, 100, "coin")
super_knopka_text1 = wrap.sprite.add_text("10", 445, 100, font_size=25)
knopka_coin1 = wrap.sprite.add("picture", 397, 100, "coin")
knopka_text1 = wrap.sprite.add_text("4", 377, 100, font_size=25)
study1 = wrap.sprite.add("picture", 30, 131, "WATER")
study2 = wrap.sprite.add_text("=", 52, 135, font_size=25)
study3 = wrap.sprite.add("picture", 74, 136)
klick_text1 = wrap.sprite.add_text(str(click_sprite), 30, 175, font_size=30)
klick_sprite1 = wrap.sprite.add("picture", 65, 170, "klick1")
wrap.sprite.set_size(study1, 25, 35)
wrap.sprite.set_size(study3, 26, 26)


@wrap.always(800)
def create_snezhinki():
    if player_coin <= 300:
        s1 = wrap.sprite.add("picture", random.randint(50, 650), -10, "SNOWFLAKE")
        wrap.sprite.set_angle(s1, random.randint(1, 5))
        snezhinki.append(s1)
        wrap.sprite_text.set_text(text, str(len(snezhinki)))
    else:
        wrap.sprite.add_text("Поздравляю! Ты прошёл игру!", random.randint(0, 700), random.randint(0, 600),font_size=50)


@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def peretaskivanie1(pos_x, pos_y):
    global s2, msn1, msn2, msn3, player_coin, text1, coins
    if s2 != None:
        if wrap.sprite.get_costume(s2) == "snowflake_fioletovay":
            wrap.sprite.set_costume(s2, "SNOWFLAKE")
        if wrap.sprite.get_costume(s2) == "fire":
            for s in snezhinki:
                if wrap.sprite.is_collide_sprite(s2, s):
                    wrap.sprite.set_costume(s, "WATER")
                    wrap.sprite.set_angle(s, 90)
            wrap.sprite.remove(s2)
        s2 = None
        return

    if s2 == None:
        for s in snezhinki:
            if wrap.sprite.is_collide_point(s, pos_x, pos_y, True) and wrap.sprite.get_costume(s) != "WATER":
                s2 = s
                wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)
                return
        if wrap.sprite.is_collide_point(msn1, pos_x, pos_y, True) and player_coin >= 1:
            player_coin -= 1
            wrap.sprite_text.set_text(text1, str(player_coin))
            s2 = msn1
            wrap.sprite.set_angle(msn1, random.randint(1, 5))
            snezhinki.append(msn1)
            msn1 = wrap.sprite.add("picture", 590, 50, "SNOWFLAKE")
            wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)
        if wrap.sprite.is_collide_point(msn2, pos_x, pos_y, True) and player_coin >= 2:
            player_coin -= 2
            wrap.sprite_text.set_text(text1, str(player_coin))
            s2 = msn2
            snezhinki.append(msn2)
            msn2 = wrap.sprite.add("picture", 650, 50, "WATER")
            wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)
        if wrap.sprite.is_collide_point(msn3, pos_x, pos_y, True) and player_coin >= 3:
            player_coin -= 3
            wrap.sprite_text.set_text(text1, str(player_coin))
            s2 = msn3
            msn3 = wrap.sprite.add("picture", 525, 50, "fire")
            wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)
        if wrap.sprite.is_collide_point(msn4, pos_x, pos_y) and player_coin >= 10:
            player_coin -= 10
            wrap.sprite_text.set_text(text1, str(player_coin))
            for s in snezhinki:
                wrap.sprite.set_costume(s, "WATER")
                wrap.sprite.set_angle(s, 90)
        if wrap.sprite.is_collide_point(msn5, pos_x, pos_y) and player_coin >= 4:
            player_coin -= 4
            wrap.sprite_text.set_text(text1, str(player_coin))
            for s in snezhinki:
                if wrap.sprite.get_costume(s) == "WATER":
                    player_coin = player_coin
                if wrap.sprite.get_costume(s) == "SNOWFLAKE":
                    wrap.sprite.set_costume(s, "WATER")
                    wrap.sprite.set_angle(s, 90)
                    coins += 1
                    if coins == 6:
                        coins = 0
                        return
        if wrap.sprite.is_collide_point(msn6, pos_x, pos_y) and player_coin >= 1:
            player_coin -= 1
            wrap.sprite_text.set_text(text1, str(player_coin))
            for s in snezhinki:
                x1 = wrap.sprite.get_right(s)
                if wrap.sprite.get_costume(s) == "SNOWFLAKE":
                    wrap.sprite.move(s, 30, -8)
                if wrap.sprite.get_costume(s) == "WATER":
                    wrap.sprite.move(s, 35, 4)
                if x1 > 700:
                    wrap.sprite.move_right_to(s, 700)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def voda(pos_x, pos_y):
    global click, click_sprite
    if click != 15:
        for s in snezhinki:
            if wrap.sprite.is_collide_point(s, pos_x, pos_y, True) and wrap.sprite.get_costume(
                    s) != "WATER":  # and s != s2:
                wrap.sprite.set_costume(s, "WATER")
                wrap.sprite.set_angle(s, 90)
                click += 1
                click_sprite -= 1
                wrap.sprite_text.set_text(klick_text1, str(click_sprite))
                break


@wrap.on_mouse_move()
def peretaskivanie2(pos_x, pos_y):
    global s2
    if s2 != None:
        wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)


@wrap.always()
def morganie():
    global a

    if s2 != None and time.time() - a > wrap.sprite.get_angle(s2) / 3:
        a = time.time()
        if wrap.sprite.get_costume(s2) == "SNOWFLAKE":
            wrap.sprite.set_costume(s2, "snowflake_fioletovay")
            return
        if wrap.sprite.get_costume(s2) == "snowflake_fioletovay":
            wrap.sprite.set_costume(s2, "SNOWFLAKE")


@wrap.always(50)
def snezhinka():
    global player_coin, text1, blokirovka
    for s in snezhinki:
        rand = random.randint(1, 50)
        cost = wrap.sprite.get_costume(s)
        if cost == "SNOWFLAKE" and s != s2:
            wrap.sprite.move(s, 0, wrap.sprite.get_angle(s))
        elif cost == "WATER" and s != s2:
            wrap.sprite.move(s, 0, 7)
            if wrap.sprite.is_collide_any_sprite(s, snezhinki) and rand == 75:
                player_coin += 1
                wrap.sprite_text.set_text(text1, str(player_coin))
        visota = wrap.sprite.get_top(s)
        if visota > 600:
            if wrap.sprite.get_costume(s) == "WATER":
                player_coin += 1
                wrap.sprite_text.set_text(text1, str(player_coin))
            wrap.sprite.remove(s)
            snezhinki.remove(s)
            wrap.sprite_text.set_text(text, str(len(snezhinki)))


@wrap.on_key_down(wrap.K_d)
def kody():
    global player_coin, text1
    player_coin += 99
    wrap.sprite_text.set_text(text1, str(player_coin))
