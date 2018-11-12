# -*- coding: utf-8 -*-

import os
from misc import Option
import json
from collections import OrderedDict

## 주의!!!!  myconfig.json 파일은 개발환경별로 각각 세팅되는 환경설정이므로,
## 절대 형상관리에 업로드하지 말 것!!!

def load_config(config_file='./myconfig.json'):
    if not os.path.exists(config_file):
        config_data = OrderedDict()

        ##################################################################
        # default option setting..
        config_data["data_dir"] = '~/usb/project/kakao_arena/data'
        config_data["dataset_dir"] = '~/usb/project/kakao_arena/dataset'

        ##################################################################
        # kakao default setting
        config_data["unigram_hash_size"] = 100000
        config_data["min_word_length"] = 2
        config_data["max_word_length"] = 31
        config_data["max_len"] = 32
        config_data["db_chunk_size"] = 100000
        config_data["num_workers"] = 10
        config_data["num_preidct_workers"] = 2
        config_data["embd_size"] = 128
        config_data["lr"] = 1e-4
        config_data["num_epochs"] = 100
        config_data["batch_size"] = 1024
        ##################################################################

        with open(config_file, 'w') as fp:
            json.dump(config_data, fp, ensure_ascii=False, indent=4)
        fp.close()

    return Option(config_file)