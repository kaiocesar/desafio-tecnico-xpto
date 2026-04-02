# Desafio técnico

### requisitos:
- docker >= 29.3

### instalação
1. clone o repositório
2. execute o comando `docker compose up -d` para subir os containers
3. via client acess o curl:
```bash
curl --request GET \
  --url http://0.0.0.0:8080/api/v1/catalog/awards \
  --header 'User-Agent: insomnia/8.3.0'
```
e veja o resultado:

```json
{
	"max": [
		{
			"producer": "Matthew Vaughn",
			"interval": 13,
			"previousWin": "2002",
			"followingWin": "2015"
		},
		{
			"producer": "Buzz Feitshans",
			"interval": 9,
			"previousWin": "1985",
			"followingWin": "1994"
		}
	],
	"min": [
		{
			"producer": "Bo Derek",
			"interval": 6,
			"previousWin": "1984",
			"followingWin": "1990"
		},
		{
			"producer": "Joel Silver",
			"interval": 1,
			"previousWin": "1990",
			"followingWin": "1991"
		}
	]
}
```

2. modelo de dados baseado no CSV:


<img width="1385" height="416" alt="image" src="https://github.com/user-attachments/assets/a4d43419-6da8-4fe5-8733-1d461e2e51ba" />
