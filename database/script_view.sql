CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `gestaofuncionarios`.`vw_dados_completos` AS
    SELECT 
        `f`.`idfuncionario` AS `idFuncionario`,
        `f`.`nome` AS `nomeFuncionario`,
        `f`.`cpf` AS `CPF`,
        `f`.`salario` AS `salarioFuncionario`,
        `c`.`descricao` AS `tipoFuncionario`,
        `p`.`nome` AS `nomeProjeto`,
        `a`.`horas_trabalhadas` AS `CargaHoraria`,
        `a`.`papel_funcionario` AS `Funcao`
    FROM
        (((`gestaofuncionarios`.`funcionario` `f`
        JOIN `gestaofuncionarios`.`cargo` `c` ON ((`f`.`cargo_idcargo` = `c`.`idcargo`)))
        JOIN `gestaofuncionarios`.`alocacoes` `a` ON ((`f`.`idfuncionario` = `a`.`funcionario_idfuncionario`)))
        JOIN `gestaofuncionarios`.`projetos` `p` ON ((`a`.`projetos_idprojetos` = `p`.`idprojetos`)))
