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
