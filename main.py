# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import argparse
import datetime
import time

from googletrans import Translator

dest_lang_list_test = [
    ('en-us', 'en-us', '英语（美国）', 68),
    ('en-uk', 'en-uk', '英语（英国）', 69),
    ('en-za', 'en-za', '英语（印度）', 70),
]

dest_lang_list = [
    ('sq', 'albanian', '阿尔巴尼亚语', 0),
    ('ar', 'arabic', '阿拉伯语', 1),
    ('am', 'amharic', '阿姆哈拉语', 2),
    ('as', 'assamese', '阿萨姆语', 3),
    ('az', 'azerbaijani', '阿塞拜疆语', 4),
    ('et', 'estonian', '爱沙尼亚语', 5),
    ('or', 'odia', '奥里亚语', 6),
    ('eu', 'basque', '巴斯克语', 7),
    ('be', 'belarusian', '白俄罗斯语', 8),
    ('bg', 'bulgarian', '保加利亚语', 9),
    ('is', 'icelandic', '冰岛语', 10),
    ('pl', 'polish', '波兰语', 11),
    ('bs', 'bosnian', '波斯尼亚语', 12),
    ('fa', 'persian', '波斯语', 13),
    ('da', 'danish', '丹麦语', 14),
    ('de', 'german', '德语', 15),
    ('ru', 'russian', '俄语', 16),
    ('fr', 'french', '法语', 17),
    ('tl', 'filipino', '菲律宾语', 18),
    ('fi', 'finnish', '芬兰语', 19),
    ('km', 'khmer', '高棉语', 20),
    ('ka', 'georgian', '格鲁吉亚语', 21),
    ('kk', 'kazakh', '哈萨克语', 22),
    ('ko', 'korean', '韩语', 23),
    ('nl', 'dutch', '荷兰语', 24),
    ('gl', 'galician', '加利西亚语', 25),
    ('ca', 'catalan', '加泰罗尼亚语', 26),
    ('cs', 'czech', '捷克语', 27),
    ('kn', 'kannada', '卡纳达语', 28),
    ('hr', 'croatian', '克罗地亚语', 29),
    ('lv', 'latvian', '拉脱维亚语', 30),
    ('lo', 'lao', '老挝语', 31),
    ('lt', 'lithuanian', '立陶宛语', 32),
    ('ro', 'romanian', '罗马尼亚语', 33),
    ('mr', 'marathi', '马拉地语', 34),
    ('ml', 'malayalam', '马拉雅拉姆语', 35),
    ('ms', 'malay', '马来语', 36),
    ('mk', 'macedonian', '马其顿语', 37),
    ('mn', 'mongolian', '蒙古语', 38),
    ('bn', 'bengali', '孟加拉语', 39),
    ('my', 'myanmar (burmese)', '缅甸语', 40),
    ('ne', 'nepali', '尼泊尔语', 41),
    ('no', 'norwegian', '挪威语', 42),
    ('pa', 'punjabi', '旁遮普语', 43),
    ('pt', 'portuguese', '葡萄牙语', 44),
    ('ja', 'japanese', '日语', 45),
    ('sv', 'swedish', '瑞典语', 46),
    ('sr', 'serbian', '塞尔维亚语', 47),
    ('si', 'sinhala', '僧伽罗语', 48),
    ('sk', 'slovak', '斯洛伐克语', 49),
    ('sl', 'slovenian', '斯洛文尼亚语', 50),
    ('sw', 'swahili', '斯瓦希里语', 51),
    ('te', 'telugu', '泰卢固语', 52),
    ('ta', 'tamil', '泰米尔语', 53),
    ('th', 'thai', '泰语', 54),
    ('tr', 'turkish', '土耳其语', 55),
    ('ur', 'urdu', '乌尔都语', 56),
    ('uk', 'ukrainian', '乌克兰语', 57),
    ('uz', 'uzbek', '乌兹别克语', 58),
    ('es', 'spanish', '西班牙语', 59),
    ('iw', 'hebrew', '希伯来语', 60),
    ('el', 'greek', '希腊语', 61),
    ('hu', 'hungarian', '匈牙利语', 62),
    ('hy', 'armenian', '亚美尼亚语', 63),
    ('it', 'italian', '意大利语', 64),
    ('hi', 'hindi', '印地语', 65),
    ('id', 'indonesian', '印度尼西亚语', 66),
    ('en', 'english', '英语', 67),
    ('en-us', 'en-us', '英语（美国）', 68),
    ('en-uk', 'en-uk', '英语（英国）', 69),
    ('en-za', 'en-za', '英语（印度）', 70),
    ('vi', 'vietnamese', '越南语', 71),
    ('af', 'afrikaans', '南非荷兰语', 100),
    ('ceb', 'cebuano', '宿务', 101),
    ('ny', 'chichewa', '奇切瓦', 102),
    ('zh-cn', 'chinese (simplified)', '简体中文', 103),
    ('zh-tw', 'chinese (traditional)', '繁体中文', 104),
    ('co', 'corsican', '科西嘉岛', 105),
    ('eo', 'esperanto', '世界语', 106),
    ('fy', 'frisian', '弗里斯兰语', 107),
    ('gu', 'gujarati', '古吉拉特语', 108),
    ('ht', 'haitian(creole)', '海地克里奥尔语', 109),
    ('ha', 'hausa', '豪萨', 110),
    ('haw', 'hawaiian', '夏威夷语', 111),
    ('he', 'hebrew', '希伯来语', 112),
    ('hmn', 'hmong', '苗族', 113),
    ('ig', 'igbo', '伊博', 114),
    ('ga', 'irish', '爱尔兰语', 115),
    ('jw', 'javanese', '爪哇语', 116),
    ('ku', 'kurdish (kurmanji)', '库尔德语（kurmanji）', 117),
    ('ky', 'kyrgyz', '吉尔吉斯斯坦', 118),
    ('la', 'latin', '拉丁', 119),
    ('lb', 'luxembourgish', '卢森堡语', 120),
    ('mg', 'malagasy', '马尔加什', 121),
    ('mt', 'maltese', '马耳他语', 122),
    ('mi', 'maori', '毛利语', 123),
    ('or', 'odia', '奥里亚语', 124),
    ('ps', 'pashto', '普什图语', 125),
    ('sm', 'samoan', '萨摩亚语', 126),
    ('gd', 'scots (gaelic)', '苏格兰盖尔语', 127),
    ('st', 'sesotho', '塞索托', 128),
    ('sn', 'shona', '绍纳', 129),
    ('sd', 'sindhi', '信德', 130),
    ('so', 'somali', '索马里', 131),
    ('su', 'sundanese', '巽他语', 132),
    ('tg', 'tajik', '塔吉克', 133),
    ('ug', 'uyghur', '维吾尔族', 134),
    ('cy', 'welsh', '威尔士语', 135),
    ('xh', 'xhosa', '科萨', 136),
    ('yi', 'yiddish', '意第绪语', 137),
    ('yo', 'yoruba', '约鲁巴', 138),
    ('zu', 'zulu', '祖鲁', 139),
]

