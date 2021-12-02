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

## Descriere proiect:

Scripturi pentru encriptarea și decriptarea unui fisier text, folosind operatia XOR. Acestea iau ca 
parametru în linia de comandă o cheie, un fișier input, care urmează să fie encriptat 
și un fișier output, unde se va scrie encriptarea/decriptarea fișierului input, folosind cheia 
și operația XOR.



## Sintaxa valida pentru rularea scripturilor:

    • python encrypt.py password2021 input.txt output
    • python decrypt.py output password2021 input_recuperat.txt

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
https://www.educative.io/edpresso/what-are-xor-encryption-and-decryption