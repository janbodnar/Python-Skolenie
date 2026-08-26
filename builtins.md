# Vstavané funkcie Pythonu

Python obsahuje množstvo funkcií, ktoré sú dostupné kdekoľvek vo vašom kóde bez nutnosti importovať žiadne moduly . Sú zoskupené podľa oblastí použitia.

#### **1. Práca s číslami a matematika**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`abs(x)`** | Vráti absolútnu hodnotu čísla. Pre komplexné čísla vráti veľkosť (magnitúdu) . | `abs(-5)` vráti `5`; `abs(3+4j)` vráti `5.0`. |
| **`divmod(a, b)`** | Vráti dvojicu čísel `(podiel, zvyšok)` po celočíselnom delení . | `divmod(10, 3)` vráti `(3, 1)`. |
| **`max(iterable, *[, key, default])`**<br/>**`max(arg1, arg2, *args[, key])`** | Vráti najväčšiu položku z iterovateľného objektu alebo z dvoch a viac argumentov . | `max([1, 5, 2])` vráti `5`; `max(3, 7, 2)` vráti `7`. |
| **`min(iterable, *[, key, default])`**<br/>**`min(arg1, arg2, *args[, key])`** | Vráti najmenšiu položku z iterovateľného objektu alebo z dvoch a viac argumentov . | `min([1, 5, 2])` vráti `1`; `min(3, 7, 2)` vráti `2`. |
| **`pow(base, exp[, mod])`** | Vráti `base` umocnenú na `exp`. Ak je zadané `mod`, vráti výsledok modulo `mod` . | `pow(2, 3)` vráti `8`; `pow(2, 3, 5)` vráti `3` (pretože `8 % 5 = 3`). |
| **`round(number[, ndigits])`** | Vráti číslo `number` zaokrúhlené na `ndigits` desatinných miest . | `round(3.14159, 2)` vráti `3.14`. |
| **`sum(iterable, /, start=0)`** | Spočíta všetky položky v iterovateľnom objekte od počiatočnej hodnoty `start` . | `sum([1, 2, 3])` vráti `6`; `sum([1, 2, 3], 10)` vráti `16`. |

---

#### **2. Konverzia typov**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`bin(x)`** | Prevedie celé číslo na binárny reťazec s predponou `'0b'` . | `bin(10)` vráti `'0b1010'`. |
| **`bool([x])`** | Prevedie hodnotu na booleovský typ (`True` alebo `False`) podľa pravidiel pravdivosti . | `bool(0)` vráti `False`; `bool("ahoj")` vráti `True`. |
| **`chr(i)`** | Vráti reťazec s jedným znakom, ktorého Unicode kód je celé číslo `i` . | `chr(97)` vráti `'a'`; `chr(8364)` vráti `'€'`. |
| **`complex([real[, imag]])`** | Vytvorí komplexné číslo z reálnej a imaginárnej časti . | `complex(2, 3)` vráti `(2+3j)`. |
| **`float([x])`** | Prevedie číslo alebo reťazec na číslo s pohyblivou rádovou čiarkou . | `float("3.14")` vráti `3.14`. |
| **`hex(x)`** | Prevedie celé číslo na hexadecimálny reťazec s predponou `'0x'` . | `hex(255)` vráti `'0xff'`. |
| **`int([x], base=10)`** | Prevedie číslo alebo reťazec na celé číslo. Parameter `base` určuje základ (2-36) . | `int("1010", 2)` vráti `10`; `int(3.14)` vráti `3`. |
| **`oct(x)`** | Prevedie celé číslo na osmičkový reťazec s predponou `'0o'` . | `oct(8)` vráti `'0o10'`. |
| **`ord(c)`** | Vráti Unicode kód znaku (reťazec dĺžky 1) . | `ord('a')` vráti `97`; `ord('€')` vráti `8364`. |
| **`str(object='')`** | Vráti reťazcovú verziu objektu . | `str(100)` vráti `'100'`. |

---

