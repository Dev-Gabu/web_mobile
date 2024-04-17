Uma aplicação web degina de forma geral toda e qualquer sistema projetado para a utilização em um navegador, desenvolvidos utilizandose tecnologias web ( HTML, JS, CSS). Pode ser executado a partir de um servidor HTTP (Webhost) e localmente, no dispositivo do usuário.

### Receber uma solicitação (requisição) e devolve conteúdo (response) para o cliente. Geralmente os servidores enviam instruções para o Browser escritas instruçõoes para o browser escritas em HTML. O HTML diz ao browser como apresentar o conteudo ao usuário web.

HTML

Linguagem de marcação (delineamento) padrão utilizada para criar páginas WEb
Não é uma linguagem de programação
Utilizada para fins estruturais
HTML apenas encapsula dados e descreve o que fazer com eles, não como fazer.

JavaScript

Linguagem de programação de alto nível, leve e interpretada, criada, a principio, para ser executada em navegadores para manipular comportamentos de páginas web.
Conhecida como linguagem de script da internet
Uma das mais importantes tecnllogias voltadas para o desenvolvimento front-end
Atualmente nao se restringe apenas a páginas de navegadores. Xom o advento dos frameworks, APIs, melhorias e dcriação de novos recursos, hoje é possível utilizar Javascript em aplicativos mobile, softwares para desktop e até mesmo serviços back-end

CSS 

Assim como HTML, não é uma linguagem de programação
Trata-se de uma linguagem de folhas de estilos que é utilizada para definir como os documentos escritos na linguagem de marcação (HTML ou XML) devem ser apresentados em termos de formatação, de layout.

Em um cenário ideal, o HTML é usado para estruturar os conteúdos, o CSS é utilizado para formatá--los e o JavaScript para prover dinamismo.

GET POST PUT DELETE

Framework é um conjunto de conceitos usado para resolver um problema de um domínio específico. Um framework, conceitualmente, não se trata de um software executável, mas sim de um modelo de dados para um domínio. Framework de software compreende de um conjunto de classes implementadas em uma linguagem de programação específica, usadas para auxiliar o desenvolvimento de software. O framworl atua onde há funcionalidades em comum a várias aplicações, porém para isso as aplicações devem ter algo razoavelmente grande em comum para que o mesmo possa ser utilizado em vária aplicações.

Bootstrap   
    O mais popular framework HTML, CSS, e JS para desenvolvimento de projetos responsivos. Originalmente foi desenvolvido para o Twitter. Posteriormente, se tornou uma das estruturas de front-end de código aberto mais populares do mundo.

JQuery
    Biblioteca JavaScript cross--browser desenvolvida para simplificar os scripts client-side que iinteragem com o HTML. Usada por cerca de 77% dos 10 mil sites mais visitados do mundo, JQuery é a mais popular biblioteca Javascript.

### Padrões Arquiteturais

Definem a estrutura, interações e organização dos componentes do software, facilitando a comunicação entre desenvolvedores e garantindo a escalabilidade, manutenção e reutilização de código.

Padrões existentes:
    - Monolítico
    - Microserviços
    - Modelo-Visão-Controlador (MVC)

Padrão Monolitico: Aplicação formada por módulos que, mesmo agindo separadamente, continuam ligados, transformando o conjunto em um único sistema. Facilidade (inicialmente) de criar uma solução única, interligando todas as funcionalidades do sistema. Problemas: Escalabilidade, agregação de tecnologias, demora no aculturamento para novos integrantes, aumento da complexidade e do tamanho do código ao longo do tempo, alta depend:ência de componentes de código, falta de flexibilidade, dificuldade para colocar alterações na produção.

Padrão Microserviços: Prevê a separação dos elementos de funcionalidade, colocados em serviços separados, dessa forma tornando-os totalmente autônomos e totalmente independentes, que se comunicam por meio de APIs. Cada funcionalidade é separada em serviços bem definidos que podem ou não complementar outra funcionalidade. Principal dificuldade: necessidade de desenvolvedores qualificados. 

