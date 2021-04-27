## lit-ncov-report
洛阳理工学院 "健康状况管控平台" 的一个非官方`Python封装库`兼`CLI工具`与`拓展实现` (for severless)

[![Build SCF ZIP](https://github.com/icepie/lit-ncov-report/actions/workflows/build-scf-zip.yml/badge.svg)](https://github.com/icepie/lit-ncov-report/actions/workflows/build-scf-zip.yml) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

[![QQ Group](https://img.shields.io/badge/QQ%20Group-647027400-red.svg)](https://jq.qq.com/?_wv=1027&k=lz0XyN86) [![TG Group](https://img.shields.io/badge/TG%20Group-lit_edu-blue.svg)](https://t.me/lit_edu)

## 须知

> 没想到突然用户多了这么多, 写点重要的...
> 
> 等闲下来再更新

### 待修复

- `20210303` 及之前发布版本中的基本配置里的 `second` 和 `third` 的模式请不要设置为 `last`

### 待更新

- 更新暴力模式
- 添加更多的推送模式
- 优化日志输出

### 友情链接

 - 感谢[阿加Erin](https://www.gaoajia.com/start-page.html)老兄的 `cqhttp` 推送配置[教程](https://www.gaoajia.com/ganhuo/97.html)

## 函数部署

### 程序下载

在此 [releases](https://github.com/icepie/lit-ncov-report/releases/tag/lit-ncov-report-scf) 下载最新自动打包的版本

### 选择平台

> 现已支持 { `腾讯云 云函数 SCF` , `阿里云 函数计算 FC` , `华为云 函数工作流 FG` }
> 
> 请点击你青睐的 `severless` 服务平台查看详细部署教程

<details>
<summary>腾讯云 SCF</summary>

#### 创建函数

打开 **云函数控制台-新建-自定义模板**,  如图

![tencent-scf](https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b1ebbd3c-ca49-405b-957b-effe60782276/f35d1ce1-18b8-4f00-8452-6edf3118011b.png)

#### 函数代码

1. 然后在 **提交方法** , 中选择 **本地上传zip包** 的方式上传 **lit-ncov-report-scf-xxxxxx.zip**

2. 在 **执行方法** , 中使用 `index.main_handler` (一般默认就可)

3. 点击选择好文件即可

#### 高级配置

- 选中 **固定出口IP** (推送服务正常工作的必要选项)

- **执行超时时间** 设置为 **900秒**

#### 触发器配置

**自定义创建-定时触发-自定义触发周期**

> 提示: 该触发器使用 `UTC+8` 即北京时间
>

例如每日 6点, 12点, 20点进行轮询上报

```corn
0 0 6,12,20 * * * *
```

</details>


<details>
<summary>阿里云 FC</summary>

#### 创建函数

打开 **函数计算控制台-服务与函数-服务列表-新增服务** , 如图

![1i2sU.png](https://img.ams1.imgbed.xyz/2021/03/12/1i2sU.png)

确认后提交

#### 函数代码

1. 接着点击右上角 **新增函数** , 再选择配置部署 **事件函数**

2. 然后在 **上传** , 中选择 **本地上传zip包** 的方式上传 **lit-ncov-report-scf-xxxxxx.zip**


[![1i3EX.png](https://img.ams1.imgbed.xyz/2021/03/12/1i3EX.png)](https://www.imgbed.com/image/1i3EX)


#### 配置

- 高级设置中超时时间拉满到 **600秒** 即可

- 其他保持默认

#### 触发器配置

> 提示: 该触发器使用 `UTC` 时间(请自行计算), 且比腾讯云少一位
>

例如每日 6点, 12点, 20点进行轮询上报

```corn
0 0 4,10,22 * * *
```

</details>


<details>
<summary>华为云 FG</summary>

#### 创建函数

打开 **函数工作流-创建函数** , 如图

![1iVz2.png](https://img.ams1.imgbed.xyz/2021/03/13/1iVz2.png)

#### 函数代码

在 **上传ZIP文件** , 中选择 **本地上传zip包** 的方式上传 **lit-ncov-report-scf-xxxxxx.zip**

#### 配置

- 配置中超时时间拉满到 **900秒** 即可


#### 触发器配置

> 提示: 该触发器使用 `UTC8` 时间, 即北京时间, 且比腾讯云少一位
>

例如每日 6点, 12点, 20点进行轮询上报

```corn
0 0 6,12,20 * * *
```

</details>

### 程序配置

在完成上诉操作后, 点击完成, 接下来打开 **函数代码** 进行配置

> 提示: 华为云用户目前需要先在 `zip` 代码包当中修改配置后重新上传

#### 基本配置

在`src/conf/conf.json`当中, 请自行查看并编辑

```json
{
    "report": {
        "first": {
            "mode": "last",
            "temperature": 36.3
        },
        "second": {
            "mode": "random",
            "temperature": 36.2
        },
        "third": {
            "mode": "manual",
            "temperature": 36.1
        }
    },
    "push": {
        "serverchan": {
            "enabled": true,
            "sckey": "SCKEY"
        },
        "cqhttp": {
            "enabled": false,
            "url": "http://0.0.0.0:5700",
            "touser": 0,
            "isgroup": true
        }
    }
}
```

- 上报模式: `last`, `random`, `manual` 分别代表 `上次记录温度`, `随机安全温度`, `手动填入温度(temperature)`

- 推送方式: 目前支持 [serverchan](http://sc.ftqq.com), [cqhttp](https://github.com/Mrs4s/go-cqhttp), 

#### 用户配置

在`src/conf/users.csv`当中

```csv
user,pwd
B19XXXXXX,PASS123
Z20XXXXXX,PASS123
```

- 如上例, 即可实现多用户

- 如需使用`v1`版本的用户配置, 请使用 [v1toscf.py](https://github.com/icepie/lit-ncov-report/blob/scf/v1toscf.py) 进行转换

## 最后

点击部署, 再测试一下就没问题啦

望使用愉快, 欢迎fork修改

![scf-cq-push](https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b1ebbd3c-ca49-405b-957b-effe60782276/ae0a2dc0-3880-45ec-b9b6-57e2af3e3887.jpg)
![scf-sc-push](https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b1ebbd3c-ca49-405b-957b-effe60782276/b1f69c81-6c58-4321-8b89-e7a56f98d5b3.jpg) 
