# lit-ncov-report
洛阳理工学院 “健康状况管控平台” 每日自动上报程序

![test](https://raw.githubusercontent.com/icepie/lit-ncov-report/master/docs/run.png) 

## eof
本branch为最初的版本, 已迭代至1.9, 因个人的一些原因已停止其开发生命周期, 将会抽空重构此项目~
并会使用golang设计一款go风格的同类软件[lit-health-go](https://github.com/icepie/lit-health-go)

## ~~fbi~~ warning!!
1. 本程序上报的信息均为上次用户自己上报的信息(包括体温)!
2. 仅作为交流使用, 不可商用盗用!

## how to use
### to prepare
1. 准备好`python3`环境
2. 安装所需依赖：`pip3 install -r requirements.txt` 或者 `make init`
3. 运行程序:`python3 main.py`
### mode
#### 单用户上报
```bash
main.py -u <username> -p <password> 
```
##### 例如
```bash
main.py -u B9071121 -p  12345678
```
#### 批量上报
```bash
main -m [-f <filename>]
```
##### 例如
```bash
main.py -m -f config/myuser.json
```
若`-f`参数不存在, 将会加载默认配置文件 `config\user.json`

##### json guide
```json
{
    "1": {
        "name":"class1",
        "1":{ "un":"xxxxxxxxx", "pw": "" },
        "2":{ "un":"xxxxxxxxx", "pw": "" },
        "3":{ "un":"xxxxxxxxx", "pw": "" }
    },
    "2": {
        "name":"classmate",
        "1":{ "un":"xxxxxxxxx", "pw": "" },
        "2":{ "un":"xxxxxxxxx", "pw": "" },
        "3":{ "un":"xxxxxxxxx", "pw": "" }
    }
}
```
ps:
请按照该格式修改

`class` 和 `classmate` 为组名

前段`1` 和`2`为组序

`un`  为学号, `pw`为密码

前段`1` 和`2`及 `3`为成员序号
### table show
添加参数 `-b` 即可输出结果表格
> 注意: 只针对多用户模式生效且支持提醒模块
##### 例如
```bash
$icepie:python3 main.py -m -b
[s]程序运行中...
[s]正在生成结果...
+--------------+-----------+----------+---------------------+------------+
|     编号     |    学号   |   姓名   |         上次        | 本次       |
+--------------+-----------+----------+---------------------+------------+
|   兄弟萌:1   | B19xxxxxx |  李狗蛋  | 2020-03-31 00:00:16 | 今日已提交 |
|   兄弟萌:2   | B19xxxxxx | 登陆失败 |       无法解析      | 未知操作   |
|   兄弟萌:3   | B19xxxxxx |  张三丰  | 2020-03-31 00:00:17 | 今日已提交 |
|   宝贝萌:1   | B19xxxxxx |   王者   | 2020-03-31 00:00:18 | 今日已提交 |
|   宝贝萌:2   | B19xxxxxx |  猪肉荣  | 2020-03-31 00:00:19 | 今日已提交 |
|   宝贝萌:3   | B19xxxxxx |  牛旺仔  | 2020-03-31 00:00:20 | 今日已提交 |
+--------------+-----------+----------+---------------------+------------+
[f]已生成结果表格
```

### remind sever
#### wechat提醒

![test](https://raw.githubusercontent.com/icepie/lit-ncov-report/master/docs/sc1.png) 
![test](https://raw.githubusercontent.com/icepie/lit-ncov-report/master/docs/sc2.png)
![test](https://raw.githubusercontent.com/icepie/lit-ncov-report/master/docs/sc3.png)

1. 进入 http://sc.ftqq.com/3.version ,按照教程获取你的 `sckey`
2. 打开 `config/push.json`

```json
{
    "sckey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

3. 将 `sckey` 替换为你自己的
4. 在 `批量报告` 的基础上添加 `-s` 或者 `--serverchan` 参数即可开启
##### 例如
```bash
main.py -m -s
```

#### tgbot提醒

![test](https://raw.githubusercontent.com/icepie/lit-ncov-report/master/docs/tg.png)

1. 进入 https://core.telegram.org/bots/api ,按照教程获取你的 `tgtoken` 和 `tgid`
2. 打开 `config/push.json`

```json
{
    "tgtoken": "xxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "tgid" : "xxxxxxxxx"
}
```

3. 将其中的 `tgtoken` 和 `tgid` 替换为你自己bot的
4. 在 `批量报告` 的基础上添加 `-t` 或者 `--tgbot` 参数即可开启

##### 例如
```bash
main.py -m -t
```
##### proxy
1. 国内网络环境启用 `tgbot提醒` 需要开启代理模式
2. 打开 `src/push.py`
3. 将以下内容修改并去掉注释(代理地址支持 `http` 以及 `socks`)
```python
telebot.apihelper.proxy = {'https':'代理地址'}
```

### 定时上报
1. 打开 `task.py` 查看并修改确认配置
2. 终端输入 `python3 task.py` 或者 `make task` 运行
3. 在 `config/jobs.conf` 可查看运行情况
4. 可使用`supervisor`守护该脚本的进程
5. ~~使用`github actions`正在开发中~~

### 其他
若要求每日在Q群发送提交图片的话, 参考[mirai-bot-fun](https://github.com/icepie/mirai-bot-fun)

## todo
### 基础功能
- [x] 登录
- [x] 上报
- [x] 定时上报
- [x] 批量上报
- [x] 表格生成
### 推送模块
- [x] wechat提醒(基于 `serverchan` )
- [x] tgbot提醒
### 进阶使用
- [ ] web管理
