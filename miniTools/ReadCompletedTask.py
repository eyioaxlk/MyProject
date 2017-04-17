#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re


# 切换路径
os.chdir(r'/Users/yexiao/Dropbox/Todoist/Completed Tasks')

# 判断文件是否存在
if not os.path.exists('completed_todoist_tasks.txt'):
    print('文件不存在！')
else:
    with open('completed_todoist_tasks.txt', 'r') as task_txt:
        tasks = task_txt.read()

        # 分割
        tasks = tasks.split('\n\n')
        # print(tasks)

        each_task_dict = {}
        for each_task in tasks:
            # print(each_task)

            if each_task.find('Completed At') > 0:
                each_task_list = each_task.split('\n')
                for each_task_list_item in each_task_list:
                    each_task_dict = {}
                    each_task_list_item_d = each_task_list_item.split(':', maxsplit=1)
                    each_task_dict[each_task_list_item_d[0]] = each_task_dict[each_task_list_item_d[1]]
            else:
                each_task_list_item_d = each_task.split(':', maxsplit=1)
                each_task_dict[each_task_list_item_d[0]] = each_task_dict[each_task_list_item_d[1]]

            print(each_task_dict)


            # print(each_task_list)

        """
        task = task_txt.readlines()
        task_dic = {}
        task_dic_l = {}
        task_num = 0
        while len(task):

            # task_dic_l = {}
            # task_item = task.pop()
            if task[-1] != '\n':
                task_split = task[-1].split(':', maxsplit=1)
                task_dic_l[task_split[0]] = task_split[1]
                task.pop()
            else:
                task_dic['task_%s' % str(task_num)] = task_dic_l
                task_num += 1
                task.pop()
                task_dic_l = {}

        # print(task_dic)


for each_task in task_dic.values():
    try:
        print('任务名称：%s；完成时间：%s' % (each_task['Task content'].replace('\n',''),each_task['Completed At'].replace('\n','')))
    except:
        print('ss')
    """





