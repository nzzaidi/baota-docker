#coding: utf-8
import sys,os
os.chdir("/www/server/panel/")
sys.path.append("/www/server/panel/class/")
import public,db

username = 'nzzaidi'
password = 'dockerbaota'
new_port = 10808

sql = db.Sql()

# 修改默认用户名、密码
username_result = sql.table('users').where('id=?',(1,)).setField('username',username)
password_result = sql.table('users').where('id=?',(1,)).setField('password',public.password_salt(public.md5(password),uid=1))
public.writeFile('default.pl', password)


# 修改面板安全入口
public.writeFile('data/admin_path.pl', '/xeu7TwHvtcfuj')


# 修改默认面板端口
old_port = public.readFile('data/port.pl')
if sys.version_info[0] == 3: new_port = int(new_port)
public.writeFile('data/port.pl',str(new_port))
port_result = sql.table('firewall').where('port=?',(8888,)).setField('port',new_port)

if os.path.exists("/usr/bin/firewall-cmd"):
	os.system("firewall-cmd --permanent --zone=public --remove-port=%s/tcp" % old_port)
	os.system("firewall-cmd --permanent --zone=public --add-port=%s/tcp" % new_port)
	os.system("firewall-cmd --reload")
elif os.path.exists("/etc/sysconfig/iptables"):
    os.system("iptables -D INPUT -p tcp -m state --state NEW -m tcp --dport %s -j ACCEPT" % old_port)
    os.system("iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport %s -j ACCEPT" % new_port)
    os.system("service iptables save")
else:
	os.system("ufw delete allow %s" % old_port)
	os.system("ufw allow %s" % new_port)
	os.system("ufw reload")
print("|-已将面板端口修改为：%s" % new_port)
print("|-若您的服务器提供商是[阿里云][腾讯云][华为云]或其它开启了[安全组]的服务器,请在安全组放行[%s]端口才能访问面板" % new_port)


# 自动同意首次登陆的用户协议
licenes = 'data/licenes.pl'
public.writeFile(licenes, 'True')


# 输出
print('------username_result------:')
print(username_result)
print('------password_result------:')
print(password_result)
print('------port_result------:')
print(port_result)