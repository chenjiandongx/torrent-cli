# 磁力获取器命令行工具

[![PyPI version](https://badge.fury.io/py/torrent-cli.svg)](https://badge.fury.io/py/torrent-cli) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

作为一个搞代码的，找资源这种事，肯定不能像普通老百姓一样打开百度盲目查找啦！你需要写个爬虫工具来帮你完成这件事情啦！

### 兼容环境
Windwos/Linux/MacOs


### 安装
#### pip 安装
```
$ pip install torrent-cli
```

#### 源码安装
```
 $ git clone https://github.com/chenjiandongx/torrent-cli.git
 $ cd torrent-cli
 $ pip install -r requirements.txt
 $ python setup.py install
 ```


### 用法
```
C:\Users\chenjiandongx>torrent-cli
usage: torrent-cli [-h] [-k KEYWORD] [-n NUM] [-s SORT_BY] [-o OUTPUT] [-p]
                   [-v]

Magnets-Getter CLI Tools.

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
                        magnet keyword.
  -n NUM, --num NUM     magnet number.(default 10)
  -s SORT_BY, --sort-by SORT_BY
                        0: Sort by date，1: Sort by size. 2. Sort by hot-
                        rank.(default 0)
  -o OUTPUT, --output OUTPUT
                        output file path, supports csv and json format.
  -p, --pretty-oneline  show magnets info with one line.
  -v, --version         version information.
```


#### 简单示范
```
C:\Users\chenjiandongx>torrent-cli -k 战狼2
Crawling data for you.....
磁链: magnet:?xt=urn:btih:5E6BCE50844BFB6616F409595186913B17585085
名称: 战狼2.Wolf.Warriors.2.2017.1080p.WEB-DL.X264.AAC-BT4K
大小: 2.3 GB
日期: 2018-01-02
热度: 1

磁链: magnet:?xt=urn:btih:621C1325452840BA221740B0C6D305A625ECBC81
名称: 战狼2.新战狼.2017.HD2160P.X264.AAC.国语中字
大小: 5.4 GB
日期: 2018-01-01
热度: 2

磁链: magnet:?xt=urn:btih:A8E41331091160C1660404EA37CDABABA8616C21
名称: 战狼2.Wolf.Warriors.2.2017.1080p.WEB-DL.X264.AAC-bbs.homefei.me
大小: 3.5 GB
日期: 2018-01-01
热度: 118

磁链: magnet:?xt=urn:btih:5B411E880CB585B5B596DBB25BB7F0927FD44F54
名称: 战狼2.Wolf.Warriors.II.2017.BD1080P.X264.DTS-HD.MA.7.1.Mandarin&English.CHS-ENG.Mp4BaFans
大小: 13.2 GB
日期: 2018-01-01
热度: 9

磁链: magnet:?xt=urn:btih:73B9961CF84B39EBCCEB223A1D15DE2ECE4CF2F9
名称: 战狼2 2017_BD.mp4
大小: 1.6 GB
日期: 2017-12-22
热度: 50

磁链: magnet:?xt=urn:btih:51C8ACED86C6B073642D63CF502A00666B912AD1
名称: 战狼2.Wolf.Warriors.2.2017.WEB-DL.X264.AAC.1080P.CHS-MP44K
大小: 2.3 GB
日期: 2017-12-21
热度: 7

磁链: magnet:?xt=urn:btih:6DF8018D9D1B3058946E5E6CF07DF1FF0A59F254
名称: 战狼2.Wolf.Warriors.2.2017.BD720P.X264.AAC.Mandarin.CHS.国语中字
大小: 2.0 GB
日期: 2017-12-21
热度: 12

磁链: magnet:?xt=urn:btih:DFC0B3DBF09DD65426C4B7C5619CB00DB078F5D7
名称: 战狼2.Wolf.Warriors.II.2017.1080p.BluRay.x264-中英双字-RARBT
大小: 3.5 GB
日期: 2017-12-18
热度: 4

磁链: magnet:?xt=urn:btih:34F0C102D57A9AE77A93A22D27770452649E7AAA
名称: 【Mp4Bao.COM】战狼2.国语中英双字.Wolf.Warriors.2.2017.HD1080P.X264.AAC.CHS-ENG
大小: 2.3 GB
日期: 2017-12-18
热度: 1

磁链: magnet:?xt=urn:btih:57E9D5355EEFFC71DCAECC9B20014D0436D376A3
名称: 战狼2.Wolf.Warriors.II.2017.BD-1080p.X264.AAC-99Mp4.mp4
大小: 3.3 GB
日期: 2017-12-17
热度: 12
```

**单行显示并按大小排序（也可以指定排序顺序为 2，按热度排序）**
```
C:\Users\chenjiandongx>torrent-cli -k 战狼2 -p -s 1
Crawling data for you.....
magnet:?xt=urn:btih:5B411E880CB585B5B596DBB25BB7F0927FD44F54 13.2 GB 2018-01-01
magnet:?xt=urn:btih:621C1325452840BA221740B0C6D305A625ECBC81 5.4 GB 2018-01-01
magnet:?xt=urn:btih:A8E41331091160C1660404EA37CDABABA8616C21 3.5 GB 2018-01-01
magnet:?xt=urn:btih:DFC0B3DBF09DD65426C4B7C5619CB00DB078F5D7 3.5 GB 2017-12-18
magnet:?xt=urn:btih:57E9D5355EEFFC71DCAECC9B20014D0436D376A3 3.3 GB 2017-12-17
magnet:?xt=urn:btih:5E6BCE50844BFB6616F409595186913B17585085 2.3 GB 2018-01-02
magnet:?xt=urn:btih:51C8ACED86C6B073642D63CF502A00666B912AD1 2.3 GB 2017-12-21
magnet:?xt=urn:btih:34F0C102D57A9AE77A93A22D27770452649E7AAA 2.3 GB 2017-12-18
magnet:?xt=urn:btih:6DF8018D9D1B3058946E5E6CF07DF1FF0A59F254 2.0 GB 2017-12-21
magnet:?xt=urn:btih:73B9961CF84B39EBCCEB223A1D15DE2ECE4CF2F9 1.6 GB 2017-12-22
```

**或者可以保存为 csv 或者 json 文件**（建议保存为 csv 文件，json 数据会被序列化，转为 utf 编码）
```
C:\Users\chenjiandongx>torrent-cli -k 战狼2 -o movie.csv
```

#### 尝试了一下，支持各种正经的和有点不正经的资源！！！不信你试试！！！你会回来 star 的！！！
