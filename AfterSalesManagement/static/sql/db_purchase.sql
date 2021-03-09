/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : db_purchase

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 08/03/2021 07:43:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for case_info
-- ----------------------------
DROP TABLE IF EXISTS `case_info`;
CREATE TABLE `case_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IEMI` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `case_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `lot_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `iphone_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `problem` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `change_time` date NULL DEFAULT NULL,
  `operation` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `feedback` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `iphone_storage` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `apply_price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `approve_price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `IEMI`) USING BTREE,
  UNIQUE INDEX `IEMI`(`IEMI`) USING BTREE,
  INDEX `case_id`(`case_id`) USING BTREE,
  INDEX `problem`(`problem`) USING BTREE,
  INDEX `operation`(`operation`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 155 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of case_info
-- ----------------------------

-- ----------------------------
-- Table structure for case_operations
-- ----------------------------
DROP TABLE IF EXISTS `case_operations`;
CREATE TABLE `case_operations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_operations` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `problem`(`case_operations`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of case_operations
-- ----------------------------
INSERT INTO `case_operations` VALUES (15, '');
INSERT INTO `case_operations` VALUES (1, '申请退款');
INSERT INTO `case_operations` VALUES (16, '退货退款');

-- ----------------------------
-- Table structure for case_status
-- ----------------------------
DROP TABLE IF EXISTS `case_status`;
CREATE TABLE `case_status`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of case_status
-- ----------------------------
INSERT INTO `case_status` VALUES (2, '');
INSERT INTO `case_status` VALUES (3, '打开');
INSERT INTO `case_status` VALUES (4, '申请售后');
INSERT INTO `case_status` VALUES (5, '退货出库');
INSERT INTO `case_status` VALUES (6, '关闭');

-- ----------------------------
-- Table structure for cases_table
-- ----------------------------
DROP TABLE IF EXISTS `cases_table`;
CREATE TABLE `cases_table`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` date NULL DEFAULT NULL,
  `lot_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bad_count` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `bad_rate` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `RMA_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tracking_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `responsible` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `case_id`) USING BTREE,
  INDEX `lot_num`(`lot_num`) USING BTREE,
  INDEX `case_id`(`case_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cases_table
-- ----------------------------

-- ----------------------------
-- Table structure for iphone_storage
-- ----------------------------
DROP TABLE IF EXISTS `iphone_storage`;
CREATE TABLE `iphone_storage`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `iphone_storage` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of iphone_storage
-- ----------------------------
INSERT INTO `iphone_storage` VALUES (1, NULL);
INSERT INTO `iphone_storage` VALUES (2, '16 GB');
INSERT INTO `iphone_storage` VALUES (3, '32 GB');
INSERT INTO `iphone_storage` VALUES (4, '64 GB');
INSERT INTO `iphone_storage` VALUES (5, '128 GB');
INSERT INTO `iphone_storage` VALUES (6, '256 GB');
INSERT INTO `iphone_storage` VALUES (7, '512 GB');
INSERT INTO `iphone_storage` VALUES (9, '');

-- ----------------------------
-- Table structure for iphone_type
-- ----------------------------
DROP TABLE IF EXISTS `iphone_type`;
CREATE TABLE `iphone_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `iphone_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `iphone_type`(`iphone_type`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of iphone_type
-- ----------------------------
INSERT INTO `iphone_type` VALUES (9, '');
INSERT INTO `iphone_type` VALUES (8, 'iphone 11');
INSERT INTO `iphone_type` VALUES (10, 'iphone 11 Pro');
INSERT INTO `iphone_type` VALUES (13, 'iphone 11 Pro Max');
INSERT INTO `iphone_type` VALUES (11, 'iphone 12');
INSERT INTO `iphone_type` VALUES (1, 'iphone 7');
INSERT INTO `iphone_type` VALUES (2, 'iphone 7 Plus');
INSERT INTO `iphone_type` VALUES (3, 'iphone 8');
INSERT INTO `iphone_type` VALUES (4, 'iphone 8 Plus');
INSERT INTO `iphone_type` VALUES (6, 'iphone X');
INSERT INTO `iphone_type` VALUES (5, 'iphone XR');
INSERT INTO `iphone_type` VALUES (7, 'iphone XS');

-- ----------------------------
-- Table structure for problem
-- ----------------------------
DROP TABLE IF EXISTS `problem`;
CREATE TABLE `problem`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `problem`(`problem`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of problem
-- ----------------------------
INSERT INTO `problem` VALUES (11, '');
INSERT INTO `problem` VALUES (10, 'Face ID');
INSERT INTO `problem` VALUES (2, 'ID锁');
INSERT INTO `problem` VALUES (1, 'SIM锁');
INSERT INTO `problem` VALUES (4, 'SIM锁/监管');
INSERT INTO `problem` VALUES (8, '功能不良');
INSERT INTO `problem` VALUES (9, '外观/功能');
INSERT INTO `problem` VALUES (7, '外观不良');
INSERT INTO `problem` VALUES (3, '监管');
INSERT INTO `problem` VALUES (6, '错内存');
INSERT INTO `problem` VALUES (5, '错机');

-- ----------------------------
-- Table structure for receipts_table
-- ----------------------------
DROP TABLE IF EXISTS `receipts_table`;
CREATE TABLE `receipts_table`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lot_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `in_time` date NULL DEFAULT NULL,
  `supply_company` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `credit_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `iphone_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `iphone_storage` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `amount` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `lot_num`(`lot_num`) USING BTREE,
  INDEX `supply_company`(`supply_company`) USING BTREE,
  INDEX `iphone_type`(`iphone_type`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 80 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of receipts_table
-- ----------------------------

-- ----------------------------
-- Table structure for responsible
-- ----------------------------
DROP TABLE IF EXISTS `responsible`;
CREATE TABLE `responsible`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `responsible` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of responsible
-- ----------------------------
INSERT INTO `responsible` VALUES (1, '');
INSERT INTO `responsible` VALUES (2, '采购');
INSERT INTO `responsible` VALUES (3, 'HK');

-- ----------------------------
-- Table structure for supply_company
-- ----------------------------
DROP TABLE IF EXISTS `supply_company`;
CREATE TABLE `supply_company`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supply_company` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `supply_company`(`supply_company`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of supply_company
-- ----------------------------
INSERT INTO `supply_company` VALUES (3, '');
INSERT INTO `supply_company` VALUES (1, 'AT&T');
INSERT INTO `supply_company` VALUES (5, 'Cwork');
INSERT INTO `supply_company` VALUES (4, 'HYLA');
INSERT INTO `supply_company` VALUES (6, 'SPR');
INSERT INTO `supply_company` VALUES (2, 'Sprint');

SET FOREIGN_KEY_CHECKS = 1;
