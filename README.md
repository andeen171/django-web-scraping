## Aplicação Django + Vue3 para pesquisar e exibir produtos da drogasil 

# Instruções para rodar a aplicação

## Inicie o ambiente virtual (venv)
```
/venv/bin/activate
ou
/venv/bin/activate.ps1
```

## Instale as dependências da api
```
pip install requirements.txt
```

## Instale as dependências do cliente
```
yarn add
```

## Compile os arquivos do cliente
```
yarn build
```

## Prepare os arquivos estáticos
```
python manage.py collectstatic
```

## Rode a aplicação
```
python manage.py runserver
```

# Acessível em http://localhost:8000/
