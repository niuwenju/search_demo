# encoding=utf-8
import jieba

seg_list = jieba.cut_for_search("狮子王")
print("Full Mode: " + "/ ".join(seg_list))  # 全模式