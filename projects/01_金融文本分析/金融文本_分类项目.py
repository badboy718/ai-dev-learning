"""
一.文本分类
1.参考文本
    '新闻报道': '今日，股市经历了一轮震荡，受到宏观经济数据和全球贸易紧张局势的影响。投资者密切关注美联储可能的政策调整，以适应市场的不确定性。',
    '财务报告': '本公司年度财务报告显示，去年公司实现了稳步增长的盈利，同时资产负债表呈现强劲的状况。经济环境的稳定和管理层的有效战略执行为公司的健康发展奠定了基础。',
    '公司公告': '本公司高兴地宣布成功完成最新一轮并购交易，收购了一家在人工智能领域领先的公司。这一战略举措将有助于扩大我们的业务领域，提高市场竞争力',
    '分析师报告': '最新的行业分析报告指出，科技公司的创新将成为未来增长的主要推动力。云计算、人工智能和数字化转型被认为是引领行业发展的关键因素，投资者应关注这些趋势'

2.验证文本
    "今日，央行发布公告宣布降低利率，以刺激经济增长。这一降息举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。",
    "ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在扩大业务范围、加强市场竞争力方面的重要举措。据悉，此次收购将进一步巩固ABC公司在行业中的地位，并为未来业务发展提供更广阔的发展空间。详情请见公司官方网站公告栏",
    "公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础。",
    "最新的分析报告指出，可再生能源行业预计将在未来几年经历持续增长，投资者应该关注这一领域的投资机会",
"""
'''
核心思路：
1.定义解析规范
2.调用模型
3.传入需要解析的文本
'''

import os
from openai import OpenAI

#定义模型解析规范
def init_history_messages():
    #few-shot 例子文本
    contents={
    '新闻报道': '今日，股市经历了一轮震荡，受到宏观经济数据和全球贸易紧张局势的影响。投资者密切关注美联储可能的政策调整，以适应市场的不确定性。',
    '财务报告': '本公司年度财务报告显示，去年公司实现了稳步增长的盈利，同时资产负债表呈现强劲的状况。经济环境的稳定和管理层的有效战略执行为公司的健康发展奠定了基础。',
    '公司公告': '本公司高兴地宣布成功完成最新一轮并购交易，收购了一家在人工智能领域领先的公司。这一战略举措将有助于扩大我们的业务领域，提高市场竞争力',
    '分析师报告': '最新的行业分析报告指出，科技公司的创新将成为未来增长的主要推动力。云计算、人工智能和数字化转型被认为是引领行业发展的关键因素，投资者应关注这些趋势'
    }
    #系统提示词
    system_prompt = f"你是一个专业的文本分类模型，你需要根据提供的文本内容，将文本分类为优先为以下四种类型：{list(contents.keys())},对于不在这四类中的数据，输出'不清楚类型'"
    history_messages = [
        {"role": "system", "content": system_prompt},
    ]
    # 系统提示词拼接小样本few-shot
    for key_category,value_text in contents.items():
        history_messages.append({"role": "user", "content": value_text})
        history_messages.append({"role": "assistant", "content": key_category})
    return history_messages


def call_LLM(questions):
    client = OpenAI(
        #若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://ws-rbug1o8iq6u98wxb.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    )
    history_messages = init_history_messages()
    for question in questions:
        new_message = [
            {"role": "user", "content": question}
        ]
        completion = client.chat.completions.create(
            # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            model = "qwen3.8-max",
            messages = history_messages + new_message
        )

        #print('传给模型的是：',init_history_messages() + new_message)
        result = completion.choices[0].message.content
        print(f'{question}\n',result)


if __name__ == '__main__':
    #print(init_history_messages())
    questions = [
        "今日，央行发布公告宣布降低利率，以刺激经济增长。这一降息举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。",
        "ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在扩大业务范围、加强市场竞争力方面的重要举措。据悉，此次收购将进一步巩固ABC公司在行业中的地位，并为未来业务发展提供更广阔的发展空间。详情请见公司官方网站公告栏",
        "公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础。",
        "最新的分析报告指出，可再生能源行业预计将在未来几年经历持续增长，投资者应该关注这一领域的投资机会",
        "时隔35年，电影《纵横四海》内地首次公映，正式定档5月3日全国公映。周润发、张国荣、钟楚红绝版同框，全新4K高清修复，还原最清晰的银幕传奇。"
    ]
    call_LLM(questions)




