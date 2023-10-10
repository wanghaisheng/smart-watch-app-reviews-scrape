#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import urllib.request
import re
import xlsxwriter
import json
import os


def getHTMLText(url):
    response = urllib.request.urlopen(url)
    myjson = json.loads(response.read().decode())

    return myjson

    # try:
    #     r = requests.get(url)
    #     r.raise_for_status()
    #     r.encoding = r.apparent_encoding
    #     return r.text
    # except:
    #     return ''


def main():

    try:
    # https://apps.apple.com/us/app/indycar/id606905722
    #     https://apps.apple.com/us/app/capcut-video-editor/id1500855883
    #https://apps.apple.com/cn/app/妙健康-健康管理平台/id841386224?l=ru&see-all=reviews
    #https://apps.apple.com/cn/app/%E5%A6%99%E5%81%A5%E5%BA%B7-%E5%81%A5%E5%BA%B7%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0/id841386224?l=ru&see-all=reviews
        apple_app_package_url = os.getenv('apple_app_package_url').strip()
        if 'https://apps.apple.com' in apple_app_package_url:
            if '?' in apple_app_package_url:
                apple_app_package_url=apple_app_package_url.split('?')[0]

            appName=apple_app_package_url.split('/')[-2]
            appid=apple_app_package_url.split('/')[-1]
            if not len(appName)>0:
                print('not support package,',apple_app_package_url,appName)        
    except:
        apple_app_package_name='capcut-video-editor'

#     appid = input("请输入应用id号:")
#     appName = input("请输入应用名称:")

    if not os.path.exists(appid):
        os.system('mkdir ' + appid)

    workbook = xlsxwriter.Workbook(appid + '/' + appName + '_comments.xlsx')
    worksheet = workbook.add_worksheet()
    format = workbook.add_format()
    format.set_border(1)
    format.set_border(1)
    format_title = workbook.add_format()
    format_title.set_border(1)
    format_title.set_bg_color('#cccccc')
    format_title.set_align('left')
    format_title.set_bold()
    title = ['作者', '标题', '评论内容', '版本', '评级', '投票']

    # 设置单元格宽度
    worksheet.set_column(0, 0, 30)
    worksheet.set_column(1, 1, 40)
    worksheet.set_column(2, 2, 100)
    worksheet.set_column(3, 3, 10)
    worksheet.set_column(4, 4, 10)
    worksheet.set_column(5, 5, 10)

    worksheet.write_row('A1', title, format_title)

    count = 0

    total = 10
    totalCount = 0
    for n in range(total):
        url = 'https://itunes.apple.com/rss/customerreviews/page=' + \
            str(n+1) + '/id=' + str(appid) + \
            '/sortby=mostrecent/json?l=en&&cc=kh'

        print('当前地址：' + url)

        jsonText = getHTMLText(url)

        fileName = appid + '/' + str(n+1) + '.json'

        data_feed = jsonText['feed']
        entry = data_feed['entry']
        for i in range(len(entry)):
            value = entry[i]
            fixedIndex = i + 1
            startRow = totalCount + 1
            worksheet.write(
                startRow, 0, value['author']['name']['label'], format)
            worksheet.write(startRow, 1, value['title']['label'], format)
            worksheet.write(startRow, 2, value['content']['label'], format)
            worksheet.write(
                startRow, 3, value['im:version']['label'], format)
            worksheet.write(
                startRow, 4, value['im:rating']['label'], format)
            worksheet.write(
                startRow, 5, value['im:rating']['label'], format)
            totalCount = totalCount + 1

        with open(fileName, 'w') as file:
            file.write(json.dumps(jsonText, sort_keys=True,
                                  indent=4, ensure_ascii=False))

        count = count + 1
        print("当前进度: {:.2f}%".format(count * 100 / total), end="\n\n")

    workbook.close()


if __name__ == '__main__':
    main()
