USE testemed;
DELETE FROM paciente WHERE cpf IN ('78160552009', '12345678901');
INSERT INTO paciente (id, cpf, nome, email, estaAtivo, senha, telefone, possuiPlanoSaude, planosSaude, historico, imagemUrl, role)
VALUES 
  (uuid(), '78160552009', 'Emerson Laranja', 'emerson@email.com', true, 'Senh@forte123', '34999335522', true, '[2]', "['sinusite,moderado']", 'https://img.freepik.com/fotos-gratis/designer-trabalhando-no-modelo-3d_23-2149371896.jpg', 'PACIENTE'),
  (uuid(), '12345678901', 'Joana Silva', 'joana@email.com', true, 'MinhaSenha123', '34999887766', true, '[1, 3]', "['rinite,leve', 'asma,médio']", 'https://img.freepik.com/fotos-premium/retrato-de-uma-jovem-brasileira-sorridente-em-um-vestido-mexicano-ai-gerado_632984-139.jpg', 'PACIENTE');
SELECT 
CONCAT('KILL ', id, ';') 
FROM INFORMATION_SCHEMA.PROCESSLIST 
WHERE User = 'root' 
AND Host = 'db'
AND db = 'testemed';