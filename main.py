import wrap, random, time

wrap.world.create_world(700, 600)
wrap.world.set_back_color(30, 25, 200)
wrap.add_sprite_dir("sprite")
snezhinki = []
meteoriti = []
kod = 0
text = wrap.sprite.add_text(str(len(snezhinki)), 40, 40, font_size=80)
text1 = wrap.sprite.add_text("0", 30, 90, font_size=30)
player_coin = 0
s2 = None
a = time.time()
propusk1 = "Yes"
polosa = None
kkorronna = None
coins = 0
click = 0
koroni = []
boss = []
click_sprite = 15
shirina = 200
blok = None
super_snowflake = None
propusk = 0
msn1 = wrap.sprite.add("picture", 590, 50, "SNOWFLAKE")
msn2 = wrap.sprite.add("picture", 650, 50, "WATER")
msn3 = wrap.sprite.add("picture", 525, 50, "fire")
msn4 = wrap.sprite.add("picture", 457, 50, "super_knopka")
msn5 = wrap.sprite.add("picture", 385, 50, "knopka")
msn6 = wrap.sprite.add("picture", 305, 50, "veter")
msn7 = wrap.sprite.add("picture", 240, 50, "vulkan")
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
study3 = wrap.sprite.add("picture", 74, 136, "coin")
study4 = wrap.sprite.add("picture", 30, 213, "korona")
study5 = wrap.sprite.add_text("=", 55, 216, font_size=30)
study6 = wrap.sprite.add_text("6", 72, 217, font_size=28)
study7 = wrap.sprite.add("picture", 90, 218, "coin")
vulkan_text1 = wrap.sprite.add_text("7", 231, 100, font_size=25)
vulkan_coin1 = wrap.sprite.add("picture", 251, 100, "coin")
klick_text1 = wrap.sprite.add_text(str(click_sprite), 30, 175, font_size=30)
klick_sprite1 = wrap.sprite.add("picture", 65, 170, "klick1")
wrap.sprite.set_size(study1, 25, 35)
wrap.sprite.set_size(study3, 26, 26)
wrap.sprite.set_size(study4, 35, 35)
wrap.sprite.set_size(study7, 20, 20)


@wrap.always(800)
def create_snezhinki():
    global blok, super_snowflake, polosa, propusk, kkorronna, propusk1
    if player_coin >= 150 and blok == None and propusk == 0:
        blok = 0
        propusk = 1
        wrap.world.set_back_color(105, 0, 0)
        polosa = wrap.sprite.add("picture", 350, 570, "red_polosa")
        wrap.sprite.set_size(polosa, shirina, 17)
        super_snowflake = wrap.sprite.add("picture", 350, 195, "snowflake_fioletovay")
        kkorronna = wrap.sprite.add("picture", 350, 150, "korona")
        wrap.sprite.set_size(kkorronna, 43, 43)
        qwe = wrap.sprite.add("picture", random.randint(50, 650), -20, "boss_atack1")
        boss.append(qwe)
        qwe = wrap.sprite.add("picture", random.randint(50, 650), -70, "boss_atack1")
        boss.append(qwe)
        qwe = wrap.sprite.add("picture", random.randint(50, 650), -20, "boss_atack1")
        boss.append(qwe)
        qwe = wrap.sprite.add("picture", random.randint(50, 650), -70, "boss_atack1")
        boss.append(qwe)
        qwe = wrap.sprite.add("picture", random.randint(50, 650), -20, "boss_atack1")
        boss.append(qwe)
        if propusk1 == "No":
            qwe = wrap.sprite.add("picture", random.randint(50, 650), -70, "boss_atack1")
            boss.append(qwe)
            qwe = wrap.sprite.add("picture", random.randint(50, 650), -20, "boss_atack1")
            boss.append(qwe)
            qwe = wrap.sprite.add("picture", random.randint(50, 650), -70, "boss_atack1")
            boss.append(qwe)
            qwe = wrap.sprite.add("picture", random.randint(50, 650), -20, "boss_atack1")
            boss.append(qwe)
            qwe = wrap.sprite.add("picture", random.randint(50, 650), -70, "boss_atack1")
            boss.append(qwe)

    if blok == None:
        rand = random.randint(1, 100)
        s1 = wrap.sprite.add("picture", random.randint(50, 650), -10, "SNOWFLAKE")
        wrap.sprite.set_angle(s1, random.randint(1, 5))
        snezhinki.append(s1)
        wrap.sprite_text.set_text(text, str(len(snezhinki)))
        if rand == 100 and click == 15:
            k = wrap.sprite.add("picture", random.randint(50, 650), -10, "korona")
            koroni.append(k)

    if player_coin >= 225 and blok == None and propusk1 == "Yes":
        propusk = 0
        propusk1 = "No"


