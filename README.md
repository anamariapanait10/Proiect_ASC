# XOR encyption & decyption


<!-- Scripts for encryption and decryption with XOR that take as a parameter from the command line a key and a file and perform encryption/decryption using the given key.

Example of valid inputs:

• python encrypt.py password2021 input.txt output

• python decrypt.py output password2021 input_recuperat.txt

Note that the input.txt file is always a text file and the output file is a binary file.
-->
### Numele echipei: **Unbreakables**

### Proiect realizat de: 

    • Panait Ana-Maria (grupa 132)
    • Teodorescu George-Tiberiu (grupa 132)
## Sintaxa valida pentru rularea scripturilor:

    • python encrypt.py password2021 input.txt output
    • python decrypt.py output password2021 input_recuperat.txt

## Mesaj pentru echipa ErrorsGenerators
Din neatenție am pus o cheie necorespunzătoare și am cerut permisiunea domnului profesor să o 
modificăm ca să fie conform cu cerința, fară să difere mult de cea inițială.
De aceea apare modificat fisierul output dupa deadline, în caz ca vă întrebați.

## Partea a doua a proiectului:
**Echipă adversă:** ErrorsGenerators

**Cheia echipei adverse:** c6MnGDupeDHnGk 

### Cerințe:
    
    1. Folosiți fișierul input.txt, output și fișierele sursă de pe pagina github a 
    echipei adverse pentru a afla cheia (dacă cheia este disponibilă undeva pe pagina github a
    echipei adverse, folosiți-o; folosiți-vă de orice mijloace tehnice pentru a descoperi cheia)
    2. Folosiți fișierul output și fișierele sursă de pe pagina github a echipei
    adverse pentru a afla cheia (NU aveți voie să folosiți input.txt)

### Abordarea cerințelor:
 
**Rezlvoare Partea I:**

Pentru rezolvarea primei părți am realizat un script python denumit [xor_cipher_cracker_1.py](./xor_cipher_cracker_1.py), care face XOR între 
caracterele din fisierul **input.txt** și cele din **output**. Caracterele din **output** sunt calculate după formula X ⊕ K = Y, unde  
X este un caracter din **input.txt**, K este carcterul din cheie corespunzator pozitiei lui X, ⊕ este operația XOR, iar
Y este caracterul din **output**. Când efectuăm operația de XOR cu X în ambele părți ale egalității obținem K = X ⊕ Y și
dacă aplicam formula pentru fiecare caracter din fișiere ajungem la un sir de carcatere ce conține cheia repetată.
Dupa aceea, am luat primele 30 de caractere din șirul obținut în care știm sigur că se 
repeta cheia măcar de două ori și maxim de trei ori, deoarece cheia are lungimea între 10 și 15 caractere. 
Apoi am căutat o secvența de lungime între 10 și 15 care să se repete și când am găsit 
una înseamnă că aceea este cheia cautată pe care o scriem apoi în fișierul **key.txt**.

**Rezolvare Partea a II-a:**

Pentru rezolvarea părții a doua am realizat un script python denumit [xor_cipher_cracker_2.py](./xor_cipher_cracker_2.py).
Mai întâi am aflat lungimea cheii, luând în considerare toate variantele posibile (numerele de la 10 la 15), 
iar pentru fiecare împarțim fisierul output în secvente de lungime egala cu cea presupusă, apoi 
calculăm media distantelor Hamming. Lungimea cheii va fi, în majoritatea cazurilor, cea care produce o medie cat mai mică.
Dupa ce am aflat lungimea cheii, vom afla carcterele din cheie. Fisierul **input.txt** 
este unul scris în limba romana, fara diacritice. Astfel, cele mai comune caractere sunt `"abcdefghijklmnopqrtuvwxyz -.,"`. 
Cum lungimea cheii este mică, intuim că, pentru fiecare element al cheii, operatia XOR se va realiza de cele mai multe 
ori cu un caracter din string-ul de mai sus, atunci când este construit **output**. Prin urmare, folosind doar fisierul 
**output**, vom încerca să aflăm caracterul corespunzator pentru fiecare pozitie din cheie. Astfel, contorizăm, 
pentru fiecare pozitie din chieie, de cate ori un elelement din multimea  
`"ABCDEFGHIJKLMNOPQRTUVWXYZabcdefghijklmnopqrtuvwxyz0123456789"` are ca rezultat, în urma operatiei XOR cu un caracter 
din output, un element din multimea `"abcdefghijklmnopqrtuvwxyz -.,"`, iar cheia va fi formată din caracterele pentru 
care contorul este cel mai mare. La final cheia este scisă în fișierul **key.txt**.

## Prima parte a proiectului:

Scripturi pentru encriptarea și decriptarea unui fisier text, folosind operatia XOR. Acestea iau ca 
parametru în linia de comandă o cheie, un fișier input, care urmează să fie encriptat 
și un fișier output, unde se va scrie encriptarea/decriptarea fișierului input, folosind cheia 
și operația XOR.


## Ce este XOR?
XOR (Exclusive OR) este un operator binar care are ca rezultat numărul obținut prin 
disjuncția exclusivă a fiecărei perechi de biți ce apare în reprezentarea binară a operanzilor.
XOR este reprezentat, de obicei, prin simbolul ⊕ pentru că este echivalent cu operația de adunare 
pe numere întregi modulo 2: 

    0 ⊕ 0 = 0
    0 ⊕ 1 = 1
    1 ⊕ 0 = 1
    1 ⊕ 1 = 0

