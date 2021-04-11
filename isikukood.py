# 47610112243 - True в задании
# 47211999275 - False
# 57211999276 - False
# 30209210034 - False
# 30204140793 - True
# Это женцина, его/ее день рождения 11.10.1976  и место рождения Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi).


Truelist = []
Falselist = []

try:
    n = 9
    for i in range(n+1):
        while True:
            print("".center(71, "="))
            print(f"| Try: {i + 1} |".center(71, "-"))
            print("".center(71, "="))
            print()

            try:

                isikukood = list(str(input("-> Введите свой личный код: ")))

                if len(isikukood) != 11:
                    continue

                if int(isikukood[0]) <= 6:
                    if int(isikukood[0]) == 1 or int(isikukood[0]) == 3 or int(isikukood[0]) == 5:
                        sugu = "Mees"
                    else:
                        sugu = "Naine"

                if int(isikukood[1]) <= 9 and int(isikukood[2]) <= 9:
                    if int(isikukood[0]) <= 4:
                        aastat = isikukood[1:3]
                        aastat = "19" + "".join(aastat)
                    else:
                        aastat = isikukood[1:3]
                        aastat = "20" + "".join(aastat)

                if int(isikukood[3]) <= 9 and int(isikukood[4]) <= 9:
                    kuu = str(isikukood[3]) + str(isikukood[4])
                    if int(kuu) <= 12:
                        pass
                    else:
                        pass

                if int(isikukood[5]) <= 9 and int(isikukood[6]) <= 9:
                    day = str(isikukood[5]) + str(isikukood[6])
                    if int(day) <= 31:
                        pass
                    else:
                        pass

                if int(isikukood[7]) <= 9 and int(isikukood[8]) <= 9 and int(isikukood[9]) <= 9:

                    kood = isikukood[7] + isikukood[8] + isikukood[9]

                    # 50209200284

                    ikood = ""

                    for i in kood:
                        if kood[0] == "0" and kood[1] == "0" and kood[2] != "0":
                            if i == "0":
                                continue
                            ikood += i

                        if kood[0] == "0" and kood[1] != "0" and kood[2] == "0":
                            kood = list(kood)
                            kood = kood[1:3]
                            kood = "".join(kood)
                            ikood += kood
                            break

                        if kood[0] == "0" and kood[1] != "0" and kood[2] != "0":
                            kood = list(kood)
                            kood = kood[1:3]
                            kood = "".join(kood)
                            ikood += kood
                            break

                        if kood[0] != "0":
                            ikood += i


                    if 0 <= int(ikood) <= 700:

                        if int(ikood) <= 10:
                            haigla = "Kuressaare haigla"

                        if 11 <= int(ikood) <= 19:
                            haigla = "Tartu Ülikooli Naistekliinik"

                        if 21 <= int(ikood) <= 150:
                            haigla = "Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)"

                        if 151 <= int(kood) <= 160:
                            haigla = "Keila haigla"

                        if 161 <= int(kood) <= 220:
                            haigla = "Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)"

                        if 221 <= int(kood) <= 270:
                            haigla = "Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)"

                        if 271 <= int(kood) <= 370:
                            haigla = "Maarjamõisa kliinikum (Tartu), Jõgeva haigla"

                        if 371 <= int(kood) <= 420:
                            haigla = "Narva haigla"

                        if 421 <= int(kood) <= 470:
                            haigla = "Pärnu haigla"

                        if 471 <= int(kood) <= 490:
                            haigla = "Haapsalu haigla"

                        if 491 <= int(kood) <= 520:
                            haigla = "Järvamaa haigla (Paide)"

                        if 521 <= int(kood) <= 570:
                            haigla = "Rakvere haigla, Tapa haigla"

                        if 571 <= int(kood) <= 600:
                            haigla = "Valga haigla"

                        if 601 <= int(kood) <= 650:
                            haigla = "Viljandi haigla"

                        if 651 <= int(kood) <= 700:
                            haigla = "Lõuna-Eesti haigla (Võru), Põlva haigla"

                # 1 × 3 + 2 × 7 + 3 × 6 + 4 × 0 + 5 × 5 + 6 × 0 + 7 × 3 + 8 × 0 + 9 × 2 + 1 × 9 = 108.
                # 30209210034

                kontrollikood = 0

                k = 1
                for i in isikukood[:-1]:
                    if k == 10:
                        k = 1
                    result = int(i) * k
                    kontrollikood += result
                    k += 1

                kontrollikood = kontrollikood % 11

                print(f"----> {sugu=}, {aastat=}, {kuu=}, {day=}, {ikood=}, {kood=}, {kontrollikood=}")
                print(f"-------> Это {sugu}, его/ее день рождения {day}.{kuu}.{aastat} "
                          f"и место рождения {haigla}")
                print()

                if sugu == "Mees" or sugu == "Naine":

                    if int(isikukood[1]) <= 9 and int(isikukood[2]) <= 9:
                        pass

                        if int(day) <= 31:
                            pass

                            if int(kuu) <= 12:
                                pass

                                if int(kuu) <= 12:

                                    if int(isikukood[7]) <= 9 and int(isikukood[8]) <= 9 and int(isikukood[9]) <= 9:
                                            if int(isikukood[-1]) == kontrollikood:
                                                Truelist.append("".join(isikukood))
                                            else:
                                                Falselist.append("".join(isikukood))

                                    else:
                                        Falselist.append("".join(isikukood))

                                else:
                                    Falselist.append("".join(isikukood))

                            else:
                                Falselist.append("".join(isikukood))

                        else:
                            Falselist.append("".join(isikukood))

                    else:
                        Falselist.append("".join(isikukood))

                else:
                    Falselist.append("".join(isikukood))

                break



            except:
                pass

except:
    print("Непральное первое число: от 1 до 6")

print("".center(71, "="))
print("| Finally |".center(71, "-"))
print("".center(71, "="))
print()

count = 1

print("Правильный личный код: ")
for i in Truelist:
    print(f"---> {count}. {i}")
    count += 1

print()

count1 = 1
print("Неправильный личный код: ")
for j in Falselist:
    print(f"---> {count1}. {j}")
    count1 += 1

if len(Falselist) ==  0:
          print("---> Список пуст")

print()
