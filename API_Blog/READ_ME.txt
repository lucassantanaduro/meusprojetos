#Como usar.

1. Execute o arquivo api_app.py
2. Utilize o Postman ou outra plataforma de API
3. Faça login no endpoint http://localhost:8080/login com o username: Lucas Santana Senha: 654321; Adicionando autorização do tipo Basic Auth no header.
4. Faça a requisição e obtenha um token (o token tem validade de 30 minutos apartir do momento em que foi gerado).
5. Faça requisições do tipo GET, UPDATE, PUT, DELETE adicionando ao HEADER a key "x-access-token" com o value = token.

#endpoints no arquivo api_app.py

