# Python_Library

## Arquivos de exemplos de bibliotecas do Python

* [requests -> awesomeapi CEP](./get_address_by_cep.py)

Instale a biblioteca requests pelo seu terminal

```bash
pip install requests
```

----
Link da API -> [https://docs.awesomeapi.com.br/api-cep](https://docs.awesomeapi.com.br/api-cep)

----

```python
import requests

CEP = '91250105'
URL = f'https://cep.awesomeapi.com.br/json/{CEP}'

RESPONSE = requests.get(URL)
JSON = RESPONSE.json()
ADDRESS = JSON['address']

print(ADDRESS)

```

* [deep_translator -> Google Tradutor](./deep-translator.py)

```bash
pip install deep_translator
```

----

```python
from deep_translator import GoogleTranslator

PT, EN = 'pt', 'en'

GOOGLE = GoogleTranslator(source=PT, target=EN)

NAME, AGE = 'Adryan Maikel da Cunha Kuhne', 21
TEXT = f'Olá Mundo! Meu nome é {NAME}, e tenho {AGE} anos de idade.'

translator = GOOGLE.translate(TEXT)
print(translator)

```

* [Pegar um endereço passando CEP](./get_address_by_cep.py)

* []()
