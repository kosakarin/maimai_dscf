#该函数在/libraries/maimai_best_40.py下有，但是数值不对，需要修改
def computeRa(ds: float, achievement:float) -> int:
    baseRa = 14.0
    if achievement < 50:
        baseRa = 0
    elif achievement < 60:
        baseRa = 5.0
    elif achievement < 70:
        baseRa = 6.0
    elif achievement < 75:
        baseRa = 7.0
    elif achievement < 80:
        baseRa = 7.5
    elif achievement < 90:
        baseRa = 8.0
    elif achievement < 94:
        baseRa = 9.0
    elif achievement < 97:
        baseRa = 10.5
    elif achievement < 98:
        baseRa = 12.5
    elif achievement < 99:
        baseRa = 12.75
    elif achievement < 99.5:
        baseRa = 13.0
    elif achievement < 100:
        baseRa = 13.25
    elif achievement < 100.5:
        baseRa = 13.5

    return math.floor(ds * (min(100.5, achievement) / 100) * baseRa)


@sv.on_prefix('定数查分')
async def dscf(bot, ev: CQEvent):
    kw = ev.message.extract_plain_text().strip()
    
    arr = kw.split(' ')
    flag = len(arr)
    
    msg = ''

    if flag <= 0 or flag > 2:
        await bot.send(ev, "计算错误", at_sender=True)
    elif flag == 1:        
        try:
            ds = float(arr[0])
            msg += '歌曲定数' + arr[0] + '的各达成率对应底分为:\n'
            msg += 'SSS+: ' + str(computeRa(ds, 100.5)) + '\n'
            msg += 'SSSmax: ' + str(computeRa(ds, 100.4999)) + ', '
            msg += 'min: ' + str(computeRa(ds, 100.0)) + '\n'
            msg += 'SS+max: ' + str(computeRa(ds, 99.9999)) + ', '
            msg += 'min: ' + str(computeRa(ds, 99.5000)) + '\n'
            msg += 'SSmax: ' + str(computeRa(ds, 99.4999)) + ', '
            msg += 'min: ' + str(computeRa(ds, 99.0000)) + '\n'
            msg += 'S+max: ' + str(computeRa(ds, 98.9999)) + ', '
            msg += 'min: ' + str(computeRa(ds, 98.0000)) + '\n'
            msg += 'Smax: ' + str(computeRa(ds, 97.9999)) + ', '
            msg += 'min: ' + str(computeRa(ds, 97.0000))
            await bot.send(ev, msg, at_sender=True)
        except Exception as e:
            msg = '计算错误'
            await bot.send(ev, msg, at_sender=True)
            
    elif flag == 2:
        try:
            ds = float(arr[0])
            achievement = float(arr[1])
            msg += '歌曲定数' + arr[0] + '达成率' + arr[1] + '对应分数为:\n'
            msg += str(computeRa(ds, achievement))

            await bot.send(ev, msg, at_sender=True)
        except Exception as e:
            msg += '计算错误'
            await bot.send(ev, msg, at_sender=True)

@sv.on_rex(r'^(查分[绿黄红紫白]?)id ([0-9]+)')
async def query_chart_score(bot, ev:CQEvent):
    match = ev['match']
    level_labels = ['查分绿', '查分黄', '查分红', '查分紫', '查分白']
    
    try:
        level_index = level_labels.index(match.group(1))
        level_name = ['Basic', 'Advanced', 'Expert', 'Master', 'Re: MASTER']
        name = match.group(2)
        music = total_list.by_id(name)
        
        ds = music['ds'][level_index]
        level = music['level'][level_index]
        result = f'''{level_name[level_index]} {level}({ds})
对应达成率底分为：
SSS+: {computeRa(ds, 100.5)}
SSSmax: {computeRa(ds, 100.4999)}, min: {computeRa(ds, 100.000)}
SS+max: {computeRa(ds, 99.9999)}, min: {computeRa(ds, 99.5)}
SSmax: {computeRa(ds, 99.4999)}, min: {computeRa(ds, 99.0)}
S+max: {computeRa(ds, 98.9999)}, min: {computeRa(ds, 98.0)}
Smax: {computeRa(ds, 97.9999)}, min: {computeRa(ds, 97.0)}'''


        msg = f'''
{music["id"]}. {music["title"]}
[CQ:image,file=https://www.diving-fish.com/covers/{music["id"]}.jpg]
{result}'''
        await bot.send(ev, msg, at_sender=True)
    except:
        await bot.send(ev, '未找到该谱面', at_sender=True)



    
