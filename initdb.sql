CREATE TABLE `tuxpas`.`careers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `career` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`)
) COMMENT = 'Table that saves the list of careers';

CREATE TABLE `tuxpas`.`courses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `course` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ifk_career_idd`)
) COMMENT = 'Table that saves the list of courses';

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