dest_lang_you_want = [
    '阿尔巴尼亚语',
    '阿拉伯语',
    '阿姆哈拉语',
    '阿萨姆语',
    '阿塞拜疆语',
    '爱沙尼亚语',
    '奥里亚语',
    '巴斯克语',
    '白俄罗斯语',
    '保加利亚语',
    '冰岛语',
    '波兰语',
    '波斯尼亚语',
    '波斯语',
    '丹麦语',
    '德语',
    '俄语',
    '法语',
    '菲律宾语',
    '芬兰语',
    '高棉语',
    '格鲁吉亚语',
    '哈萨克语',
    '韩语',
    '荷兰语',
    '加利西亚语',
    '加泰罗尼亚语',
    '捷克语',
    '卡纳达语',
    '克罗地亚语',
    '拉脱维亚语',
    '老挝语',
    '立陶宛语',
    '罗马尼亚语',
    '马拉地语',
    '马拉雅拉姆语',
    '马来语',
    '马其顿语',
    '蒙古语',
    '孟加拉语',
    '缅甸语',
    '尼泊尔语',
    '挪威语',
    '旁遮普语',
    '葡萄牙语',
    '日语',
    '瑞典语',
    '塞尔维亚语',
    '僧伽罗语',
    '斯洛伐克语',
    '斯洛文尼亚语',
    '斯瓦希里语',
    '泰卢固语',
    '泰米尔语',
    '泰语',
    '土耳其语',
    '乌尔都语',
    '乌克兰语',
    '乌兹别克语',
    '西班牙语',
    '希伯来语',
    '希腊语',
    '匈牙利语',
    '亚美尼亚语',
    '意大利语',
    '印地语',
    '印度尼西亚语',
    '英语',
    '英语（美国）',
    '英语（英国）',
    '英语（印度）',
    '越南语'
]

