# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： test3.py
    @date：2023/12/15 15:10
    
"""
input_string = "01 样样红 黄安 妹妹我爱你 6fflpoac https://webfs.hw.kugou.com/202312141531/0bad3cc9ff6bc854e87bd04fc654afb3/v2/29343942c40d6a662adcf6fc5e55fcc6/G373/M00/EB/3D/VZUEAGU8XH6AAe5fAD0zyrsWTnE692.mp3"

# 使用空格拆分字符串并转换为列表
parts = input_string.split()
print(len(parts))
# 按顺序排序列表
ordered_list = sorted(parts,key=lambda x:len(x))

# 输出有序的列表集合
print(ordered_list)