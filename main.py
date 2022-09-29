# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

from googletrans import Translator

dest_lang_list = [
    ('en', 'english', '英语'),
    ('ja', 'japanese', '日语'),
    ('zh-tw', 'chinese (traditional)', '中文-繁体')
]

srcFilePath = 'captions.sbv'
srcTitleFilePath = 'title_and_desc.sbv'
destTitleFilePath = 'title_and_desc_所有语种.sbv'
destFileFormat = 'captions_{}.sbv'
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
    dest_file_path = destFileFormat.format(dest_lang)
    delFileIsExist(dest_file_path)
    dest_file = open(dest_file_path, 'x')
    for dest_tup in dest_tup_list:
        dest_file.write(dest_tup[0] + '\n')
        dest_file.write(dest_tup[1] + '\n\n')
    dest_file.close()


def transFileToMultiLang(dest_list):
    if len(dest_list) == 0:
        return
    src_tup_list = getFromFile(srcFilePath)
    if len(src_tup_list) == 0:
        return
    for dest in dest_list:
        dest_tup_list = batchTranslateForTup(src_tup_list, dest[0])
        genSrcFileByTup(dest_tup_list, dest[2])


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


def translateTitleAndDesc(title, desc, dest_lang):
    title_t = translator.translate(title, dest=dest_lang)
    desc_t = translator.translate(desc, dest=dest_lang)
    return title_t.text, desc_t.text


def transTitleFileToMultiLang(dest_list):
    if len(dest_list) == 0:
        return
    title, desc = getTitleAndDescFromFile(srcTitleFilePath)
    if title == '' or desc == '':
        return
    delFileIsExist(destTitleFilePath)
    dest_title_file = open(destTitleFilePath, 'x')
    for dest in dest_list:
        dest_title_file.write('========================{}========================\n'.format(dest[2]))
        title_dest, desc_dest = translateTitleAndDesc(title, desc, dest[0])
        dest_title_file.write(title_dest + '\n')
        dest_title_file.write('------------------------描述-----------------------')
        dest_title_file.write(desc_dest + '\n\n')
    dest_title_file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transFileToMultiLang(dest_lang_list)
    transTitleFileToMultiLang(dest_lang_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