Padrão MVC: Model-View-COntroller é um padrão de arquitetura de software que separa a representação da informação da interação do usuário com ele. Alterações feitas no layout não afetam a manipulação de dados, e estes poderão ser organizados sem alterar o layout. Provê a separação das tarefas de acesso aos dados e lógica de negócio, lógica de apresentação e de interação com o utilizador, introduzindo um componente entre os dois: O controlador

    Modelo (Model): Consiste nos dados da aplicação, regras de negócio, lógica e funções.

    Visão: Pode ser qualquer saída de representaçãoo dos dados, como uma tabela ou um diagrama. É possível ter várias visões do mesmo dado, como um gráfico de barras para gerenciamento e uma visão tabular para contadores.

    Controlador: Fas a mediação da entrada, convertendo-a eem comandos para o modelo ou visão. As ideias centrais por trás do MVC são a reusabilidade do código e separação do código. O controlador vai estar tradicionalmente relacionado a uma rota URL.

Browser -> 1. O usuário envia um pedido de url -> Controlador
Controlador -> 2. O controlador pede dados ao modelo -> Modelo
Modelo -> 3. O modelo devolve os dados pedidos -> Controlador
Controlador -> 4. O controlador seleciona a visão e fornece os dados -> Visão
Visão -> 5. A visão selecionada é devolvida ao controlador -> Controlador
Controlador -> 6. O controlador devolve a visão como a resposta para o browser -> Browser

Model View Template (MVT): 

    Modelo representa a camada de acesso aos dados, geralmente é responsável pelo acesso ao banco de dados. 
    
    Template: camada de apresentação da informação, que lida com a interface para o usuário.

    View: Camada usada para inplementar a lógica de negócios e interagir com um modelo para transportar os dados e renderizar um template.

### Mapeamento Objeto Relacional

Técnica de desenvolvimmento de softwares utilizado para reduzir a demanda de trabalho em programação orientada a objetos ao se utilizar de bancos de dados relacionais. As tabelas do banco de dados são representadas através de classes e os reistros de cada tabela são representados como instâncias das classes correspondentes.

Com essa técnica, o programador não precisa se preocupar com os comandos em linguagem SQL. Ele irá usar uma interface de programação simples que faz todo o trabalho de persistência. Não é necessária uma correspondência direta entre as tabelas de dados e as classes do programa. A relação entre as tabelas onde originam os dados e o objeto que os disponibiliza é configurada pelo programador isolando o código do programa das alterações à organização dos dados nas tabelas do banco de dados.

A forma como esse mapeamento é configurado depende da ferramenta utilizada. Como exemplo, o programador que use Hibernate na linguagem Java pode usar arquivos XML ou o sistema de anotações (annotations) que a linguagem providencia. Em outros casos o mapeamento é feito diretamente no código, através de herança de classes especiais como é o caso do ORM no Django e do SqlAlchemy na linguagem Python.

Algumas ferramentas gráficas podem ser usadas para gerar o código que representa o modelo do banco, como o ORM Python também na linguagem Python.

### DESENVOLVIMENTO DE SOFTWARE

Levantamento de Requisitos: Propiciar que usuários e desenvolvedores tenham a mesma compreensão do problema a aser resolvido

Análise: Construir modelos que determinam qual é o problema para o qual estamos tentando conceber uma solução de software

Projeto: estágio no qual o modelo de análise terá de ser adaptado de tal modo que possa servir como base para implementação no ambiente alvo.

Codificação: a codificação do sistema efetivamente executada.

Testes: 

# Desenvolvimento Agil

Agilidade: capacidade de responder adequadamanete a mudanças (software, equipe, tecnologias, ets...) Adequado para gerenciamento de requisitos e prioridades instáveis (volateis). Projeto e construção são realizados simultaneamente. Analise, projeto, implementação e testes não são tão previsíveis (planejamento). 

# Extreme Progamming - XP

