# baota-docker
Deploying baota panel via docker. 通过docker一键部署宝塔面板。

## 一、前言

好像很多人对这个感兴趣，但是实现得不多，能找到的资料也不多。

首先感谢前辈的分享，[https://github.com/pch18-docker/baota](https://github.com/pch18-docker/baota)，受此启发，鉴于原作者长时间未更新，且部分功能未完善，于是在此分享下本人改进过的docker一键部署宝塔面板的经验。能力有限，对github、Linux、docker等并不是特比的熟悉，基本上就是靠着文档+谷歌+实践慢慢学了些皮毛，所以本源码的不周全之处还请见谅，也希望各位前辈们多多指教。

初衷是每次部署宝塔面板的安装过程都非常繁琐和漫长，考虑到docker的便捷性，如果能将宝塔面板的成品环境打包成docker镜像，每次部署只需要一键拉取和部署即可，方便快捷，简单省事，无需等待每次部署环境的漫长过程。同时镜像环境可以自定义包括nginx、Apache、php、mysql、redis、memcached等软件。

另一方面，docker打包的宝塔环境镜像，可以仅作为反代使用，网站文件从外部挂载，或者反代远程or本地其他端口程序，或反代其他容器，与其他程序docker镜像相互搭配使用，进一步提高安全性和便捷性。

查过一些资料，本仓库源码主要受上述原始仓库的启发，进一步优化和改进，感谢前辈们的无私分享，也希望大家踊跃探讨，继续完善。

## 二、镜像特点

- 全程自动安装依赖
- 自动安装宝塔面板、环境、插件
- 自动修改默认面板端口、用户名、密码、安全入口
- 自动配置镜像ssh
- 自动同意首次登陆的用户协议
- 自动取消强制登录
- 自动降级为7.7.0版本

## 三、**特别提醒**

本仓库采用github action自动构建镜像并推送至docker hub，源码公开透明，所以请放心使用。但由于镜像内涉及到面板的用户名密码等敏感信息，建议各位自行修改与构建。

## 四、如何部署

- 面板默认登录地址：```http://{{面板ip地址}}:10808/xeu7TwHvtcfuj```
- 面板默认用户名：```nzzaidi```
- 面板默认密码：```dockerbaota```
- 面板默认端口：```10808```
- 面板默认安全入口：```/xeu7TwHvtcfuj```
- 镜像内部ssh端口：```1072```
- 镜像内部ssh root用户密码：```dockerbaota```

**注意**：部署后务必先修改如上信息！！！或者修改代码后自行构建使用！！！以防止被利用！！！

镜像仓库地址：[https://hub.docker.com/r/nzzaidi/baota-docker](https://hub.docker.com/r/nzzaidi/baota-docker)

代码仓库地址：[https://github.com/nzzaidi/baota-docker](https://github.com/nzzaidi/baota-docker)

### 1.通过 docker run 运行

```bash
docker run -itd \
  --name baota \
  --network=host \
  --privileged=true \
  --restart=unless-stopped \
  -v ~/www/wwwroot:/www/wwwroot \
  -v ~/www/vhost:/www/server/panel/vhost \
  nzzaidi/baota-docker:lnp
```

### 2. 通过 docker-compose 运行

```bash
git clone https://github.com/nzzaidi/baota-docker.git
cd baota-docker
docker pull nzzaidi/baota-docker:lnp
COMPOSE_HTTP_TIMEOUT=1200 docker-compose --verbose up -d
```

### 常用命令：

```bash
# 获取宝塔面板默认信息
docker exec -it baota /etc/init.d/bt default

# 重启nginx
docker exec -it baota /etc/init.d/nginx restart

# 重启PHP
docker exec -it baota /etc/init.d/php-fpm-80 restart

# 重启mysql
docker exec -it baota /etc/init.d/mysqld restart

# 进入宝塔容器
docker exec -it baota /bin/sh
```



## 五、版本区别

|已安装软件|clear| ln   | lnp  | lnmp |
| ---- | ---- | ---- | ---- | ---- |
| nginx | - | √-1.21 | √-1.21 | √-1.21 |
| php                                | -     | -      | √-8.0  | √-8.0          |
| mysql                              | - | - | - | √-mariadb_10.2 |
| phpmyadmin                         | -     | -      | -      | √-5.1          |
| redis                              | -     | -      | √      | √              |
| memcached                          | -     | -      | √      | √              |
| fileinfo                           | - | - | √ | √ |
| pm2 | - | - | √ | √ |
| phpguard（PHP守护） | - | - | √ | √ |
| ip_configuration（IP配置工具） | √ | √ | √ | √ |
| score（宝塔跑分） | √ | √ | √ | √ |
| webssh（宝塔SSH终端） | √ | √ | √ | √ |
| firewall（系统防火墙） | √ | √ | √ | √ |
| boot（系统启动项） | √ | √ | √ | √ |
| linuxsys（Linux工具箱） | √ | √ | √ | √ |
| supervisor（Supervisor管理器） | √ | √ | √ | √ |
| webshell_check（webshell查杀工具） | √ | √ | √ | √ |
| clear（日志清理工具） | √ | √ | √ | √ |
| webhook（宝塔WebHook） | √ | √ | √ | √ |
| msonedrive（微软OneDrive） | √ | √ | √ | √ |
| psync_api（宝塔一键迁移API版本） | √ | √ | √ | √ |
| gdrive（谷歌云网盘） | √ | √ | √ | √ |
| qiniu（七牛云存储） | √ | √ | √ | √ |
| txcos（腾讯云COS） | √ | √ | √ | √ |
| backup（宝塔配置备份） | √ | √ | √ | √ |

（√ 表示已安装，- 表示未安装）

建议使用ln / lnp 版本镜像，数据库外置，比如搭配adminer+mariadb+postgres的docker镜像，将宝塔面板容器和数据库容器连接使用，以防止意外发生导致数据库丢失或泄露。

