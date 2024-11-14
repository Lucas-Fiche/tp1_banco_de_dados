# Programa de Sócio Torcedor

<details>

<summary>📘 1. Introdução ao Programa de Sócio Torcedor</summary>

  ## 1. Introdução ao Programa de Sócio Torcedor

  O programa de Sócio Torcedor é uma iniciativa de clubes de futebol voltada para o engajamento e fidelização dos seus torcedores, oferecendo a eles a oportunidade de apoiar diretamente o clube e, em troca, obter benefícios exclusivos. Comum em diversos times ao redor do mundo, esse programa se tornou uma fonte importante de receita para as equipes, complementando os ganhos com venda de ingressos, patrocínios e direitos de transmissão.

  A principal ideia por trás do programa é criar um vínculo mais próximo entre o clube e seus torcedores, oferecendo vantagens como prioridade na compra de ingressos, descontos em produtos oficiais, acesso a áreas exclusivas nos estádios, e a possibilidade de participar de eventos especiais, como encontros com jogadores e visitas às instalações do clube. Esse modelo de fidelização não apenas beneficia os torcedores, que têm acesso a experiências e serviços diferenciados, como também representa uma importante estratégia financeira e de marketing para o clube.

  Além dos benefícios diretos, o Sócio Torcedor incentiva uma base de fãs mais engajada e comprometida com o sucesso do clube, criando um ciclo de apoio mútuo. Muitos clubes oferecem diferentes planos, adaptando os benefícios e preços às preferências e possibilidades de cada torcedor, aumentando assim o alcance e a acessibilidade do programa.

  ### Exemplo para o Trabalho: Programa de Sócios "Camisa 7" do Botafogo de Futebol e Regatas


  Para o desenvolvimento do presente trabalho, utilizaremos como exemplo o programa de Sócio Torcedor do Botafogo de Futebol e Regatas, denominado "Camisa 7". Este programa é direcionado aos torcedores do Botafogo e oferece uma série de vantagens para aqueles que se tornam sócios, fortalecendo o vínculo entre o clube e sua torcida apaixonada.

  O programa "Camisa 7" concede aos sócios benefícios como prioridade e descontos na compra de ingressos, vantagens em produtos e serviços oficiais, acesso a eventos e experiências exclusivas, além de promoções junto a parceiros comerciais. Essa estrutura proporciona um caso rico para modelagem de banco de dados, uma vez que envolve uma diversidade de informações sobre o relacionamento entre o torcedor e o clube, planos de associação, regras de uso e diferentes tipos de benefícios e acessos.

  No decorrer do trabalho, focaremos na criação de uma estrutura de banco de dados que capture os principais aspectos do programa "Camisa 7", incluindo a modelagem de dados para sócios, planos, benefícios, e registros de transações, garantindo um sistema que pode sustentar tanto as operações internas do clube quanto o suporte aos torcedores cadastrados no programa.

  ## 2. Resumo sobre o Negócio


  O programa de sócios torcedores "Camisa 7" do Botafogo de Futebol e Regatas visa fortalecer a relação entre o clube e seus torcedores, oferecendo benefícios exclusivos para aqueles que aderirem ao programa. Atuando no setor esportivo e de entretenimento, o programa permite que os torcedores apoiem diretamente o clube, contribuindo para a sustentabilidade financeira e participando de um modelo de engajamento que vai além dos jogos.

  ### Ramo de Atuação


  O "Camisa 7" opera no mercado de fidelização esportiva, focado em oferecer vantagens exclusivas aos sócios torcedores, como prioridade na compra de ingressos, descontos em produtos oficiais, acesso a eventos exclusivos e outras experiências voltadas para os fãs.

  ### Tipos de Serviços e Benefícios

  <ul>
    <li>Prioridade e desconto na compra de ingressos para jogos do Botafogo.
    <li>Descontos em produtos oficiais do clube e de parceiros.
    <li>Acesso a áreas exclusivas do estádio.
    <li>Possibilidade de participar de eventos e experiências únicas com o clube, como visitas ao estádio e encontros com jogadores.
    <li>Benefícios relacionados a parceiros comerciais (lojas, restaurantes, academias, etc.).
  </ul>

  ### Principais Atores

  <ul>
    <li>Sócio Torcedor**: O torcedor cadastrado no programa, que possui diferentes níveis de adesão e benefícios.
    <li>Clube (Botafogo de Futebol e Regatas)**: Responsável por gerenciar o programa, estabelecer parcerias e promover os eventos e benefícios.
    <li>Fornecedores e Parceiros Comerciais**: Empresas e lojas que oferecem benefícios exclusivos aos sócios.
  </ul>

  ### Dados Essenciais

  <ul>
    <li>Informações pessoais dos sócios (nome, CPF, endereço, e-mail…).
    <li>Dados de adesão ao programa (tipo de plano, data de adesão, status…).
    <li>Histórico de benefícios e utilização de serviços.
    <li>Informações sobre pagamentos e renovação de planos.
    <li>Detalhes de eventos exclusivos e ingressos adquiridos.
  </ul>

  ### Fluxos de Processos Cotidianos

  <ul>
    <li>Adesão e Cancelamento**: Processo pelo qual o torcedor adere ao programa ou cancela sua inscrição.
    <li>Gerenciamento de Benefícios**: Atribuição e gestão dos benefícios que cada sócio tem direito, de acordo com o plano.
    <li>Compra de Ingressos**: Prioridade e descontos na compra de ingressos para partidas, com controle de disponibilidade e acesso.
    <li>Renovação de Planos**: Procedimento para renovação automática ou manual dos planos dos sócios.
  </ul>

  ### Regras e Restrições

  <ul>
    <li>Cada sócio tem direito a um único cadastro, identificado pelo CPF.
    <li>O sócio deve manter as mensalidades em dia para usufruir dos benefícios.
    <li>Há limites de quantidade e frequência para alguns benefícios, como a compra de ingressos com desconto.
    <li>As vantagens e os preços podem variar conforme o plano escolhido pelo torcedor.
  </ul>
