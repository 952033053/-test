import os
def result_path():
    # test_dir = os.path.dirname(os.path.abspath(__file__))
    # print(test_dir)
    #D:\python3\接口自动化\禾贝\comm\email_html
    a = os.getcwd()
    # print(a)
    path = os.path.join(a, "comm", "email_html")
    # print(path)
    return path


if __name__ == '__main__':
    a = result_path()
