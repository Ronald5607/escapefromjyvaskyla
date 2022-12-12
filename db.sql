SET FOREIGN_KEY_CHECKS=0;
DROP TABLE game;
DROP TABLE goal;
DROP TABLE goal_reached;
SET FOREIGN_KEY_CHECKS=1;
 
CREATE TABLE player (
ID varchar(40) not null,
screen_name varchar(20),
points int,
hp int,
fuel int,
primary key (ID)
);
 
CREATE TABLE enemy (
enemy_ID varchar(40) not null,
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

CREATE TABLE last_airports (
ID int not null auto_increment,
last1 varchar(10),
last2 varchar(10),
last3 varchar(10),
last4 varchar(10),
last5 varchar(10),
last6 varchar(10),
last7 varchar(10),
last8 varchar(10),
last9 varchar(10),
last10 varchar(10),
primary key (ID),
foreign key (ID) REFERENCES player(ID)
);