#### **3. Práca s dátovými štruktúrami**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`enumerate(iterable, start=0)`** | Vráti enumerátor, ktorý generuje dvojice `(index, položka)` . | `list(enumerate(['jaro', 'leto']))` vráti `[(0, 'jaro'), (1, 'leto')]`. |
| **`len(s)`** | Vráti dĺžku (počet položiek) objektu . | `len("ahoj")` vráti `4`; `len([1, 2, 3])` vráti `3`. |
| **`reversed(seq)`** | Vráti iterátor, ktorý prechádza sekvenciou v opačnom poradí . | `list(reversed([1, 2, 3]))` vráti `[3, 2, 1]`. |
| **`slice(start, stop[, step])`** | Vráti objekt reprezentujúci výrez (slice) . | `s = slice(1, 4, 2)`; `"ahoj svet"[s]` vráti `'h'`. |
| **`sorted(iterable, /, *, key=None, reverse=False)`** | Vráti nový zoradený zoznam z položiek iterovateľného objektu . | `sorted([3, 1, 2])` vráti `[1, 2, 3]`. |
| **`zip(*iterables, strict=False)`** | Vytvorí iterátor, ktorý agreguje prvky z viacerých iterovateľných objektov do n-íc . | `list(zip([1, 2], ['a', 'b']))` vráti `[(1, 'a'), (2, 'b')]`. |

---

#### **4. Vstup a výstup**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`input([prompt])`** | Prečíta riadok zo štandardného vstupu (klávesnice) a vráti ho ako reťazec . | `meno = input("Zadajte meno: ")` |
| **`open(file, mode='r', ...)`** | Otvorí súbor a vráti príslušný objekt súboru . | `with open("subor.txt", "r") as f: obsah = f.read()` |
| **`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`** | Vypíše objekty na textový výstupný prúd (zvyčajne na konzolu) . | `print("Ahoj", "svet", sep="-")` vypíše `Ahoj-svet`. |

---

#### **5. Logické a porovnávacie funkcie**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`all(iterable)`** | Vráti `True`, ak sú **všetky** položky v iterovateľnom objekte pravdivé (alebo je iterovateľný objekt prázdny) . | `all([True, 1, "ahoj"])` vráti `True`; `all([True, 0, "ahoj"])` vráti `False`. |
| **`any(iterable)`** | Vráti `True`, ak **aspoň jedna** položka v iterovateľnom objekte je pravdivá . | `any([False, 0, ""])` vráti `False`; `any([False, 0, "ahoj"])` vráti `True`. |
| **`isinstance(object, classinfo)`** | Vráti `True`, ak je `object` inštanciou triedy `classinfo` alebo jej podtriedy . | `isinstance(5, int)` vráti `True`; `isinstance("text", int)` vráti `False`. |
| **`issubclass(class, classinfo)`** | Vráti `True`, ak je `class` podtriedou `classinfo` . | `issubclass(bool, int)` vráti `True`. |

---

#### **6. Dynamická kompilácia a spúšťanie kódu**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`compile(source, filename, mode, ...)`** | Skompiluje zdrojový kód na kódový alebo AST objekt pripravený na spustenie . | `code = compile('a = 5', '<string>', 'exec')`; `exec(code)` vytvorí premennú `a`. |
| **`eval(expression, globals=None, locals=None)`** | Vyhodnotí reťazec ako Python výraz a vráti výsledok . | `eval('2 + 2')` vráti `4`; `eval('x + 1', {'x': 3})` vráti `4`. |
| **`exec(object, globals=None, locals=None, /, *, closure=None)`** | Dynamicky spustí Python kód (reťazec alebo kódový objekt) . | `exec('print("Ahoj")')` vypíše `Ahoj`. |

---

