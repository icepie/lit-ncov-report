# lit-ncov-report
洛阳理工学院 “健康状况管控平台” 每日自动上报

![test](https://raw.githubusercontent.com/icepie/lit-ncov-report/master/docs/run.png) 
## how to use
### to prepare
1. 准备好`python3`环境
2. 安装所需依赖：`pip3 install -r requirements.txt` 或者 `make init`
3. 运行程序:`python3 main.py`
### mode
#### 单用户报告
```bash
main.py -u <username> -p <password> 
```
##### 例如
```bash
main.py -u B9071121 -p  12345678
```
#### 批量报告
```bash
main -m [-f <filename>]
```
##### 例如
```bash
main.py -m -f config/myuser.json
```
若`-f`参数不存在, 将会加载默认配置文件`config\user.json`

##### json guide
```json
{
    "1": {
        "name":"class1",
        "1":{ "un":"B1907xxxx", "pw": "" },
        "2":{ "un":"B1907xxxx", "pw": "" },
        "3":{ "un":"B1907xxxx", "pw": "" }
    },

    "2": {
        "name":"classmate",
        "1":{ "un":"B1907xxxx", "pw": "" },
        "2":{ "un":"B1907xxxx", "pw": "" },
        "3":{ "un":"B1907xxxx", "pw": "" }
    }
}
```
ps:
请按照该格式修改

`class` 和 `classmate` 为组名

前段`1` 和`2`为组序

`un`  为学号, `pw`为密码

前段`1` 和`2`及  `3`为成员序号

### remind sever
> 注意: 只针对多用户模式生效
#### wechat提醒

![test](https://raw.githubusercontent.com/icepie/lit-ncov-report/master/docs/sc.png)

1. 进入 http://sc.ftqq.com/3.version ,按照教程获取你的 `sckey`
2. 打开 `config/push.json｀

```json
{
    "sckey": "xxxxxxxxxxxxx"
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
2. 打开 `config/push.json｀

```json
{
    "tgtoken": "xxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "tgid" : "xxxxxxxxx"
}
```

3. 将 `tgtoken` 和 `tgid` 替换为你自己的t
4. 在 `批量报告` 的基础上添加 `-t` 或者 `--tgbot` 参数即可开启

##### 例如
```bash
main.py -m -t
```
## todo
### 基础功能
- [x] 登录
- [x] 报告
- [ ] 定时报告
- [x] 批量报告
### 提醒模块
- [x] wechat提醒(基于 `serverchan` )
- [x] tgbot提醒
### 进阶使用
- [ ] web管理