Altfel spus, identifică diferențele din perechile de biți din reprezentarea binară. Daca consideram 0 ca fiind fals și 1 ca fiind adevărat, se observă că A ⊕ B este adevărat dacă și numai dacă unul 
dintre A și B este adevărat.
		
## Proprietăți importante ale operației XOR
    1. A ⊕ B = B ⊕ A
    2. A ⊕ ( B ⊕ C ) = ( A ⊕ B ) ⊕ C
    3. A ⊕ 0 = 0 ⊕ A = A
    4. A ⊕ A = 0

## Algoritmul de baza
Algoritmul de criptare cu XOR este un exemplu de criptare simetrică, unde aceeași cheie este folosită 
atât la encriptarea, cât și la decriptarea unui text. Astfel, pentru a encripta un fișier se poate aplica 
operația XOR între caracterele din acesta și cheia dată, iar pentru decriptare se aplică încă o dată 
operația XOR și se ajunge la textul inițial. Acest fapt rezultă din proprietățiile
operației XOR, după cum se poate vedea în continuare. Fie „key” cheia aleasă și „ch” caracterul curent din textul care trebuie encriptat. 
Atunci pentru fiecare caracter din text vom avea:
    
    caracter encriptat = ch ⊕ key
    caracter decriptat = ch ⊕ key ⊕ key = ch ⊕ (key ⊕ key) = ch ⊕ 0 = ch

## De ce folosim XOR pentru criptare?

### Avantajele folosirii acestei criptări sunt:
- este ușor de implementat și analizat
- este rapidă din punct de vedere computațional
- nu contează între câți operanzi facem XOR și nici în ce ordine
- XOR este o operație „echilibrată”, adică pentru un input de 0 sau 1, folosind o cheie aleatoare,
  sunt șanse egale ca rezultatul să fie 0 sau 1, iar dacă nu este știut inputul și nici cheia 
  nu se poate știi cu certitudine rezultatul
- este greu de spart folosind algoritmul brut de generare a tuturor posibilităților de chei
  
### Dezavantajele sunt:
- criptarea are un nivel de securitate scăzut dacă nu sunt îndeplinite următoarele condiții: o cheie este folosită la o singură criptare 
  și nu este dezvăluită, lungimea ei să fie măcar la fel de mare ca textul de encriptat, iar caracterele din cheie sa fie perfect aleatoare, 
  cum se întampla în cazul dispozitivelor hardware de generare aleatoare a unor numere ce se bazează pe fenomene fizice
  și nu pe algoritmi (HRNG)
- dacă cheia este mai scută decât textul de encriptat și se repetă, codul ar putea fi spart ușor, folosind analiza 
  frecvenței caracterelor din limba română. Cu cât e mai scurtă cheia cu atât e mai ușor de spart cripatarea.
- dacă conținutul textului input poate fi ghicit sau aflat, atunci cheia poate fi descoperită, făcând 
XOR între textul inițial și cel encriptat
  
### Concluzie: 

Algoritmul de encriptare XOR care folosește repetarea cheii este ideal pentru a ascunde informații 
pentru care nu este necesară o securitate ridicată, fiind ușor de implemetat. Dacă informația necesită o
encriptare mai puternică, atunci trebuie respectate cele trei condiții destul de stricte menționate la dezavataje
(prima bulină).

## Prezentarea algoritmului implementat

Algortimul propus realizează criptarea XOR, folosind varianta în care cheia se repetă. Atât pentru encriptare, 
cât și pentru decriptare este folosit același algoritm, ce are la bază operația XOR. Pașii algoritmului principal sunt:
Fiecare caracter din textul input va fi XOR-at cu un caracter din cheie. Astfel, primul caracter din text 
va fi XOR-at cu primul caracter din cheie, iar rezultatul este concatenat la un nou sir de caractere, 
care la final va reprezenta encriptarea sau decriptarea fișierulu input, în funcție de ce script este folosit.
Apoi, al doilea caracter din text va fi XOR-at cu al doilea caracter din cheie, apoi concatenat de șirul de caractere
și tot așa până când se termină textul. Având în vederea lungimea fișierului input este foarte posibil ca
lungimea cheii să fie mai mică decât textul și de aceea o repetăm când se ajunge la finalul ei, prin 
reluarea parcurgerii de la început fără a afecta parcurgerea textului input. Această repetare a cheii
o realizăm folosind operatorul %(lungimea_cheii) care ne va da întotdeauna un indice valid pentru cheie.



## Bibliografie

https://www.geeksforgeeks.org/xor-cipher \
https://stackoverflow.com/questions/1135186/whats-wrong-with-xor-encryption \
https://en.wikipedia.org/wiki/XOR_cipher \
https://en.wikipedia.org/wiki/Hardware_random_number_generator \
https://defendtheweb.net/article/the-xor-cipher \
https://www.tech-faq.com/xor-encryption.html \
https://infosecwriteups.com/the-making-of-the-xor-cipher-794d2e6c964f \
https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_xor_process.htm \
https://www.abhishekshukla.com/python/adventures-in-cryptography-with-python-xor-cipher \
https://www.101computing.net/xor-encryption-algorithm \
https://md5decrypt.net/en/Xor \
https://qvault.io/cryptography/why-xor-in-cryptography/ \
https://weinman.cs.grinnell.edu/courses/CSC161/2019S/homework/xor-cipher.shtml \
https://www.dcode.fr/xor-cipher \
https://stackoverflow.com/questions/20579363/how-to-decrypt-simple-xor-encryption \
https://www.educative.io/edpresso/what-are-xor-encryption-and-decryption \
https://github.com/gcjensen/xor-cipher-cracker