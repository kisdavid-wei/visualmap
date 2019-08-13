# 视觉地图
把地址通过视觉化的方式呈现在地图上。

# 准备工作
1.在高德地图API中申请APIKey，用APIKey替换/visualmap/spiders/gaode.py 和 /templates/map.html 里面的yourgaodekey
2. 把需要展现的地址放在addresses.txt文件里面
3. 运行scrapy crawl gaode
4. 运行python map.py
