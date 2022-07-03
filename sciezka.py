# Program znajduje drogę w labiryncie
# Plik z danymi pochodzi ze strony: https://eduinf.waw.pl/inf/alg/001_search/0128.php
#---------------------------
import os
os.system("cls")
#--------------------------
plik=open("labirynt.txt","r")
plikWy=open("labiryntWynik.txt","w")
tab=[]
print("Labirynt na początku")
wiersz=plik.readline()#odczytujemy pierwsza linię
tab.append(wiersz)
n=len(wiersz)-1    # ilość kolumn, -1 bo ostatni znak to \n
m=0 #ilość wierszy
while(wiersz!="*"): 
    wiersz=plik.readline() #odczytujemy kolejne linie
    tab.append(wiersz)
    m+=1
# wyświetlamy labirynt

for i in range (m):
    for j in range(n):
        print(tab[i][j],end=" ")
        if(tab[i][j]=="S"): #Zapamiętujemy położenie S (start)
            xS=i
            yS=j
        if(tab[i][j]=="W"): #Zapamietujemy położenie W (wyjście)
            xW=i
            yW=j
            tab[xW]=tab[xW][0:yW]+"."+tab[xW][yW+1:] # zamieniamy W na "."   
            # w wierszu nr xW podmieniamy znak nr yW   
    print()
# szukamt ścieżki metoda BFS
x=-1 # bieżący wiersz
y=-1 # bieżąca kolumna
kolejka=[]
kolejka.append(xS) #dodajemy do kolejki wierzchołek startowy
kolejka.append(yS)

while(kolejka!=[]):
    x=kolejka.pop(0) #pobieramy z kolejki położenie
    y=kolejka.pop(0)
    if(x==xW and y==yW): #doszliśmy do końca 
        break
    #sprawdzamy sąsiadów
    for i in range(-1,2):   #-1 z góry, 1 z dołu - idziemy po wierszach
        for j in range(-1,2): #-1 z lewej, 1 z prawej - idziemy po kolumnach
            if(i!=j and (i==0 or j==0)): # nie możemy iść po przekątnej - tylko lewo albo prawo albo góra albo dół
                if(tab[x+i][y+j]=="."):
                    if i==-1:  # przyszliśmy z dołu
                        skad="d" 
                    elif i==1:   # przyszliśmyz góry
                        skad="g"
                    elif j==-1:  # przyszliśmy z prawej
                        skad="p" 
                    else:   #przyszliśmy z lewej
                        skad="l"
                    tab[x+i]=tab[x+i][0:y+j]+skad+tab[x+i][y+j+1:] # zamieniamy "."  na znak l,p,g,d,
                    kolejka.append(x+i)
                    kolejka.append(y+j)

print()
# print("Labirynt z kierunkami")
# # wyświetlamy labirynt
# for i in range (m):
#     for j in range(n):
#         print(tab[i][j],end=" ")
#     print()
# print()
print("Labirynt z trasą")

if tab[xW][yW]!=".": # czy doszliśmy do W
    i=xW
    j=yW
    while(i!=xS or j!=yS):
        temp=tab[i][j]
        tab[i]=tab[i][0:j]+"o"+tab[i][j+1:]
        if temp=="g": 
            i-=1
        elif temp=="d":
            i+=1
        elif temp=="l":
            j-=1
        else:
            j+=1

    tab[xW]=tab[xW][0:yW]+"W"+tab[xW][yW+1:] # wstawiamy z powrotem W  
    kierunki=["l","p","g","d"]
    for i in range (m):
        for j in range(n):
            if(tab[i][j] in kierunki):
                tab[i]=tab[i][0:j]+"."+tab[i][j+1:]
            print(tab[i][j],end=" ")
        plikWy.write(tab[i])
        print()
else:
    print("Nie znaleziono ścieżki")
print()
plik.close()
plikWy.close()
