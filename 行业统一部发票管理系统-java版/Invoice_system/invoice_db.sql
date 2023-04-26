/*
SQLyog v10.2 
MySQL - 5.7.20 : Database - invoice_db
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`invoice_db` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `invoice_db`;

/*Table structure for table `invoice_invoice` */

DROP TABLE IF EXISTS `invoice_invoice`;

CREATE TABLE `invoice_invoice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `invoicetype_id` int(11) DEFAULT NULL,
  `invoice_amount` int(11) DEFAULT NULL,
  `invoice_code` varchar(30) DEFAULT NULL,
  `invoice_explain` varchar(1000) DEFAULT NULL,
  `creat_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `invoice_invoice` */

insert  into `invoice_invoice`(`id`,`user_id`,`company_id`,`department_id`,`product_id`,`invoicetype_id`,`invoice_amount`,`invoice_code`,`invoice_explain`,`creat_time`) values (1,1,3,2,1,2,700,'jt123456','每天的交通费啊','2023-01-16 11:00:20'),(2,1,3,2,1,1,600,'cy123456','每天的餐饮费','2023-01-16 11:06:30'),(3,2,1,1,1,2,600,'jt123457','每天的交通费','2023-01-20 11:06:30'),(4,2,1,1,1,3,600,'zs123458','每天的住宿费','2023-01-20 11:06:30'),(5,3,2,3,1,4,1000,'sl123459','给客户送礼','2023-01-20 11:06:30'),(6,3,2,3,1,5,8000,'sl123459','差旅费','2023-01-20 11:06:30'),(7,3,2,3,1,5,8000,'sl123459','差旅费','2023-01-20 15:51:01'),(8,1,3,2,1,2,500,'jt123456','每天的交通费','2023-03-24 12:15:04'),(9,1,3,2,1,2,500,'jt123456','每天的交通费','2023-03-25 15:18:18'),(10,1,3,2,1,2,800,'jt123457','每天每日的交通费','2023-04-25 10:49:34'),(11,1,3,2,1,2,800,'jt123458','每天每日每时交通费','2023-04-25 11:49:34'),(12,1,3,2,1,2,800,'jt123459','每天每日每时交通费','2023-04-25 12:40:34'),(13,1,3,2,1,2,800,'jt123460','每天每日每时每刻的交通费','2023-04-25 12:49:34');

/*Table structure for table `system_company` */

DROP TABLE IF EXISTS `system_company`;

CREATE TABLE `system_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) DEFAULT NULL,
  `company_abbreviation` varchar(30) DEFAULT NULL,
  `company_explain` varchar(1000) DEFAULT NULL,
  `creat_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

/*Data for the table `system_company` */

insert  into `system_company`(`id`,`company_name`,`company_abbreviation`,`company_explain`,`creat_time`) values (1,'百度','你好百度','小度','2023-01-17 16:01:38'),(2,'阿里巴巴','阿里','马老板的阿里帝国','2023-01-17 16:01:38'),(3,'腾讯','tx',NULL,'2023-01-17 16:01:38'),(4,'京东','jd','强子的世界','2023-01-17 18:04:39'),(5,'腾八',NULL,NULL,NULL),(6,'腾九',NULL,'dff放寒假的首付款交hi爱好还记得和接口代理费三然后IU然后以傲娇的撒课后辅导萨克解放军的是否会的叫法hfkjdsfhaufhodasjfhkjdsahiurytiurhgiurewyt9843943tyriuhgireu',NULL),(7,'飞奔','你好飞奔','飞奔集团，飞奔帝国',NULL);

/*Table structure for table `system_company_department` */

DROP TABLE IF EXISTS `system_company_department`;

CREATE TABLE `system_company_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

/*Data for the table `system_company_department` */

insert  into `system_company_department`(`id`,`company_id`,`department_id`) values (1,1,1),(2,1,2),(3,1,3),(4,2,4),(5,2,5),(6,2,6),(7,3,7),(8,3,8),(9,3,9),(10,4,1),(11,4,1),(12,4,10),(13,3,11),(14,1,7),(15,1,12),(16,1,13),(17,1,14);

/*Table structure for table `system_department` */

DROP TABLE IF EXISTS `system_department`;

CREATE TABLE `system_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(30) DEFAULT NULL,
  `department_explain` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `system_department` */

insert  into `system_department`(`id`,`department_name`,`department_explain`) values (1,'开发部','百度的开发部'),(2,'测开部','百度的测开部'),(3,'财务部','百度的财务部'),(4,'开发部','阿里的开发部'),(5,'测开部','阿里的测开部'),(6,'财务部','阿里的财务部'),(7,'开发部','腾讯的开发部'),(8,'测开部','腾讯的测开部'),(9,'财务部','腾讯的财务部'),(10,'人事部','京东的人事部'),(11,'人力资源部','玩你没商量'),(12,'劳保部','负责劳保用品'),(13,'保安部','负责劳保用品'),(14,'劳保部2','负责劳保用品');

/*Table structure for table `system_invoicetype` */

DROP TABLE IF EXISTS `system_invoicetype`;

CREATE TABLE `system_invoicetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `invoicetype_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

/*Data for the table `system_invoicetype` */

insert  into `system_invoicetype`(`id`,`invoicetype_name`) values (1,'餐饮'),(2,'交通'),(3,'住宿'),(4,'送礼'),(5,'差旅'),(6,'按摩'),(7,'搓澡');

/*Table structure for table `system_product` */

DROP TABLE IF EXISTS `system_product`;

CREATE TABLE `system_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `product_abbreviation` varchar(30) DEFAULT NULL,
  `product_explain` varchar(1000) DEFAULT NULL,
  `creat_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `system_product` */

insert  into `system_product`(`id`,`product_name`,`product_abbreviation`,`product_explain`,`creat_time`) values (1,'发票管理系统','FPS','本公司自用系统','2023-01-19 10:17:19'),(2,'人力管理系统','RLS','本公司自用系统','2023-01-19 10:32:12'),(3,'设备管理系统','SBS','本公司自用系统','2023-01-19 10:58:48'),(4,'罪犯管理系统','XF_system','管理罪犯之用','2023-04-30 10:58:48');

/*Table structure for table `system_user` */

DROP TABLE IF EXISTS `system_user`;

CREATE TABLE `system_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_login_name` varchar(30) DEFAULT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `system_user` */

insert  into `system_user`(`id`,`user_login_name`,`user_name`,`password`,`company_id`,`department_id`) values (1,'guolin','郭霖','e10adc3949ba59abbe56e057f20f883e',3,2),(2,'wangruihao','王睿昊','e10adc3949ba59abbe56e057f20f883e',1,1),(3,'qihongzhi','齐宏志','e10adc3949ba59abbe56e057f20f883e',2,3),(4,'zhaojinghu1','赵静湖','e10adc3949ba59abbe56e057f20f883e',3,1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