@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def peretaskivanie1(pos_x, pos_y):
    global s2, msn1, msn2, msn3, player_coin, text1, coins, shirina, blok, polosa, kkorronna, super_snowflake
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
    if s2 == None and super_snowflake != None:
        if wrap.sprite.is_collide_point(super_snowflake, pos_x, pos_y):
            shirina -= 20
            wrap.sprite.set_width(polosa, shirina)
            if shirina < 5:
                blok = None
                wrap.sprite.remove(polosa)
                wrap.sprite.remove(super_snowflake)
                wrap.sprite.remove(kkorronna)
                polosa = None
                kkorronna = None
                super_snowflake = None
                shirina = 200
                wrap.world.set_back_color(30, 25, 200)
        for b in boss:
            if wrap.sprite.is_collide_point(b, pos_x, pos_y, True):
                wrap.sprite.remove(b)
                boss.remove(b)

    if s2 == None and blok == None:
        for s in snezhinki:
            if wrap.sprite.is_collide_point(s, pos_x, pos_y, True) and wrap.sprite.get_costume(s) != "WATER":
                s2 = s
                wrap.sprite.move_to(s2, pos_x + 40, pos_y + 40)
                return
        for k in koroni:
            if wrap.sprite.is_collide_point(k, pos_x, pos_y, True):
                wrap.sprite.remove(k)
                koroni.remove(k)
                player_coin += 6
                wrap.sprite_text.set_text(text1, str(player_coin))
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
        if wrap.sprite.is_collide_point(msn7, pos_x, pos_y) and player_coin >= 7:
            rand0m = random.randint(1, 3)
            player_coin -= 7
            wrap.sprite_text.set_text(text1, str(player_coin))
            m = wrap.sprite.add("picture", random.randint(100, 800), 0, "meteor")
            meteoriti.append(m)
            if rand0m >= 2:
                m = wrap.sprite.add("picture", random.randint(100, 800), 0, "meteor")
                meteoriti.append(m)
            if rand0m == 3:
                m = wrap.sprite.add("picture", random.randint(100, 800), 0, "meteor")
                meteoriti.append(m)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def voda(pos_x, pos_y):
    global click, click_sprite
    if click != 15:
        for s in snezhinki:
            if wrap.sprite.is_collide_point(s, pos_x, pos_y, True) and wrap.sprite.get_costume(s) != "WATER":
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
        rand = random.randint(1, 75)
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
    for b in boss:
        wrap.sprite.move(b, 0, 10)
        if wrap.sprite.get_y(b) == 620:
            wrap.sprite.remove(b)
            boss.remove(b)
            player_coin -= 20
            wrap.sprite_text.set_text(text1, str(player_coin))


@wrap.always()
def meteorit():
    for k in koroni:
        if wrap.sprite.get_costume(k) == "korona":
            wrap.sprite.move(k, random.randint(-5, 5), random.randint(10, 20))
    if len(meteoriti) >= 1:
        for m in meteoriti:
            wrap.sprite.move(m, -5, 10)
            if wrap.sprite.is_collide_any_sprite(m, snezhinki):
                for s in snezhinki:
                    if wrap.sprite.is_collide_sprite(m, s) and wrap.sprite.get_costume(s) != "WATER" and s2 == None:
                        wrap.sprite.set_costume(s, "WATER")
                        wrap.sprite.set_angle(s, 90)
                        width = wrap.sprite.get_width(m)
                        height = wrap.sprite.get_height(m)
                        wrap.sprite.set_size(m, width - 15, height - 15)
            if wrap.sprite.get_y(m) > 700:
                wrap.sprite.remove(m)
                meteoriti.remove(m)


@wrap.on_key_down(wrap.K_d, wrap.K_a, wrap.K_q, wrap.K_s)
def kody(key):
    global player_coin, text1, kod
    if key == wrap.K_q and kod == 0:
        kod += 1
    if key == wrap.K_d and kod == 1:
        player_coin += 99
        wrap.sprite_text.set_text(text1, str(player_coin))
        kod -= 1
    if key == wrap.K_a and kod == 1:
        player_coin += 10
        wrap.sprite_text.set_text(text1, str(player_coin))
        kod -= 1
    if key == wrap.K_s and kod == 1:
        player_coin += 5
        wrap.sprite_text.set_text(text1, str(player_coin))
        kod -= 1
