/*
Navicat MySQL Data Transfer

Source Server         : MjData
Source Server Version : 50726
Source Host           : localhost:3306
Source Database       : mjnews

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2019-08-09 18:29:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `n_id` int(11) NOT NULL AUTO_INCREMENT,
  `n_title` varchar(255) DEFAULT NULL,
  `n_content` varchar(255) DEFAULT NULL,
  `n_writer` varchar(255) DEFAULT NULL,
  `n_time` varchar(255) DEFAULT NULL,
  `n_fk_code` int(11) DEFAULT NULL,
  `n_picture` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`n_id`),
  KEY `t_fk_code` (`n_fk_code`),
  CONSTRAINT `t_fk_code` FOREIGN KEY (`n_fk_code`) REFERENCES `newstype` (`t_code`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` VALUES ('57', '任天堂发新款Switch\"Switch Lite\":预计9月20日开卖', '值得一提的是，之前有传言称任天堂正在开发两个不同的新机型，其中一个是目前已经公布的Lite，那么对于传闻中的另外一款，任天堂是否正在开发中呢?', 'capcom', '2019-07-16', '7', '201907221707153.jpg');
INSERT INTO `news` VALUES ('64', '中国人的幸福生活', '即使对方拉萨大家发逻辑上的了发吉萨大了空间家乐福的老师就打发了撒娇', '卡普空', '2019-07-18', '2', '201907181854171.jpg');
INSERT INTO `news` VALUES ('65', '中国经济持续高速发展', '鬼泣5天下第一！！永远的第一！！！但丁的终极魔人觉醒了！！！！！！！！！', '中国财经', '2019-07-18', '1', '201908091806233.png@1280w_1l_2o_100sh');
INSERT INTO `news` VALUES ('66', '巫师3：狂猎', '巫师3是个好游戏，ing给了9.3分，非常值得一玩的游戏！！！', '波兰蠢驴', '2019-07-18', '7', '201908091807096.jpg');
INSERT INTO `news` VALUES ('68', '中国导弹', '军队是保卫国家的有力屏障！！！', '军事网', '2019-07-09', '5', '201907191023101.jpg');
INSERT INTO `news` VALUES ('69', '特朗普会见金正恩', '即使对方拉萨大家发逻辑上的了发吉萨大了空间家乐福的老师就打发了撒娇', '卡普空', '2019-07-18', '2', '201907181854171.jpg');
INSERT INTO `news` VALUES ('71', '狮子王', '狮子王是小时候的美好回忆，让你和小狮子一样勇敢坚强！！！', '迪斯尼', '2019-07-17', '3', '201907191023101.jpg');
INSERT INTO `news` VALUES ('72', '杨广夺嫡', '杨广是如何通过一步步的算计去多夺得太子之位？', '历史网', '2019-07-17', '6', '201907191023101.jpg');
INSERT INTO `news` VALUES ('73', '大数据时代来临', '大数据分析，通过数据总结出人的规律和习惯，更好的了解人的生活习性。', '中国科技', '2019-07-18', '4', '201907181854171.jpg');
INSERT INTO `news` VALUES ('74', '公司招聘的原则', '解密公司招聘的规则以及如何得到面试官的认可。', '卡普空', '2019-07-18', '8', '201907181854171.jpg');
INSERT INTO `news` VALUES ('75', '庆余年首播', '猫腻大神的代表作作品，非常值得一看，宫廷斗争，尔虞我诈！！', '猫腻', '2019-07-18', '2', '201907221707371.jpg');
INSERT INTO `news` VALUES ('76', '政府开启扶贫政策', '猫腻大神的代表作作品，非常值得一看，宫廷斗争，尔虞我诈！！', '猫腻', '2019-07-18', '2', '201907221707371.jpg');
INSERT INTO `news` VALUES ('77', '鬼泣合集打折优惠', '真的来了，就是好的', '卡普空', '2019-07-18', '7', '201908091807096.jpg');

-- ----------------------------
-- Table structure for newstype
-- ----------------------------
DROP TABLE IF EXISTS `newstype`;
CREATE TABLE `newstype` (
  `t_id` int(11) NOT NULL AUTO_INCREMENT,
  `t_code` int(11) DEFAULT NULL,
  `t_content` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`t_id`),
  KEY `t_code` (`t_code`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of newstype
-- ----------------------------
INSERT INTO `newstype` VALUES ('1', '1', '财经');
INSERT INTO `newstype` VALUES ('2', '2', '政治');
INSERT INTO `newstype` VALUES ('3', '3', '娱乐');
INSERT INTO `newstype` VALUES ('4', '4', '科技');
INSERT INTO `newstype` VALUES ('5', '5', '军事');
INSERT INTO `newstype` VALUES ('6', '6', '历史');
INSERT INTO `newstype` VALUES ('7', '7', '游戏');
INSERT INTO `newstype` VALUES ('8', '8', '职场');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `u_id` int(255) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `u_age` int(255) DEFAULT NULL,
  `u_phone_number` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `u_sex` int(255) DEFAULT NULL,
  `u_pwd` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'Alan', '40', '13130464888', '1', '123');
INSERT INTO `user` VALUES ('2', 'Bolb', '25', '15948756693', '1', '456');
INSERT INTO `user` VALUES ('3', 'Lily', '32', '18954374455', '0', '789');
INSERT INTO `user` VALUES ('4', 'Nero', '25', '13130464889', '1', 'devil');
INSERT INTO `user` VALUES ('5', 'tnero', '26', 'g23435324543', '0', 'sfjdla');
INSERT INTO `user` VALUES ('6', 'alan nero', '45', '54646464546', '1', 'fwefwe');
INSERT INTO `user` VALUES ('7', 'nero,alan', '55', '4646546466', '1', 'fewf');
INSERT INTO `user` VALUES ('8', 'alan nero dante', '65', '465465+4655', '2', 'fwef');
INSERT INTO `user` VALUES ('9', 'lday,nero,dar', '65', '484654465464', '1', 'fewfew');
INSERT INTO `user` VALUES ('11', 'denero', '15', '15565845655', '0', '464');
INSERT INTO `user` VALUES ('12', 'dante', '78', '15646546546', '1', '456');
