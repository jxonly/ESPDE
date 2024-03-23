import time

import openai

from utils import getKey

def decoder_for_gpt3(engine,input, max_length, apikey,path_num):
    # openai.api_key = apikey
    # print("in decoder-------------------")
    engine = engine
    top_p = 1
    frequency_penalty = 0
    presence_penalty = 0
    temperature = 0.25
    stop = ["\n\n"] if max_length == 32 else None
    cots = []

    # print("path_nun:",path_num)
    response = openai.Completion.create(
        model=engine,
        prompt=input,
        max_tokens=max_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        n=path_num,
        stop=stop,
        api_key=apikey,
        api_base="https://api.keya.pw"
    )
    # print("res:",response)
    cots = [p['text'] for p in response["choices"]]
    return cots
    


def basic_runner(engine,inputs, max_length,path_num,apikey,max_retry=3):
    # print("in basic runner-----------------")
    retry = 0
    api_time_interval = 2.0
    # apikey_list = getKey()
    # print("keys:",apikey_list)
    # apikey_dict = dict(enumerate(apikey_list))
    # key_list = list(apikey_dict.keys())
    # key_l = key_list[key_index]
    # apikey = apikey_dict[key_l]
    # apikey = "sk-JdqdUv6vmySJkVXVB546E498802b4dBc92B9Ff504102051c"
    get_result = False
    pred = []
    error_msg = ''
    while not get_result:
        try:
            pred = decoder_for_gpt3(engine, inputs, max_length, apikey,path_num)
            get_result = True
            # print("pred:",pred)
            # print('当前的良好的apikey:',apikey)
            # time.sleep(1)

        except openai.error.RateLimitError as e:
            if 'You exceeded your current quota, please check your plan and billing details.' in e.user_message or e.user_message == 'Your account is not active, please check your billing details on our website.':
                print('出问题的key:',apikey)
                # apikey_dict.pop(key_l)
                # key_list.pop(key_index)
                # if len(key_list)!=0:
                #     key_index = (key_index) % (len(key_list))
                #     key_l = key_list[key_index]
                #     apikey = apikey_dict[key_l]
                #     time.sleep(api_time_interval)
                # else:
                #     print("-------------no key------------")
                raise e
            elif 'Rate limit reached for text-davinci-003 in organization' in e.user_message:
                # if 'Limit 200' in  e.user_message:
                #     print("达到每日200条限制的key：",apikey)
                # if len(apikey_list)>1:
                #     key_index = (key_index+1) % len(key_list)
                #     key_l = key_list[key_index]
                #     apikey = apikey_dict[key_l]
                #     time.sleep(api_time_interval)
                #     # print(apikey)
                # else:
                #     print("-------------no key------------")
                raise e
            elif retry < max_retry:
                time.sleep(api_time_interval)
                retry += 1
            else:
                print('最后的问题apikey:',apikey)
                # error_msg = e.user_message
                # apikey_dict.pop(key_l)
                # key_list.pop(key_index)
                # if len(key_list)!=0:
                #     key_index = (key_index) % (len(key_list))
                #     key_l = key_list[key_index]
                #     apikey = apikey_dict[key_l]
                #     time.sleep(api_time_interval)
                # else:
                #     print("-------------no key------------")
                break
        except Exception as e:
            raise e
    return get_result, pred, error_msg
