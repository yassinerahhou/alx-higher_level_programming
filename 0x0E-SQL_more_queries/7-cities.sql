-- creat database
create table if not exists cities (
id INT not null PRIMARY KEY  AUTO_INCREMENT,
state_id INT not null PRIMARY KEY FOREIGN KEY (state_id) REFERENCES states(id)  ,
states,
name VARCHAR(256) not null

);
