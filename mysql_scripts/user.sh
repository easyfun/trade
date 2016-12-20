#!/bin/bash

password="easyfun"
mysql_exec="msyql -uroot -p$password"
db=user

$mysql_exec -e "create database &db"

#用户总表
$mysql_exec $db -e "create table t_users(
        user_id bigint NOT NULL COMMENT '用户id，末两位与mobile末两位相同',
        real_name char(64) NOT NULL COMMENT '用户姓名',
        nick_name char(128) NOT NULL COMMENT '昵称',
        login_password char(128) NOT NULL COMMENT '密码',
        withdrawal_password char(128) NOT NULL DEFAULT '' COMMENT '取款密码',
        mobile char(24) NOT NULL COMMENT '手机号，末两位与user_id末两位相同',
        status int NOT NULL DEFAULT '0' COMMENT '状态 0正常 1锁定 2黑名单',
        from_type int NOT NULL COMMENT '来源类型 0:PC 1:IOS 2:Andriod',
        user_type int NOT NULL DEFAULT '0' COMMENT '用户类型 0投资用户 1借款用户 2平台用户',
        register_date datetime NOT NULL COMMENT '注册日期',
        referee_uid bigint NOT NULL COMMENT '推荐人uid',
        referee_name char(64) NOT NULL COMMENT '推荐人姓名',
        referee_mobile char(24) NOT NULL COMMENT '推荐人手机号',
        update_time datetime DEFAULT NULL COMMENT '最后一次修改时间',
        create_time datetime DEFAULT NULL COMMENT '创建时间',
        head_portrait_url varchar(256) DEFAULT '' COMMENT '头像地址url',
        PRIMARY KEY (user_id),
        UNIQUE KEY (mobile)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';"

for i in {0..99}
do
    m=$(($i/10))
    n=$(($i%10))
    
    #用户表
    $mysql_exec $db -e "create table t_user_${m}${n}(
        user_id bigint NOT NULL COMMENT '用户id，末两位与mobile末两位相同',
        real_name char(64) NOT NULL COMMENT '用户姓名',
        nick_name char(128) NOT NULL COMMENT '昵称',
        login_password char(128) NOT NULL COMMENT '密码',
        withdrawal_password char(128) NOT NULL DEFAULT '' COMMENT '取款密码',
        mobile char(24) NOT NULL COMMENT '手机号，末两位与user_id末两位相同',
        status int NOT NULL DEFAULT '0' COMMENT '状态 0正常 1锁定 2黑名单',
        from_type int NOT NULL COMMENT '来源类型 0:PC 1:IOS 2:Andriod',
        user_type int NOT NULL DEFAULT '0' COMMENT '用户类型 0投资用户 1借款用户 2平台用户',
        register_date datetime NOT NULL COMMENT '注册日期',
        referee_uid bigint NOT NULL COMMENT '推荐人uid',
        referee_name char(64) NOT NULL COMMENT '推荐人姓名',
        referee_mobile char(24) NOT NULL COMMENT '推荐人手机号',
        update_time datetime DEFAULT NULL COMMENT '最后一次修改时间',
        create_time datetime DEFAULT NULL COMMENT '创建时间',
        head_portrait_url varchar(256) DEFAULT '' COMMENT '头像地址url',
        PRIMARY KEY (user_id),
        UNIQUE KEY (mobile)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';"

    #用户表流水
    $mysql_exec $db -e "create table t_user_flow_${m}${n}(
        flow_id bigint NOT NULL COMMENT '流水id',
        real_name char(64) NOT NULL COMMENT '用户姓名',
        nick_name char(128) NOT NULL COMMENT '昵称',
        login_password char(128) NOT NULL COMMENT '密码',
        withdrawal_password char(128) NOT NULL DEFAULT '' COMMENT '取款密码',
        mobile char(24) NOT NULL COMMENT '手机号',
        from_type int NOT NULL COMMENT '来源类型 0:PC 1:IOS 2:Andriod',
        user_type int NOT NULL DEFAULT '0' COMMENT '用户类型 0投资用户 1借款用户 2平台用户',
        register_date datetime NOT NULL COMMENT '注册日期',
        referee_uid bigint NOT NULL COMMENT '推荐人uid',
        referee_name char(64) NOT NULL COMMENT '推荐人姓名',
        referee_mobile char(24) NOT NULL COMMENT '推荐人手机号',
        operation int NOT NULL DEFAULT 0 COMMENT '操作类型 0注册用户请求 1注册用户成功 2注册用户失败'
        remark char(128) NOT NULL COMMENT '备注',
        create_time datetime DEFAULT NULL COMMENT '创建时间',
        PRIMARY KEY (flow_id),
        UNIQUE KEY (mobile)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表流水';"
done