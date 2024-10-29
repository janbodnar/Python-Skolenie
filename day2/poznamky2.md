# Priklady 29.10. 2024

Toto je moj odstavec.  

## Nacitanie retazcov

Tento priklad nacita subor a vyfiltruje vsetky slova majuce 2 alebo 3 znaky.  

```python
import re

file_name = 'thermopylae.txt'

with open(file_name, 'r') as f:
    
    content = f.read()

    words = re.split(r'\W+', content)
    words.pop()
    print(words)

    words_2_3 = list(filter(lambda e: len(e) == 2 or len(e) == 3, words))
    print(words_2_3)
```
