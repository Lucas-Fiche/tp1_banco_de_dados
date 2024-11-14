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
