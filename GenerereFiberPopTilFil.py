from math import *
from random import *

#Lage modeller
def modellereRVEsnitt():  # Lage fiber populasjon
    coord = list()  # liste for aa holde koordinatene, koordinatene lagres til coordpath
    books = list()  # liste for aa vite fremgangen paa iterasjonene i  prosessen
    Iterasjonsflag = 0
    fVfforrige = 0
    nplassert = 0.0  # antall fiber plassert
    nkrasj = 0  # antall krasj
    sidepunkt = 0
    hjornepunkt = 0
    senterpunkt = 0
    while nplassert < nf:
        frem = countsjikt(coord) / nf  # Forlopig fremdrift - antall fibersenter som finnes i RVE/totalt antall fiber (nf)
        fvf = frem * Vf  # Forlopig volumfraksjon

        # se om fiberutplasseringa har mott iterasjonsgrene for krasj og fibere skal shake up
        if nkrasj > iterasjonsgrense:
            # reset systemet for nytt forsok paa utplassering.
            if fVfforrige == fvf:
                Iterasjonsflag = Iterasjonsflag + 1
            if Iterasjonsflag > 5:
                Iterasjonsflag = 0
                coord = shakeitdown(coord)

            else:
                coord = shakeitdown(coord)
            fVfforrige = fvf
            nkrasj = 0

        # genererer nye fiberkoordinater"
        if nf <= 1:
            x = 0.0
            y = 0.0
        else:
            x = dL * random() - dL * 0.5
            y = dL * random() - dL * 0.5
        # sjekke krasj mot tidligere fiber, at avstand mot hjornet er utenfor eller innenfor doedsonegrensene for hjornet og at avstand fra sidene er over og under doedsonegrensene for kantene.
        if not krasj(x, y, coord) and (sqrt((dL / 2-abs(x)) ** 2 + (dL / 2- abs(y)) ** 2) > ytredodgrense or sqrt((dL / 2-abs(x)) ** 2 + (dL / 2- abs(y)) ** 2) < indredodgrense) and (abs(x)>dL/2-indredodgrense or abs(x)<dL/2-ytredodgrense):
            if ishjornep(x, y):  # Er koordinatet i hjornesone?
                # Krasjer dette hjornepunktet med fiber i de andre hjornene?
                if x < 0 and y < 0 and not krasj(x, y, coord) and not krasj(x + dL, y, coord) and not krasj(x,y+dL, coord) and not krasj(x + dL, y + dL, coord):
                    coord.append([x, y])
                    coord.append([x + dL, y])
                    coord.append([x, y + dL])
                    coord.append([x + dL, y + dL])
                    hjornepunkt = hjornepunkt + 1
                    nplassert = nplassert + 1
                    printprog(coord, fvf, nkrasj, books)
                    Iterasjonsflag = 0
                elif x >= 0 and y < 0 and not krasj(x, y, coord) and not krasj(x - dL, y, coord) and not krasj(x,y + dL,coord) and not krasj(x - dL, y + dL, coord):
                    coord.append([x, y])
                    coord.append([x - dL, y])
                    coord.append([x, y + dL])
                    coord.append([x - dL, y + dL])
                    hjornepunkt = hjornepunkt + 1
                    nplassert = nplassert + 1
                    printprog(coord, fvf, nkrasj, books)
                    Iterasjonsflag = 0
                elif x < 0 and y >= 0 and not krasj(x, y, coord) and not krasj(x + dL, y, coord) and not krasj(x,
                                                                                                               y - dL,
                                                                                                               coord) and not krasj(
                        x + dL, y - dL, coord):
                    coord.append((x, y))
                    coord.append((x + dL, y))
                    coord.append((x, y - dL))
                    coord.append((x + dL, y - dL))
                    hjornepunkt = hjornepunkt + 1
                    nplassert = nplassert + 1
                    printprog(coord, fvf, nkrasj, books)
                    Iterasjonsflag = 0
                elif x >= 0 and y >= 0 and not krasj(x, y, coord) and not krasj(x - dL, y, coord) and not krasj(x,
                                                                                                                y - dL,
                                                                                                                coord) and not krasj(
                        x - dL, y - dL, coord):
                    coord.append([x, y])
                    coord.append([x - dL, y])
                    coord.append([x, y - dL])
                    coord.append([x - dL, y - dL])
                    hjornepunkt = hjornepunkt + 1
                    nplassert = nplassert + 1
                    printprog(coord, fvf, nkrasj, books)
                    Iterasjonsflag = 0
                else:
                    nkrasj = nkrasj + 1


            # Kan koordinatet vere et sidepunkt? Krasjer det med punkter paa motsatt side?
            elif issidep(x, y):
                if x > dL / 2 - indredodgrense and not krasj(x - dL, y, coord):
                    coord.append([x, y])
                    coord.append([x - dL, y])
                    nplassert = nplassert + 1
                    printprog(coord, fvf, nkrasj, books)
                    Iterasjonsflag = 0
                    sidepunkt = sidepunkt + 1

                elif x < -dL / 2 + indredodgrense and not krasj(x + dL, y, coord):
                    coord.append([x, y])
                    coord.append([x + dL, y])
                    nplassert = nplassert + 1
                    printprog(coord, fvf, nkrasj, books)
                    Iterasjonsflag = 0
                    sidepunkt = sidepunkt + 1

                elif y > dL / 2 - indredodgrense and not krasj(x, y - dL, coord):
                    coord.append([x, y])
                    coord.append([x, y - dL])
                    nplassert = nplassert + 1
                    printprog(coord, fvf, nkrasj, books)
                    Iterasjonsflag = 0
                    sidepunkt = sidepunkt + 1
                    # print ("topp punkt")

                elif y < -dL / 2 + indredodgrense and not krasj(x, y + dL, coord):
                    coord.append([x, y])
                    coord.append([x, y + dL])
                    nplassert = nplassert + 1
                    printprog(coord, fvf, nkrasj, books)
                    Iterasjonsflag = 0
                    sidepunkt = sidepunkt + 1
                else:
                    nkrasj = nkrasj + 1

            #senterpunkt
            elif abs(y) < dL/2-ytredodgrense and abs(x) < dL/2-ytredodgrense:
                coord.append([x, y])
                nplassert = nplassert + 1
                senterpunkt = senterpunkt + 1
                printprog(coord, fvf, nkrasj, books)
                Iterasjonsflag = 0
        else:
            nkrasj = nkrasj + 1
        books.append(nplassert)  # keeping record of amount of tries
    g = open(coordpath, "w")
    for l in range(0, len(coord)):
        g.write(str(coord[l][0]) + '\t' + str(coord[l][1]))
        if l < (len(coord)-1):
            g.write('\n')
    g.close()
    del Iterasjonsflag
    del fVfforrige
    del nplassert  # antall fiber plassert
    del nkrasj  # antall krasj
    del coord
    del books

