
# 새로운 데이터 베이스 생성
CREATE DATABASE IF NOT EXISTS `pythondb`;

USE `pythondb`;

CREATE TABLE IF NOT EXISTS `tbl_crawlingdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `contents` text DEFAULT NULL,
  `keyword` varchar(50) DEFAULT NULL,
  `regdate` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `tbl_keyword` (
  `keyword` varchar(50) NOT NULL,
  PRIMARY KEY (`keyword`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
