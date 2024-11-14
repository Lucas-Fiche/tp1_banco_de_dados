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