#### **7. Funkcie na prácu s objektmi a atribútmi**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`delattr(object, name)`** | Zmaže atribút s názvom `name` z objektu . | `delattr(obj, 'x')` je ekvivalentné `del obj.x`. |
| **`dir([object])`** | Vráti zoznam mien v aktuálnom lokálnom rozsahu alebo atribútov daného objektu . | `dir(str)` vráti zoznam metód reťazcov. |
| **`getattr(object, name[, default])`** | Vráti hodnotu atribútu `name` z objektu; ak neexistuje a je zadané `default`, vráti ho . | `getattr(obj, 'x', 0)` získa hodnotu `obj.x` alebo `0` ak neexistuje. |
| **`hasattr(object, name)`** | Vráti `True`, ak má objekt atribút s názvom `name` . | `hasattr(obj, 'x')` skontroluje, či má `obj` atribút `x`. |
| **`id(object)`** | Vráti unikátnu identitu objektu ako celé číslo . | `id(obj)` vráti adresu objektu v pamäti (v CPythone). |
| **`setattr(object, name, value)`** | Nastaví hodnotu atribútu `name` na `value` . | `setattr(obj, 'x', 10)` je ekvivalentné `obj.x = 10`. |
| **`type(object)`** | Vráti typ (triedu) objektu . | `type(5)` vráti `<class 'int'>`. |
| **`vars([object])`** | Vráti `__dict__` atribút objektu (slovník menného priestoru) . | `vars(obj)` vráti slovník atribútov objektu. |

---

#### **8. Funkcie pre iterátory a generátory**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`filter(function, iterable)`** | Vytvorí iterátor z prvkov `iterable`, pre ktoré `function` vráti `True` . | `list(filter(lambda x: x > 0, [-1, 0, 1]))` vráti `[1]`. |
| **`iter(object[, sentinel])`** | Vráti iterátor. Bez `sentinel` pracuje s iterovateľnými objektmi. S `sentinel` volá `object` až kým nevráti `sentinel` . | `iter([1, 2, 3])` vráti iterátor; `iter(f.readline, '')` číta riadky zo súboru. |
| **`map(function, iterable, ...)`** | Aplikuje `function` na každú položku z iterovateľného objektu a vráti iterátor s výsledkami . | `list(map(lambda x: x*2, [1, 2, 3]))` vráti `[2, 4, 6]`. |
| **`next(iterator[, default])`** | Získa ďalšiu položku z iterátora. Ak je iterátor vyčerpaný a je dané `default`, vráti ho, inak vyvolá `StopIteration` . | `it = iter([1, 2])`; `next(it)` vráti `1`; `next(it, 0)` vráti `0` po vyčerpaní. |
| **`range(stop)`**<br/>**`range(start, stop[, step])`** | Vráti nemennú postupnosť čísel, používa sa často v cykloch `for` . | `list(range(3))` vráti `[0, 1, 2]`; `list(range(1, 5, 2))` vráti `[1, 3]`. |

---

#### **9. Triedy a dekorátory**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`classmethod`** | Premení metódu na metódu triedy. Ako prvý argument dostáva triedu (`cls`) . | Používa sa ako dekorátor `@classmethod`. |
| **`property(fget=None, fset=None, fdel=None, doc=None)`** | Vráti property atribút, ktorý umožňuje riadený prístup k inštančným atribútom . | Používa sa na definovanie getterov, setterov a deleterov. |
| **`staticmethod`** | Premení metódu na statickú metódu, ktorá nedostáva automaticky ani triedu (`cls`), ani inštanciu (`self`) . | Používa sa ako dekorátor `@staticmethod`. |
| **`super([type[, object-or-type]])`** | Vráti proxy objekt, ktorý deleguje volania metód na rodičovskú alebo súrodeneckú triedu . | Používa sa na volanie metód z nadradenej triedy. |

---

#### **10. Rôzne užitočné funkcie**

| Funkcia | Popis | Príklad použitia |
| :--- | :--- | :--- |
| **`breakpoint(*args, **kws)`** | Zavolá ladiaci program na mieste, kde sa nachádza . | `breakpoint()` spustí `pdb` v bode zastavenia. |
| **`callable(object)`** | Vráti `True`, ak je `object` možné zavolať (napr. funkcia, metóda, trieda) . | `callable(print)` vráti `True`; `callable(5)` vráti `False`. |
| **`globals()`** | Vráti slovník reprezentujúci aktuálny globálny menný priestor . | Používa sa na prístup k globálnym premenným. |
| **`locals()`** | Vráti slovník reprezentujúci aktuálny lokálny menný priestor . | Používa sa na prístup k lokálnym premenným. |
| **`help([object])`** | Spustí vstavaný nápovedný systém . | `help(str)` zobrazí dokumentáciu k triede `str`. |
| **`__import__(name, globals=None, locals=None, fromlist=(), level=0)`** | Volá sa príkazom `import` a umožňuje dynamický import modulov . | `math = __import__('math')` importuje modul `math`. |


