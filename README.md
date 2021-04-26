# HelperHelper
基于Python的监听剪切板自动处理m3u8下载任务的小工具

## 注意
本工具仅供学习使用, 搞出什么大新闻不要找我负责!

## 可以做什么?
后台监听剪切板, 当检测到特定格式的连接后, 自动处理m3u8下载任务.
```
格式例如: https://www.abcd.com/efgh.m3u8#IJK-123
```
检测到该链接后程序会自动下载
```https://www.abcd.com/efgh.m3u8```
并将文件保存为```IJK-123.mp4```

## 使用方法

### 下载
* Clone本项目, 命令行运行helper.py即可
* 在[release](https://github.com/FupengWang/HelperHelper/releases)界面直接下载编译后的二进制可执行文件

### 使用
+ 每次运行会检测当前目录是否存在配置文件, 如若不存在会进入向导, 帮助生成配置文件
+ "Tools Path" 指下载工具的保存位置
+ "Download Path" 指视频文件的保存位置
+ 如果需要使用代理请填写"Proxy Address", 否则请直接回车
+ "Proxy Address"的格式例如 http://127.0.0.1:1080 or socks5://127.0.0.1:7890
+ 配置完成后请等待, 直至屏幕上打印了"Launched Successfully!"的信息, 此时程序进入了监听剪贴板的状态, 读取到特定格式的剪辑版后会自动下载文件到先前设定的"Download Path"中

### 配置文件格式参考
```
[setting]
toolpath = E:\tp18
downloadpath = E:\tp18
proxies = http://127.0.0.1:7890
```
### 其他注意事项
如果出现了不知名的错误, 请重新打开程序即可.

如果首次启动较慢, 可能是因为网络不佳导致依赖文件下载较慢, 请尝试使用代理网络或者耐心等待.

## 版权声明
该项目签署了MPL-2.0授权许可，详情请参阅 LICENSE.md 

## 鸣谢
该项目使用[@nilaoda](https://github.com/nilaoda)的[N_m3u8DL-CLI](https://github.com/nilaoda/N_m3u8DL-CLI)项目作为依赖