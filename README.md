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
> `main.py -u <username> -p <password> `

##### 例如
 
> `main.py -u B9071121 -p  12345678`

#### 批量报告
> `main -m [-f=<filename>]`

##### 例如
> `main.py -m`

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

## todo
- [x] 登录
- [x] 报告
- [ ] 定时报告
- [x] 批量报告
- [ ] tgbot提醒
