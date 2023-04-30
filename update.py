#!/usr/bin/env python3
import json
import datetime
import requests
html = f"""<!DOCTYPE html>
<head>
    <title>Visual Studio C++ 运行库列表（来自 Wine 运行器）</title>
    <meta name="viewport" content="width=device-width" initial-scale="1" />
    <meta charset='UTF-8'>
    <meta http-equiv="content-language" content="zh-cn">
    <meta name="description" content="用于下载 Wine 的网站" >
</head>

<body>
    <h1>Visual Studio C++ 运行库列表（来自 Wine 运行器）</h1>
    <p>点击下方链接下载</p>
    <h3>推荐在 Wine 运行器内安装</h3>
    <h3>更新时间：{datetime.datetime.now().year}年{datetime.datetime.now().month}月{datetime.datetime.now().day}日 {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}</h3>
"""
#with open(f"information.json", "r") as file:
#    lists = json.loads(file.read())
lists = requests.get("http://vcpp.wine-runner.gfdgdxi.top/list.json").json()
for i in lists:
    html += f"    <p><a href='{i[1]}'>{i[0]}</a></p>\n"
html += f"""    <p><a href='https://gitee.com/gfdgd-xi-org/deep-wine-runner/stargazers'><img src='https://gitee.com/gfdgd-xi-org/deep-wine-runner/badge/star.svg?theme=dark' alt='star'></img></a><a href='https://gitee.com/gfdgd-xi-org/deep-wine-runner/members'><img src='https://gitee.com/gfdgd-xi-org/deep-wine-runner/badge/fork.svg?theme=dark' alt='fork'></img></a></p>
    <hr/>
    <h2>Wine 运行器</h2>
    <p><img src='https://gitee.com/gfdgd-xi-org/deep-wine-runner/widgets/widget_card.svg?colors=eae9d7,2e2f29,272822,484a45,eae9d7,747571'></p>
    <hr/>
    <h1 id="copyright">©2020~{datetime.datetime.now().year} gfdgd xi、为什么您不喜欢熊出没和阿布呢</h1>
</body>
<script>
    window.onload = function(){{
        var d = new Date();
        document.getElementById("copyright").innerHTML = "©2020~" + d.getFullYear() + " gfdgd xi、为什么您不喜欢熊出没和阿布呢";
    }}
</script>
"""
with open(f"index.html", "w") as file:
    file.write(html)