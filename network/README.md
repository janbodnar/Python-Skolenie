# ⚡ Load testovanie async serverov (aiohttp)

Pri testovaní výkonu asynchrónnych HTTP serverov (napr. aiohttp) je dôležité vedieť, že  
nie všetky nástroje podporujú streamované telá (`chunked upload`).  
Nižšie je prehľad najpoužívanejších nástrojov, ich silné stránky a konkrétne príkazy.

---

## 🧪 Najčastejšie používané load testery

### **1) ab (ApacheBench)**  
Klasický nástroj, jednoduchý, ale starší.  
Nevie streamovať request body – používa statické payloady.

**Príklad:**
```
ab -n 10000 -c 200 http://localhost:8000/
```

---

### **2) wrk** (najvýkonnejší, moderný)
Extrémne rýchly, ideálny na testovanie latencie a priepustnosti.  
Podporuje Lua skripty pre custom requesty.

**Príklad:**
```
wrk -t4 -c200 -d30s http://localhost:8000/
```

---

### **3) hey** (Go nástroj od Google)
Jednoduchý, pekný výstup, cross‑platform.

**Príklad:**
```
hey -n 10000 -c 200 http://localhost:8000/
```

---

### **4) bombardier** (Go, veľmi rýchly)
Moderný, rýchly, vhodný na vysoké concurrency.

**Príklad:**
```
bombardier -c 200 -n 10000 http://localhost:8000/
```

---

### **5) oha** (Rust, async-friendly)
Rýchly, moderný, ergonomický.

**Príklad:**
```
oha -n 10000 -c 200 http://localhost:8000/
```

---

## 📡 Testovanie streamovaných uploadov

Väčšina load testerov **nevie** posielať chunked streaming (`Transfer-Encoding: chunked`).  
Na testovanie streamingu je najlepšie použiť:

- **xh**
- **curl**
- alebo vlastný Python async klient

### Paralelné streamovanie pomocou `xh`:

```
seq 1 200 | xargs -n1 -P200 -I{} xh POST http://localhost:8000/upload @largefile.bin
```

- `-P200` → 200 paralelných procesov  
- každý proces pošle jeden upload  
- toto simuluje reálny tlak na `stream_reader()` v aiohttp

---

## 🧭 Ktorý nástroj použiť?

| Nástroj | Najlepšie použitie | Podpora streamingu | Poznámka |
|--------|--------------------|---------------------|----------|
| **ab** | rýchly sanity test | ❌ nie | starší, jednoduchý |
| **wrk** | max. výkon, latencia | ❌ nie | najrýchlejší nástroj |
| **hey** | jednoduché testy | ❌ nie | pekný výstup |
| **bombardier** | vysoké concurrency | ❌ nie | moderný, rýchly |
| **oha** | async-friendly testy | ❌ nie | Rust, veľmi rýchly |
| **xh + xargs** | **streamované uploady** | ✅ áno | najlepšie pre aiohttp streaming |

---

## 📝 Odporúčanie pre aiohttp

- **Na testovanie servera bez streamingu:**  
  → *wrk* alebo *oha*

- **Na testovanie streamovaného uploadu:**  
  → *xh + xargs* (jediná realistická voľba)

---

Ak chceš, doplním aj **sekciu pre testovanie streaming downloadu** (chunked response), alebo **Python skript**, ktorý generuje stovky async requestov cez `aiohttp.ClientSession`.
