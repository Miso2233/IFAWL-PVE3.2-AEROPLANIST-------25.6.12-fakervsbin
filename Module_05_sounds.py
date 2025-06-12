import os,winsound

assert os.path.exists("sound") , "sound路径不存在>>此模块可能来自高版本的未知IFAWL|sound文件夹可能被删除"

sound_assets = {} #dict[文件名|str,文件路径|str]
for filename in os.listdir("sound"):
    if filename.lower().endswith('.wav'):
        name = os.path.splitext(filename)[0] 
        filepath = os.path.join("sound", filename)
        if os.path.isfile(filepath):
            sound_assets[name] = filepath

_current_loops = set()

def play_sound(name, async_play=True, loop=False):
    """
    播放指定名称的音效
    :param name: 音效名称
    :param async_play: 是否异步播放 (循环播放时自动强制异步)
    :param loop: 是否循环播放
    """
    if not sound_assets:
        print("音效不可用：未找到音效资源")
        return
    
    filepath = sound_assets.get(name)
    if not filepath:
        print(f"音效 '{name}' 不存在")
        return
    
    try:
        flags = winsound.SND_FILENAME
        
        if loop:
            # 循环播放必须使用异步模式
            flags |= winsound.SND_LOOP | winsound.SND_ASYNC
            _current_loops.add(name)
        else:
            if async_play:
                flags |= winsound.SND_ASYNC

        winsound.PlaySound(filepath, flags)
    except Exception as e:
        print(f"播放音效 '{name}' 失败：{str(e)}")
        _current_loops.discard(name)

def stop_sound(name=None):
    """
    停止指定音效的播放 (仅对循环播放有效)
    :param name: 要停止的音效名称，None表示停止所有
    """
    try:
        if name is None:
            winsound.PlaySound(None, winsound.SND_PURGE)
            _current_loops.clear()
        elif name in _current_loops:
            winsound.PlaySound(None, winsound.SND_PURGE)
            _current_loops.discard(name)
    except Exception as e:
        print(f"停止音效失败：{str(e)}")