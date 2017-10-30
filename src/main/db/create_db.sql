
CREATE DATABASE database;

CREATE TABLE `sales` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`customer_id`	INTEGER,
	`product_name`	TEXT,
	`net_value`	INTEGER,
	`tax_rate`	INTEGER
);
CREATE TABLE `customers` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`name`	TEXT,
	`surname`	TEXT,
	`birthyear`	INTEGER,
	`gender`	TEXT
);

