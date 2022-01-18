FROM centos:7
MAINTAINER nzzaidi

# 将当前目录文件复制到根目录
COPY . /code/

#设置init.d和letsencrypt映射到www文件夹下持久化
RUN mkdir -p /www/letsencrypt /www/wwwroot \
    && ln -s /www/letsencrypt /etc/letsencrypt \
    && rm -f /etc/init.d \
    && mkdir /www/init.d \
    && ln -s /www/init.d /etc/init.d \
    && chmod +x -R /code

#更新系统 安装依赖 安装宝塔面板 清理缓存 输出面板默认信息
RUN cd /code \
    && yum -y update \
    && yum -y install wget curl vim openssh-server \
    && bash set_sshd_config.sh \
    && wget -O install.sh http://download.bt.cn/install/install_6.0.sh \
    && sed -i 's/8888/10808/g' install.sh \
    && echo y | bash install.sh \
    && curl -sL http://download.bt.cn/install/update6.sh|sed 's/version=.*/version=7.7.0/g'|bash \
    && bash /www/server/panel/install/install_soft.sh 0 install nginx 1.21 \
    && bash /www/server/panel/install/install_soft.sh 0 install php 8.0 || echo 'Ignore Error' \
    && bash /www/server/panel/install/install_soft.sh 0 install mysql mariadb_10.2 \
    && bash /www/server/panel/install/install_soft.sh 0 install phpmyadmin 5.1 || echo 'Ignore Error' \
    && bash /www/server/panel/install/install_soft.sh 0 install redis 80 \
    && bash /www/server/panel/install/install_soft.sh 0 install memcached 80 \
    && bash /www/server/panel/install/install_soft.sh 0 install fileinfo 80 \
    && bash /www/server/panel/install/install_soft.sh 0 install pm2 5 \
    && python install_plugin.py "phpguard,ip_configuration,score,webssh,firewall,boot,linuxsys,supervisor,webshell_check,clear,webhook,msonedrive,psync_api,gdrive,qiniu,txcos,backup" \
    && echo '["nginx", "mysql", "phpmyadmin", "php-8.0", "pm2", "supervisor", "redis", "memcached", "webhook", "linuxsys", "firewall", "boot"]' > /www/server/panel/config/index.json \
    && python set_default.py \
    && yum clean all \
    && rm -f /www/server/panel/data/bind.pl \
    && bash initialize_node.sh \
    && bt reload \
    && bt restart \
    && bt default

WORKDIR /www/wwwroot
CMD /code/entrypoint.sh
EXPOSE 10808 888 21 20 443 80

VOLUME ["/www/wwwroot","/www/wwwroot"]

HEALTHCHECK --interval=5s --timeout=3s CMD curl -fs http://localhost:10808/xeu7TwHvtcfuj || exit 1