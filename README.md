# 磁力获取器命令行工具

作为一个学编程的，找资源这种事，肯定不能像普通老百姓一样打开百度盲目查找啦。此时你就需要大喊一声 Python 大法好。
近日无意中看到了一个不错的网站，心想着就把它利用起来吧，就写了一个磁力资源获取器命令行工具。

### 开发环境
Windows10 + Python3


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
  -n NUM, --num NUM     magnet number.(default 20)
  -s SORT_BY, --sort-by SORT_BY
                        0: Sort by date，1: Sort by size.(default 0)
  -o OUTPUT, --output OUTPUT
                        output file path, supports csv and json format.
  -p, --pretty-oneline  show magnets info with one line.
  -v, --version         version information.

```


#### 简单示范

```
C:\Users\chenjiandongx>torrent-cli -k 战狼2
Crawling data for you.....
{'magnet': 'magnet:?xt=urn:btih:621c1325452840ba221740b0c6d305a625ecbc81',
 'magnet_date': '2017-11-15',
 'magnet_name': '战狼2.新战狼.2017.HD2160P.X264.AAC.国语中字',
 'magnet_size': '5.43 GB'}
{'magnet': 'magnet:?xt=urn:btih:a8e41331091160c1660404ea37cdababa8616c21',
 'magnet_date': '2017-11-12',
 'magnet_name': '战狼2.Wolf.Warriors.2.2017.1080p.WEB-DL.X264.AAC-bbs.homefei.me',
 'magnet_size': '3.5 GB'}
{'magnet': 'magnet:?xt=urn:btih:1647c411b8481738d29661b96629c7493f62ed12',
 'magnet_date': '2017-11-12',
 'magnet_name': '战狼2.新战狼.2017.HD1080P.X264.AAC.国语中字',
 'magnet_size': '2.61 GB'}
{'magnet': 'magnet:?xt=urn:btih:afbda9a99b38f4fb974931fac6b9817126ce25f0',
 'magnet_date': '2017-11-11',
 'magnet_name': '战狼2.mp4',
 'magnet_size': '2.32 GB'}
......
```

单行显示并按大小排序
```
C:\Users\chenjiandongx>torrent-cli -k 战狼2 -p -s 1
Crawling data for you.....
magnet:?xt=urn:btih:b6401277ba77620727f7d6fe1345501555f7ca28 7.75 GB 2017-11-09
magnet:?xt=urn:btih:8cdba300f43884ef7958c75343f3b10dd0009881 7.49 GB 2017-11-09
magnet:?xt=urn:btih:7e364fe1ef493761aa7c2c4231f5d8dc34df90fe 5.44 GB 2017-11-06
magnet:?xt=urn:btih:fad291b30048f367c4324cbef6fa6ce127ae6940 5.44 GB 2017-11-08
magnet:?xt=urn:btih:de42bc281cf39f0f489b64f06c2440466d545c83 5.44 GB 2017-11-11
magnet:?xt=urn:btih:621c1325452840ba221740b0c6d305a625ecbc81 5.43 GB 2017-11-15
magnet:?xt=urn:btih:bf2f95270fb94bf98dd23e0546c463c7343fbfca 3.56 GB 2017-11-10
magnet:?xt=urn:btih:a8e41331091160c1660404ea37cdababa8616c21 3.5 GB 2017-11-12
magnet:?xt=urn:btih:f26ce21764f946c92da5aa89d6db067d751c0d3f 2.76 GB 2017-11-07
magnet:?xt=urn:btih:244d7f5b281b0c3731f345f4c46259954d3bddf4 2.72 GB 2017-11-09
magnet:?xt=urn:btih:6bb32d1fd3f44293657e7f23f163c8af21c27d52 2.69 GB 2017-11-06
magnet:?xt=urn:btih:c60e1f9436118b36ce8d3bfdf16504b71d18d4f9 2.69 GB 2017-11-09
magnet:?xt=urn:btih:1647c411b8481738d29661b96629c7493f62ed12 2.61 GB 2017-11-12
magnet:?xt=urn:btih:770ad4f9882ba6245bdf7d7aa97d2dd8afa691b5 2.55 GB 2017-11-10
magnet:?xt=urn:btih:5e6bce50844bfb6616f409595186913b17585085 2.32 GB 2017-11-07
magnet:?xt=urn:btih:34f0c102d57a9ae77a93a22d27770452649e7aaa 2.32 GB 2017-11-09
magnet:?xt=urn:btih:2fb2595d41c7570b1a50634b2e466a149c0a2f7d 2.32 GB 2017-11-09
magnet:?xt=urn:btih:9aabc55040066ce78d27ca36d8c15ae56ccf5b0b 2.32 GB 2017-11-10
magnet:?xt=urn:btih:afbda9a99b38f4fb974931fac6b9817126ce25f0 2.32 GB 2017-11-11
magnet:?xt=urn:btih:b2489aed91b9a154bcb31147897d8183ca1707bd 720.82 MB 2017-11-06
```

或者可以保存为 csv 或者 json 文件
```
C:\Users\chenjiandongx>torrent-cli -k 战狼2 -o movie.csv
```

#### 尝试了一下，支持各种正经的和有点不正经的资源！！！不信你试试！！！你会回来 star 的！！！
