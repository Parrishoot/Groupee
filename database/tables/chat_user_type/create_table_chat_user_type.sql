DROP TABLE `models`.`chat_user_type`;

CREATE TABLE `models`.`chat_user_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type_description` VARCHAR(64) NOT NULL UNIQUE,
  PRIMARY KEY (`id`));
  
INSERT INTO chat_user_type 
	VALUE 
	(NULL, 'POSTER'),
	(NULL, 'INTERACTER'),
	(NULL, 'VIEWER')

select * from chat_user_type