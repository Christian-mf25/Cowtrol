# READ.ME (1)

## Sobre:

A Cowtrol é uma plataforma para pastejo rotacionado, que basicamente é: permitir movimentar o gado entre áreas diferentes da fazenda que geram ganho de peso diferenciados aos animais.

<br>

## Base URL

```jsx
https://cowtrol.herokuapp.com/api/
```

Os endpoints que tiverem sinalizados com “**AUTH” deverão ser feitas as requisições com token de usuário logado.

Todas as requisições deverão ser feitas em JSON.
Todas as repostas serão entregues em JSON.

<br>

## Endpoints em Farm

### POST -                                   /farms/

Rota insere uma fazenda não cadastrada no banco de dados.

```json
{
	"name": "boaterra",
	"email": "boa_terra@mail.com",
	"password": "SenhaForte"
}
```

| CHAVES | VALORES | OBRIGATORIEDADE |
| --- | --- | --- |
| name | string | sim |
| email | string, email | sim |
| password | string | sim |

Exemplo de requisição:

```json
{
	"name": "boaterra",
	"email": "boa_terra@mail.com",
	"password": "SenhaForte"
}
```

exemplo de resposta:

```json
201 - CREATED

{
	"id": "dcb47e12-f1fa-401b-beff-212d8e2055e9",
	"name": "Boaterra",
	"email": "boa_terra@mail.com"
}
```

<br>

### POST -                                   /login/

Rota faz o login e insere um token no banco de dados.

```json
{
	"email": "boa_terra@mail.com",
	"password": "SenhaForte"
}
```


| CHAVES | VALORES | OBRIGATORIEDADE |
| --- | --- | --- |
| email | string, email | sim |
| password | string | sim |

Exemplo de requisição:

```json
{
	"email": "boa_terra@mail.com",
	"password": "SenhaForte"
}
```

exemplo de resposta:

```json
200 - OK

{
	"token": "754fa977c732d3319513ecfc6e0128219e3a9cfa"
}
```

<br>

## Endpoints em Area

### POST - **AUTH -                   /areas/

Rota insere uma área não cadastrada no banco de dados.

| CHAVES | VALORES | OBRIGATORIEDADE |
| --- | --- | --- |
| area_name | string, único | sim |
| limit_space | number, integer | sim |
| gmd | number, float | sim |

Significado das chaves:
─ area_name: Nome para definir uma área.
─ limit_space: Capacidade de animais na área.
─ gmd: Ganho médio diário.

Exemplo de requisição:

```json
{
	"area_name": "A",
	"limit_space": 10,
	"gmd": 1
}
```

exemplo de resposta:

```json
201 - CREATED

{
	"id": "0e60da12-ba9e-4e8c-b8a6-0abfc8f7bdf3",
	"area_name": "A",
	"limit_space": 10,
	"free_space": 10,
	"occupied_space": 0,
	"gmd": 1.00
}
```

<br>

### GET -   **AUTH -                   /areas/

Não tem corpo na requisição.

Exemplo de resposta:

```json
200 - OK
[
	{
		"id": "0e60da12-ba9e-4e8c-b8a6-0abfc8f7bdf3",
		"area_name": "A",
		"limit_space": 10,
		"free_space": 10,
		"occupied_space": 0,
		"gmd": 1.00
	},
	{
		"id": "e95323a1-7625-4ffe-9410-113c960bc3b9",
		"area_name": "B",
		"limit_space": 10,
		"free_space": 10,
		"occupied_space": 0,
		"gmd": 0.80
	}
]
```

<br>

## Endpoints em Animal

### POST - **AUTH -                   /animals/

Rota insere um animal não cadastrado no banco de dados.

| CHAVES | VALORES | OBRIGATORIEDADE |
| --- | --- | --- |
| name | string, único | sim |
| weight | number, float | sim |
| area | string | sim |

Significado das chaves:
─ name: Nome para definir um animal.
─ weight: Peso do animal.
─ area: Nome da área que o animal está (A área deverá estar registrada).

Exemplo de requisição:

```json
{
	"name": "A1",
	"weight": 150,
	"area": "A"
}
```

exemplo de resposta:

```json
201 - CREATED

{
	"name": "A1",
	"weight": 150.00,
	"area": "A"
}
```

<br>

### GET -   **AUTH -                   /animals/

Retorna todos animais ou apenas os animais solicitados.

Para retornar todos seus animais não é necessário ter corpo na requisição

Para retorna os animais desejados utilize a chave mencionada na tabela.

| CHAVES | VALORES | OBRIGATORIEDADE |
| --- | --- | --- |
| animal_names | lista de string | Não |

Exemplo de requisição:

```json
{
	"animal_names": [
		"A1",
		"A2"
	]
}
```

Exemplo de resposta:

```json
200 - OK

[
	{
		"name": "A1",
		"weight": 150.00,
		"area": {
			"area_name": "A",
			"gmd": 1.00
		}
	},
	{
		"name": "A2",
		"weight": 163.00,
		"area": {
			"area_name": "A",
			"gmd": 1.00
		}
	}
]
```

<br>

## Endpoints em Movement

### POST - **AUTH -                   /movements/

Rota faz a movimentação de um ou mais animais, altera as chaves “limit_space”, “free_space”, “occupied_space” da tabela “areas” e criada o registro da movimentação no banco de dados.

| CHAVES | VALORES | OBRIGATORIEDADE |
| --- | --- | --- |
| move_to | string | sim |
| days | number | sim |
| animals | lista de string | sim |

Significado das chaves:
─ move_to: A área para onde quer enviar o animal.
─ days: Quantos dias ele ficará na área.
─ animals: Os animais que estão sendo movido para a área.

Exemplo de requisição:

```json
{
	"move_to": "B",
	"days": 8,
	"animals": ["A1"]
}
```

exemplo de resposta:

```json
201 - CREATED

{
	"animals": [
		"A1"
	],
	"move_to": "B",
	"days": 8
}
```