srcFilePathDefault = 'captions.sbv'
srcTitleFilePathDefault = 'title.sbv'
destTitleFilePathFmt = '{}_title.md'
destFileFmt = '{:03d}_{}.sbv'
translator = Translator()


def getFromFile(path):
    src_file = open(path, 'r')
    file_content = src_file.read()
    group_list = file_content.split('\n\n')
    src_tup_list = []
    for group in group_list:
        time_and_text = group.split('\n')
        if len(time_and_text) >= 2:
            src_tup_list.append((
                time_and_text[0],
                time_and_text[1],
            ))
    return src_tup_list


def getTitleAndDescFromFile(path):
    src_file = open(path, 'r')
    file_content = src_file.read()
    title_and_content_mix = file_content.split('\n\n')
    if len(title_and_content_mix) < 2:
        return '', ''
    title = title_and_content_mix[0]
    desc = '\n\n'.join(title_and_content_mix[1:])
    return title, desc


def delFileIsExist(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)


def genSrcFileByTup(dest_tup_list, dest_lang):
    dest_file_path = destFileFmt.format(dest_lang[3], dest_lang[2])
    delFileIsExist(dest_file_path)
    dest_file = open(dest_file_path, 'x')
    for dest_tup in dest_tup_list:
        dest_file.write(dest_tup[0] + '\n')
        dest_file.write(dest_tup[1] + '\n\n')
    dest_file.close()


def transFileToMultiLang(content_src_file_path, dest_list, package_name):
    print('开始执行内容翻译, 源文件路径:{}, 要翻译的语言数量:{}, 打包后的文件名称:{}_content.zip'.format(content_src_file_path, len(dest_list),
                                                                            package_name))
    # 删除原来的垃圾文件
    os.popen('rm -f 0*.sbv')
    os.popen('rm -rf {}'.format(package_name))
    os.popen('rm -rf {}_content.zip'.format(package_name))
    time.sleep(3)

    if len(dest_list) == 0:
        return
    src_tup_list = getFromFile(content_src_file_path)
    if len(src_tup_list) == 0:
        return
    for dest in dest_list:
        if dest[3] >= 100:
            continue
        dest_tup_list = batchTranslateForTup(src_tup_list, dest[0])
        genSrcFileByTup(dest_tup_list, dest)

    time.sleep(5)
    # 打包
    os.popen('mkdir {}'.format(package_name))
    time.sleep(1)
    os.popen('mv 0*.sbv {}'.format(package_name))
    time.sleep(1)
    zip_out = os.popen('zip -r {}_content.zip {}'.format(package_name, package_name)).read()
    print(zip_out)
    mv_out = os.popen('mv {}_content.zip ~/Downloads'.format(package_name)).read()
    print(mv_out)
    print('完成内容的翻译，路径:~/Downloads/{}_content.zip'.format(package_name))
    os.popen('rm -rf {}'.format(package_name))


def get_text_from_tup_list(src_tup_list):
    src_tup_text_list = []
    for src_tup in src_tup_list:
        src_tup_text_list.append(src_tup[1])
    return src_tup_text_list


def batchTranslateForTup(src_tup_list, desc_lang):
    src_do_trans_text_list = get_text_from_tup_list(src_tup_list)
    dest_text_map = batchTranslate(src_do_trans_text_list, desc_lang)
    dest_tup_list = []
    for src_tup in src_tup_list:
        dest_tup_list.append((
            src_tup[0], dest_text_map[src_tup[1]]
        ))
    return dest_tup_list


def batchTranslate(src_list, dest_lang):
    dest_text_map = dict()
    src_text = '\n'.join(src_list)
    t = translator.translate(src_text, dest=dest_lang)
    dest_text_list = t.text.split('\n')
    for i in range(len(src_list)):
        dest_text_map[src_list[i]] = dest_text_list[i]
    #
    #
    # for src in src_list:
    #     t = translator.translate(src, dest=dest_lang)
    #     dest_text_map[t.origin] = t.text
    return dest_text_map


def singleTranslate(src, dest_lang):
    t = translator.translate(src, dest=dest_lang)
    return t.text


def translateTitleAndDesc(title, desc, dest_lang):
    title_t = translator.translate(title, dest=dest_lang)
    desc_t = translator.translate(desc, dest=dest_lang)
    return title_t.text, desc_t.text


