import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key="sk-ws-H.EPPXHME.6w77.MEUCIQDlQEoQYVtCQFxQFfdtr5S5MCJeqW9nwLQsokGkWIFULgIgUxwxH_76FeHVJFpuZ7-iHCP3NBMUsVDCaKooNx-thRU",
    base_url="https://ws-rbug1o8iq6u98wxb.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen3.8-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ]
)
print(completion.model_dump_json())
print(completion.choices)
print(completion.choices[0])
print(completion.choices[0].message)
print(completion.choices[0].message.content)