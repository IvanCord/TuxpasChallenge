DROP TABLE IF EXISTS  careers;
CREATE TABLE `tuxpas`.`careers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `career` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`)
) COMMENT = 'Table that saves the list of careers';

INSERT INTO careers (id, career) VALUES (1, "Informatics Engineering");
INSERT INTO careers (id, career) VALUES (2, "Electric Engineering");

DROP TABLE IF EXISTS  courses CASCADE;
CREATE TABLE `tuxpas`.`courses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `course` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`)
) COMMENT = 'Table that saves the list of courses';

INSERT INTO courses (id, course) VALUES (1, "Algorithms");
INSERT INTO courses (id, course) VALUES (2, "Software Deployment 1");

DROP TABLE IF EXISTS  students CASCADE;
CREATE TABLE `tuxpas`.`students` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `enrolment` VARCHAR(45) NOT NULL,
  `career_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_career_id`
    FOREIGN KEY (`career_id`)
    REFERENCES `tuxpas`.`careers` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_course_id`
    FOREIGN KEY (`course_id`)
    REFERENCES `tuxpas`.`courses` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
) COMMENT = 'Table that saves the record of students';

INSERT INTO students (id, name, enrolment, career_id, course_id) VALUES (1, "Ivan Cordova", "2021-11-07T02:48:42Z", 1, 1);
INSERT INTO students (id, name, enrolment, career_id, course_id) VALUES (2, "Katherine Cordova", "2022-11-07T02:48:42Z", 2, 2);