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