# Zadania

V tejto časti nájdeme zadania na prehĺbenie znalostí o jazyku Python.

V niektorých príkladoch sa používa nasledujúci súbor:

Súbor `thermopylae.txt`:

```
The Battle of Thermopylae was fought between an alliance of Greek city-states,
led by King Leonidas of Sparta, and the Persian Empire of Xerxes I over the course
of three days, during the second Persian invasion of Greece.
```

Pokús sa vyriešiť nasledovné zadania:

---

## Začiatočník (Beginner)  

1. **Zisti verziu Pythonu.**  
   - Uses basic module access (`sys`).
2. **Zisti verziu operačného systému.**  
   - Simple use of `platform` module.
3. **Zisti dnešný dátum.**  
   - Basic use of `datetime`.
4. **Zisti aktuálny čas.**  
   - Simple time retrieval with `datetime`.
5. **Zisti univerzálny čas.**  
   - Basic UTC time retrieval.
9. **Vypíš čísla od 0 po 100 (vrátane).**  
   - Simple loop or range.
10. **Vypíš desať čísiel od 0 po 100 (vrátane) náhodným spôsobom.**  
   - Basic use of `random` module.
11. **Vypíš čísla z n-tice (3, 5, 7, 8, 19) na jednom riadku vo forme '3-5-7-8-19'.**  
   - Simple string joining with a tuple.
12. **Vypočítaj sumu čísiel z reťazca '3-5-7-8-19'.**  
   - Basic string splitting and summing.
16. **Vypíš všetky párne čísla od 1 do 100 (vrátane).**  
   - Simple loop with condition.
19. **Napíš funkciu ktorá reverzne (otočí) zadaný reťazec (napr. 'hello' => 'olleh').**  
   - Basic string manipulation with a function.
21. **Napíš funkciu ktorá vypíše slová z n-tice ('forest', 'wood', 'sky') veľkými písmenami.**  
   - Simple string method (`upper()`) in a function.
27. **Zaokrúhli výraz 334/5000 na dve a tri desatinné miesta.**  
   - Basic use of `round()` function.
34. **Vypýtaj si od užívateľa veľkosť polomeru a vypočítaj obvod a obsah kruhu.**  
   - Simple input and math operations.

---

## Stredne pokročilý (Intermediate)  

6. **Zisti aktuálny čas v Moskve, Paríži a Osle.**  
   - Requires `pytz` for timezone handling.
7. **Napíš program, ktorý spustí aplikáciu Notepad (alebo inú).**  
   - Basic use of `os` or `subprocess` for system calls.
8. **Vytvor klasický program 99 bottles of beer.**  
   - Loop with string formatting and conditionals.
13. **Zoraď nasledovné čísla vzostupne a zostupne (2, 5, 1, 9, 11, 12, 8, 7).**  
   - List sorting with `sort()` or `sorted()`.
14. **Vypočítaj súčin čísiel z n-tice (2, 5, 1, 9, 11, 12, 8, 7).**  
   - Looping over a tuple with multiplication.
15. **Z n-tice (2, 5, 1, 9, 11, 12, 8, 7) vytvor novú, ktorej každý prvok je prenásobený 3.**  
   - Tuple manipulation with mapping or comprehension.
17. **Vypočítaj faktoriál čísiel z n-tice (3, 5, 10 a 20).**  
   - Requires a factorial function or `math.factorial`.
18. **Vygeneruj náhodným spôsobom 20 čísiel od 1 do 10 vrátane a zisti, koľko krát sa vyskytuje číslo 7.**  
   - Random generation and counting (e.g., with `list.count()`).
20. **Napíš funkciu ktorá reverzne (otočí) zadané číslo (napr. 521 => 125).**  
   - Number-to-string conversion and reversal.
22. **Napíš funkciu isAnagram, ktorá zistí, či dané slovo je anagram iného.**  
   - String comparison with sorting or counting.
23. **Napíš funkciu isPalindrome, ktorá zistí, či dané slovo je palindróm iného.**  
   - String comparison with reversal.
24. **Nájdi počet samohlások vo vete "Today is a beatiful day".**  
   - String iteration with conditional checks.
25. **Majme n-ticu (3, 5, 2, 1, 8, 9, 12, 11, 7, 6). Vypíš najväčšie minimum, maximum, sumu a počet prvkov v n-tici.**  
   - Basic tuple operations (`min()`, `max()`, `sum()`, `len()`).