#Stotte funsjoner til modellere RVE
def countsjikt(coord):
    i_sjikt = 0.0
    for i in range(len(coord)):
        if abs(coord[i][0]) <= dL / 2 and abs(coord[i][1]) <= dL / 2:
            i_sjikt = i_sjikt + 1.0
    return i_sjikt
def krasj(x, y, coord):
    for c in coord:
        xp, yp = c[0], c[1]
        if sqrt((x - xp) ** 2 + (y - yp) ** 2) < 2 * (r + rtol):
            return True

    return False
def issidep(x, y):
    if abs(x) > dL / 2 - indredodgrense and abs(y) < dL / 2 - ytredodgrense:
        return True
    elif abs(x) < dL / 2 - ytredodgrense and abs(y) > dL / 2 - indredodgrense:
        return True
    return False
def ishjornep(x, y):
    if abs(x) > dL / 2 - indredodgrense and abs(y) > dL / 2 - indredodgrense:
        return True
    else:
        return False
def shakeitdown(coord):
    for k in range(0, 20):
        t = 0
        for c in coord:
            i = list()
            i.append([dL * 2, dL * 2])
            x, y = c[0], c[1]
            if dL / 2 - ytredodgrense > abs(x) and dL / 2 - ytredodgrense > abs(y):
                coord[t] = i[0]
                for j in range(0, 100):
                    xp, yp = [x + wiggle * random() - wiggle * 0.5, y + wiggle * random() - wiggle * 0.65]
                    if not krasj(xp, yp, coord) and dL / 2 - ytredodgrense > abs(
                            xp) and dL / 2 - ytredodgrense > abs(yp):
                        coord[t] = [xp, yp]
                        break
                    coord[t] = [x, y]
            t = t + 1
    return coord
def shakeitrand(coord):
    for k in range(0, 20):
        t = 0
        for c in coord:
            i = list()
            i.append([dL * 2, dL * 2])
            x, y = c[0], c[1]
            if dL / 2 - ytredodgrense > abs(x) and dL / 2 - ytredodgrense > abs(y):
                coord[t] = i[0]
                for j in range(0, 100):
                    xp, yp = [x + wiggle * random() - wiggle * 0.5, y + wiggle * random() - wiggle * 0.5]
                    if not krasj(xp, yp, coord) and dL / 2 - ytredodgrense > abs(
                            xp) and dL / 2 - ytredodgrense > abs(yp):
                        coord[t] = [xp, yp]
                        break
                    coord[t] = [x, y]
            t = t + 1  # moves to next fiber no matter moved or not
    return coord
def printprog(coord,fvf,nkrasj,books):
    print 'Fiber added! Fiber =', countsjikt(coord), 'av nf = ', nf, 'Koordinater = ', len(coord),' Vf = ',round(
        fvf, 3), ' av ', Vf, ' Krasjes:', nkrasj, 'Tries:', len(books)

GitHub ='C:/Multiscale-Modeling/'
parameterpath = GitHub+'Parametere.txt'

f = open(parameterpath, 'r')
tekst = f.read()

f.close()
lines = tekst.split('\n')
print lines[1]+'\n'
data = lines[1].split('\t')
Q, r, nf, Vf, wiggle, coordpath,iterasjonsgrense, rtol, gtol = float(data[0]),float(data[1]),float(data[2]), float(data[3]), float(data[4]),data[5],float(data[6]), float(data[7]), float(data[8])

#str(Q) + '\t' + str(r) + '\t' + str(nf) + '\t' + str(Vf) + '\t' + str(wiggle) + '\t' + coordpath + '\t' + str(iterasjonsgrense) + '\t' + str(rtol) + '\t' +str(gtol)+ '\t' +str(dL)
dL = ((nf * pi * r ** 2) / (Vf)) ** 0.5
seed(Q)
ytredodgrense = r + gtol
indredodgrense = r - gtol

modellereRVEsnitt()