</details>

<details>

<summary>📘 2. Modelo Conceitual (MER) </summary>

# Modelo Conceitual (MER)

## Introdução

O Modelo Conceitual é a primeira etapa na criação de um banco de dados e representa uma visão abstrata e de alto nível do sistema, descrevendo os principais elementos (entidades) e como eles se relacionam entre si. O objetivo do modelo conceitual é garantir que todos os requisitos do sistema sejam capturados de forma clara, sem se preocupar ainda com a estrutura física ou a implementação específica no banco de dados. É uma visão do “mundo real” do sistema, com foco em como os dados e informações devem ser organizados e compreendidos.

## Estrutura e Funcionamento do Modelo Conceitual

No Modelo Conceitual, usamos o Modelo Entidade-Relacionamento (MER) para identificar:

<ul>
  <li> Entidades: Representam os principais elementos do sistema, como pessoas, objetos ou eventos. Cada entidade é algo do “mundo real” que deve ser armazenado no banco de dados. No caso deste trabalho, as entidades incluem Sócio, Plano, Benefício, Ingresso, Pagamento, Setor_Estadio, Evento_Exclusivo, entre outras.

  <li> Atributos: São as características ou informações relevantes sobre cada entidade. Por exemplo, a entidade Sócio possui atributos como Nome, CPF, Endereço, Telefone, e Pontos_Socio. Esses atributos são as informações que devem ser registradas para cada instância da entidade.

  <li> Relacionamentos: Descrevem como as entidades estão conectadas. Cada relacionamento possui uma cardinalidade, que indica o tipo de ligação entre as entidades, como um-para-um (1:1), um-para-muitos (1:N), ou muitos-para-muitos (N:N). Os relacionamentos entre entidades são essenciais para definir a lógica de como os dados se conectam no sistema.

  <li> Cardinalidade: Define o número de instâncias de uma entidade que podem se associar a instâncias de outra entidade. Por exemplo, a relação entre Sócio e Plano é N:1, indicando que um sócio está associado a um único plano, mas um plano pode ter vários sócios.
</ul>

## Como o Modelo Conceitual foi Feito neste Trabalho

Neste trabalho, o Modelo Conceitual do sistema foi desenvolvido para organizar os dados de um programa de sócios torcedores de um clube de futebol, chamado "Camisa 7". Este modelo conceitual visa representar todos os dados relevantes do sistema, incluindo o gerenciamento de sócios, planos, pagamentos, ingressos, benefícios e eventos exclusivos para sócios.

### Principais Etapas do Desenvolvimento do Modelo Conceitual:

#### Identificação das Entidades:

As principais entidades identificadas foram:
<ul>
	<li> Sócio: Representa os membros do programa de sócios torcedores.
	<li> Plano: Representa os diferentes tipos de planos disponíveis para os sócios.
	<li> Benefício: Representa os benefícios oferecidos nos planos.
	<li> Ingresso: Representa os ingressos para eventos (jogos) que os sócios podem comprar com desconto.
	<li> Setor_Estadio: Representa as diferentes áreas do estádio onde os sócios podem adquirir ingressos.
	<li> Pagamento: Representa os pagamentos feitos pelos sócios para manterem sua adesão ao plano.
	<li> Evento_Exclusivo: Representa os eventos exclusivos disponíveis apenas para os sócios do clube.
</ul>

#### Definição dos Atributos:


Cada entidade recebeu uma série de atributos que descrevem suas características principais. Por exemplo:
<ul>
  <li> A entidade **Sócio** inclui atributos como `ID_Socio` (chave primária), `Nome`, `CPF`, `Endereço`, `Telefone`, `E-mail`, `Data_Adesao`, `Status_Socio`, e `Pontos_Socio`.
  <li> A entidade **Plano** inclui atributos como `ID_Plano` (chave primária), `Nome_Plano`, `Valor_Mensal`, `Valor_Anual` e `Descrição`.
</ul>
#### Definição dos Relacionamentos:


Para capturar as conexões entre as entidades, foram definidos vários relacionamentos, incluindo:
<ul>
  <li> ASSOCIADO_A: Relaciona Sócio e Plano, indicando que cada sócio é associado a um único plano, mas um plano pode ter vários sócios.
  <li> REALIZA: Relaciona Sócio e Pagamento, indicando que um sócio pode fazer vários pagamentos.
  <li> COMPRA: Relaciona Sócio e Ingresso, indicando que um sócio pode comprar vários ingressos.
  <li> PARTICIPA: Relaciona Sócio e Evento_Exclusivo via uma tabela intermediária, permitindo que sócios se inscrevam para participar de eventos exclusivos.
  <li> INCLUI: Representa a relação N:N entre Plano e Benefício. Essa relação indica que um plano pode incluir vários benefícios, e um benefício pode estar disponível em vários planos.
</ul>

#### Ajustes e Correções no Modelo Conceitual:

