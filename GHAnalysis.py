import sys,getopt,json,os

#批量读取json文件 初始化
def read_json(path):
    data=[]
    filelist = os.listdir(path)#读取文件列表
    f2=open('data.json','w',encoding='utf-8')
    for file in filelist:#读json文件
        pathname=path+'\\'+file
        with open(pathname,encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line))
                f2.write(line)

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
    opt2,arv2= getopt.getopt(sys.argv[1:],'i:u:r:e:',['user=','repo=','event=','init='])
    #初始化
    if opt2[0][0] == '-i' or opt2[0][0] == '--init':
        read_json(opt2[0][1])
        exit()
    else:#数据读取
        with open('data.json',encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line))
    #查询信息
    for i in range(0,len(opt2)):
        if '--user' == opt2[i][0]:
            username=opt2[i][1]
            continue
        else:
            pass
        if '-u' == opt2[i][0]:
            username=opt2[i][1]
            continue
        else:
            pass
        if '--repo' == opt2[i][0]:
            repo=opt2[i][1]
            continue
        else:
            pass
        if '-r' == opt2[i][0]:
            repo=opt2[i][1]
            continue
        else:
            pass
        if '--event' == opt2[i][0]:
            event=opt2[i][1]
            continue
        else:
            pass
        if '-e' == opt2[i][0]:
            event=opt2[i][1]
            continue
        else:
            pass
    #查询
    print(caculate_ans(data,username,repo,event))
