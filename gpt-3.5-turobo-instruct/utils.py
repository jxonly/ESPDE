import json
import datetime
import os

def mkpath(path):
    if not os.path.exists(path):
        os.mkdir(path)

def load_data(datapath,dataset):
    # print('1')
    decoder = json.JSONDecoder()
    questions = []
    answers = []
    ids = []
    if dataset.lower() in ['svamp', 'svamp_sorted', 'gsm8k', 'gsm8k_sorted', 'multiarith', 'addsub', 'singleeq',
                                'strategyqa', 'coin_flip', 'last_letters']:
        # print('2')
        with open(datapath) as f:
            # print('3')
            if dataset.lower() in ['coin_flip', 'last_letters', 'strategyqa']:
                json_data = json.load(f)["examples"]
            else:
                json_data = json.load(f)

            for idx, line in enumerate(json_data):
                if dataset.lower() == 'svamp':
                    if line['Body'][-1] != '.':
                        q = line['Body'].strip() + ". " + line["Question"].strip()
                    else:
                        q = line['Body'].strip() + " " + line["Question"].strip()
                    a = float(line["Answer"])
                    id = line["ID"]
                elif dataset == 'svamp_sorted':
                    q = line['Question']
                    a = float(line['Answer'])
                    id = line['ID']
                elif dataset.lower() == 'strategyqa':
                    q = line["input"].strip()
                    a = int(line["target_scores"]["Yes"])
                    if a == 1:
                        a = "yes"
                    else:
                        a = "no"
                    id = 'temp_{}'.format(idx)
                elif dataset.lower() in ['coin_flip', 'last_letters']:
                    q = line["question"]
                    a = line["answer"]
                    id = 'temp_{}'.format(idx)
                elif dataset.lower() in ["multiarith", 'addsub', 'singleeq']:
                    q = line['sQuestion']
                    a = float(line['lSolutions'][0])
                    id = 'temp_{}'.format(idx)
                elif dataset.lower() in ['gsm8k', 'gsm8k_sorted', 'examples', 'examples']:
                    q = line['question']
                    a = float(line['answer'])
                    print(q,a)
                    id = 'temp_{}'.format(idx)
                else:
                    raise ValueError('not support dataset: {}'.format(dataset))
                questions.append(q)
                answers.append(a)
                ids.append(id)
    elif dataset.lower() in ['aqua', 'commonsenseqa']:
        print(datapath)
        with open(datapath,encoding='utf-8') as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                if dataset.lower() == 'aqua':
                    json_res = decoder.raw_decode(line)[0]
                    choice = "(" + "(".join(json_res["options"])
                    choice = choice.replace("(", " (").replace(")", ") ")
                    choice = "Answer Choices:" + choice
                    q = json_res["question"].strip() + ' ' + choice
                    a = json_res["correct"]
                    id = 'temp_{}'.format(idx)
                elif dataset.lower() == 'commonsenseqa':
                    json_res = decoder.raw_decode(line)[0]
                    choice = "Answer Choices:"
                    for c in json_res["question"]["choices"]:
                        choice += " ("
                        choice += c["label"]
                        choice += ") "
                        choice += c["text"]
                    q = json_res["question"]["stem"].strip() + " " + choice
                    a = json_res["answerKey"]
                    id = 'temp_{}'.format(idx)
                else:
                    raise ValueError('not support dataset: {}'.format(dataset))
                questions.append(q)
                answers.append(a)
                ids.append(id)
    return questions, answers, ids

def write_json(data, path):
    f = open(path, mode='a', encoding='utf-8')
    json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()
    
def getKey():
    apikey_list = json.load(open('./jx_apikeys.json', 'r', encoding='utf-8'))
    assert len(apikey_list) >= 1, f"need 1 apikey, find {len(apikey_list)} in '/apikeys.json'"
    return apikey_list