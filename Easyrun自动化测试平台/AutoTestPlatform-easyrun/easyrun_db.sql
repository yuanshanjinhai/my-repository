/*
SQLyog v10.2 
MySQL - 5.7.20 : Database - easyrun_db
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`easyrun_db` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `easyrun_db`;

/*Table structure for table `system_product` */

DROP TABLE IF EXISTS `system_product`;

CREATE TABLE `system_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) DEFAULT NULL,
  `product_abbreviation` varchar(30) DEFAULT NULL,
  `product_explain` varchar(1000) DEFAULT NULL,
  `creat_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `system_product` */

insert  into `system_product`(`id`,`product_name`,`product_abbreviation`,`product_explain`,`creat_time`) values (1,'舆情监控系统','舆情','只用于用例验证，无法执行','2023-01-11 21:22:46'),(2,'接口测试教学系统','教学','可发送请求','2023-01-11 21:30:21');

/*Table structure for table `system_resource` */

DROP TABLE IF EXISTS `system_resource`;

CREATE TABLE `system_resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resource_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

/*Data for the table `system_resource` */

insert  into `system_resource`(`id`,`resource_name`) values (1,'home'),(2,'interface-singlerun'),(3,'interface-interface'),(4,'interface-case_group'),(5,'interface-global'),(6,'interface-encypt_decypt'),(7,'interface-case'),(8,'interface-run'),(9,'interface-result'),(10,'interface-singlerun'),(11,'tools-creat_boundart'),(12,'tools-str_len'),(13,'help-case_rule'),(14,'admin-product'),(15,'admin-user'),(16,'admin-role');

/*Table structure for table `system_role` */

DROP TABLE IF EXISTS `system_role`;

CREATE TABLE `system_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `system_role` */

/*Table structure for table `system_role_resource` */

DROP TABLE IF EXISTS `system_role_resource`;

CREATE TABLE `system_role_resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) DEFAULT NULL,
  `resource_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `system_role_resource` */

/*Table structure for table `system_user` */

DROP TABLE IF EXISTS `system_user`;

CREATE TABLE `system_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_login_name` varchar(30) DEFAULT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `system_user` */

/*Table structure for table `system_user_role` */

DROP TABLE IF EXISTS `system_user_role`;

CREATE TABLE `system_user_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `system_user_role` */

/*Table structure for table `test_case` */

DROP TABLE IF EXISTS `test_case`;

CREATE TABLE `test_case` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `case_group_id` int(11) DEFAULT NULL,
  `interface_id` int(11) DEFAULT NULL,
  `interface_address` text,
  `is_relationed` int(11) DEFAULT NULL,
  `case_name` varchar(100) DEFAULT NULL,
  `case_order` int(11) DEFAULT NULL,
  `is_urlencode_pwd` int(11) DEFAULT NULL,
  `encrypt_decrypt_file` varchar(50) DEFAULT NULL,
  `case_explain` varchar(500) DEFAULT NULL,
  `header` text,
  `body` text,
  `expect_response` text,
  `creat_time` varchar(20) DEFAULT NULL,
  `update_time` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

/*Data for the table `test_case` */

insert  into `test_case`(`id`,`product_id`,`case_group_id`,`interface_id`,`interface_address`,`is_relationed`,`case_name`,`case_order`,`is_urlencode_pwd`,`encrypt_decrypt_file`,`case_explain`,`header`,`body`,`expect_response`,`creat_time`,`update_time`) values (1,2,1,1,'http://101.42.247.45:8080/register/',0,'正确注册',1,0,'','首次注册','','{\"username\":\"【+guolin||G1】\",\"password\":\"guolin123456\",\"email\":\"guolin@126.com\"}','{\"code\":\"00\",\"userid\":\"【d】\"}','2023-01-12 22:31:14',NULL),(2,2,1,1,'http://101.42.247.45:8080/register/',0,'重复注册',2,0,'','重复注册','','{\"username\":\"【+guolin||G1】\",\"password\":\"guolin123456\",\"email\":\"guolin@126.com\"}','{\"code\":\"01\",\"username\":\"【guolin||G1】\"}','2023-01-12 22:31:14',NULL),(3,2,1,1,'http://101.42.247.45:8080/login/',1,'登录',3,0,'','使用注册的用户名登录','','{\"username\":\"【+guolin||G1】\",\"password\":\"3661d7d0d787828f2caa6fa021fccf1c\",\"email\":\"guolin@126.com\"}','{\"code\":\"00\",\"userid\":\"【d】\",\"token\":\"【ad32】\",\"login_time\":\"【时间3】\"}','2023-01-12 22:31:14',NULL),(4,2,1,NULL,NULL,0,'$get_token',4,NULL,NULL,NULL,NULL,NULL,'[\"token\"]','2023-01-12 22:31:14',NULL),(5,2,1,NULL,NULL,0,'$get_userid',5,NULL,NULL,NULL,NULL,NULL,'[\"userid\"]','2023-01-12 22:31:14',NULL),(6,2,2,1,'http://101.42.247.45:8080/create/',0,'创建博文',1,0,'','创建一条博文','','{\"userid\":\"【$get_userid】\",\"token\":\"【$get_token】\",\"title\":\"【+我的标题||G1】\",\"content\":\"【+我的内容||G1】\"}','{\"code\":\"00\",\"data\":[{\"content\":\"【+我的内容||G1】\",\"title\":\"【+我的标题||G1】\"}],\"userid\":\"【$get_userid】\"}','2023-01-12 22:31:14',NULL),(7,2,2,1,'http://101.42.247.45:8080/getBlogsOfUser/',0,'查询用户博文',2,0,'','查询某用户创建的所有博文','','{\"userid\":\"【$get_userid】\",\"token\":\"【$get_token】\"}','{\"code\":\"00\",\"data\":[{\"articleId\":8705,\"content\":\"我的内容2\",\"owner\":\"【$get_userid】\",\"posted_on\":\"2021-06-22 14:01:51\",\"title\":\"我的标题2\",\"update_time\":\"null\"},{\"articleId\":8704,\"content\":\"我的内容1\",\"owner\":\"【$get_userid】\",\"posted_on\":\"2021-06-22 14:01:37\",\"title\":\"我的标题1\",\"update_time\":\"null\"}],\"userid\":\"【$get_userid】\"}','2023-01-12 22:31:14',NULL);

/*Table structure for table `test_case_group` */

DROP TABLE IF EXISTS `test_case_group`;

CREATE TABLE `test_case_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `is_run` varchar(1) DEFAULT NULL,
  `case_group_name` varchar(100) DEFAULT NULL,
  `case_group_order` int(11) DEFAULT NULL,
  `case_group_type` enum('起始组','并发组','结束组') DEFAULT NULL,
  `case_group_explain` varchar(800) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `test_case_group` */

