import os

def get_report():
    result_dir = 'F:\\Unittest\\report'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getatime(result_dir+'\\'+fn))
    #print('最新报告：'+lists[-1])
    file = os.path.join(result_dir,lists[-1])
    #print(file)
    return [file,lists[-1]]

if __name__ == '__main__':
    print(get_report())