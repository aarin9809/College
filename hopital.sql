CREATE TABLE `user` (
  `id` varchar(30) PRIMARY KEY AUTO_INCREMENT,
  `password` varchar(30),
  `name` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `birth` birth NOT NULL,
  `contacts` varchar(50),
  `email` varchar(50)
);

CREATE TABLE `doctor` (
  `doc_no` integer(30) PRIMARY KEY,
  `doc_name` varchar(20) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `hos_name` varchar(50) NOT NULL,
  `possible` boolean,
  `time` time NOT NULL
);

CREATE TABLE `hospital_info` (
  `address` varchar(50) UNIQUE PRIMARY KEY,
  `hos_name` varchar(30) NOT NULL,
  `hos_contacts` varchar(255) NOT NULL,
  `hos_homepage` varchar(255),
  `dept` varchar(50) NOT NULL,
  `score` varchar(255)
);

CREATE TABLE `reservation` (
  `res_no` integer PRIMARY KEY AUTO_INCREMENT,
  `hos_name` varchar(30),
  `id` varchar(30),
  `doc_no` integer(30),
  `date` date NOT NULL,
  `time` time NOT NULL,
  `dept` varchar(30) NOT NULL,
  `created_at` timestamp DEFAULT (now()),
  `deleted_at` timestamp DEFAULT (now())
);

CREATE TABLE `hospital_info_doctor` (
  `hospital_info_dept` varchar(50),
  `doctor_dept` varchar(50),
  PRIMARY KEY (`hospital_info_dept`, `doctor_dept`)
);

ALTER TABLE `hospital_info_doctor` ADD FOREIGN KEY (`hospital_info_dept`) REFERENCES `hospital_info` (`dept`);

ALTER TABLE `hospital_info_doctor` ADD FOREIGN KEY (`doctor_dept`) REFERENCES `doctor` (`dept`);


ALTER TABLE `reservation` ADD FOREIGN KEY (`id`) REFERENCES `user` (`id`);

ALTER TABLE `reservation` ADD FOREIGN KEY (`doc_no`) REFERENCES `doctor` (`doc_no`);

ALTER TABLE `reservation` ADD FOREIGN KEY (`hos_name`) REFERENCES `hospital_info` (`hos_name`);

ALTER TABLE `reservation` ADD FOREIGN KEY (`dept`) REFERENCES `doctor` (`dept`);

ALTER TABLE `reservation` ADD FOREIGN KEY (`dept`) REFERENCES `hospital_info` (`dept`);
