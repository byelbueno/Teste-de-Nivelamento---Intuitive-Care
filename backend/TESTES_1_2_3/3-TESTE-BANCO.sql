-- COPY DEMONSTRAÇÕES UTILIZANDO POSTGRES
COPY demonstracoes_contabeis
(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/caminho para o arquivo/demonstrações.csv'
DELIMITER ';'
CSV HEADER;



-- COPY OPERADORAS UTILIZANDO POSTGRES
 COPY operadoras_ans(
    registro_ans,
    cnpj,
    razao_social,
    nome_fantasia,
    modalidade,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    uf,
    cep,
    ddd,
    telefone,
    fax,
    endereco_eletronico,
    representante,
    cargo_representante,
    regiao_de_comercializacao,
    data_registro_ans
)
FROM '/caminho para o arquivo/Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER;




-- SELECT COM AS 10 OPERADORES COM MAIORES DESPESAS DO ULTIMO ANO
SELECT 
    o.razao_social AS operadora,
    SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS total_despesas
FROM 
    demonstracoes_contabeis dc
JOIN 
    operadoras_ans o ON dc.reg_ans = o.registro_ans
WHERE 
    dc.descricao ILIKE '%EVENTOS/SINISTROS%'
    AND dc.data BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY 
    o.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;




-- SELECT COM AS 10 OPERADORES COM MAIORES DESPESAS DO ULTIMO  TRIMESTRE DE DADOS (OUTUBRO, NOVEMBRO E DEZEMBRO DE 2024 )
SELECT 
    o.razao_social AS operadora,
    SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS total_despesas
FROM 
    demonstracoes_contabeis dc
JOIN 
    operadoras_ans o ON dc.reg_ans = o.registro_ans
WHERE 
    dc.descricao ILIKE '%EVENTOS/SINISTROS%'
    AND dc.data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY 
    o.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;

