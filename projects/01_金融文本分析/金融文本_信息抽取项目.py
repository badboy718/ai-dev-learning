"""
二.信息抽取
1.参考文本
    [{
        'content': '2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。',
        'answers': {
            '日期': ['2023-01-10'],
            '股票名称': ['古哥-D[EOOE]美股'],
            '开盘价': ['100美元'],
            '收盘价': ['102美元'],
            '成交量': ['520000'],
        }
    }]
2.验证文本
'2025-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。',
'2025-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。',
"""
import json
import os
from openai import OpenAI

'''
核心思路：
1.初始化历史提示词（system + user + assistant)
2.定义调用模型
3.传入验证文本
'''

def init_history_messages():
    examples = [
        {
            'content': '2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。',
            'answers': {
                '日期': ['2023-01-10'],
                '股票名称': ['古哥-D[EOOE]美股'],
                '开盘价': ['100美元'],
                '收盘价': ['102美元'],
                '成交量': ['520000'],
            }
        }
    ]
    types = {'金融':['日期','股票名称','开盘价','收盘价','成交量']}
    #print(types['金融'])
    system_prompts =  f"""你一个专业的文本信息抽取模型，你需要根据提供的文本内容，严格抽取出以下信息：{types['金融']}!不要胡编乱造!"""
    history_messages = [{'role':'system','content':system_prompts}]
    for example in examples:
        history_messages.append({'role':'user','content':example['content']})
        history_messages.append({'role':'assistant','content':json.dumps(example['answers'],ensure_ascii=False)})
        #print(json.dumps(example['answers'], ensure_ascii=False))
        #print(example['answers'])
        #print(json.dumps(example['content'], ensure_ascii=False))
        #print(example['content'])
    return history_messages

client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com"
    )

def LLM_extract_info_model(questions):
    history_messages = init_history_messages()
    for question in questions:
        new_messages = [{'role':'user','content':question}]
        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=history_messages + new_messages,
        )
        result = response.choices[0].message.content
        #print('messages',history_messages + new_messages)
        print(question,'\n', result)

if __name__ == '__main__':
    #init_history_messages()
    questions = [
        '2025-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。',
        '2025-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。'
    ]
    LLM_extract_info_model(questions)