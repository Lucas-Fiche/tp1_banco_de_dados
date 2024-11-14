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
