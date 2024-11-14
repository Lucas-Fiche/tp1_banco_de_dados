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
