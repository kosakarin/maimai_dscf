# maimai_dscf
基于hoshinobot的maimaiDX插件原有功能上修改出的一个直接给出歌曲定数达成率对应底分的补充

# 更新日志
10.08 适配了一波最新的含有b50功能（把括号内的False改为True的话可以得到sp分数哦）

# 原项目地址
你都找到这个项目了还不知道原项目地址？（不是

https://github.com/Yuri-YuzuChaN/maimaiDX

# 使用方法：

首先你得装了maimaiDX插件

然后打开maimai.py

把代码复制进去（


# 使用例：
## 指定定数查询全部达成度下的底分
实际只能查高于S的（大嘘

格式：[定数查分][浮点数(整数也行)]

--定数查分 14.4

--@sender 歌曲定数14.4的各达成率对应底分为:

SSS+: 202

SSSmax: 195, min: 194

SS+max: 190, min: 189

SSmax: 186, min: 185

S+max: 181, min: 179

Smax: 176, min: 174

## 指定定数和达成率查询此时底分
格式：[定数查分][浮点数(整数也行)][空格][浮点数(整数也行)]

--定数查分 14.4 97.012

--@sender 歌曲定数14.4达成率97.012对应分数为:

174


## 指定歌曲难度和ID查询此歌曲的各达成率对应底分
格式：[查分绿|黄|红|紫|白id][空格][歌曲ID号]

--查分紫id 363

--@sender

/song_cover_img

363. Oshama Scramble! Master 14(14.2)

对应达成率底分为：

SSS+: 199

SSSmax: 192, min: 191

SS+max: 188, min: 187

SSmax: 183, min: 182

S+max: 179, min: 177

Smax: 173, min: 172
