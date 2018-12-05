# coding=utf-8
import os
from chardet.universaldetector import UniversalDetector
import codecs

ROOT_PATH = "some_absolute_path"
SUFFIX_LIST = [".java"]
SOURCE_ENCODING_LIST = ["gbk", "gb2312", "gb18030"]
TARGET_ENCODING = "utf-8"

detector = UniversalDetector()

def get_encoding(filepath):
    with open(filepath, mode="r") as a_file:
        detector.reset()
        for line in a_file:
            detector.feed(line)
            if detector.done: break
        detector.close()
        return detector.result['encoding']

def change_encoding(source_path, target_path, source_encoding, target_encoding):
    BLOCKSIZE = 1048576
    with codecs.open(source_path, "r", source_encoding) as source_file:
        with codecs.open(target_path, "w", target_encoding) as target_file:
            while True:
                contents = source_file.read(BLOCKSIZE)
                if not contents:
                    break
                target_file.write(contents)


if __name__ == '__main__':

    SUFFIX_LIST = [suffix.lower() for suffix in SUFFIX_LIST]
    SOURCE_ENCODING_LIST = [encoding.lower() for encoding in SOURCE_ENCODING_LIST]
    TARGET_ENCODING = TARGET_ENCODING.lower()

    for root, dirs, files in os.walk(ROOT_PATH):

        if not root.endswith("/"):
            root = root + "/"

        for name in files:

            need_change = False
            for suffix in SUFFIX_LIST:
                if name.lower().endswith(suffix):
                    need_change = True
                    break

            if not need_change:
                continue

            fullpath = root + name
            encoding = get_encoding(fullpath)

            if encoding == None:
                print "detect encoding of [%s] failed" % (fullpath)
                continue

            if encoding.lower() not in SOURCE_ENCODING_LIST:
                continue

            print "change encoding of [%s] from [%s] to [%s]: " % (fullpath, encoding, TARGET_ENCODING),
            fullpath_bak = fullpath + ".bak"
            os.rename(fullpath, fullpath_bak)
            change_encoding(fullpath_bak, fullpath, encoding, TARGET_ENCODING)
            os.remove(fullpath_bak)
            print "SUCCESS!"
