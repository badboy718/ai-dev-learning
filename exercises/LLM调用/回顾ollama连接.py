#导包
import ollama


ollama = ollama.Client(host='localhost')
res = ollama.chat(
    model='qwen2',
    messages=[
        {'role':'system','content':'你是一个金融分析师'},
        {'role':'user','content':'标普500值得买吗'}
    ]
)
print(res.message.content)