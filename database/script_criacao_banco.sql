-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema gestaoFuncionarios
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema gestaoFuncionarios
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gestaoFuncionarios` DEFAULT CHARACTER SET utf8 ;
USE `gestaoFuncionarios` ;

-- -----------------------------------------------------
-- Table `gestaoFuncionarios`.`tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gestaoFuncionarios`.`tipo` (
  `idtipo` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(100) NULL,
  `informacao_adicional` VARCHAR(100) NULL,
  PRIMARY KEY (`idtipo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gestaoFuncionarios`.`projetos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gestaoFuncionarios`.`projetos` (
  `idprojetos` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `descricao` VARCHAR(200) NULL,
  PRIMARY KEY (`idprojetos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gestaoFuncionarios`.`funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gestaoFuncionarios`.`funcionario` (
  `idfuncionario` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `cpf` VARCHAR(20) NULL,
  `salario` FLOAT NULL,
  `tipo_idtipo` INT NOT NULL,
  PRIMARY KEY (`idfuncionario`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE,
  INDEX `fk_funcionario_tipo1_idx` (`tipo_idtipo` ASC) VISIBLE,
  CONSTRAINT `fk_funcionario_tipo1`
    FOREIGN KEY (`tipo_idtipo`)
    REFERENCES `gestaoFuncionarios`.`tipo` (`idtipo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gestaoFuncionarios`.`alocacoes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gestaoFuncionarios`.`alocacoes` (
  `idalocacoes` INT NOT NULL AUTO_INCREMENT,
  `horas_trabalhadas` INT NULL,
  `papel_funcionario` VARCHAR(100) NULL,
  `projetos_idprojetos` INT NOT NULL,
  `funcionario_idfuncionario` INT NOT NULL,
  PRIMARY KEY (`idalocacoes`),
  INDEX `fk_alocacoes_projetos_idx` (`projetos_idprojetos` ASC) VISIBLE,
  INDEX `fk_alocacoes_funcionario1_idx` (`funcionario_idfuncionario` ASC) VISIBLE,
  CONSTRAINT `fk_alocacoes_projetos`
    FOREIGN KEY (`projetos_idprojetos`)
    REFERENCES `gestaoFuncionarios`.`projetos` (`idprojetos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_alocacoes_funcionario1`
    FOREIGN KEY (`funcionario_idfuncionario`)
    REFERENCES `gestaoFuncionarios`.`funcionario` (`idfuncionario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
