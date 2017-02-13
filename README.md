架构：B/S架构，接入层使用Nginx，业务层Tornado，数据存储层Mysq+Redis。MySQL用于存储用户信息，用户信息放置在user数据库，分成100张表。给每个用户分配一个唯一user id，利用user id末两位定位分表。Redis按业务类型存储最新ID信息。DAO层简单封装MySQL的Python驱动，ORM框架开销比较大没有采用。
系统模块：ID系统，用户系统。
部署方式：Nginx负载均衡，T ID系统按照业务类型生成唯一ID，用户系统完成开通、登录、注销、修改用户信息、修改密码等功能。ornado开启多个实例，MySQL一主多从、读写分离，Redis一主一从。
