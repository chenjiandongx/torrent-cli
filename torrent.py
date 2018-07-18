#!/usr/bin/env python
# coding=utf-8
from __future__ import division

import os
import re
import csv
import math
import argparse
import json
import codecs

import requests
from bs4 import BeautifulSoup, Comment


HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

VERSION = "VERSION 0.0.8"
DOMAIN = "http://www.btyunsou.co"


def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(description='Magnets-Getter CLI Tools.')
    parser.add_argument('keyword', metavar="KEYWORD", type=str, nargs="*",
                        help='magnet keyword.')
    parser.add_argument('-n', '--num', type=int, default=10,
                        help='magnet number.(default 10)')
    parser.add_argument('-s', '--sort-by', type=int, default=0,
                        help='0: Sort by date，1: Sort by size. 2: Sort by hot-rank.(default 0)')
    parser.add_argument('-o', '--output', type=str,
                        help='output file path, supports csv and json format.')
    parser.add_argument('-p', '--pretty-oneline', action='store_true',
                        help='show magnets info with one line.')
    parser.add_argument('-v', '--version', action='store_true',
                        help='version information.')
    return parser


def command_line_runner():
    """
    执行命令行操作
    """
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(VERSION)
        return

    if not args["keyword"]:
        parser.print_help()
    else:
        magnets = run(kw=args["keyword"],
                      num=args["num"], sort_by=args["sort_by"])
        if args["output"]:
            _output(magnets, args["output"])
        else:
            _print(magnets, args["pretty_oneline"])


def run(kw, num, sort_by):
    """
    爬虫入口

    :param kw: 资源名称
    :param num: 资源数量
    :param sort_by: 排序方式。0：按磁力时间排序，1：按文件大小排序 2：按磁力热度排序
    """
    print("Crawling data for you.....")
    _kw = "%20".join(kw)
    # 排序类型选择
    if sort_by == 0:
        sort_str = "ctime"
    elif sort_by == 1:
        sort_str = "length"
    elif sort_by == 2:
        sort_str = "click"
    else:
        raise ValueError("Unknown Sort Method")

    # 确保 num 有效
    if num < 0 or num > 200:
        num = 10
    # 每页最多 10 条磁力信息
    page = int(math.ceil(num / 10))
    magnets = []
    for p in range(1, page + 1):
        url = DOMAIN + "/search/{kw}_{s}_{p}.html".format(kw=_kw, s=sort_str, p=p)
        try:
            resp = requests.get(url, headers=HEADERS).text.encode("utf-8")
            try:
                bs = BeautifulSoup(resp, "lxml").find(
                    'ul', class_='media-list media-list-set').find_all('li')
                if not bs:
                    print("Sorry, found nothing :(")
                    return
                for b in bs:
                    _name = b.find(
                        class_='media-body').find('h4').find(
                        'a', class_='title').get_text(strip=True)
                    # 资源名称判断
                    is_name_found= False
                    name = _name.lower()
                    for n in kw:
                        if n.lower() in name:
                            is_name_found = True
                    if is_name_found:
                        item = b.find('div', class_='media-more')
                        time = item.find(class_='label label-success').text
                        size = item.find(class_='label label-warning').text
                        rank = item.find(class_='label label-primary').text
                        link = re.findall(
                            r'href="(.*?)">',
                            str(item.find(text=lambda text: isinstance(text, Comment))))[0]
                        magnets.append({
                            "magnet": link,             # 磁力链接
                            "magnet_name": name,        # 磁力名称
                            "magnet_date": time,        # 磁力日期
                            "magnet_size": size,        # 磁力大小
                            "magnet_rank": int(rank)    # 磁力热度
                        })
            except:
                pass
        except Exception as e:
            print(e)
    return sort_magnets(magnets, sort_by, num)


def sort_magnets(magnets, sort_by, num):
    """
    排序磁力

    :param magnets: 磁力列表
    :param sort_by: 排序方式
    """
    # 按日期排序，默认
    if sort_by == 0:
        _magnets = sorted(magnets,
                          key=lambda x: x["magnet_date"],
                          reverse=True)
    # 按大小排序，统一单位为 kb
    elif sort_by == 1:
        for m in magnets:
            unit = m["magnet_size"].split()
            if unit[1] == "GB":
                _size = float(unit[0]) * 1024 * 1024
            elif unit[1] == "MB":
                _size = float(unit[0]) * 1024
            else:
                _size = float(unit[0])
            m["magnet_size_kb"] = _size
        _magnets = sorted(magnets,
                          key=lambda x: x["magnet_size_kb"],
                          reverse=True)
    else:
        _magnets = sorted(magnets,
                          key=lambda x: x["magnet_rank"],
                          reverse=True)
    return _magnets[:num]


def _print(magnets, is_show_magnet_only):
    """
    在终端界面输出结果

    :param magnets: 磁力列表
    :param is_show_magnet_only: 单行输出
    """
    if not magnets:
        return
    if is_show_magnet_only:
        for row in magnets:
            print(row["magnet"], row["magnet_size"], row["magnet_date"])
    else:
        for row in magnets:
            try:
                print("磁链:", row["magnet"])
                print("名称:", row["magnet_name"])
                print("大小:", row["magnet_size"])
                print("日期:", row["magnet_date"])
                print("热度:", row["magnet_rank"], "\n")
            except:
                print("磁链:", row["magnet"])
                print("名称:", row["magnet_name"].encode('utf-8'))
                print("大小:", row["magnet_size"])
                print("日期:", row["magnet_date"])
                print("热度:", row["magnet_rank"], "\n")


def _output(magnets, path):
    """
    将数据保存到本地文件

    :param magnets: 磁力列表
    :param path: 文件路径，支持 csv 和 json 两种文件格式
    """
    if path:
        _, extension = os.path.splitext(path)
        if extension == ".csv":
            # 不兼容 Python2
            with open(path, mode="w+", encoding="utf-8-sig", newline="") as fout:
                fieldnames = (
                    "magnet",
                    "magnet_name",
                    "magnet_size",
                    "magnet_date",
                    "magnet_rank"
                )
                f_csv = csv.DictWriter(fout, fieldnames, extrasaction="ignore")
                f_csv.writeheader()
                f_csv.writerows(magnets)
            print("Save successfully!")
        elif extension == ".json":
            with codecs.open(path, mode="w+", encoding="utf-8") as f:
                json.dump(magnets, f, indent=2)
            print("Save successfully!")
        else:
            print("Failed to save the file!")


if __name__ == "__main__":
    command_line_runner()
