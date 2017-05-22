# Prospera |Prõs-pé-ra|

## Objetivo do Projeto



### Requisitos de Software

- Git
- Python 2.7
- Python PIP

## Como instalar

```
# Baixar o código fonte
git clone git@github.com:bodedev/prospera.git

# Instalar o VirtualEnv
pip install virtualenv

# Criar um VirtualEnv
virtualenv env

# Ativar o VirtualEnv
source env/bin/activate

# Instalar dependências de bibliotecas do sistema
pip install -r conf/requirements.txt

# Executar o servidor de testes
python manage.py runserver 0.0.0.0:8000

# O sistema estará disponível no navegador de internet através do endereço http://localhost:8000/
```