DROP TABLE `models`.`chat_type`;

CREATE TABLE `models`.`chat_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type_description` VARCHAR(64) NOT NULL UNIQUE,
  PRIMARY KEY (`id`));

INSERT INTO chat_type 
	VALUE 
	(NULL, 'PUBLIC'),
	(NULL, 'SELECTIVE'),
	(NULL, 'PRIVATE')