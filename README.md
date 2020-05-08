**Leonardo‌ ‌Torres‌ ‌Montero‌ ‌**
DevOps‌ ‌-‌ ‌ltmleo@hotmail.com‌ ‌
(19)‌ ‌99287-8554‌ ‌

# DOCUMENTAÇÃO
[https://github.com/ltmleo/carros-case](https://github.com/ltmleo/carros-case)

# Carros API

Esse projeto mostra de maneira simplificada o funcionamento de um ecossistema de uma API para cadastrar a entidade carros em um banco de dados (mongoDB): A API espera o cadastro de quatros atributos:

* **Cor**: A cor do carro, deve ser uma string;

* **Placa**: A placa do veículo, deve ser uma string no formato AAA-0000, não pode haver placas duplicadas;

* **Ano**:  O ano do veículo, deve ser um inteiro;

* **Modelo**: O modelo do veículo, deve ser uma string; 

 

## Requisitos

* Docker: v18.09.7

* Docker-compose: v1.17.1

* Helm: v2.14.2

* Python: v3.6.9

## Cadastro:

Para cadastrar um novo veículo deve ser feito um método de POST para o endpoint [http://127.0.0.1:8081/cadastrar](http://127.0.0.1:8081/cadastrar) com o seguinte body:

```
{
"Cor": "preto",
"Placa": "AAA-0000",
"Ano": "1111",
"Modelo": "modelo"
}
```


A API deverá retornar o seguinte resultado: 

```
{
    "ID": "5eb55d196bab77dde878197a",
    "status": "OK"
}
```

onde o campo ID, representa o ID cadastrado no banco de dados.

 

Duplicação:

Caso a placa já existir no banco de dados, o seguinte resultado será retornado:

```
{
    "msg": "Carro com a placa aaa-0000 Duplicado",
    "status": "NOT OK"
}
```


### Erro na chave:

Caso alguma chave não seja passada, ou exista algum eror em uma das chaves, o seguinte resultado é retornado:

```
{
    "msg": "Chaves Inválidas",
    "status": "NOT OK"
}
```


### Erro no valor:

Caso algum valor não seja passado conforme o esperado, exemplo: palca: abc0000, o seguinte erro será retornado:

```
{
    "msg": "Valores Inválidos",
    "status": "NOT OK"
}
```


## GET

Além do cadastro, um método de get foi implementado, para realizar uma consulta, uma chamada do tipo GET deve ser feita para o seguinte endpoint. [http://127.0.0.1:8081/consulta/<chave>/](http://127.0.0.1:8081/consulta/<chave>/) ou http://127.0.0.1:8081/consulta/<chave>/<valor>;

Onde a chave podemos fazer buscas mais abrangentes, como por exemplo, [http://127.0.0.1:8081/consulta/all](http://127.0.0.1:8081/consulta/all) , que retorna tudo o que tem salvo no banco de dados:

```
{"results":[{"ano":2017,"cor":"branco","modelo":"hb20","placa":"abc-1111"},{"ano":2017,"cor":"branco","modelo":"hb20","placa":"abc-1112"},{"ano":1111,"cor":"cor","modelo":"modelo","placa":"aaa-0000"}]}
```


Ou então buscas mais específicas, como por exemplo: [http://127.0.0.1:8081/consulta/](http://127.0.0.1:8081/consulta/all)cor/preto


```{"results":[{"ano":1111,"cor":"preto","modelo":"modelo","placa":"aaa-0000"}]}```

## Deploy:

Para simplificar o deploy da aplicação, foi implementado o docker-compose, portanto para subir a aplicação e o banco de dados, pronto para funcionar, o comando abaixo deve ser executado.

`$ docker-compose up -d`
