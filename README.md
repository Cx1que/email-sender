# email-sender

## Dependências necessárias

Após clonar o projeto, é necessário baixar as dependências com:

"""py 
pip install -r requirements.txt
 """

Após todas serem baixadas, para rodar o projeto basta rodar no terminal:

"""py
uvicorn src.api.main:app --host 0.0.0.0 --port 10000
"""

Assim, a API já estará no ar.

## A FAZER

### Validações

+ EndPoints de desativar e listar ativas;

+ Compras parceladas devem ter os campos de parcelas preenchidos;

+ Os tipos de conta devem ser AVULSA, RECORRENTE e PARCELADA;