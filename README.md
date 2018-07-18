# 磁力获取器命令行工具

[![PyPI version](https://badge.fury.io/py/torrent-cli.svg)](https://badge.fury.io/py/torrent-cli) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

作为一个搞代码的，找资源这种事肯定不能像普通人一样打开百度盲目查找，你需要写个爬虫工具来帮你完成这件事情啦！

### 兼容环境
Windows/Linux/MacOs


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


### 如何使用
```
$ torrent-cli
usage: torrent-cli [-h] [-n NUM] [-s SORT_BY] [-o OUTPUT] [-p] [-v]
                   [KEYWORD [KEYWORD ...]]

Magnets-Getter CLI Tools.

positional arguments:
  KEYWORD               magnet keyword.

optional arguments:
  -h, --help            show this help message and exit
  -n NUM, --num NUM     magnet number.(default 10)
  -s SORT_BY, --sort-by SORT_BY
                        0: Sort by date，1: Sort by size. 2: Sort by hot-
                        rank.(default 0)
  -o OUTPUT, --output OUTPUT
                        output file path, supports csv and json format.
  -p, --pretty-oneline  show magnets info with one line.
  -v, --version         version information.
```


#### 示例

**根据关键字搜索**
```
$ torrent-cli 战狼2
Crawling data for you.....
磁链: magnet:?xt=urn:btih:80B24033541A8DE529876488E68DCD707B074990
名称: 战狼2.2017.tc720p.中英双字.制作@卡其，更多免费资源关注微信公众号 ：卡其影视控
大小: 829.0 MB
日期: 2018-05-15
热度: 1

磁链: magnet:?xt=urn:btih:CC3854CACBB5434E03EFF39C693B20223E0AA39D
名称: [hao4k.com]战狼2.4k.wolf.warriors.ii.2017.hk.2160p.uhd.blu-ray.hevc.truehd.atmos.7.1
大小: 56.8 GB
日期: 2018-05-14
热度: 25

磁链: magnet:?xt=urn:btih:F0BAFA381B258540374F854688CFFC7A590596F0
名称: 2017战狼2幕后全纪实hd720p中字.mp4
大小: 148.3 MB
日期: 2018-03-11
热度: 5

磁链: magnet:?xt=urn:btih:E7FC73D9E20697C6C440203F5884EF52F9E4BD28
名称: 战狼2.wlf.wrrirs.2.2017.hd720p.x264.aac-国语中字-rarbt
大小: 2.2 GB
日期: 2018-03-11
热度: 3

磁链: magnet:?xt=urn:btih:B8E5C85B5B368060AB245AC5E434981B0D5543CA
名称: 战狼2.字幕修复版.wolf.warriors.ii.2017.bd1080p.x264.dts-hd.ma.7.1.mandarin&english.chs-eng.mp4bafans
大小: 12.4 GB
日期: 2018-02-23
热度: 15

磁链: magnet:?xt=urn:btih:D6A5598C03C3123038DB6CAA04AE36D90BB569C6
名称: 战狼2.wolf.war[email protected]ourbits
大小: 35.0 GB
日期: 2018-02-22
热度: 16

磁链: magnet:?xt=urn:btih:5FE0D9709B9578DBD68BAAB949E00C502C703DE3
名称: [战狼2wolf.warrior.2][bluray-720p.mkv][3.42gb][国英双语]
大小: 3.4 GB
日期: 2018-02-22
热度: 25

磁链: magnet:?xt=urn:btih:5DFBF035D2CFAB3E04373C92A6463358ED5DA4E7
名称: 战狼2.超清国语中字.mp4
大小: 1.8 GB
日期: 2018-02-22
热度: 3

磁链: magnet:?xt=urn:btih:E478E2A78ECBD02C0AFC92D6E1552C09C834B43C
名称: 战狼2.wolf.warriors.ⅱ.2017.1080p.web-dl.x264.aac.mp4
大小: 2.8 GB
日期: 2018-02-22
热度: 54

磁链: magnet:?xt=urn:btih:AD222466087EC7D65A961BB293CE476F936C69B5
名称: 战狼2.2017.bd1280高清中英双字-www.iidvd.com.mp4
大小: 1.1 GB
日期: 2018-02-21
热度: 29
```

**单行显示并按大小排序（也可以指定排序顺序为 2，按热度排序）**
```
$ torrent-cli 战狼2 -p -s 1
Crawling data for you.....
magnet:?xt=urn:btih:CC3854CACBB5434E03EFF39C693B20223E0AA39D 56.8 GB 2018-05-14
magnet:?xt=urn:btih:D6A5598C03C3123038DB6CAA04AE36D90BB569C6 35.0 GB 2018-02-22
magnet:?xt=urn:btih:5B411E880CB585B5B596DBB25BB7F0927FD44F54 13.2 GB 2018-01-01
magnet:?xt=urn:btih:B8E5C85B5B368060AB245AC5E434981B0D5543CA 12.4 GB 2018-02-23
magnet:?xt=urn:btih:4640565A71BB840D6A082B7F8D387A5FF604941A 9.2 GB 2017-12-12
magnet:?xt=urn:btih:B6401277BA77620727F7D6FE1345501555F7CA28 7.8 GB 2017-11-16
magnet:?xt=urn:btih:2154B29E07DF4D21B67488C55667B1AB22CD63F4 7.8 GB 2017-12-17
magnet:?xt=urn:btih:C1F01F089892ECF2AF168C190754B2921902D9E1 7.5 GB 2017-11-16
magnet:?xt=urn:btih:DE42BC281CF39F0F489B64F06C2440466D545C83 5.4 GB 2017-12-13
```

**或者可以保存为 csv 或者 json 文件**（建议保存为 csv 文件，json 数据会被序列化，转为 utf 编码）
```
$ torrent-cli 战狼2 -o movie.csv
```


### License

MIT [©chenjiandongx](https://github.com/chenjiandongx)