26. **Majme n-ticu ('Martin', 'Lucy', 'Peter', 'Martin', 'Robert', 'Peter'). Vytvor z nej novú n-ticu bez duplikátov.**  
   - Conversion to set and back to tuple.
29. **Načítaj súbor *thermopylae.txt* a vypíš jeho obsah.**  
   - Basic file reading with `open()`.
30. **Skopíruj súbor *thermopylae.txt* do súboru *thermopylae2.txt*.**  
   - File reading and writing.
31. **Zisti veľkosť súboru *thermopylae.txt* v bajtoch a kilobajtoch.**  
   - Use of `os.path.getsize()` with unit conversion.
32. **Vypíš názov svojho domovského adresára.**  
   - Use of `os.path.expanduser()` or similar.
33. **Vypíš obsah svojho domovského adresára.**  
   - Directory listing with `os.listdir()`.
35. **Zisti počet dní do Vianoc (25.12.).**  
   - Date arithmetic with `datetime`.
36. **Zisti koľko dní ubehlo od bitky pri Borodine.**  
   - Historical date calculation (requires research: September 7, 1812).
37. **Vygeneruj plochý zoznam zo zoznamu zoznamov (napr. [[1, 2], [3, 4], [5, 6], [7]] => [1, 2, 3, 4, 5, 6, 7]).**  
   - List flattening with loops or comprehension.
38. **Pivo stojí 1.46 a predá sa 100000 kusov. Napíš program ktorý vypočíta presný obrat.**  
   - Simple multiplication with potential floating-point precision.

---

## Pokročilý (Advanced)  


28. **Konvertuj čísla z n-tice (23, 168, 997, 1455, 3999) na rímsku sústavu.**  
   - Requires logic for Roman numeral conversion.
39. **Naištaluj si pomocou nástroja pip modul psutil a zisti pomocou neho veľkosť operačnej pamäte svojho počítača.**  
   - External library installation and system info retrieval.
40. **Vypíš obsah titulku zo stránky learnpython.pro (zo značky title).**  
   - Web scraping with `requests` and `beautifulsoup4`.
41. **Vypíš hexadecimálny výstup z malého PNG obrázka. Výstup bude mať desať stĺpcov oddelených medzerou.**  
   - File reading in binary mode and hex formatting.
42. **Načítaj súbor *thermopylae.txt* a zisti počet jeho slov.**  
   - File reading with string splitting.
43. **Načítaj súbor *thermopylae.txt* a zisti frekvenciu výskytu každého slova.**  
   - File reading with dictionary for word frequency.
44. **Vygeneruj 30 náhodných čísiel od 1 do 100 (vrátane) a zapíš ich do súboru *nums.csv*. Na každom riadku nech je 10 čísiel, ktoré sú oddelené čiarkou.**  
   - Random generation and CSV file writing.
45. **Načítaj čísla z predchádzajúceho príkladu a zisti základné štatistiky: minimum, maximum, sumu, medián, počet prvkov a štandardnú odchýlku.**  
   - File reading and statistical calculations (requires `statistics` module).
46. **Zašifruj povel 'Full attack at dawn' pomocou cézarovej šifry. Spätne ho potom dekóduj.**  
   - Implementation of Caesar cipher with encoding/decoding logic.

---

## Expert (Expert)  

47. **Vytvor jednoduchú webovú aplikáciu pomocou knižnice Flask.**  
   - Web development with Flask framework.
48. **Vytvor koláčový graf pomocou knižnice matplotlib.**  
   - Data visualization with Matplotlib.
49. **Pomocou knižnice numpy vypočítaj súčin dvoch ľubovolných 3x3 matíc.**  
   - Matrix multiplication with NumPy.
50. **Vytvor tkinter GUI aplikáciu s jedným tlačidlom. Kliknutím na tlačidlo sa aplikácia ukončí.**  
   - GUI programming with Tkinter.

---

### Summary of Task Distribution

- **Beginner (14 tasks):** 1-5, 9-12, 16, 19, 21, 27, 34  
  - Focus on basic syntax, loops, and simple functions.
- **Intermediate (22 tasks):** 6-8, 13-15, 17-18, 20, 22-26, 29-33, 35-38  
  - Introduce file I/O, data structures, and moderate logic.
- **Advanced (9 tasks):** 28, 39-46  
  - Involve external libraries, file manipulation, and algorithms.
- **Expert (5 tasks):** 47-50  
  - Require frameworks, GUI, and advanced computation.