Após definir as entidades e relacionamentos, ajustes foram feitos para melhorar a clareza e a precisão do modelo. Atributos adicionais foram adicionados a algumas relações para capturar informações específicas (por exemplo, a quantidade de ingressos disponíveis para um setor específico). Também foi garantido que as setas de relacionamento estivessem corretamente apontadas das chaves estrangeiras para as chaves primárias correspondentes, reforçando a integridade dos dados no modelo.

## Conclusão do Modelo Conceitual

O modelo conceitual construído para o programa "Camisa 7" do Botafogo proporciona uma base clara e bem estruturada para o sistema de banco de dados. Ele descreve como cada entidade se relaciona com as demais e garante que todas as informações relevantes estão organizadas de forma lógica e compreensível. Esse modelo é fundamental para a próxima etapa do desenvolvimento do banco de dados, onde será criado o Modelo Lógico, que traduzirá essa visão conceitual em um formato mais próximo da implementação no banco de dados.
</details>

<details>

<summary>📘 3. Modelo Lógico - Diagrama de Engenharia de Informação</summary>

# Modelo Lógico - Diagrama de Engenharia de Informação

## Introdução

O Modelo Lógico é uma etapa intermediária entre o modelo conceitual e a implementação física no banco de dados. Ele representa a estrutura de dados de maneira mais detalhada, especificando as tabelas, chaves primárias, chaves estrangeiras e relacionamentos de forma que se aproxime do formato final a ser utilizado no banco de dados. O objetivo é traduzir as ideias do modelo conceitual em uma estrutura que possa ser implementada no sistema de gerenciamento de banco de dados (SGBD), garantindo a integridade e a consistência dos dados.

## Estrutura e Funcionamento do Modelo Lógico

No Modelo Lógico, cada entidade do modelo conceitual se torna uma tabela, e os relacionamentos entre as entidades são implementados usando chaves estrangeiras e, quando necessário, tabelas intermediárias. A modelagem lógica envolve:

### Tabelas e Atributos

<ul>
  <li> Cada entidade do modelo conceitual é convertida em uma tabela com atributos bem definidos.
  <li> Cada tabela possui uma chave primária (PK), que é um identificador único de cada registro, além de outros atributos que representam as informações que serão armazenadas.
</ul>

**Exemplo**: A entidade `Sócio` se tornou a tabela `Sócio`, contendo atributos como `ID_Socio` (PK), `Nome`, `CPF`, `Endereço`, `Pontos_Socio`, entre outros.

### Chaves Estrangeiras (FK)

<ul>
  <li> Para conectar as tabelas e garantir a integridade referencial, foram adicionadas chaves estrangeiras nas tabelas dependentes.
  <li> As chaves estrangeiras estabelecem relacionamentos entre as tabelas, apontando para a chave primária de outra tabela.
</ul>

**Exemplo**: Na tabela `Pagamento`, o campo `ID_Socio` é uma chave estrangeira que se conecta à chave primária `ID_Socio` na tabela `Sócio`. Isso indica que cada pagamento está associado a um sócio específico.

### Relacionamentos com Tabelas Intermediárias para Relacionamentos ‘N:N’


- Relacionamentos muitos-para-muitos (N:N) foram implementados usando tabelas intermediárias, chamadas de tabelas associativas. Cada tabela intermediária possui chaves estrangeiras que se conectam a duas tabelas principais, estabelecendo o relacionamento N:N de forma indireta.
  
  **Exemplos**:
  - `Plano_Beneficio`: Tabela intermediária entre `Plano` e `Benefício`, permitindo que um plano inclua vários benefícios e que cada benefício esteja disponível em vários planos.
  - `Participacao_Evento`: Relaciona `Sócio` e `Evento_Exclusivo`, permitindo que sócios possam participar de múltiplos eventos e que cada evento tenha a participação de vários sócios.
  - `Disponibilidade_Ingresso`: Conecta `Ingresso` e `Setor_Estadio`, permitindo a configuração de ingressos disponíveis para diferentes setores em cada jogo.

### Uso de Cardinalidades com Formato "Pé de Galinha"


No modelo lógico, os relacionamentos entre as tabelas são representados com linhas e símbolos que indicam a cardinalidade, utilizando o formato "pé de galinha":
- **‘1:N’**: Indica que uma ocorrência em uma tabela pode estar relacionada a várias ocorrências em outra tabela.
- **‘N:N’**: Indica um relacionamento muitos-para-muitos, que requer uma tabela intermediária.

  **Exemplo**: O relacionamento entre `Sócio` e `Plano` é 1:N (um sócio pertence a um único plano, mas um plano pode ter vários sócios), enquanto o relacionamento entre `Plano` e `Benefício` é N:N e é implementado através da tabela intermediária `Plano_Beneficio`.

## Tabelas e Relacionamentos Principais


