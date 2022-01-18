#coding: utf-8

import sys,os
os.chdir("/www/server/panel/")
sys.path.append("/www/server/panel/class/")
import public

def install_sync(softnames):
    softname = softnames.split(',')
    for i in range(len(softname)):
        download_url = public.get_url() + '/install/plugin/' + softname[i] + '/install.sh'
        toFile = '/tmp/%s.sh' % softname[i]
        public.downloadFile(download_url,toFile)
        set_pyenv(toFile)
        public.ExecShell('/bin/bash ' + toFile + ' install &> /tmp/panelShell.pl')
        if os.path.exists('/www/server/panel/plugin/' + softname[i]):
            public.WriteLog('TYPE_SETUP','PLUGIN_INSTALL_LIB',(softname[i],))
            if os.path.exists(toFile): os.remove(toFile)
            public.returnMsg(True," √ PLUGIN_INSTALL_SUCCESS： %s" % softname[i])
            print(" √ Plugin_Install_Success： %s" % softname[i])
            continue
        public.returnMsg(False," × 【 %s 】 安装失败!" % softname[i])

def set_pyenv(filename):
    if not os.path.exists(filename): return False
    env_py = '/www/server/panel/pyenv/bin'
    if not os.path.exists(env_py): return False
    temp_file = public.readFile(filename)
    env_path=['PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin']
    rep_path=['PATH={}/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin'.format(env_py+":")]
    for i in range(len(env_path)):
        temp_file = temp_file.replace(env_path[i],rep_path[i])
    public.writeFile(filename,temp_file)
    return True

if __name__ == "__main__":
    softnames = sys.argv[1]
    install_sync(softnames)