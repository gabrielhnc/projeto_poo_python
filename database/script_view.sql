CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `vw_dados_completos` AS
    SELECT 
        `f`.`idfuncionario` AS `idFuncionario`,
        `f`.`nome` AS `nomeFuncionario`,
        `f`.`cpf` AS `cpf_funcionario`,
        `f`.`salario` AS `salario_Funcionario`,
        `t`.`descricao` AS `tipoFuncionario`,
        `p`.`nome` AS `nomeProjeto`,
        `a`.`horas_trabalhadas` AS `horasTrabalhadas`,
        `a`.`papel_funcionario` AS `papelNoProjeto`
    FROM
        (((`funcionario` `f`
        JOIN `tipo` `t` ON ((`f`.`tipo_idtipo` = `t`.`idtipo`)))
        JOIN `alocacoes` `a` ON ((`f`.`idfuncionario` = `a`.`funcionario_idfuncionario`)))
        JOIN `projetos` `p` ON ((`a`.`projetos_idprojetos` = `p`.`idprojetos`)))