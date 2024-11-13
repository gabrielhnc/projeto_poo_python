use gestaofuncionarios;

-- TIPO
INSERT INTO tipo (descricao, informacao_adicional) VALUES
('Gerente', 'Gerenciar setores'),
('Desenvolvedor', 'Dev Python'),
('Estagiário', 'Auxiliar nas tarefas'),
('Analista', 'Analisar dados'),
('Coordenador', 'Coordenar atividades de projetos');


-- FUNCIONARIO
INSERT INTO funcionario (nome, cpf, salario, tipo_idtipo) VALUES
('Carlos Silva', '12345678901', 5000.00, 1), 
('Ana Oliveira', '23456789012', 4000.00, 2), 
('Pedro Santos', '34567890123', 1500.00, 3),
('Maria Costa', '45678901234', 3500.00, 4), 
('João Souza', '56789012345', 6000.00, 1),
('Fernanda Lima', '67890123456', 2500.00, 3),
('Lucas Martins', '78901234567', 4500.00, 2),
('Patrícia Almeida', '89012345678', 3800.00, 4), 
('Ricardo Pereira', '90123456789', 4700.00, 5), 
('Juliana Rocha', '01234567890', 3200.00, 2); 


-- PROJETO
INSERT INTO projetos (nome, descricao) VALUES
('Sistema de Gestão Empresarial', 'Gestão de áreas empresariais.'),
('Análise de Big Data', 'Análise de grandes dados.'),
('Chatbot para Suporte ao Cliente', 'Automação do atendimento.'),
('Upgrade de Infraestrutura de TI', 'Melhoria de TI e servidores.'),
('Aplicativo de Gestão Financeira Pessoal', 'Controle de finanças pessoais.');


-- ALOCACOES
INSERT INTO alocacoes (horas_trabalhadas, papel_funcionario, projetos_idprojetos, funcionario_idfuncionario) VALUES
(40, 'Líder de Projeto', 1, 1), 
(35, 'Desenvolvedor', 1, 2), 
(20, 'Estagiário', 1, 3),
(25, 'Analista de Dados', 2, 4),
(40, 'Gerente de TI', 3, 5), 
(30, 'Estagiário', 3, 6), 
(35, 'Desenvolvedor Backend', 4, 7),
(45, 'Analista de Sistemas', 4, 8), 
(25, 'Coordenador de Equipe', 5, 9), 
(30, 'Desenvolvedor Frontend', 5, 10);

 SELECT * FROM vw_dados_completos