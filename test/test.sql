show databases;
CREATE DATABASE test;
use test;

show tables;

DROP TABLE users;
DROP TABLE books;
DROP TABLE grades;
DROP TABLE user_info;

CREATE TABLE IF NOT EXISTS `test`.`user_info` (
  `user_no` INT NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(50) NOT NULL,
  `user_pw` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`user_no`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE);

CREATE TABLE IF NOT EXISTS `test`.`book_info` (
  `book_no` INT NOT NULL AUTO_INCREMENT,
  `book_name` VARCHAR(100) NOT NULL,
  `book_price` INT NOT NULL,
  `book_date` DATE NULL,
  `book_writter` VARCHAR(50) NULL,
  PRIMARY KEY (`book_no`));

CREATE TABLE grades(
	grade_no int(10) PRIMARY KEY,
	user_no int(10) not null, -- 사용자 id
    bood_no int(10) not null, -- 책 id
    last_book_bo int(10) not null, 
    grade_sec int(10) not null, -- 평가에 걸린 시간
	grade DECIMAL(3, 1) not null -- 평점	
);
SELECT VERSION();

insert into users values(1, "nanhee", "nanhee0225");

insert into books (book_no, book_name, book_price) values(1, "twile", 15000);
insert into books (book_no, book_name, book_price) values(2, "love", 21000);

insert into grades values(1, 2, 5, -1, 4.5);

desc users;
select * from user_info;
select * from books;
select * from grades;