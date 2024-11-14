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