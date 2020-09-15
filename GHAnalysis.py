import sys,getopt,json,os

#批量读取json文件 初始化
def read_json(path):
    filelist = os.listdir(path)#读取文件列表
    f2=open('data.json','w',encoding='utf-8')
    for file in filelist:#读json文件
        pathname=path+'\\'+file
        with open(pathname,encoding='utf-8') as f:
            for line in f:
                f2.write(line)#写入data.json
    return

#获得答案
def caculate_ans(data,username,repo,event):
    ans=0
    for da in data:
        if not len(username)==0:#判断有无username
            if not username==da['actor']['login']:
                continue
            else:
                pass
        else:
            pass
        if not len(repo)==0:#判断有无repo
            if not repo==da['repo']['name']:
                continue
            else:
                pass
        else:
            pass
        #判断项目
        if da['type'] == event:
                ans=ans+1
        else:
            pass
    return ans

if __name__ == '__main__':
    #参数
    data=[]
    username=''
    repo=''
    event=''
    #命令参数
    opt,arv= getopt.getopt(sys.argv[1:],'i:u:r:e:',['user=','repo=','event=','init='])
    #初始化
    if opt in ("-i" , "--init"):
        read_json(opt[0][1])
        print(0)
        exit()
    else:#数据读取
        with open('data.json', encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line))
    #查询信息
    for o,a in opt:
        if o in ("-u","--user"):
            username = a
        elif o in("-r","--repo"):
            repo = a
        elif o in ("-e","--event"):
            event = a
    #查询
    print(caculate_ans(data , username , repo , event))
