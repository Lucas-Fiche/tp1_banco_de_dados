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