### **1. Práca s číslami a matematika**

Tento program ukazuje základné matematické operácie s číslami.

```python
# Ukážka matematických funkcií
cisla = [-5, 3.14, 10, 2]

# Absolútna hodnota
print(f"Absolútna hodnota -5 je: {abs(-5)}")

# Delenie so zvyškom
podiel, zvysok = divmod(10, 3)
print(f"10 / 3 = {podiel}, zvyšok = {zvysok}")

# Najväčšia a najmenšia hodnota
print(f"Maximum z {cisla} je: {max(cisla)}")
print(f"Minimum z {cisla} je: {min(cisla)}")

# Umocňovanie
print(f"2 na 3 = {pow(2, 3)}")
print(f"2 na 3 modulo 5 = {pow(2, 3, 5)}")

# Zaokrúhľovanie
print(f"Číslo 3.14159 zaokrúhlené na 2 desatinné miesta: {round(3.14159, 2)}")

# Súčet
print(f"Súčet čísel {cisla} je: {sum(cisla)}")
```

**Výstup:**
```
Absolútna hodnota -5 je: 5
10 / 3 = 3, zvyšok = 1
Maximum z [-5, 3.14, 10, 2] je: 10
Minimum z [-5, 3.14, 10, 2] je: -5
2 na 3 = 8
2 na 3 modulo 5 = 3
Číslo 3.14159 zaokrúhlené na 2 desatinné miesta: 3.14
Súčet čísel [-5, 3.14, 10, 2] je: 10.14
```

---

### **2. Konverzia typov a práca s reťazcami**

Ukážka prevodu medzi rôznymi dátovými typmi.

```python
# Konverzie typov
cislo = 255
retazec = "Ahoj"

# Prevod na rôzne číselné sústavy
print(f"Číslo {cislo} v binárnej sústave: {bin(cislo)}")
print(f"Číslo {cislo} v osmičkovej sústave: {oct(cislo)}")
print(f"Číslo {cislo} v hexadecimálnej sústave: {hex(cislo)}")

# Prevod medzi znakmi a Unicode kódmi
print(f"Unicode kód znaku 'A' je: {ord('A')}")
print(f"Znak pre kód 65 je: {chr(65)}")

# Konverzia na iné typy
print(f"Reťazec '3.14' ako float: {float('3.14')}")
print(f"Binárny reťazec '1010' ako int: {int('1010', 2)}")
print(f"Booleovská hodnota čísla 0: {bool(0)}")
print(f"Booleovská hodnota reťazca 'Ahoj': {bool('Ahoj')}")

# Vytvorenie komplexného čísla
komplexne = complex(2, 3)
print(f"Komplexné číslo: {komplexne}")
```

**Výstup:**
```
Číslo 255 v binárnej sústave: 0b11111111
Číslo 255 v osmičkovej sústave: 0o377
Číslo 255 v hexadecimálnej sústave: 0xff
Unicode kód znaku 'A' je: 65
Znak pre kód 65 je: A
Reťazec '3.14' ako float: 3.14
Binárny reťazec '1010' ako int: 10
Booleovská hodnota čísla 0: False
Booleovská hodnota reťazca 'Ahoj': True
Komplexné číslo: (2+3j)
```

---

### **3. Práca s dátovými štruktúrami**

Ukážka práce so zoznamami, n-ticami a slovníkom pomocou vstavaných funkcií.

