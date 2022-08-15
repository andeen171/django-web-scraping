## Aplicação Django + Vue3 para pesquisar e exibir produtos da drogasil 

# Instruções para rodar a aplicação

## Inicie o ambiente virtual (venv)
```
python -m venv venv
```
então
```
/venv/bin/activate
```
ou
```
/venv/Scripts/activate
```

## Instale as dependências da api
```
pip install -r requirements.txt
```

## Instale as dependências do cliente
```
yarn global add @vue/cli
```
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
