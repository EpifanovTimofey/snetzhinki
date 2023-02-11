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
msn1 = wrap.sprite.add("picture",590,50,"SNOWFLAKE")
msn2 = wrap.sprite.add("picture",650,50,"WATER")
msn3 = wrap.sprite.add("picture",525,50,"fire")
text_coin1 = wrap.sprite.add("picture",55,93,"coin")
fire_coin1 = wrap.sprite.add("picture",515,100,"coin")
fire_coin2 = wrap.sprite.add("picture",525,100,"coin")
fire_coin3 = wrap.sprite.add("picture",535,100,"coin")
snowflake_coin1 = wrap.sprite.add("picture",590,100,"coin")
water_coin1 = wrap.sprite.add("picture",645,100,"coin")
water_coin2 = wrap.sprite.add("picture",655,100,"coin")


@wrap.always(1100)
def create_snezhinki():
    s1 = wrap.sprite.add("picture", random.randint(50, 650), -10,"SNOWFLAKE")
    wrap.sprite.set_angle(s1, random.randint(1, 5))
    snezhinki.append(s1)
    wrap.sprite_text.set_text(text, str(len(snezhinki)))
@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def peretaskivanie1(pos_x, pos_y):
    global s2,msn1,msn2,msn3,player_coin,text1
    if s2 != None:
        if wrap.sprite.get_costume(s2) == "snowflake_fioletovay":
            wrap.sprite.set_costume(s2,"SNOWFLAKE")
        if wrap.sprite.get_costume(s2) == "fire":
            for s in snezhinki:
                if wrap.sprite.is_collide_sprite(s2,s):
                    wrap.sprite.remove(s)
                    snezhinki.remove(s)
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
            wrap.sprite.set_angle(msn1,random.randint(1,5))
            snezhinki.append(msn1)
            msn1 = wrap.sprite.add("picture", 590, 50,"SNOWFLAKE")
            wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)
        if wrap.sprite.is_collide_point(msn2, pos_x, pos_y, True) and player_coin >= 2:
            player_coin -= 2
            wrap.sprite_text.set_text(text1, str(player_coin))
            s2 = msn2
            snezhinki.append(msn2)
            msn2 = wrap.sprite.add("picture", 650, 50,"WATER")
            wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)
        if wrap.sprite.is_collide_point(msn3, pos_x, pos_y, True) and player_coin >= 3:
            player_coin -= 3
            wrap.sprite_text.set_text(text1, str(player_coin))
            s2 = msn3
            msn3 = wrap.sprite.add("picture", 525, 50,"fire")
            wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def voda(pos_x, pos_y):
    for s in snezhinki:
        if wrap.sprite.is_collide_point(s, pos_x, pos_y, True):  # and s != s2:
            wrap.sprite.set_costume(s, "WATER")
            wrap.sprite.set_angle(s, 90)
            break


@wrap.on_mouse_move()
def peretaskivanie2(pos_x, pos_y):
    global s2
    if s2 != None:
        wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)
    # if wrap.sprite.get_costume(s2) == "fire" and wrap.sprite. and s2 != None:
    #     wrap.sprite.remove(s2)
    #     s2 = None
    #     wrap.sprite.remove(s)
    #     snezhinki.remove(s)


@wrap.always()
def morganie():
    global a

    if s2 != None and time.time() - a > wrap.sprite.get_angle(s2)/3:
        a = time.time()
        if wrap.sprite.get_costume(s2) == "SNOWFLAKE":
            wrap.sprite.set_costume(s2, "snowflake_fioletovay")
            return
        if wrap.sprite.get_costume(s2) == "snowflake_fioletovay":
            wrap.sprite.set_costume(s2, "SNOWFLAKE")

@wrap.always(50)
def snezhinka():
    global player_coin,text1
    for s in snezhinki:
        cost = wrap.sprite.get_costume(s)
        if cost == "SNOWFLAKE" and s != s2:
            wrap.sprite.move(s, 0, wrap.sprite.get_angle(s))
        elif cost == "WATER" and s != s2:
            wrap.sprite.move(s, 0, 7)
        visota = wrap.sprite.get_top(s)
        if visota > 600:
            if wrap.sprite.get_costume(s) == "WATER":
                player_coin += 1
                wrap.sprite_text.set_text(text1, str(player_coin))
            wrap.sprite.remove(s)
            snezhinki.remove(s)
            wrap.sprite_text.set_text(text, str(len(snezhinki)))

@wrap.on_key_always(wrap.K_d)
def kod():
    global player_coin,text1
    player_coin += 99
    wrap.sprite_text.set_text(text1, str(player_coin))