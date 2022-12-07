SET FOREIGN_KEY_CHECKS=0;
DROP TABLE game;
DROP TABLE goal;
DROP TABLE goal_reached;
SET FOREIGN_KEY_CHECKS=1;
 
CREATE TABLE player (
ID int not null,
screen_name varchar(20),
points int,
hp int,
fuel int,
primary key (ID)
);
 
CREATE TABLE enemy (
enemy_ID int not null,
e1 varchar(20),
e2 varchar(20),
e3 varchar(20),
e4 varchar(20),
e5 varchar(20),
e1_moves int,
e2_moves int,
e3_moves int,
e4_moves int,
e5_moves int,
primary key (enemy_ID),
foreign key (enemy_ID) REFERENCES player(ID)
);