```python
# Práca s dátovými štruktúrami
ovocie = ["jablko", "hruška", "banán", "pomaranč"]
cisla = [3, 1, 4, 1, 5, 9, 2]

# Enumerate - získanie indexu a hodnoty
for index, polozka in enumerate(ovocie, start=1):
    print(f"{index}. {polozka}")

# Dĺžka zoznamu
print(f"Počet druhov ovocia: {len(ovocie)}")

# Opačné poradie
print(f"Ovocie v opačnom poradí: {list(reversed(ovocie))}")

# Zoradenie
print(f"Zoradené čísla: {sorted(cisla)}")
print(f"Zoradené čísla zostupne: {sorted(cisla, reverse=True)}")

# Slice (výrez)
moj_slice = slice(1, 4)
print(f"Výrez z ovocia [1:4]: {ovocie[moj_slice]}")

# Zip - spojenie dvoch zoznamov
mena = ["Janko", "Marienka", "Petro"]
vek = [25, 30, 35]
for meno, vek_osoby in zip(mena, vek):
    print(f"{meno} má {vek_osoby} rokov.")
```

**Výstup:**
```
1. jablko
2. hruška
3. banán
4. pomaranč
Počet druhov ovocia: 4
Ovocy v opačnom poradí: ['pomaranč', 'banán', 'hruška', 'jablko']
Zoradené čísla: [1, 1, 2, 3, 4, 5, 9]
Zoradené čísla zostupne: [9, 5, 4, 3, 2, 1, 1]
Výrez z ovocia [1:4]: ['hruška', 'banán', 'pomaranč']
Janko má 25 rokov.
Marienka má 30 rokov.
Petro má 35 rokov.
```

---

### **4. Vstup a výstup, práca so súbormi**

Ukážka jednoduchého vstupu a výstupu vrátane zápisu a čítania súborov.

```python
# Vstup a výstup
meno = input("Zadajte svoje meno: ")
print(f"Ahoj, {meno}! Vitaj v ukážkovom programe.")

# Práca so súborom - zápis
with open("test.txt", "w", encoding="utf-8") as subor:
    subor.write("Toto je testovací súbor.\n")
    subor.write(f"Vytvorený pre {meno}.\n")

# Práca so súborom - čítanie
with open("test.txt", "r", encoding="utf-8") as subor:
    obsah = subor.read()
    print("\nObsah súboru:")
    print(obsah)

# Vypísanie viacerých hodnôt s oddelovačom
print("Jablko", "Hruška", "Banán", sep=", ", end="!\n")
```

**Výstup (príklad):**
```
Zadajte svoje meno: Janko
Ahoj, Janko! Vitaj v ukážkovom programe.

Obsah súboru:
Toto je testovací súbor.
Vytvorený pre Janko.

Jablko, Hruška, Banán!
```

---

### **5. Logické a porovnávacie funkcie**

Ukážka vyhodnotenia pravdivostných hodnôt.

```python
# Logické funkcie
data = [True, 1, "Ahoj", 0, False, "", [1, 2]]

# all() - všetky hodnoty musia byť pravdivé
vsetky_pravdive = all(data[:3])  # True, 1, "Ahoj"
print(f"Sú všetky hodnoty {data[:3]} pravdivé? {vsetky_pravdive}")

# any() - aspoň jedna hodnota musí byť pravdivá
aspon_jedna_pravdiva = any(data[3:])  # 0, False, "", [1, 2]
print(f"Je aspoň jedna hodnota z {data[3:]} pravdivá? {aspon_jedna_pravdiva}")

# Kontrola typov
cislo = 5
text = "Python"
print(f"Je 5 inštanciou int? {isinstance(cislo, int)}")
print(f"Je 'Python' inštanciou str? {isinstance(text, str)}")

# Kontrola podtried
print(f"Je bool podtriedou int? {issubclass(bool, int)}")
print(f"Je str podtriedou int? {issubclass(str, int)}")
```

**Výstup:**
```
Sú všetky hodnoty [True, 1, 'Ahoj'] pravdivé? True
Je aspoň jedna hodnota z [0, False, '', [1, 2]] pravdivá? True
Je 5 inštanciou int? True
Je 'Python' inštanciou str? True
Je bool podtriedou int? True
Je str podtriedou int? False
```

---

### **6. Dynamická kompilácia a spúšťanie kódu**

