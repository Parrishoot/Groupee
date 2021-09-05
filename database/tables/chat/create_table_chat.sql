DROP TABLE `models`.`chat`;

CREATE TABLE `models`.`chat` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL UNIQUE,
  `description` VARCHAR(128) NULL DEFAULT '',
  `type_id` INT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`));