| Tabela 1        | Tabela 2        | Cardinalidade | Implementação               | Descrição                                                                                   |
|-----------------|-----------------|---------------|-----------------------------|---------------------------------------------------------------------------------------------|
| Sócio           | Plano           | 1 : N         | Direta (FK em Sócio)        | Cada sócio está associado a um único plano, mas um plano pode ter vários sócios.            |
| Sócio           | Pagamento       | 1 : N         | Direta (FK em Pagamento)    | Um sócio pode realizar vários pagamentos, mas cada pagamento pertence a um único sócio.     |
| Pagamento       | Plano           | N : 1         | Direta (FK em Pagamento)    | Vários pagamentos podem estar vinculados a um único plano, mas cada pagamento é relacionado a um plano específico. |
| Sócio           | Ingresso        | 1 : N         | Direta (FK em Ingresso)     | Um sócio pode comprar vários ingressos, mas cada ingresso é comprado por um único sócio.    |
| Ingresso        | Setor_Estadio   | N : N         | Tabela Disponibilidade_Ingresso | Um ingresso pode estar disponível em vários setores, e um setor pode ter vários ingressos. |
| Sócio           | Evento_Exclusivo| N : N         | Tabela Participacao_Evento  | Um sócio pode participar de vários eventos exclusivos, e cada evento pode ter a participação de vários sócios. |
| Plano           | Benefício       | N : N         | Tabela Plano_Beneficio      | Um plano pode incluir vários benefícios, e um benefício pode estar disponível em vários planos. |

## O Funcionamento do Modelo Lógico no Sistema

O Modelo Lógico para o programa de sócios torcedores "Camisa 7" foi desenvolvido com o objetivo de organizar e estruturar todos os dados relacionados aos sócios, planos, pagamentos, ingressos, benefícios e eventos exclusivos. Esse modelo lógico descreve como cada tabela (entidade) está conectada a outras, definindo as interações permitidas entre os dados.

### Gerenciamento de Sócios e Planos


- A tabela `Sócio` está ligada à tabela `Plano` para garantir que cada sócio esteja associado a um plano específico, e os detalhes do plano, como valores mensal e anual, estão disponíveis na tabela `Plano`.
- Essa estrutura facilita o gerenciamento dos planos dos sócios e permite a atualização dos dados conforme necessário.

### Controle de Pagamentos


- A tabela `Pagamento` está relacionada a `Sócio` e `Plano`, permitindo registrar e monitorar os pagamentos realizados por cada sócio para o plano específico.
- A chave estrangeira `ID_Socio` em `Pagamento` conecta cada pagamento a um sócio específico, enquanto `ID_Plano` conecta ao plano relacionado, garantindo que o sistema possa verificar o status de pagamento de cada sócio.

### Distribuição de Ingressos e Setores do Estádio


- Com a tabela intermediária `Disponibilidade_Ingresso`, é possível definir a quantidade de ingressos disponíveis para cada setor do estádio em diferentes jogos.
- As conexões entre `Ingresso`, `Setor_Estadio` e `Disponibilidade_Ingresso` permitem gerenciar a disponibilidade de ingressos e organizar a venda por setor.

### Benefícios Associados aos Planos


- A tabela `Plano_Beneficio` conecta `Plano` e `Benefício`, permitindo que cada plano ofereça um conjunto de benefícios específicos.
- A estrutura N:N garante que benefícios possam ser oferecidos em múltiplos planos, e que cada plano possa ter vários benefícios, oferecendo flexibilidade no gerenciamento das vantagens dos sócios.

### Eventos Exclusivos para Sócios


- A tabela `Participacao_Evento` conecta `Sócio` e `Evento_Exclusivo`, permitindo que os sócios se inscrevam para participar de eventos exclusivos e que o clube possa monitorar a participação.
- Isso permite ao sistema registrar e gerenciar a participação dos sócios em eventos especiais oferecidos pelo programa.
</details>

<details>

<summary>📘 4. Modelo Físico</summary>

# Modelo Físico

## Introdução

O Modelo Físico é a etapa final de modelagem de dados, onde os conceitos do modelo lógico são traduzidos diretamente para o formato de um banco de dados relacional. Essa etapa envolve a definição detalhada de cada tabela, incluindo os tipos de dados, restrições, chaves primárias e estrangeiras, e qualquer regra adicional necessária para garantir a integridade e consistência dos dados.

Neste trabalho sobre o programa de sócios torcedores "Camisa 7" do Botafogo, o Modelo Físico descreve como os dados são organizados e armazenados no banco de dados, permitindo que o sistema funcione conforme planejado. Ele estabelece a estrutura real que será implementada no sistema de gerenciamento de banco de dados (SGBD) com o MySQL.

## Estrutura e Aplicação do Modelo Físico ao Programa de Sócios Torcedores

### Definição de Tabelas com Tipos de Dados Específicos

- Cada entidade do modelo lógico foi convertida em uma tabela física com um conjunto de campos (atributos).
- Os tipos de dados foram escolhidos com base na natureza das informações armazenadas: por exemplo, `VARCHAR` para textos como nome e e-mail, `DATE` para datas, `DECIMAL` para valores monetários e `BOOLEAN` para status.

### Chaves Primárias e Unicidade dos Registros

- Em cada tabela, um campo foi escolhido como chave primária (PK) para garantir que cada registro seja único. As chaves primárias permitem identificar cada linha de maneira exclusiva.
- Em tabelas intermediárias (como `Plano_Beneficio` para o relacionamento N:N entre `Plano` e `Benefício`), uma chave primária composta foi definida usando múltiplos campos para garantir a unicidade das combinações entre entidades.

  **Exemplos**:
  - `ID_Socio` é a chave primária na tabela `Sócio`, garantindo que cada sócio seja identificado unicamente.
  - Na tabela intermediária `Plano_Beneficio`, a chave primária composta (`ID_Plano`, `ID_Beneficio`) impede a duplicação de combinações entre planos e benefícios.

### Chaves Estrangeiras e Relacionamentos


- Para conectar as tabelas de maneira lógica e garantir a integridade referencial, foram definidas chaves estrangeiras (FK) que referenciam as chaves primárias de outras tabelas.
- Isso garante que os dados em uma tabela estejam sempre relacionados de forma consistente a dados de outras tabelas.

