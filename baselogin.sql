/*
SQLyog Enterprise v13.1.1 (64 bit)
MySQL - 10.4.20-MariaDB : Database - baselogin
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`baselogin` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `baselogin`;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `imagen` blob NOT NULL,
  `celular` varchar(12) NOT NULL,
  `direccion` varchar(30) NOT NULL,
  `descripcion` varchar(50) NOT NULL,
  `estado` bigint(20) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4;

/*Data for the table `users` */

insert  into `users`(`id`,`name`,`email`,`password`,`imagen`,`celular`,`direccion`,`descripcion`,`estado`) values 
(19,'adrian','prueba16@yopmail.com','$2b$12$vJslUVOg1Otv0','WhatsApp Image 2022-03-22 at 9.34.31 AM(1).jpeg','3143425736','luis carlos galan','mega tienda',0),
(37,'adrian angulo','angulo@yopmail.com','$2b$12$iQqTHa2FrnQyE','WhatsApp Image 2022-03-22 at 9.13.03 AM(2).jpeg','3143425736','calle 16','empanadas',0),
(38,'andres','andres@yopmail.com','$2b$12$bQC1.1r2R9b2V','WhatsApp Image 2022-03-22 at 9.34.31 AM(1).jpeg','1531','OBREOR','HDBVJB',0),
(39,'andres','andres@yopmail.com','$2b$12$LX7T/sihvQ4eX','WhatsApp Image 2022-03-22 at 9.34.31 AM(1).jpeg','1531','OBREOR','HDBVJB',0),
(40,'adri','adri@yopmail.com','adri','WhatsApp Image 2022-03-22 at 9.29.49 AM.jpeg','123456','nose','nose',0),
(41,'jj','jj@yopmail.com','$2b$12$7/clCHR1EFpwN','WhatsApp Image 2022-03-22 at 9.34.31 AM.jpeg','14785','arriba','arriba',0);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
