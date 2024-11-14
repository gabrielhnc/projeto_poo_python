USE gestaofuncionarios;

-- TIPO
INSERT INTO cargo (descricao, informacao_adicional) VALUES
('Gerente', 'Gerenciar setores e supervisionar operações críticas'),
('Desenvolvedor', 'Especialista em desenvolvimento de software, Python e JavaScript'),
('Estagiário', 'Auxiliar nas tarefas e adquirir experiência prática'),
('Analista', 'Analista de dados e suporte em Business Intelligence'),
('Coordenador', 'Coordenação de atividades e suporte aos gerentes'),
('Arquiteto de Software', 'Desenvolvimento de arquitetura para sistemas complexos'),
('Engenheiro de Dados', 'Processamento e estruturação de dados para análise'),
('Administrador de Sistemas', 'Manutenção e configuração de infraestrutura de TI');

-- FUNCIONARIO
INSERT INTO funcionario (nome, cpf, salario, cargo_idcargo) VALUES
('Carlos Silva', '12345678901', 5000.00, 1),
('Ana Oliveira', '23456789012', 7000.00, 7), 
('Pedro Santos', '34567890123', 1500.00, 3),
('Maria Costa', '45678901234', 3500.00, 4),
('João Souza', '56789012345', 6000.00, 1),
('Fernanda Lima', '67890123456', 2500.00, 3),
('Lucas Martins', '78901234567', 4500.00, 2),
('Patrícia Almeida', '89012345678', 3800.00, 4),
('Ricardo Pereira', '90123456789', 4700.00, 5),
('Juliana Rocha', '01234567890', 5200.00, 2),
('Marcelo Duarte', '11112222333', 6200.00, 6),
('Beatriz Fernandes', '44455566577', 3800.00, 5),
('Hugo Vasconcelos', '22233445566', 8000.00, 1),
('Isabela Sampaio', '55536677788', 3000.00, 7),
('Thiago Almeida', '64677788899', 4100.00, 8);

-- PROJETO
INSERT INTO projetos (nome, descricao) VALUES
('Sistema de Gestão Empresarial', 'Gestão de áreas empresariais e recursos humanos.'),
('Análise de Big Data', 'Análise de grandes volumes de dados para insights estratégicos.'),
('Chatbot para Suporte ao Cliente', 'Automação do atendimento com IA e NLP.'),
('Upgrade de Infraestrutura de TI', 'Melhoria de infraestrutura de TI e segurança de dados.'),
('Aplicativo de Gestão Financeira Pessoal', 'Controle e planejamento financeiro para usuários.'),
('Plataforma de E-commerce', 'Sistema robusto para vendas online e gerenciamento de inventário.'),
('Automação de Processos', 'Implementação de automação para otimização de tarefas manuais.'),
('Sistema de CRM', 'Gerenciamento de relacionamento com clientes e histórico de interações.');

-- ALOCACOES
INSERT INTO alocacoes (horas_trabalhadas, papel_funcionario, projetos_idprojetos, funcionario_idfuncionario) VALUES
(40, 'Líder de Projeto', 1, 1),
(35, 'Desenvolvedor Backend', 1, 2),
(20, 'Estagiário', 1, 3),
(25, 'Analista de Dados', 2, 4),
(40, 'Gerente de TI', 3, 5),
(30, 'Estagiário em Suporte', 3, 6),
(35, 'Desenvolvedor Frontend', 4, 7),
(45, 'Analista de Sistemas', 4, 8),
(25, 'Coordenador de Equipe', 5, 9),
(30, 'Desenvolvedor Fullstack', 5, 10),
(50, 'Arquiteto de Software', 6, 11),
(40, 'Analista de CRM', 7, 12),
(60, 'Engenheiro de Dados', 2, 13),
(45, 'Desenvolvedor Mobile', 5, 14),
(20, 'Administrador de Sistemas', 3, 15);

SELECT * FROM vw_dados_completos;
