#!/bin/bash

# 删除原设置，在sshd_config末尾添加新设置

sed -i '/^.*Port.*/d' /etc/ssh/sshd_config \
&& sed -i '/^.*PermitRootLogin.*/d' /etc/ssh/sshd_config \
&& sed -i '/^.*PubkeyAuthentication.*/d' /etc/ssh/sshd_config \
&& sed -i '/^.*PasswordAuthentication.*/d' /etc/ssh/sshd_config \
&& sed -i '/^.*PermitEmptyPasswords.*/d' /etc/ssh/sshd_config \
&& sed -i '$a\
Port 1072  # ssh端口号\
PermitRootLogin yes  # 允许以root身份登录\
PubkeyAuthentication no  #禁止通过密钥登录\
PasswordAuthentication yes  # 允许通过密码登录\
PermitEmptyPasswords no  # 禁止空密码' /etc/ssh/sshd_config \
&& echo root:dockerbaota | chpasswd

# systemctl restart sshd