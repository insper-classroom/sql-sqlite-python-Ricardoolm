[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11573542&assignment_repo_type=AssignmentRepo)
# ProjÁgil - 2023

Material de apoio sobre SQL: https://www.devmedia.com.br/guia/guia-completo-de-sql/38314

### Exercício 1: SQL

Iremos utilizar a plataforma https://sqliteonline.com/ para treinar comandos SQL básicos. O arquivo que usaremos é "vgsales_pbi.csv" que pode ser baixado no link https://drive.google.com/file/d/1fhcUzrJau2w5zcQ1B3wpKhOv9mWet0xR/view?usp=sharing.

1. **Jogos da plataforma Xbox One**:
   - **Enunciado**: Liste todos os jogos disponíveis para a plataforma Xbox One. (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql      
        SELECT * FROM vgsales_pbi
        WHERE platform="XOne";   
     ```
   - **Resultado**
"Call of Duty: Black Ops 3"	"XOne"	"2015,0"	"Shooter"	"Activision"	"4,52"	"2,09"	"0,01"	"7,3"
"Halo 5: Guardians"	"XOne"	"2015,0"	"Shooter"	"Microsoft Game Studios"	"2,64"	"1,2"	"0,03"	"4,26"
"Fallout 4"	"XOne"	"2015,0"	"Role-Playing"	"Bethesda Softworks"	"2,45"	"1,26"	"0,01"	"4,09"
"Gears of War: Ultimate Edition"	"XOne"	"2015,0"	"Shooter"	"Microsoft Game Studios"	"2,38"	"0,32"	"0,0"	"3,0"
"Star Wars Battlefront (2015)"	"XOne"	"2015,0"	"Shooter"	"Electronic Arts"	"1,94"	"1,22"	"0,02"	"3,49"
"FIFA 16"	"XOne"	"2015,0"	"Sports"	"Electronic Arts"	"0,88"	"2,11"	"0,0"	"3,23"
"Destiny"	"XOne"	"2014,0"	"Shooter"	"Activision"	"2,13"	"0,92"	"0,0"	"3,28"
"Halo: The Master Chief Collection"	"XOne"	"2014,0"	"Shooter"	"Microsoft Game Studios"	"1,89"	"0,99"	"0,03"	"3,15"
"Assassin's Creed: Unity"	"XOne"	"2014,0"	"Action"	"Ubisoft"	"2,26"	"0,89"	"0,0"	"3,46"
"Grand Theft Auto V"	"XOne"	"2014,0"	"Action"	"Take-Two Interactive"	"2,66"	"2,01"	"0,0"	"5,08"
"Call of Duty: Advanced Warfare"	"XOne"	"2014,0"	"Shooter"	"Activision"	"3,21"	"1,53"	"0,01"	"5,13"

    


2. **Jogos de Ação após 2010**:
   - **Enunciado**: Liste todos os jogos do gênero "Ação" que foram lançados após 2010.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi
      WHERE GENRE="Action" and year>2010;
      
     ```
   - **Resultado**
   Brothers Conflict: Precious Baby	PSV	2017,0	Action	Idea Factory	0,0	0,0	0,01	0,01
   Lego Star Wars: The Force Awakens	PS4	2016,0	Action	Warner Bros. Interactive Entertainment	0,14	0,32	0,0	0,54
   Gundam Breaker 3	PS4	2016,0	Action	Namco Bandai Games	0,0	0,0	0,09	0,09
   Taiko no Tatsujin: Don Don! Mystery Adventure	3DS	2016,0	Action	Namco Bandai Games	0,0	0,0	0,09	0,09
    ReCore	XOne	2016,0	Action	Microsoft Game Studios	0,06	0,03	0,0	0,1

3. **Jogos mais recentes**:
   - **Enunciado**: Liste os 5 jogos mais recentes lançados.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi
      WHERE year>2017;
      
     ```
   - **Resultado**
   Imagine: Makeup Artist	DS	2020,0	Simulation	Ubisoft	0,27	0,0	0,0	0,29
   Phantasy Star Online 2 Episode 4: Deluxe Package	PS4	2017,0	Role-Playing	Sega	0,0	0,0	0,03	0,03
   Brothers Conflict: Precious Baby	PSV	2017,0	Action	Idea Factory	0,0	0,0	0,01	0,01
   Phantasy Star Online 2 Episode 4: Deluxe Package	PSV	2017,0	Role-Playing	Sega	0,0	0,0	0,01	0,01
    


4. **Jogos mais antigos**:
   - **Enunciado**: Liste os 5 jogos mais antigos.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi
      WHERE year<1981;    
      
     ```
   - **Resultado**
   Bridge	2600	1980,0	Misc	Activision	0,25	0,02	0,0	0,27
   Freeway	2600	1980,0	Action	Activision	0,32	0,02	0,0	0,34
   Defender	2600	1980,0	Misc	Atari	0,99	0,05	0,0	1,05
   Kaboom!	2600	1980,0	Misc	Activision	1,07	0,07	0,0	1,15
   Boxing	2600	1980,0	Fighting	Activision	0,72	0,04	0,0	0,77
  The Technomancer	XOne	2016,0	Role-Playing	Focus Home Interactive	0,01	0,01	0,0	0,02


5. **Jogos de Aventura com mais vendas na América do Norte**:
   - **Enunciado**: Quais são os 3 jogos do gênero "Aventura" com as maiores vendas na América do Norte?  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi
      WHERE genre="Adventure" and na_sales>"2";
      
     ```
   - **Resultado**
   Assassin's Creed	X360	2007,0	Adventure	Ubisoft	3,28	1,65	0,07	5,55
   Super Mario Land 2: 6 Golden Coins	GB	1992,0	Adventure	Nintendo	6,16	2,04	2,69	11,18
   Zelda II: The Adventure of Link	NES	1987,0	Adventure	Nintendo	2,19	0,5	1,61	4,38
    


	 
6. **Jogos de RPG ou Estratégia lançados após 2005**:
   - **Enunciado**: Liste todos os jogos dos gêneros "RPG" ou "Strategy" lançados após 2005.  (copie e cole o comando e as 5 primeiras linhas do resultado aqui)
   - **Query**:
     ```sql
      SELECT * FROM vgsales_pbi
      WHERE genre='Role-Playing' or genre="Strategy" and year > "2005";

     ```
   - **Resultado**
    Phantasy Star Online 2 Episode 4: Deluxe Package	PS4	2017,0	Role-Playing	Sega	0,0	0,0	0,03	0,03
    Phantasy Star Online 2 Episode 4: Deluxe Package	PSV	2017,0	Role-Playing	Sega	0,0	0,0	0,01	0,01
    Persona 5	PS3	2016,0	Role-Playing	Unknown	0,0	0,0	0,1	0,1
    Caligula	PSV	2016,0	Role-Playing	FuRyu	0,0	0,0	0,05	0,05
    The Technomancer	XOne	2016,0	Role-Playing	Focus Home Interactive	0,01	0,01	0,0	0,02
    



### Exercício 2: Python - Sqlite

Objetivo: Familiarizar-se com os comandos básicos de SQL e aprender a filtrar registros usando o comando WHERE.

Crie uma tabela chamada "Estudantes" com os seguintes campos:

- **ID (chave primária)**
- **Nome**
- **Curso**
- **Ano de Ingresso**

Insira 5 registros de estudantes na tabela. Inclua os seguintes estudantes fictícios como parte desses registros:

- Ana Silva, Computação, Ano de Ingresso: 2019
- Pedro Mendes, Física, Ano de Ingresso: 2021
- Carla Souza, Computação, Ano de Ingresso: 2020
- João Alves, Matemática, Ano de Ingresso: 2018
- Maria Oliveira, Química, Ano de Ingresso: 2022
 
**Selecione e mostre todos os registros da tabela no console.**

- Filtre e mostre os estudantes que ingressaram entre 2019 e 2020 (inclusive) e exiba no console. Use o comando WHERE para realizar essa filtragem.

- Atualize o "Ano de Ingresso" de um estudante específico. Mostre por todos estudantes novamente.

- Delete um registro da tabela usando o ID do estudante. Mostre por todos estudantes novamente.

- Filtre e mostre os estudantes do Curso de Computação que ingressaram após 2019. Mostre o resultado.

- Imagine que alguém errou nos registros de ingresso de todos os alunos do curso de Computação, crie uma query que altere todos os registros dos alunos de Computação, campo ingresso para 2018. Mostre por todos estudantes novamente.




### Exercicio 3: Python - SQLite

**Exercício de Reaproveitamento e Organização de Código**

A medida que os sistemas crescem e se tornam mais complexos, a necessidade de manter o código organizado e reutilizável torna-se cada vez mais evidente. Manter funções comuns em módulos separados não apenas torna seu código mais legível, mas também permite que você reutilize funções sem duplicar o código. Isso reduz o risco de erros, facilita a manutenção e economiza tempo no longo prazo.

Considere o arquivo `main_1.py` que vocês trabalharam anteriormente. Nele, várias operações relacionadas ao banco de dados foram realizadas. Estas operações são comuns em muitas aplicações e podem ser reutilizadas em diversos contextos.

**Tarefa:** 

1. Crie um arquivo chamado `db_utils.py` dentro da pasta `db`.
2. Crie funções mais comuns relacionadas ao banco de dados para este novo arquivo. Por exemplo, funções para criar tabelas, inserir registros, consultar registros, atualizar e deletar.
3. No `main_2.py`, importe e utilize as funções do arquivo `db_utils.py` para realizar as operações do Exercício 2.

**Dica:** Ao organizar seu código desta maneira, você estará aplicando o princípio DRY (Don't Repeat Yourself) do desenvolvimento de software, que visa reduzir a repetição de informações de todos os tipos.