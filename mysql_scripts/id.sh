#!/bin/bash

password="easyfun"
mysql_exec="msyql -uroot -p$password"
db=id

$mysql_exec -e "create database &db"

#用户总表
$mysql_exec $db -e "create table t_id(
        user_id bigint NOT NULL COMMENT '用户id，末两位与mobile末两位相同',
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';"
