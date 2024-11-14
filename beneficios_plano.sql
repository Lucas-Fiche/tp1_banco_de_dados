SELECT 
    pl.Nome_Plano,
    b.Tipo_Beneficio,
    b.Quantidade_limite,
    b.Pontos_necessarios,
    b.Descrição
FROM 
    Plano_Beneficio pb
JOIN 
    Plano pl ON pb.ID_Plano = pl.ID_Plano
JOIN 
    Benefício b ON pb.ID_Beneficio = b.ID_Beneficio
ORDER BY 
    pl.Nome_Plano, b.Tipo_Beneficio;
