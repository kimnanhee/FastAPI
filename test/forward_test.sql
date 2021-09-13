-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `test` DEFAULT CHARACTER SET utf8 ;
USE `test` ;

-- -----------------------------------------------------
-- Table `test`.``
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`` (
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test`.`user_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`user_info` (
  `user_no` INT NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(50) NOT NULL,
  `user_pw` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`user_no`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE);


-- -----------------------------------------------------
-- Table `test`.`book_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`book_info` (
  `book_no` INT NOT NULL AUTO_INCREMENT,
  `book_name` VARCHAR(100) NOT NULL,
  `book_price` INT NOT NULL,
  `book_date` DATE NULL,
  `book_writter` VARCHAR(50) NULL,
  PRIMARY KEY (`book_no`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test`.`grade_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`grade_info` (
  `grade_no` INT NOT NULL,
  `user_no` INT NOT NULL DEFAULT 사용자 아이디,
  `book_no` INT NOT NULL,
  `last_book_no` INT NULL,
  `grade_sec` INT NULL,
  `grade` DECIMAL(3,1) NOT NULL,
  PRIMARY KEY (`grade_no`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
