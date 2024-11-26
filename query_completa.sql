-- Criação do Banco de Dados (DDL)
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



-- Inserção dos Dados (DDL)

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


-- Views

-- Relatório de Pagamentos
CREATE VIEW Relatorio_Pagamentos AS
SELECT 
    s.Nome AS Nome_Socio,
    p.ID_Pagamento,
    p.Data_pagamento,
    p.Valor_pago,
    p.Metodo_pagamento,
    p.Status_pagamento
FROM 
    Pagamento p
JOIN 
    Sócio s ON p.ID_Socio = s.ID_Socio;

-- Relatório de Sócios por Plano
CREATE VIEW Relatorio_Socios_Planos AS
SELECT 
    s.ID_Socio,
    s.Nome,
    s.Email,
    s.Telefone,
    s.Data_adesao,
    s.Pontos_socio,
    p.Nome_Plano
FROM 
    Sócio s
JOIN 
    Plano p ON s.ID_Plano = p.ID_Plano;


-- Consultas

-- Benefícios Disponíveis
SELECT 
    s.Nome AS Nome_Socio,
    b.Tipo_Beneficio,
    b.Pontos_necessarios,
    s.Pontos_socio
FROM 
    Sócio s
JOIN 
    Plano_Beneficio pb ON s.ID_Plano = pb.ID_Plano
JOIN 
    Benefício b ON pb.ID_Beneficio = b.ID_Beneficio
WHERE 
    s.Pontos_socio >= b.Pontos_necessarios
ORDER BY 
    s.Nome;

-- Benefícios dos Planos
SELECT 
    s.Nome AS Nome_Socio,
    b.Tipo_Beneficio,
    b.Pontos_necessarios,
    s.Pontos_socio
FROM 
    Sócio s
JOIN 
    Plano_Beneficio pb ON s.ID_Plano = pb.ID_Plano
JOIN 
    Benefício b ON pb.ID_Beneficio = b.ID_Beneficio
WHERE 
    s.Pontos_socio >= b.Pontos_necessarios
ORDER BY 
    s.Nome;
    
-- Eventos Sócios
SELECT 
    ee.Nome_evento,
    ee.Data_evento,
    s.Nome AS Nome_Socio,
    pe.Data_inscricao
FROM 
    Evento_Exclusivo ee
JOIN 
    Participacao_Evento pe ON ee.ID_Evento = pe.ID_Evento
JOIN 
    Sócio s ON pe.ID_Socio = s.ID_Socio
ORDER BY 
    ee.Data_evento, s.Nome;

-- Ingressos Sócios
SELECT 
    s.Nome AS Nome_Socio,
    i.Jogo,
    i.Data_jogo,
    i.Desconto
FROM 
    Ingresso i
JOIN 
    Sócio s ON i.ID_Socio = s.ID_Socio
ORDER BY 
    s.Nome, i.Data_jogo;

-- Pagamentos Sócios
SELECT 
    s.Nome AS Nome_Socio,
    p.ID_Pagamento,
    p.Data_pagamento,
    p.Valor_pago,
    p.Metodo_pagamento,
    p.Status_pagamento
FROM 
    Pagamento p
JOIN 
    Sócio s ON p.ID_Socio = s.ID_Socio
ORDER BY 
    s.Nome, p.Data_pagamento;

-- Pontos Sócios
SELECT 
    Nome,
    Pontos_socio
FROM 
    Sócio
ORDER BY 
    Pontos_socio DESC;

-- Sócios Ativos
SELECT 
    s.ID_Socio,
    s.Nome,
    s.Email,
    s.Telefone,
    s.Data_adesao,
    s.Pontos_socio,
    p.Nome_Plano
FROM 
    Sócio s
JOIN 
    Plano p ON s.ID_Plano = p.ID_Plano
WHERE 
    s.Status_socio = TRUE;

-- Valor do Sócio
SELECT 
    s.Nome AS Nome_Socio,
    SUM(p.Valor_pago) AS Total_Pago
FROM 
    Pagamento p
JOIN 
    Sócio s ON p.ID_Socio = s.ID_Socio
GROUP BY 
    s.Nome
ORDER BY 
    Total_Pago DESC;


