## MiniCTF

### Desafios

1. Criptografia
2. Ataques a passwords
3. Web
4. Engenharia Reversa

Em cada um dos desafios (de temas diferentes) o ninja recebe um segredo. No final vai precisar deles todos, por isso **é importante** seguir a ordem dos desafios deste documento.

#### 1. Criptografia

- **Fácil** - Cifra de César
- **Médio** - Cifra de substituição (substituir o alfabeto por um à escolha)
- **Difícil** - Cifra de Viginére

#### 2. Ataques a passwords ou a mensagens escondidas

- **Fácil** - A password está no próprio ficheiro de Python, mas não está logo à vista
- **Médio** - Recebe a password em binário e tem de a descobrir convertendo para string
- **Difícil** - É dito que isto tem de ser um ataque de força bruta, a um executável em c que recebe a password como argumento e retorna a flag. Têm de fazer um script em python que faça essa força bruta.

#### 3. Web

- **Fácil** - A mensagem está escondida no código fonte
- **Médio** - Uma página de autenticação onde a autenticação é feita no lado do cliente e a verificação está no código fonte.
- **Difícil** - É dada uma lista de subdiretorias. Eles têm de fazer um pedido para cada diretoria para ver quais existem, explorá-las e ver qual delas tema flag.

#### 4. Engenharia Reversa

- **Fácil** - Programa em python que executa a função errada
- **Médio** - Programa em python executa código encriptado
- **Difícil** - Programa em python que encripta um segredo