Cliente presente, participa ativamente do processo de desenvolvimento, facilitando a comunicação, acompanhando o processo e sendo informado sobre mudanças. Planejamento: o desenvolvimento utilizado no XP é feito em iterações. Uma iteração é um periodo curto de tempo (1 ou 2 semanas) onde a equipe desenvolve um conjunto de funcionalidades. Releases curtos: As liberações de pequenas versões funcionais do projeto auxiliam muito no proocesso de aceitação por pparte do cliente. Stand-up meeting: são reuniões feitas em pé e de curta duração, geralmente envolvendo as seguinte perguntas: o que você fez ontem? o que você vai fazer hoje? existe algum impedimento? Ainda que apareça algum problema, essa reunião não tem o propósito de pensar em soluções. Programação em pares: Programação em pares (duplas) em um único computador. Busca-se sempre a evolução da equipe melhorando a qualidade do código-fonte. Semana de 40 horas: trabalhar com qualidade buscando ter um ritmo de trabalho saudável, 40h por semana, 8h por dia. Testes constantes: Utiliza-se o desenvolvimeno Orientado a Testes (Test Driven Development). Refatoração: processo que permite a melhoria continua da programação. Refatorar melhora a clareza, leitura do código e facilita a manutenção. Padronização de código: como todo mundo trabalha no desenvolvimento do mesmo software, a equipe de desenvolvimento do mesmo software, a equipe de desenvolvimento precisa estabelecer regras para programar.

Frases conhecidas:
- Sem um processo, só uma pessoa excepcional consegue desenvolver um sistema.
- com muitos processos, pessoas excepcionais não conseguem desenvolver sistemas excepcionais.
- Um boa equipe pequena produz mais que grandes equipes.

Principios e valores: 

# Scrum

Metodologia agil para gestão e planejamento de projetos de softwarem especialmente de pequeno e médio porte. Projetos de grande complexidade exigem processos mais complexos(RUP). As funcionalidades a serem implementadas em um projeto são mantidas em uma lista que é conhecida como Product Backlog. No Scrum, o escopo do projeto (product backlog) é dividido em ciclos (tipicamente quinzenais ou mensais) chamados sprints.

# Django framework

O Django utiliza o princípio DRY (Don't Repeat Yourself), que permite que você reutilize trechos de código. 

Django utiliza o modelo (MVT), ORM *PESQUISE*

Django se comunica a partir de funções HttpRequest e HttpResponse

HttpRequest contém metadados sobre o que foi solicitado e cada view é responsável por devolver um objeto HttpResponse.

## HTTP

GET : /photo
DELETE : /photos/{photoID}
POST : /pic
PUT : /photos/{photoID}

# Status Code

*2xx Sucess*
200 Sucess / OK

*3xx Redirection*
301 Permanent Redirect
302 Temporary Redirect
304 Not Modified

*4xx Client Error*
401 Unauthorized Error
403 Forbidden
404 Not found
405 Method Not Allowed

*5xx Server Error*
501 Not Implemented
502 Bad Gateway
503 Serviice Unavaliable
504 Gateway Timeout




## Passos aula 10/04

manage.py createsuperuser

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Araguaina"
DATE_FORMAT = "%d/%m/%Y"


Intalar Postgresql 
Intalar Psycog

Criar perfil PGadmin
Criar database sistema

Atualizar Database settings.py

Atualizar view.py urls.py e templates em settings.py
Criar diretório templates

## Diagramas estruturais

Modelas aspectos estáticos do software, como métodos, interfaces, serviços, arquitetura e classes, por exemplo. Ex: diagrama de classes, diagrama de componentes diagrama de implantação, diagrama de objetos, diagrama de pacotes, etc...

## Diagramas comportamentais

Especificam detalhes do comportamento do software, demonstrando o que deve acontecer no sistema. Ex: diadrama de caso de uso, diagrama de atividades, diagram de máquina de estados, digrama de sequencia, etc.

## Fazer: Diagrama de casos de uso, Diagrama de classes e Prototipagem Gráfica




