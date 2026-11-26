ROAD_Y = 1272; RAIL_Y = 1048
BX, BY, BSC = 520, 1292, .4          # Bunny on the fence top rail (children's side, road empty while she is there)
STOP = [None, 520, 480, 520]          # road stop x for ambulance / digger / auto
def bunny_talk_set(): pass
def b_hop(t, h=60, d=.16):
    tl(f'tl.fromTo("#bhop",{{y:0}},{{y:{-h},duration:{d},yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t:.2f});')
def beacon(r, b, glow, t0, t1):
    t = t0
    while t < t1:
        tl(f'tl.set("{r}",{{opacity:1}},{t:.2f}); tl.set("{b}",{{opacity:.35}},{t:.2f}); tl.set("{glow}",{{opacity:.8}},{t:.2f}); tl.set("{r}",{{opacity:.35}},{t+.25:.2f}); tl.set("{b}",{{opacity:1}},{t+.25:.2f}); tl.set("{glow}",{{opacity:0}},{t+.25:.2f});')
        t += .5
    tl(f'tl.set("{glow}",{{opacity:0}},{t1:.2f});')
def prop_spin(t0, t1):
    n = int((t1 - t0) / .06)
    tl(f'tl.fromTo(".prop",{{scaleY:1}},{{scaleY:.15,svgOrigin:"0 0",duration:.03,yoyo:true,repeat:{2*n-1},ease:"none",immediateRender:false}},{t0:.2f});')

