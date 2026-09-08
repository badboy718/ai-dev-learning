"""
三、语义匹配
1.训练集：
'相似': [
            ('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。'),
        ],
'不相似': [
            ('黄金价格下跌，投资者抛售。', '外汇市场交易额创下新高。'),
            ('央行降息，刺激经济增长。', '新能源技术的创新。')
        ]
2.测试集：
('股票市场今日大涨，投资者乐观。', '持续上涨的市场让投资者感到满意。'),
('油价大幅下跌，能源公司面临挑战。', '未来智能城市的建设趋势愈发明显。'),
('利率上升，影响房地产市场。', '高利率对房地产有一定冲击。'),
('我爱你', '我恨你'),
('我爱你', '我喜欢你')
"""

'''
核心思路
1.初始化模型 system + user + assistant
2.调用
3.传输问题
'''

import os
from openai import OpenAI
import ollama

#初始化模型
def init_history_messages():
    train_content = {
        '相似': [
            ('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。'),
        ],
        '不相似': [
            ('黄金价格下跌，投资者抛售。', '外汇市场交易额创下新高。'),
            ('央行降息，刺激经济增长。', '新能源技术的创新。')
        ]
    }
    system_prompt = f"""你一个专业的文本匹配模型，你需要判断用户输入的句子1和句子2是否相似,最终返回对应结果: 相似或者不相似!"""
    history_messages = [
        {'role':'system', 'content':system_prompt}
    ]
    for types,contents in train_content.items():
        print(types,contents)
        for content in contents:
            history_messages.append({'role':'user', 'content':f'句子1->{content[0]}和句子2->{content[1]}是否相似'})
            history_messages.append({'role':'assistant', 'content':types})
            # print('history_messages',history_messages)
            # print('content[0]',content[0])
            # print('content[1]',content[1])
    return history_messages

ollama = ollama.Client(host='localhost')

def LLM_match(questions):
    history_messages = init_history_messages()
    for question in questions:
        new_messages = [
            {'role':'user', 'content':f"句子1->{question[0]}和句子2->{question[1]}是否相似"},
        ]
        # print(new_messages)
        # print(history_messages + new_messages)
        res = ollama.chat(
            model='qwen2',
            messages= history_messages + new_messages
        )
        result = res.message.content
        print('question',result)

if __name__ == '__main__':
    init_history_messages()
    texts = [
        ('股票市场今日大涨，投资者乐观。', '持续上涨的市场让投资者感到满意。'),
        ('油价大幅下跌，能源公司面临挑战。', '未来智能城市的建设趋势愈发明显。'),
        ('利率上升，影响房地产市场。', '高利率对房地产有一定冲击。'),
        ('我爱你', '我恨你'),
        ('我爱你', '我喜欢你')
    ]
    LLM_match(texts)