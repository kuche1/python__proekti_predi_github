al = []class a():    name = 'ERROR'    clip = 0#    clipmax = 15    ammo = 0#    ammomax = 150    dmg = 2    fr = 0.1    frt = 'semi'                                                                #'''fire type'''    frat = 0#    rl = 1    rldt = 'all'                                                                #'''reload type'''    rlding = False#    rldat = 0#    speed = 10    d = 9    bps = 1                                                                     #'''bullets per shot'''    inacc = 0.1    explrad = 0                                                                 #'''explode radius'''    remat = 3    clipcost = 5    cost = 100    meledmg = 2    melefr = 1    melefrat = 0#    melespeed = 40    meled = 40    firesound = 'default.wav'    types = ['pistol']class naimilevan(a):    name = '1911 pistol'    clipmax = 9    ammomax = 126    fr = 0.1    frt = 'semi'    rl = 0.9    rldt = 'all'    dmg = 3    inacc = 0.09    cost = 700    clipcost = 5    types = ['pistol']al.append(naimilevan)class grenadepistol(a):    name = 'Grenade pistol'    clipmax = 1    ammomax = 30    rl = 1    speed = 8    d = 4    dmg = 1    bps = 5    inacc = 0.09    explrad = 60    cost = 650    clipcost = 10    types = ['pistol', 'explosive']al.append(grenadepistol)class bullpup(a):    name = 'Bullpup'    clipmax = 30    ammomax = 200    fr = 0.1    frt = 'auto'    rl = 2    rldt = 'all'    inacc = 0.15    cost = 650    clipcost = 30    firesound = 'ak47.wav'    types = ['rifle']al.append(bullpup)class crossbow(a):    name = 'Crossbow'    clipmax = 1    ammomax = 30    fr = 1    speed = 8    d = 8    dmg = 8    inacc = 0.01    explrad = 0    cost = 50    clipcost = 10    types = ['bow']al.append(crossbow)class chainsaw(a):    name = 'Chainsaw'    clipmax = 100    ammomax = 500    fr = 0.04    frt = 'auto'    rl = 5    rldt = 'all'    speed = 40    d = 40    dmg = 1    bps = 1    inacc = 0.4    remat = 0    cost = 500    clipcost = 50    meledmg = 5    types = ['mele']al.append(chainsaw)class deagle(a):    name = 'Desert Eagle'    clipmax = 7    ammomax = 35    fr = 0.3    frt = 'semi'    rl = 1.3    rldt = 'all'    dmg = 5    bps = 1    inacc = 0.2    cost = 300    clipcost = 10    types = ['pistol']al.append(deagle)class emka(a):    name = 'M14'    clipmax = 30    ammomax = 300    fr = 0.1    frt = 'auto'    rl = 1.8    dmg = 3    cost = 2100    clipcost = 40    types = ['rifle']al.append(emka)class shotgun(a):    name = 'Shotgun'    clipmax = 8    ammomax = 32    fr = 0.8    rl = 0.8    rldt = 'one'    d = 5    dmg = 3    bps = 5    inacc = 0.3    cost = 250    clipcost = 8    types = ['shotgun']al.append(shotgun)class lopata(a):    name = 'Lopata'    clipmax = 0    ammomax = 0    fr = 0.5    frt = 'semi'    rldt = 'mele'    speed = 20    d = 60    dmg = 5    remat = 0    cost = 100    clipcost = 0    meledmg = 4    types = ['mele']al.append(lopata)class grenadelauncher(a):    name = 'Grenade Launcher'    clipmax = 1    ammomax = 20    fr = 0    rl = 1.9    speed = 5    d = 20    dmg = 4    inacc = 0.1    explrad = 50    cost = 750    clipcost = 40    types = ['explosive']al.append(grenadelauncher)class aa12(a):    name = 'AA12'    clipmax = 20    ammomax = 150    fr = 0.35    frt = 'auto'    rl = 3    bps = 4    cost = 1500    clipcost = 20    types = ['shotgun']al.append(aa12)class nmm(a):    name = '9mm'    clipmax = 15    ammomax = 150    fr = 0.1    frt = 'semi'     rl = 1    rldt = 'all'     speed = 10    d = 9    dmg = 2    bps = 1                                    inacc = 0.1    explrad = 0                                              remat = 3    cost = 100    clipcost = 5    types = ['pistol']al.append(nmm)class shamar(a):    name = '6amar'    clipmax = 0    ammomax = 0    fr = 0.2    frt = 'semi'    rldt = 'mele'    speed = 20    d = 20    dmg = 8    remat = 0    types = ['mele']al.append(shamar)'''if self.x[x] < player.x:    if self.speed[x] > player.x - self.x[x]:        movx = player.x - self.x[x]    else:        movx = self.speed[x]elif self.x[x] > player.x:    if self.speed[x] > self.x[x] - player.x:        movx = -(self.x[x] - player.x)    else:        movx = -self.speed[x]else:    movx = 0if self.y[x] < player.y:    if self.speed[x] > player.y - self.y[x]:        movy = player.y - self.y[x]    else:        movy = self.speed[x]elif self.y[x] > player.y:    if self.speed[x] > self.y[x] - player.y:        movy = -(self.y[x] - player.y)    else:        movy = -self.speed[x]else:    movy = 0'''