### Tabelas Intermediárias para Relacionamentos ‘N:N’


- Relacionamentos muitos-para-muitos, como entre `Planos` e `Benefícios` ou `Sócios` e `Eventos Exclusivos`, foram implementados usando tabelas intermediárias.
- Essas tabelas intermediárias, como `Plano_Beneficio` e `Participacao_Evento`, contêm chaves estrangeiras para ambas as tabelas principais, criando o relacionamento N:N de forma indireta.

### Restrições e Domínios para Garantir a Integridade dos Dados


- Foram aplicadas restrições adicionais, como `CHECK` para validar valores numéricos (por exemplo, garantir que os valores de descontos estejam entre 0 e 1), `UNIQUE` para garantir que determinados campos sejam únicos (por exemplo, CPF e e-mail dos sócios), e `DEFAULT` para definir valores padrão em campos booleanos e inteiros.
- Essas restrições ajudam a prevenir erros e manter a integridade dos dados no sistema.

  **Exemplo**: Em `Pagamento`, a restrição `CHECK` em `Valor_pago` garante que o valor do pagamento seja sempre positivo.

## Como o Modelo Físico se Relaciona com o Funcionamento do Programa "Camisa 7"


O Modelo Físico para o programa de sócios torcedores "Camisa 7" foi projetado para estruturar e organizar todos os dados necessários para o funcionamento do sistema. Aqui está como ele permite que o programa opere:

### Cadastro e Gestão de Sócios


- A tabela `Sócio` armazena todas as informações dos membros, incluindo o plano de associação e os pontos acumulados.
- As restrições garantem que o cadastro seja único, evitando duplicações de CPF e e-mail.

### Configuração e Atribuição de Planos e Benefícios


- `Plano` e `Benefício` são tabelas separadas que definem cada plano de associação e os benefícios correspondentes.
- A tabela intermediária `Plano_Beneficio` permite associar múltiplos benefícios a um plano específico, proporcionando flexibilidade na criação de diferentes pacotes para sócios.

### Controle de Pagamentos


- A tabela `Pagamento` armazena cada transação feita pelos sócios, conectando cada pagamento a um sócio específico. Isso permite monitorar o status de pagamento e o histórico financeiro de cada membro.

### Distribuição de Ingressos e Setores do Estádio


- `Ingresso` e `Setor_Estadio` permitem a compra de ingressos para eventos, com informações sobre descontos e setores disponíveis.
- `Disponibilidade_Ingresso` gerencia a quantidade de ingressos disponíveis em cada setor, ajudando no controle da ocupação dos espaços.

### Gestão de Eventos Exclusivos para Sócios


- `Evento_Exclusivo` armazena eventos que são acessíveis apenas aos sócios.
- A tabela `Participacao_Evento` permite registrar quais sócios participam de quais eventos, facilitando a organização e o controle de participação em eventos especiais.

## Conclusão


O Modelo Físico transforma o projeto conceitual e lógico em uma estrutura prática e implementável. Ele define como cada dado será armazenado e acessado, garantindo a integridade, consistência e organização do banco de dados para o programa "Camisa 7". Com essa estrutura física implementada no SGBD, o sistema será capaz de gerenciar as inscrições, pagamentos, benefícios, ingressos e eventos dos sócios de maneira eficiente e escalável.
</details>

<details>

<summary>📘 5. Estapas de Normalização</summary>

# Etapas de Normalização e Estrutura do Banco de Dados

## Introdução

A normalização de dados é um processo essencial na modelagem de bancos de dados relacionais. Ela organiza as tabelas e elimina redundâncias, garantindo que os dados sejam armazenados de forma eficiente e evitando inconsistências. No caso do programa de sócios torcedores "Camisa 7", a normalização foi aplicada para assegurar a integridade dos dados e otimizar o desempenho do banco de dados.

## Etapas de Normalização


Abaixo estão as principais etapas de normalização seguidas para garantir que os dados estivessem em conformidade com as regras de normalização. No final do processo, os dados já estavam organizados de maneira a eliminar redundâncias e garantir a consistência.

### 1FN - Primeira Forma Normal


Para uma tabela estar na Primeira Forma Normal (1FN), ela precisa:
- Ter somente valores atômicos, ou seja, não conter grupos repetitivos ou valores multivalorados.
- Garantir que cada campo tenha um único valor por registro.

No banco de dados do programa "Camisa 7", todas as tabelas estão na 1FN, pois cada campo contém apenas valores atômicos e não há grupos repetitivos.

### 2FN - Segunda Forma Normal


Para uma tabela estar na Segunda Forma Normal (2FN), ela deve:
- Estar na 1FN.
- Ter todos os atributos totalmente dependentes da chave primária, eliminando dependências parciais.

A 2FN é aplicada principalmente a tabelas com chaves primárias compostas. No modelo do "Camisa 7", todas as tabelas que possuem chaves primárias compostas (como tabelas intermediárias para relacionamentos N:N) foram organizadas para que cada atributo dependa totalmente da chave primária composta.

### 3FN - Terceira Forma Normal

Para uma tabela estar na Terceira Forma Normal (3FN), ela precisa:
- Estar na 2FN.
- Ter todos os atributos dependentes somente da chave primária, eliminando dependências transitivas.

No banco de dados "Camisa 7", todas as tabelas foram normalizadas até a 3FN, garantindo que cada atributo seja diretamente dependente da chave primária, sem dependências transitivas.