Ukážka dynamického vyhodnotenia a spustenia kódu (opatrne, používajte iba s dôveryhodným vstupom).

```python
# Dynamické vyhodnotenie výrazov
x = 5
y = 3
vyraz = "x * y + 2"
vysledok = eval(vyraz)
print(f"{vyraz} = {vysledok}")

# Dynamické spustenie kódu
kod = """
def pozdrav(meno):
    return f"Ahoj, {meno}!"

print(pozdrav("Svet"))
"""
exec(kod)

# Kompilácia a spustenie
kompilovany_kod = compile('print("Toto je skompilovaný kód.")', '<string>', 'exec')
exec(kompilovany_kod)
```

**Výstup:**
```
x * y + 2 = 17
Ahoj, Svet!
Toto je skompilovaný kód.
```

---

### **7. Funkcie na prácu s objektmi a atribútmi**

Ukážka práce s atribútmi objektov.

```python
# Definícia jednoduchej triedy
class Osoba:
    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek

# Vytvorenie inštancie
osoba = Osoba("Janko", 30)

# Získanie a kontrola atribútov
print(f"Meno osoby: {getattr(osoba, 'meno')}")
print(f"Má osoba atribút 'vek'? {hasattr(osoba, 'vek')}")
print(f"Má osoba atribút 'adresa'? {hasattr(osoba, 'adresa')}")

# Nastavenie atribútu
setattr(osoba, 'adresa', 'Hlavná 123')
print(f"Nový atribút 'adresa': {getattr(osoba, 'adresa')}")

# Získanie všetkých atribútov
print(f"Atribúty osoby: {dir(osoba)}")

# Typ a identita objektu
print(f"Typ osoby: {type(osoba)}")
print(f"ID osoby: {id(osoba)}")

# Zobrazenie slovníka atribútov
print(f"Slovník atribútov: {vars(osoba)}")
```

**Výstup:**
```
Meno osoby: Janko
Má osoba atribút 'vek'? True
Má osoba atribút 'adresa'? False
Nový atribút 'adresa': Hlavná 123
Atribúty osoby: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'adresa', 'meno', 'vek']
Typ osoby: <class '__main__.Osoba'>
ID osoby: 140736676234112
Slovník atribútov: {'meno': 'Janko', 'vek': 30, 'adresa': 'Hlavná 123'}
```

---

### **8. Funkcie pre iterátory a generátory**

Ukážka použitia `map`, `filter` a `range`.

```python
# Filter - vyberie iba párne čísla
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parne = filter(lambda x: x % 2 == 0, cisla)
print(f"Párne čísla: {list(parne)}")

# Map - aplikuje funkciu na každý prvok
druhe_mocniny = map(lambda x: x ** 2, cisla)
print(f"Druhé mocniny: {list(druhe_mocniny)}")

# Range - generovanie postupnosti
print(f"Čísla od 0 do 4: {list(range(5))}")
print(f"Čísla od 2 do 10 s krokom 2: {list(range(2, 11, 2))}")

# Kombinácia iterátorov - filter a map
vysledok = map(lambda x: x * 3, filter(lambda x: x > 5, cisla))
print(f"Čísla > 5 vynásobené 3: {list(vysledok)}")
```

**Výstup:**
```
Párne čísla: [2, 4, 6, 8, 10]
Druhé mocniny: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Čísla od 0 do 4: [0, 1, 2, 3, 4]
Čísla od 2 do 10 s krokom 2: [2, 4, 6, 8, 10]
Čísla > 5 vynásobené 3: [18, 21, 24, 27, 30]
```

---

### **9. Triedy a dekorátory**

Ukážka použitia `classmethod`, `staticmethod`, `property` a `super`.

