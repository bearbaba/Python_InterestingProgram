## 飞机大战pygame的学习使用
###1.游戏思路
首先需要导入pygame模块  
pygame.init()`表示加载pygame所需要的内容，同时也意味着游戏程序的加载  
同时`pygame.quit()`表示游戏结束  

游戏首先需要进行生成游戏窗口对象，这里使用的是：`screen=pygame.display.set_mode(resolution=(0,0),flags=0)`  
参数`reslution`是一个元组类型，表示游戏窗口的大小，`falgs`表示是否需要全屏，默认不全屏  
然后加载背景图，加载图片操作为`bg=pygame.load(./img/bg.jpg)`  
要将图片绘制到窗口上需要执行，`screen.blit(bg,(0,0))`第二个参数是一个元组，表示图片左上角加载到窗口的坐标  
每次在游戏窗口上需要有新的操作时，都需要刷新一下窗口，刷新命令是`pygame.display.update()`