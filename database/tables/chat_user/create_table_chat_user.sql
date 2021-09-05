DROP TABLE `models`.`chat_user`;

CREATE TABLE `models`.`chat_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `chat_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `chat_user_type_id` INT NOT NULL,
  PRIMARY KEY (`id`));