### Confirmação de Normalização

Após a aplicação das três formas normais, o banco de dados do programa "Camisa 7" está totalmente normalizado até a Terceira Forma Normal (3FN). Isso garante que os dados sejam organizados de forma lógica e eficiente, com eliminação de redundâncias e consistência referencial.

## Estrutura do Banco de Dados no Programa "Camisa 7"

O banco de dados foi projetado para estruturar e organizar todos os dados necessários para o funcionamento do programa de sócios torcedores "Camisa 7", conforme descrito nas seções de normalização e modelagem. 

### Tabelas e Relacionamentos Principais


Abaixo estão os principais relacionamentos e suas implementações na estrutura física do banco de dados:

| Tabela 1        | Tabela 2        | Cardinalidade | Implementação               | Descrição                                                                                   |
|-----------------|-----------------|---------------|-----------------------------|---------------------------------------------------------------------------------------------|
| Sócio           | Plano           | 1 : N         | Direta (FK em Sócio)        | Cada sócio está associado a um único plano, mas um plano pode ter vários sócios.            |
| Sócio           | Pagamento       | 1 : N         | Direta (FK em Pagamento)    | Um sócio pode realizar vários pagamentos, mas cada pagamento pertence a um único sócio.     |
| Pagamento       | Plano           | N : 1         | Direta (FK em Pagamento)    | Vários pagamentos podem estar vinculados a um único plano, mas cada pagamento é relacionado a um plano específico. |
| Sócio           | Ingresso        | 1 : N         | Direta (FK em Ingresso)     | Um sócio pode comprar vários ingressos, mas cada ingresso é comprado por um único sócio.    |
| Ingresso        | Setor_Estadio   | N : N         | Tabela Disponibilidade_Ingresso | Um ingresso pode estar disponível em vários setores, e um setor pode ter vários ingressos. |
| Sócio           | Evento_Exclusivo| N : N         | Tabela Participacao_Evento  | Um sócio pode participar de vários eventos exclusivos, e cada evento pode ter a participação de vários sócios. |
| Plano           | Benefício       | N : N         | Tabela Plano_Beneficio      | Um plano pode incluir vários benefícios, e um benefício pode estar disponível em vários planos. |

### Como a Estrutura Suporta o Programa "Camisa 7"


O Modelo Físico foi projetado para permitir o funcionamento completo do programa de sócios torcedores "Camisa 7". Abaixo estão algumas das funcionalidades e como a estrutura do banco de dados as suporta:

- **Cadastro e Gestão de Sócios**: A tabela `Sócio` armazena todas as informações dos membros, incluindo o plano de associação e os pontos acumulados, garantindo que o cadastro seja único, sem duplicações de CPF e e-mail.
  
- **Configuração e Atribuição de Planos e Benefícios**: As tabelas `Plano` e `Benefício` definem os planos de associação e os benefícios correspondentes, enquanto a tabela intermediária `Plano_Beneficio` associa múltiplos benefícios a um plano específico.

- **Controle de Pagamentos**: A tabela `Pagamento` registra cada transação realizada pelos sócios, conectando o pagamento a um sócio específico e ao plano correspondente.

- **Distribuição de Ingressos e Setores do Estádio**: `Ingresso` e `Setor_Estadio` facilitam a venda de ingressos para eventos com informações sobre descontos e setores. A tabela `Disponibilidade_Ingresso` gerencia a quantidade de ingressos disponíveis por setor.

- **Gestão de Eventos Exclusivos para Sócios**: `Evento_Exclusivo` armazena eventos exclusivos para sócios, e a tabela `Participacao_Evento` permite registrar quais sócios participam de quais eventos.

## Conclusão

A estrutura do banco de dados para o programa "Camisa 7" foi cuidadosamente normalizada até a Terceira Forma Normal (3FN), garantindo que todos os dados sejam armazenados de forma eficiente e consistente. O Modelo Físico transforma o projeto conceitual e lógico em uma estrutura prática e implementável, assegurando que o sistema seja capaz de gerenciar as inscrições, pagamentos, benefícios, ingressos e eventos dos sócios de maneira eficiente e escalável.
</details>

<details>

<summary>📘 6. SQL DDL</summary>

# Programa de Sócios "Camisa 7" - Banco de Dados

## Introdução ao DDL

DDL (Data Definition Language) é uma linguagem utilizada no SQL para definir e gerenciar a estrutura de um banco de dados. Por meio de comandos DDL, é possível criar, alterar e excluir tabelas e outros objetos no banco de dados. Os comandos DDL incluem `CREATE`, `ALTER`, `DROP`, entre outros, e são fundamentais para a construção da estrutura física de um banco de dados relacional.

Neste trabalho, o DDL foi utilizado para criar as tabelas que representam as principais entidades do programa de sócios torcedores "Camisa 7" do Botafogo. Cada tabela foi definida com atributos específicos, tipos de dados apropriados e restrições de integridade, como chaves primárias, chaves estrangeiras e restrições de unicidade, para garantir que o banco de dados funcione de maneira consistente e eficiente. O objetivo foi traduzir o modelo lógico em uma estrutura física implementável, organizada de forma que permita o gerenciamento de sócios, planos, pagamentos, ingressos, benefícios e eventos exclusivos para sócios.

Abaixo está o código DDL para a criação do banco de dados do programa "Camisa 7", incluindo todas as tabelas e seus relacionamentos:

