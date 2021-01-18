# lit-ncov-report
洛阳理工学院 "健康状况管控平台" 的一个非官方`Python 封装库`兼`CLI工具`与`拓展实现`
> 如需旧版请前往[v1](https://github.com/icepie/lit-ncov-report/tree/v1)

## 安装
```bash
# Python3.6+ with pip
pip install -U litncov
```

## 封装库

### 范例

```python
#  导入模块
from litncov.user import litUesr

# 新建实例
testme = litUesr("username", "password")

# 判断是否登陆成功
if testme.is_logined:
    #打印用户信息
    print(testme.info)
    #打印上次上报信息
    print(testme.get_last_record())
    #打印学生学籍信息
    print(testme.get_instructor())
    #打印用户家庭信息
    print(testme.get_familys())
    #打印用户外出信息
    print(testme.get_trips())
    #打印疫情严重地区
    print(testme.get_important_city())
    #进行当日第一次体温上报
    ## 模式：使用上一次上报信息， 次数： 只上报第一次
    print(testme.first_record(mode='last', times=1))
    #进行当日第二次体温上报
    ## 模式：手动填入， 温度： 36.6 摄氏度
    print(testme.second_record(mode='manual', temperature=36.6))
    #进行当日第二次体温上报
    ## 模式：随机生成正常体温(36.0~37.2 摄氏度)
    print(testme.third_record(mode='random'))
```

## CLI工具
### 查看帮助
```bash
litncov --help
```

### 拓展实现
