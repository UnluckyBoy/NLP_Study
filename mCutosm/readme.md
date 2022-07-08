Run steps:
1、运行 build_vocab.py 建立词汇表
2、运行 resize.py
3、运行 train_Allfilter.py
4、运行 sample.py
(其中第四步要配置参数:--image ./png/xxx.jpg)

！！!图片文件命名必须为整数！！！
1、先修改：voc2coco.py中的PRE_DEFINE_CATEGORIES = {"xxx": 1, "xxx": 2,"xxx": 3}
2、在voc数据集目录下运行Powershell：python voc2coco.py E:\QF_Data\ImageData\labels E:\QF_Data\ImageData\labels\train.json
(其中E:\QF_Data\ImageData\labels为labels目录，E:\QF_Data\ImageData\labels\train.json为json生成目录)
<voc包括images和labels两个文件夹，使用labelImg工具(conda虚拟换下使用)生成>