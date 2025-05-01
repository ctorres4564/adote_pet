 🐾 Adote um Nome de Pet

Projeto criado com Django para gerar nomes aleatórios de pets. 
Cada nome é salvo no banco de dados com contagem de cliques, e a página permite que o usuário sorteie um nome divertido para seu animal.

---

## Funcionalidades

- Gera nomes de pets aleatórios
- Conta quantas vezes cada nome foi sorteado
- Permite cadastrar nomes manualmente pelo Django Admin
- População automática do banco com 100 nomes

---

## Como usar

1. Instale as dependências:
```bash
pip install django
```

2. Faça as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. (Opcional) Crie um superusuário:
```bash
python manage.py createsuperuser
```

4. Popule o banco com nomes:
```bash
python manage.py shell
>>> from nomes.populate import popular_nomes
>>> popular_nomes()
>>> exit()
```

5. Inicie o servidor:
```bash
python manage.py runserver
```


---

## Autor

Claudio Araujo