```python
class Zamestnanec:
    # Triedna premenná
    pocet_zamestnancov = 0

    def __init__(self, meno, plat):
        self._meno = meno
        self._plat = plat
        Zamestnanec.pocet_zamestnancov += 1

    @property
    def meno(self):
        """Getter pre meno."""
        return self._meno

    @meno.setter
    def meno(self, hodnota):
        """Setter pre meno."""
        if not hodnota:
            raise ValueError("Meno nemôže byť prázdne")
        self._meno = hodnota

    @property
    def plat(self):
        return self._plat

    @plat.setter
    def plat(self, hodnota):
        if hodnota < 0:
            raise ValueError("Plat nemôže byť záporný")
        self._plat = hodnota

    @classmethod
    def get_pocet(cls):
        """Vráti počet vytvorených zamestnancov."""
        return cls.pocet_zamestnancov

    @staticmethod
    def validuj_meno(meno):
        """Statická metóda na validáciu mena."""
        return len(meno) > 0 and meno.isalpha()

    def __str__(self):
        return f"Zamestnanec: {self.meno}, plat: {self.plat}€"


class Manazer(Zamestnanec):
    def __init__(self, meno, plat, oddelenie):
        super().__init__(meno, plat)
        self.oddelenie = oddelenie

    def __str__(self):
        return f"Managér: {self.meno}, plat: {self.plat}€, oddelenie: {self.oddelenie}"


# Použitie
zam1 = Zamestnanec("Janko", 1500)
zam2 = Zamestnanec("Marienka", 1800)
manazer = Manazer("Peter", 2500, "IT")

print(zam1)
print(zam2)
print(manazer)

# Práca s property
zam1.meno = "Janko H."  # Nastavenie nového mena
print(f"Nové meno: {zam1.meno}")

# Volanie triednych a statických metód
print(f"Počet zamestnancov: {Zamestnanec.get_pocet()}")
print(f"Je 'Anna' platné meno? {Zamestnanec.validuj_meno('Anna')}")
```

**Výstup:**
```
Zamestnanec: Janko, plat: 1500€
Zamestnanec: Marienka, plat: 1800€
Managér: Peter, plat: 2500€, oddelenie: IT
Nové meno: Janko H.
Počet zamestnancov: 3
Je 'Anna' platné meno? True
```

---

### **10. Rôzne užitočné funkcie**

Ukážka funkcií ako `help`, `callable`, `globals`, `locals` a ďalších.

```python
# Kontrola, či je objekt volateľný
def moja_funkcia():
    pass

class MojaTrieda:
    pass

objekt = MojaTrieda()
print(f"Je funkcia volateľná? {callable(moja_funkcia)}")
print(f"Je trieda volateľná? {callable(MojaTrieda)}")
print(f"Je inštancia volateľná? {callable(objekt)}")

# Zobrazenie globálnych a lokálnych premenných
globalna_premenna = "Som globálna"

def test():
    lokalna_premenna = "Som lokálna"
    print("Lokálne premenné:", locals())
    print("Globálne premenné (výpis kľúčov):", list(globals().keys()))

test()

# Zobrazenie nápovedy (odkomentujte pre spustenie)
# help(print)  # Zobrazí nápovedu k funkcii print

# Dynamický import (zvyčajne sa používa import, ale tu je ukážka)
math = __import__('math')
print(f"Druhá odmocnina z 16: {math.sqrt(16)}")

# Breakpoint - spustí debugger (odkomentujte pre spustenie)
# breakpoint()  # Zastaví program a spustí ladiaci nástroj
```

**Výstup:**
```
Je funkcia volateľná? True
Je trieda volateľná? True
Je inštancia volateľná? False
Lokálne premenné: {'lokalna_premenna': 'Som lokálna'}
Globálne premenné (výpis kľúčov): ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'moja_funkcia', 'MojaTrieda', 'objekt', 'globalna_premenna', 'test', 'math']
Druhá odmocnina z 16: 4.0
```

---

### **Zhrnutie**

Tieto ukážkové programy pokrývajú väčšinu dôležitých vstavaných funkcií jazyka Python. Každý program je navrhnutý tak, aby bol samostatný a jednoducho spustiteľný. Môžete si ich skopírovať a spustiť vo svojom prostredí, aby ste lepšie porozumeli ich fungovaniu.

Ak potrebujete podrobnejšie vysvetlenie ku konkrétnej funkcii, odporúčam použiť `help(nazov_funkcie)` priamo v Pythone alebo navštíviť oficiálnu dokumentáciu.
