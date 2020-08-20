import os

def new_file(test_dir):
    #列举test_dir目录下的所有文件（名），结果以列表形式返回。
    lists=os.listdir(test_dir)

    #sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
    #最后对lists元素，按文件修改时间大小从小到大排序。
    #获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    # print(lists)
    if len(lists) == 6:
        file_path = os.path.join(test_dir, lists[0])
        os.remove(file_path)
    file_path=os.path.join(test_dir,lists[-1])
    # print(file_path)
    return file_path
if __name__ == '__main__':
    a = new_file('D:\python3\接口自动化\禾贝\comm\email_html')
    print(a)