def transTitleFileToMultiLang(title_src_file_path, dest_list, package_name):
    if len(dest_list) == 0:
        return
    title, desc = getTitleAndDescFromFile(title_src_file_path)
    if title == '' or desc == '':
        return
    title_file_name = destTitleFilePathFmt.format(package_name)
    print('开始执行标题翻译, 源文件路径:{}, 要翻译的语言数量:{}, 目标文件名称:{}'.format(title_src_file_path, len(dest_list), title_file_name))
    delFileIsExist(title_file_name)
    dest_title_file = open(title_file_name, 'x')
    for dest in dest_list:
        if dest[3] >= 100:
            continue
        dest_title_file.write('### {:02d}-{}\n'.format(dest[3], dest[2]))
        title_dest, desc_dest = translateTitleAndDesc(title, desc, dest[0])
        dest_title_file.write('```' + '\n')
        dest_title_file.write(title_dest + '\n')
        dest_title_file.write('```' + '\n')
        dest_title_file.write('```' + '\n')
        dest_title_file.write(desc_dest + '\n')
        dest_title_file.write('```' + '\n\n')
    dest_title_file.close()

    time.sleep(1)
    os.popen('mv {} ~/Downloads'.format(title_file_name))
    print('完成标题的翻译，路径:~/Downloads/{}'.format(title_file_name))


def print_without():
    i_have = []
    for d in dest_lang_list:
        i_have.append(d[2])
    for y in dest_lang_you_want:
        if y not in i_have:
            print(y + '\n')


def print_order():
    other_start = 100
    index_to_tup = dict()
    for i in range(len(dest_lang_you_want)):
        you_want = dest_lang_you_want[i]
        for i_have in dest_lang_list:
            if i_have[2] == you_want:
                index_to_tup[i] = i_have
                break
    for index in index_to_tup.keys():
        print("('{}', '{}', '{}', {}),".format(index_to_tup[index][0], index_to_tup[index][1], index_to_tup[index][2],
                                               index))
    for tup in dest_lang_list:
        if tup not in index_to_tup.values():
            print("('{}', '{}', '{}', {}),".format(tup[0], tup[1], tup[2], other_start))
            other_start = other_start + 1


def print_you_want_order():
    for i in range(len(dest_lang_you_want)):
        print("{:03d} {}".format(i, dest_lang_you_want[i]))


def quickTransLineMultiLang(line, dest_list):
    for dest in dest_list:
        if dest[3] >= 100:
            continue
        text = singleTranslate(line, dest[0])
        print('{:02d}-{}: {}'.format(dest[3], dest[2], text))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='翻译使用，示例运行：python3 /Users/bytedance/PycharmProjects/google_translate'
                                                 '/main.py -f 2 -n 搞了个蛋糕的标题 -s title.sbv -t t')
    parser.add_argument('--test', '-t', type=bool, help='测试语言', default=False, required=False)
    parser.add_argument('--func', '-f', type=str, nargs='+', help='1：翻译内容；2翻译标题；或者直接输入内容', default=['1'])
    parser.add_argument('--name', '-n', type=str, help='生成文件的名称', required=False)
    parser.add_argument('--source', '-s', type=str, help='源文件', required=False)
    args = parser.parse_args()

    d = dest_lang_list
    # 使用测试
    if args.test:
        d = dest_lang_list_test

    # 文件名
    today = datetime.datetime.today()
    name = '{}-{}-{}_{}_{}'.format(today.year, today.month, today.day, today.hour, today.minute)
    if args.name:
        name = args.name

    # 翻译内容
    if args.func == ['1']:
        # 源文件
        src_file_path = '{}/{}'.format(os.getcwd(), srcFilePathDefault)
        if args.source:
            src_file_path = '{}/{}'.format(os.getcwd(), args.source)
        transFileToMultiLang(src_file_path, d, name)
    # 标题和描述
    elif args.func == ['2']:
        # 源文件
        src_file_path = '{}/{}'.format(os.getcwd(), srcTitleFilePathDefault)
        if args.source:
            src_file_path = '{}/{}'.format(os.getcwd(), args.source)
        transTitleFileToMultiLang(src_file_path, d, name)
    else:
        content = ' '.join(args.func)
        quickTransLineMultiLang(content, d)

    # print_without()
    # print_order()
    # print_you_want_order()
    # transFileToMultiLang(dest_lang_list)
    # transTitleFileToMultiLang(dest_lang_list)