```
-- Criação do Banco de Dados 
CREATE DATABASE ProgramaSocioCamisa7; 
USE ProgramaSocioCamisa7;

-- Tabela Plano
CREATE TABLE Plano (
    ID_Plano INT PRIMARY KEY,
    Nome_Plano VARCHAR(50) UNIQUE NOT NULL,
    Valor_mensal DECIMAL(10,2) NOT NULL CHECK (Valor_mensal >= 0),
    Valor_anual DECIMAL(10,2) NOT NULL CHECK (Valor_anual >= 0),
    Descrição TEXT
);

-- Tabela Sócio
CREATE TABLE Sócio (
    ID_Socio INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    CPF CHAR(11) UNIQUE NOT NULL,
    Endereço VARCHAR(255) NOT NULL,
    Telefone VARCHAR(15) NOT NULL,
    Data_adesao DATE NOT NULL,
    Status_socio BOOLEAN DEFAULT TRUE,
    Pontos_socio INT DEFAULT 0,
    ID_Plano INT NOT NULL,
    FOREIGN KEY (ID_Plano) REFERENCES Plano(ID_Plano)
);

-- Tabela Benefício
CREATE TABLE Benefício (
    ID_Beneficio INT PRIMARY KEY,
    Tipo_Beneficio VARCHAR(50) NOT NULL,
    Quantidade_limite INT DEFAULT 1 CHECK (Quantidade_limite >= 0),
    Pontos_necessarios INT DEFAULT 0 CHECK (Pontos_necessarios >= 0),
    Descrição TEXT
);

-- Tabela Pagamento
CREATE TABLE Pagamento (
    ID_Pagamento INT PRIMARY KEY,
    Data_pagamento DATE NOT NULL,
    Valor_pago DECIMAL(10,2) NOT NULL CHECK (Valor_pago >= 0),
    Metodo_pagamento VARCHAR(20) NOT NULL,
    Status_pagamento BOOLEAN DEFAULT TRUE,
    ID_Socio INT NOT NULL,
    ID_Plano INT NOT NULL,
    FOREIGN KEY (ID_Socio) REFERENCES Sócio(ID_Socio),
    FOREIGN KEY (ID_Plano) REFERENCES Plano(ID_Plano)
);

-- Tabela Ingresso
CREATE TABLE Ingresso (
    ID_Ingresso INT PRIMARY KEY,
    Jogo VARCHAR(50) NOT NULL,
    Data_jogo DATE NOT NULL,
    Desconto DECIMAL(5,2) DEFAULT 0 CHECK (Desconto BETWEEN 0 AND 1),
    ID_Socio INT NOT NULL,
    FOREIGN KEY (ID_Socio) REFERENCES Sócio(ID_Socio)
);

-- Tabela Setor_Estadio
CREATE TABLE Setor_Estadio (
    ID_Setor INT PRIMARY KEY,
    Nome_Setor VARCHAR(50) UNIQUE NOT NULL,
    Preço DECIMAL(10,2) NOT NULL CHECK (Preço >= 0)
);

-- Tabela Disponibilidade_Ingresso (Intermediária para Ingresso e Setor_Estadio)
CREATE TABLE Disponibilidade_Ingresso (
    ID_Ingresso INT NOT NULL,
    ID_Setor INT NOT NULL,
    Quantidade_disponivel INT DEFAULT 0 CHECK (Quantidade_disponivel >= 0),
    PRIMARY KEY (ID_Ingresso, ID_Setor),
    FOREIGN KEY (ID_Ingresso) REFERENCES Ingresso(ID_Ingresso),
    FOREIGN KEY (ID_Setor) REFERENCES Setor_Estadio(ID_Setor)
);

-- Tabela Evento_Exclusivo
CREATE TABLE Evento_Exclusivo (
    ID_Evento INT PRIMARY KEY,
    Nome_evento VARCHAR(100) NOT NULL,
    Data_evento DATE NOT NULL,
    Localização VARCHAR(255) NOT NULL,
    Capacidade INT CHECK (Capacidade >= 0)
);

-- Tabela Participacao_Evento (Intermediária para Sócio e Evento_Exclusivo)
CREATE TABLE Participacao_Evento (
    ID_Socio INT NOT NULL,
    ID_Evento INT NOT NULL,
    Data_inscricao DATE NOT NULL,
    PRIMARY KEY (ID_Socio, ID_Evento),
    FOREIGN KEY (ID_Socio) REFERENCES Sócio(ID_Socio),
    FOREIGN KEY (ID_Evento) REFERENCES Evento_Exclusivo(ID_Evento)
);

-- Tabela Plano_Beneficio (Intermediária para Plano e Benefício)
CREATE TABLE Plano_Beneficio (
    ID_Plano INT NOT NULL,
    ID_Beneficio INT NOT NULL,
    PRIMARY KEY (ID_Plano, ID_Beneficio),
    FOREIGN KEY (ID_Plano) REFERENCES Plano(ID_Plano),
    FOREIGN KEY (ID_Beneficio) REFERENCES Benefício(ID_Beneficio)
);
```
</details>

<details>

<summary>📘 7. SQL DML</summary>

# Inserção de Dados - Programa de Sócios "Camisa 7"

## Introdução à DML e Inserção de Dados

A DML (Data Manipulation Language) é a linguagem usada no SQL para manipular os dados dentro de uma estrutura de banco de dados já criada. Com a DML, podemos realizar operações de inserção (`INSERT`), atualização (`UPDATE`), exclusão (`DELETE`) e consulta (`SELECT`) sobre os dados armazenados nas tabelas.