def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set(".bub",{opacity:0});')
    tl('gsap.set("#g-trunk",{svgOrigin:"0 -352",rotation:-52}); gsap.set("#g-ear",{svgOrigin:"-90 -380"}); gsap.set("#g-ear2",{svgOrigin:"90 -380"});')
    tl('gsap.set("#kA-armL",{svgOrigin:"-62 -230"}); gsap.set("#kA-armR",{svgOrigin:"62 -230"}); gsap.set("#kB-armL",{svgOrigin:"-60 -232"}); gsap.set("#kB-armR",{svgOrigin:"60 -232"});')
    tl('gsap.set("#garm",{svgOrigin:"0 0",rotation:-80}); gsap.set("#sigG",{opacity:1}); gsap.set("#sigR",{opacity:.25}); gsap.set("#sigGlow",{opacity:0});')
    tl('gsap.set("#plane",{x:-520,y:860}); gsap.set("#amb",{x:-560}); gsap.set("#dig",{x:-700}); gsap.set("#auto",{x:-560}); gsap.set("#clump",{x:832,y:1030,opacity:0});')
    tl('gsap.set("#rbunny",{x:1500}); gsap.set("#darm",{svgOrigin:"60 -230",rotation:0});')
    nb = int(DUR / BEAT)
    tl(f'tl.to("#g-body",{{scaleY:.955,scaleX:1.022,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-head",{{y:9,rotation:2,svgOrigin:"0 -240",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#kA",{{y:-12,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.1);')
    tl(f'tl.to("#kB",{{y:-10,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.33);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.2);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.45);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to(".flw",{{rotation:8,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut",stagger:.1}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    for i, d in enumerate([90, -70, 60]):
        tl(f'tl.fromTo("#cl{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    for k in range(int(DUR / 3)):
        t = 2.2 + k * 3.0
        if t > DUR - 1.5: break
        tl(f'tl.to("#g-ear",{{rotation:-8,duration:.15,yoyo:true,repeat:1}},{t:.2f}); tl.to("#g-ear2",{{rotation:8,duration:.15,yoyo:true,repeat:1}},{t+.12:.2f});')

    # ===== HOOK: Golu honks, a plane zooms LOW over the crossing, gust, Mithu spins
    tl('tl.set("#wHonk",{opacity:1,scale:.85},0); tl.to("#wHonk",{scale:1,duration:.3,ease:"back.out(3)"},0.02);'); honk(0.25, 2)
    t0 = T["plane0"]
    tl(f'tl.fromTo("#plane",{{x:-520,y:980,rotation:-6}},{{x:1700,y:820,rotation:-10,duration:.9,ease:"power1.in",immediateRender:false}},{t0});')
    prop_spin(t0, t0 + 1.0)
    tl(f'tl.set("#speed",{{opacity:1}},{t0+.2}); tl.fromTo("#speed",{{x:-200}},{{x:300,duration:.6,ease:"none",immediateRender:false}},{t0+.2}); tl.set("#speed",{{opacity:0}},{t0+.8});')
    tl(f'tl.to("#g-ear",{{rotation:-24,duration:.12,ease:"power2.out"}},{t0+.35}); tl.to("#g-ear",{{rotation:-14,duration:.07,yoyo:true,repeat:7}},{t0+.47}); tl.to("#g-ear",{{rotation:0,duration:.35,ease:"back.out(2)"}},{t0+1.05});')
    tl(f'tl.to("#g-ear2",{{rotation:26,duration:.12,ease:"power2.out"}},{t0+.4}); tl.to("#g-ear2",{{rotation:16,duration:.07,yoyo:true,repeat:7}},{t0+.52}); tl.to("#g-ear2",{{rotation:0,duration:.35,ease:"back.out(2)"}},{t0+1.1});')
    tl(f'tl.to("#gwrap",{{x:24,rotation:3,svgOrigin:"0 0",duration:.15,ease:"power2.out"}},{t0+.35}); tl.to("#gwrap",{{x:0,rotation:0,duration:.4,ease:"elastic.out(1,.5)"}},{t0+1.0});')
    happy(t0 + .35, t0 + 1.05)
    tl(f'tl.to("#m-all",{{rotation:-360,svgOrigin:"0 -100",duration:.6,ease:"power2.out"}},{t0+.4}); tl.set("#m-all",{{rotation:0}},{t0+1.01});')
    word_out("wHonk", t0 + .9)
    a2 = CUE["a2"]
    word_in("wZoom", a2 - .05); mithu_talk(a2, D["a2"])
    tl(f'tl.to("#mithu",{{rotation:8,svgOrigin:"0 -80",duration:.2,yoyo:true,repeat:3,ease:"sine.inOut"}},{a2:.2f});')
    word_out("wZoom", T["intro"] - .2)
    it = T["intro"]
    word_in("wIntro", it); jump(it + .1); happy(it + .1, it + 1.1)
    tl(f'tl.to("#g-trunk",{{rotation:-30,duration:.25,ease:"back.out(2)"}},{it:.2f}); tl.to("#g-trunk",{{rotation:-12,duration:.2,yoyo:true,repeat:3}},{it+.25:.2f}); tl.to("#g-trunk",{{rotation:0,duration:.3}},{it+1.05:.2f});')
    kids_cheer(it + .2, .9)
    word_out("wIntro", V[0]["g"] - .3)

    # ===== VEHICLES
    names = ["plane", "amb", "dig", "auto"]
    for k, v in enumerate(V):
        sel = "#" + names[k]
        tin, tg, tm, tk, tout = v["in"], v["g"], v["m"], v["k"], v["out"]
        if k == 0:   # the plane loops back and floats across the sky, bobbing, then climbs away
            tl(f'tl.fromTo("#plane",{{x:-520,y:900,rotation:-4}},{{x:560,y:860,rotation:0,duration:1.0,ease:"power2.out",immediateRender:false}},{tin:.2f});')
            n = max(1, int((tout - tin - 1.0) / .5))
            tl(f'tl.to("#plane",{{y:836,duration:.5,yoyo:true,repeat:{n-1},ease:"sine.inOut"}},{tin+1.0:.2f});')
            tl(f'tl.to("#plane",{{x:1750,y:700,rotation:-10,duration:.9,ease:"power2.in"}},{tout:.2f});')
            prop_spin(tin, tout + 1.0)
        else:
            stop = STOP[k]
            tl(f'tl.fromTo("{sel}",{{x:-560}},{{x:{stop},duration:.75,ease:"power3.out",immediateRender:false}},{tin:.2f});')
            squash(f"{sel} .vbody", tin + .72)
            tl(f'tl.to("{sel}",{{x:1650,duration:.6,ease:"power3.in"}},{tout:.2f});')
            if k != 2:
                spin(["", "wA", "", "wU"][k], tin, tin + .75, 2.5); spin(["", "wA", "", "wU"][k], tout, tout + .6, 2.5)
            if k == 1:
                beacon(".abR", ".abB", "#aglow", tin, tout + .7)
            if k == 2:   # rumble + the arm digs on "घर्र घर्र"
                tl(f'tl.to("#dig .vbody",{{y:-5,duration:.06,yoyo:true,repeat:{int((tout-tin)/.12)*2-1}}},{tin:.2f});')
                tl(f'tl.to("#darm",{{rotation:14,svgOrigin:"60 -230",duration:.3,ease:"power2.inOut",yoyo:true,repeat:1}},{tg+.25:.2f});')
                tl(f'tl.set("#dsand",{{opacity:1}},{tg+.55:.2f});')
                # fling: arm lifts, a soft sand puff arcs onto Mithu's head = hat
                fl, ld = v["fling"], v["land"]
                tl(f'tl.to("#darm",{{rotation:-22,svgOrigin:"60 -230",duration:.22,ease:"back.out(2)"}},{fl:.2f}); tl.to("#darm",{{rotation:0,svgOrigin:"60 -230",duration:.4}},{fl+.6:.2f});')
                tl(f'tl.set("#dsand",{{opacity:0}},{fl+.18:.2f}); tl.set("#clump",{{opacity:1}},{fl+.18:.2f});')
                tl(f'tl.fromTo("#clump",{{x:840,y:990,rotation:0}},{{x:866,y:900,rotation:-30,duration:.22,ease:"power2.out",immediateRender:false}},{fl+.18:.2f});')
                tl(f'tl.to("#clump",{{x:882,y:1150,rotation:-50,duration:.2,ease:"power2.in"}},{fl+.4:.2f});')
                tl(f'tl.set("#clump",{{opacity:0}},{ld:.2f}); tl.set("#m-hat",{{opacity:1}},{ld:.2f});')
                tl(f'tl.fromTo("#m-all",{{scaleY:1,scaleX:1}},{{scaleY:.86,scaleX:1.1,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1,immediateRender:false}},{ld:.2f});')
                word_in("wHat", v["hat"] - .05); mithu_talk(v["hat"], D["e4"])
                happy(ld, ld + 1.2); kids_cheer(ld + .05, .8)
                word_out("wHat", tout + .1)
            if k == 3:
                puff("apf", 3, tin + .1, -60, -40); puff("apf", 3, tout, -80, -40)
                tl(f'tl.to("#auto .vbody",{{y:-8,duration:.1,yoyo:true,repeat:3}},{tg+.4:.2f});')
                tl(f'tl.to("#auto .vbody",{{y:-8,duration:.1,yoyo:true,repeat:3}},{tk+.5:.2f});')
        look(-14, tin + (.3 if k else 0)); look(0, tin + 1.0); look(16, tout)
        if k == 0: look(0, tout + .5)
        if k == 0: tl(f'tl.to(".pup",{{y:-10,duration:.2}},{tin+.8:.2f}); tl.to(".pup",{{y:0,duration:.2}},{tout+.4:.2f});')
        word_in(f"wV{k}", tg); pulse(f"#wV{k} .en", tm); pulse(f"#wV{k} .snd", tk)
        happy(tg, tg + .9); jump(tm, 1, -40)
        if k == 1:   # siren: trunk wiggles like a siren
            tl(f'tl.to("#g-trunk",{{rotation:-40,duration:.12,yoyo:true,repeat:5,ease:"sine.inOut"}},{tg+.4:.2f});')
            trunk(0, tg + 1.2, .3, "elastic.out(1,.5)")
        elif k == 2:
            tl(f'tl.to("#gwrap",{{x:6,duration:.05,yoyo:true,repeat:11}},{tg+.5:.2f});')
        elif k == 0:  # trunk points up at the plane
            trunk(-70, tg, .3); trunk(-45, tg + .5, .2); trunk(0, tm + .4, .3, "power2.inOut")
        else:
            honk(tg + .3, 2)
        mithu_talk(tm, D[["c2", "d2", "e2", "f2"][k]])
        kids_cheer(tk, max(.8, D[["c3", "d3", "e3", "f3"][k]] - .3)); kids_talk(tk, D[["c3", "d3", "e3", "f3"][k]])
        kids_wave(tout)
        word_out(f"wV{k}", tout + .1)

    # ===== BUNNY zooms in along the fence top (too fast!), skids, then waits politely
    bn = T["bun"]
    tl(f'tl.fromTo("#rbunny",{{x:1500}},{{x:0,duration:.45,ease:"power3.out",immediateRender:false}},{bn:.2f});')
    tl(f'tl.set("#bspeed",{{opacity:1}},{bn:.2f}); tl.fromTo("#bspeed",{{x:300}},{{x:0,duration:.45,ease:"power3.out",immediateRender:false}},{bn:.2f}); tl.set("#bspeed",{{opacity:0}},{bn+.5:.2f});')
    tl(f'tl.fromTo("#rbunny",{{rotation:0}},{{rotation:-14,svgOrigin:"0 0",duration:.15,ease:"power2.out",immediateRender:false}},{bn+.3:.2f}); tl.to("#rbunny",{{rotation:0,svgOrigin:"0 0",duration:.4,ease:"back.out(3)"}},{bn+.45:.2f});')
    tl(f'tl.to("#b-earL",{{rotation:-20,svgOrigin:"-40 -300",duration:.15}},{bn+.35:.2f}); tl.to("#b-earL",{{rotation:0,svgOrigin:"-40 -300",duration:.5,ease:"elastic.out(1,.4)"}},{bn+.5:.2f});')
    tl(f'tl.to("#b-earR",{{rotation:-16,svgOrigin:"44 -300",duration:.15}},{bn+.4:.2f}); tl.to("#b-earR",{{rotation:0,svgOrigin:"44 -300",duration:.5,ease:"elastic.out(1,.4)"}},{bn+.57:.2f});')
    look(10, bn); look(0, bn + .6)
    word_in("wTurn", CUE["g0"] - .05)
    # paws folded while she waits
    tl(f'tl.to("#b-armL",{{rotation:-30,svgOrigin:"-60 -148",duration:.25}},{T["wait"]-.1:.2f}); tl.to("#b-armR",{{rotation:30,svgOrigin:"60 -148",duration:.25}},{T["wait"]-.05:.2f});')
    tl(f'tl.to("#b-armL",{{rotation:0,svgOrigin:"-60 -148",duration:.25}},{T["recap"]+.3:.2f}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -148",duration:.25}},{T["recap"]+.35:.2f});')
    word_out("wTurn", T["recap"] - .15)

    # ===== RECAP
    rc = T["recap"]
    word_in("wG", rc); jump(rc + .2); happy(rc + .2, rc + 1.2); b_hop(rc + .2, 50)
    tl(f'tl.to("#g-trunk",{{rotation:-30,duration:.25}},{rc:.2f}); tl.to("#g-trunk",{{rotation:0,duration:.3}},{rc+.9:.2f});')
    word_out("wG", T["h1"] - .15)
    for k in range(4):
        tl(f'tl.fromTo("#bub{k}",{{opacity:0,y:60}},{{opacity:1,y:0,duration:.4,ease:"back.out(2.5)",immediateRender:false}},{rc + .3 + k*.12:.2f});')
    for key, pair in (("h1", (0, 1)), ("h2", (2, 3)), ("h3", (0, 1)), ("h4", (2, 3))):
        t0 = T[key]; step = D[key] / 2.2
        if key == "h3":
            tl(f'tl.set(".bh",{{opacity:0}},{t0-.05:.2f}); tl.set(".be",{{opacity:1}},{t0-.05:.2f});')
        for j, k in enumerate(pair):
            tl(f'tl.fromTo("#bub{k}",{{y:0}},{{y:-28,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t0 + j*step:.2f});')
            b_hop(t0 + j * step, 40)
        kids_talk(t0, D[key])
    kids_cheer(T["h4"] + D["h4"] - .4, .6); bunny_cheer(T["h4"] + D["h4"] - .4, .6)
    lastb = T["end"] - .2
    for k in range(4):
        tl(f'tl.to("#bub{k}",{{opacity:0,y:40,duration:.25}},{lastb + k*.05:.2f});')

    # ===== END
    en = T["end"]
    word_in("wJ", en); pulse("#wJ .en", T["k2"]); happy(en + .1, en + 1.2)
    tl(f'tl.to("#g-trunk",{{rotation:-35,duration:.25,ease:"back.out(2)"}},{en:.2f}); tl.to("#g-trunk",{{rotation:-15,duration:.25,yoyo:true,repeat:5}},{en+.25:.2f}); tl.to("#g-trunk",{{rotation:0,duration:.25}},{en+1.75:.2f});')
    mithu_talk(T["k2"], D["k2"]); kids_wave(en + .3); kids_wave(T["k2"] + .4); jump(T["k2"], 1, -40)
    tl(f'tl.to("#rbunny",{{x:-2100,duration:.45,ease:"power3.in"}},{en+.6:.2f});')
    tl(f'tl.set(".conf",{{opacity:1}},{en:.2f});')
    for k in range(36):
        x = (k * 97) % 1080
        tl(f'tl.fromTo("#cf{k}",{{x:{x},y:-80,rotation:0}},{{y:{1500 + (k*53) % 400},x:{x + ((k*37) % 160) - 80},rotation:{360 + k*20},duration:{2.0 + (k % 5)*.15:.2f},ease:"power1.in",immediateRender:false}},{en + (k % 8)*.05:.2f});')
    tl(f'tl.set(".conf",{{opacity:0}},{min(en + 2.9, DUR - .9):.2f});')
    word_out("wJ", DUR - .85)
    lp = DUR - .8
    tl(f'tl.to("#m-hat",{{opacity:0,y:-30,duration:.3}},{lp:.2f});')
    trunk(-52, lp + .1, .35, "power2.out"); look(0, lp)
    tl(f'tl.fromTo("#wHonk",{{opacity:0,scale:.5}},{{opacity:1,scale:.85,duration:.3,ease:"power2.out",immediateRender:false}},{DUR-.35:.2f});')
    bt = 2.6
    while bt < DUR - 1:
        tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{bt:.2f});')
        tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{bt+1.1:.2f});')
        tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{bt+.6:.2f});')
        tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{bt+1.6:.2f});')
        bt += 3.4
    def lipsync(levels, mouth, rest, origin, scales):
        L = list(levels)
        for i in range(1, len(L) - 1):
            if L[i] and not L[i-1] and not L[i+1]: L[i] = 0
        prev = 0
        for i, v in enumerate(L):
            if v == prev: continue
            t = round(i / lips["fps"], 3)
            if v == 0: tl(f'tl.set("{mouth}",{{opacity:0}},{t});tl.set("{rest}",{{opacity:1}},{t});')
            else: tl(f'tl.set("{mouth}",{{opacity:1,scaleY:{scales[v]},svgOrigin:"{origin}"}},{t});tl.set("{rest}",{{opacity:0}},{t});')
            prev = v
    lipsync(lips["golu"], "#g-mouth", "#g-smile", "-62 -314", [0, .5, .8, 1.1])
    lipsync(lips["bunny"], "#b-mouth", "#b-smile", "0 -204", [0, .55, .8, 1.05])
def bunny_cheer(t, hold=.8):
    tl(f'tl.to("#b-armL",{{rotation:120,svgOrigin:"-60 -148",duration:.18,ease:"back.out(2)"}},{t:.2f}); tl.to("#b-armR",{{rotation:-120,svgOrigin:"60 -148",duration:.18,ease:"back.out(2)"}},{t+.06:.2f});')
    tl(f'tl.to("#b-armL",{{rotation:0,svgOrigin:"-60 -148",duration:.3}},{t+hold:.2f}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -148",duration:.3}},{t+hold+.06:.2f});')
