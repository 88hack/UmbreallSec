2019-06-05 15:15:36,760 - {"进程PID": "", "手工排查确认": "ifconfig | grep PROMISC | grep RUNNING", "异常时间": "", "异常文件": "", "风险名称": "网卡混杂模式检测", "处理方案": "ifconfig eth0 -promisc #关闭网卡混杂模式", "异常信息": "网卡开启混杂模式", "检测项": "## 网络链接类安全检测", "风险级别": "可疑", "所属用户": ""}
2019-06-05 15:15:36,760 - {"进程PID": "", "手工排查确认": "[1]ls -l /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/MacOS/ARDAgent", "异常时间": "2019-05-04 13:28:56", "异常文件": "/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/MacOS/ARDAgent", "风险名称": "setuid 后门", "处理方案": "chmod u-s /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/MacOS/ARDAgent #去掉setuid曲线", "异常信息": "文件/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/MacOS/ARDAgent 被设置setuid属性，通常此类被设置权限的文件执行后会给予普通用户root权限", "检测项": "常规后门检测", "风险级别": "风险", "所属用户": "root"}
2019-06-05 15:15:36,761 - {"进程PID": "", "手工排查确认": "[1]cat /etc/resolv.conf", "异常时间": "2019-06-04 08:41:46", "异常文件": "/etc/resolv.conf", "风险名称": "DNS安全配置", "处理方案": "vi /etc/resolv.conf #删除或者更改DNS境外配置", "异常信息": "DNS设置为境外IP: 114.114.114.114", "检测项": "配置类安全检测", "风险级别": "可疑", "所属用户": "root"}
2019-06-05 15:15:36,761 - {"进程PID": "", "手工排查确认": "[1]cat /etc/resolv.conf", "异常时间": "2019-06-04 08:41:46", "异常文件": "/etc/resolv.conf", "风险名称": "DNS安全配置", "处理方案": "vi /etc/resolv.conf #删除或者更改DNS境外配置", "异常信息": "DNS设置为境外IP: 180.76.76.76", "检测项": "配置类安全检测", "风险级别": "可疑", "所属用户": "root"}