Para o programa de sócios torcedores "Camisa 7", foi feito o uso da DML para realizar a inserção inicial de dados em cada tabela, com o objetivo de popular o banco de dados com informações sobre planos de sócios, membros cadastrados, benefícios, pagamentos, ingressos, setores do estádio, eventos exclusivos e associações de benefícios com planos. Abaixo está o código DML utilizado para a inserção de dados em cada uma das tabelas, garantindo um conjunto de dados inicial para testes e operações do sistema.

```
-- Inserção de dados na tabela Plano
INSERT INTO Plano (ID_Plano, Nome_Plano, Valor_mensal, Valor_anual, Descrição)
VALUES
(1, 'Plano Bronze', 29.99, 299.99, 'Acesso básico aos jogos.'),
(2, 'Plano Prata', 49.99, 499.99, 'Acesso intermediário com descontos em ingressos.'),
(3, 'Plano Ouro', 79.99, 799.99, 'Acesso completo com eventos exclusivos e descontos especiais.');

-- Inserção de dados na tabela Sócio
INSERT INTO Sócio (ID_Socio, Nome, Email, CPF, Endereço, Telefone, Data_adesao, Status_socio, Pontos_socio, ID_Plano)
VALUES
(1, 'Carlos Silva', 'carlos.silva@example.com', '12345678901', 'Rua das Flores, 123', '21987654321', '2023-01-15', TRUE, 100, 1),
(2, 'Ana Pereira', 'ana.pereira@example.com', '23456789012', 'Avenida Brasil, 456', '21912345678', '2022-05-20', TRUE, 200, 2),
(3, 'Pedro Souza', 'pedro.souza@example.com', '34567890123', 'Praça Central, 789', '21987651234', '2021-09-10', FALSE, 50, 3);

-- Inserção de dados na tabela Benefício
INSERT INTO Benefício (ID_Beneficio, Tipo_Beneficio, Quantidade_limite, Pontos_necessarios, Descrição)
VALUES
(1, 'Desconto em Ingresso', 5, 100, 'Desconto de 10% nos ingressos dos jogos.'),
(2, 'Acesso VIP', 2, 200, 'Acesso à área VIP em dois eventos por ano.'),
(3, 'Brinde Exclusivo', 1, 300, 'Receba um brinde exclusivo do clube.');

-- Inserção de dados na tabela Pagamento
INSERT INTO Pagamento (ID_Pagamento, Data_pagamento, Valor_pago, Metodo_pagamento, Status_pagamento, ID_Socio, ID_Plano)
VALUES
(1, '2023-02-15', 29.99, 'Cartão de Crédito', TRUE, 1, 1),
(2, '2023-03-20', 49.99, 'Boleto Bancário', TRUE, 2, 2),
(3, '2023-04-10', 79.99, 'Pix', FALSE, 3, 3);

-- Inserção de dados na tabela Ingresso
INSERT INTO Ingresso (ID_Ingresso, Jogo, Data_jogo, Desconto, ID_Socio)
VALUES
(1, 'Jogo A', '2023-05-01', 0.1, 1),
(2, 'Jogo B', '2023-05-15', 0.2, 2),
(3, 'Jogo C', '2023-06-01', 0.15, 3);

-- Inserção de dados na tabela Setor_Estadio
INSERT INTO Setor_Estadio (ID_Setor, Nome_Setor, Preço)
VALUES
(1, 'Arquibancada', 50.00),
(2, 'Cadeira Inferior', 100.00),
(3, 'Cadeira Superior', 80.00);

-- Inserção de dados na tabela Disponibilidade_Ingresso
INSERT INTO Disponibilidade_Ingresso (ID_Ingresso, ID_Setor, Quantidade_disponivel)
VALUES
(1, 1, 100),
(2, 2, 150),
(3, 3, 120);

-- Inserção de dados na tabela Evento_Exclusivo
INSERT INTO Evento_Exclusivo (ID_Evento, Nome_evento, Data_evento, Localização, Capacidade)
VALUES
(1, 'Evento Especial A', '2023-07-10', 'Estádio Central', 500),
(2, 'Evento Especial B', '2023-08-20', 'Arena Norte', 300),
(3, 'Evento Especial C', '2023-09-15', 'Estádio Sul', 400);

-- Inserção de dados na tabela Participacao_Evento
INSERT INTO Participacao_Evento (ID_Socio, ID_Evento, Data_inscricao)
VALUES
(1, 1, '2023-06-01'),
(2, 2, '2023-07-15'),
(3, 3, '2023-08-10');

-- Inserção de dados na tabela Plano_Beneficio (sem duplicação)
INSERT INTO Plano_Beneficio (ID_Plano, ID_Beneficio)
VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(3, 1),
(3, 2),
(3, 3);
```
</details>

<details>

<summary>📘 8. Consultas SQL, Relatórios e Views</summary>

## Consultas SQL, Relatórios e Views

A segunda etapa do trabalho envolve a criação de consultas SQL, relatórios e views que permitirão uma análise detalhada dos dados do programa de sócios "Camisa 7". Abaixo está uma descrição e o código SQL das principais consultas e views para extrair dados, gerar relatórios e acessar informações específicas de maneira organizada e eficiente.

### 1. Consultas SQL

As consultas SQL foram desenvolvidas para responder a diversas necessidades do sistema, como listar sócios ativos, calcular a pontuação acumulada, verificar pagamentos pendentes e identificar benefícios disponíveis para cada sócio.