insert  into `test_case_group`(`id`,`product_id`,`is_run`,`case_group_name`,`case_group_order`,`case_group_type`,`case_group_explain`) values (1,2,'Y','注册、登录与获取token',0,'起始组','注册、登录与获取token一气呵成'),(2,2,'Y','创建与查询博文',1,'并发组','创建与查询博文一气呵成');

/*Table structure for table `test_encrypt_decrypt` */

DROP TABLE IF EXISTS `test_encrypt_decrypt`;

CREATE TABLE `test_encrypt_decrypt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(50) DEFAULT NULL,
  `file_name_explain` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `test_encrypt_decrypt` */

/*Table structure for table `test_global_var` */

DROP TABLE IF EXISTS `test_global_var`;

CREATE TABLE `test_global_var` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `global_var_name` varchar(50) DEFAULT NULL,
  `global_var_value` varchar(300) DEFAULT NULL,
  `is_auto_add` enum('是','否') DEFAULT NULL,
  `global_var_explain` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `test_global_var` */

insert  into `test_global_var`(`id`,`product_id`,`global_var_name`,`global_var_value`,`is_auto_add`,`global_var_explain`) values (1,2,'G1','1','否','1');

/*Table structure for table `test_interface` */

DROP TABLE IF EXISTS `test_interface`;

CREATE TABLE `test_interface` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `interface_name` varchar(50) DEFAULT NULL,
  `interface_order` int(11) DEFAULT NULL,
  `interface_address` varchar(500) DEFAULT NULL,
  `method` enum('POST','GET') DEFAULT NULL,
  `interface_explain` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Data for the table `test_interface` */

insert  into `test_interface`(`id`,`product_id`,`interface_name`,`interface_order`,`interface_address`,`method`,`interface_explain`) values (1,2,'注册',1,'http://101.42.247.45:8080/register/','POST','注册用户'),(2,2,'登录',2,'http://101.42.247.45:8080/login/','POST','login系统'),(3,2,'创建博文',3,'http://101.42.247.45:8080/create/','POST','创建博文接口'),(4,2,'查询用户博文',4,'http://101.42.247.45:8080/getBlogsOfUser/','POST','查询用户博文接口'),(5,2,'注册、登录与获取token',5,'http://39.100.104.214:8080/register/','POST','查询用户博文接口');

/*Table structure for table `test_relation` */

DROP TABLE IF EXISTS `test_relation`;

CREATE TABLE `test_relation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `case_group_id` int(11) DEFAULT NULL,
  `case_id` int(11) DEFAULT NULL,
  `relation_name` varchar(50) DEFAULT NULL,
  `relation_field` varchar(15) DEFAULT NULL,
  `json_path` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `test_relation` */

insert  into `test_relation`(`id`,`product_id`,`case_group_id`,`case_id`,`relation_name`,`relation_field`,`json_path`) values (1,2,1,3,'$get_token','expect_response','[\"token\"]'),(2,2,1,3,'$get_userid','expect_response','[\"userid\"]');

/*Table structure for table `test_run_result` */

DROP TABLE IF EXISTS `test_run_result`;

CREATE TABLE `test_run_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` int(11) DEFAULT NULL,
  `actual_response` text,
  `run_time` datetime DEFAULT NULL,
  `is_pass` enum('是','否') DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Data for the table `test_run_result` */

insert  into `test_run_result`(`id`,`case_id`,`actual_response`,`run_time`,`is_pass`) values (1,1,'{\"code\":\"01\",\"username\":\"guolin1\"}','2023-01-18 22:15:30','否'),(2,2,'{\"code\":\"01\",\"username\":\"guolin1\"}','2023-01-18 22:15:30','是'),(3,3,'{\"code\":\"00\",\"userid\":31420,\"token\":\"428621ed600d3b2ba2d61f5d8be2725c\",\"login_time\":\"2023-01-18 22:15:30\"}','2023-01-18 22:15:30','是'),(4,6,'500','2023-01-18 22:15:30','否'),(5,7,'500','2023-01-18 22:15:30','否');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
