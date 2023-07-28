from django.shortcuts import render
# 在您的Django应用程序中的某个适当位置编写视图函数来处理摘要请求
# 假设您已经安装了OpenAI Python包并获得了API访问密钥

import openai
from django.http import JsonResponse

def summarize_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        # 调用GPT-3进行文本摘要
        # 在这里您需要将YOUR_OPENAI_API_KEY替换为您自己的API密钥
        openai.api_key = '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'
        response = openai.Completion.create(
            engine="text-davinci-002",  # 这是GPT-3的引擎，也可以是其他引擎
            prompt=text,
            temperature=0.7,
            max_tokens=100
        )
        # 从GPT-3的响应中提取摘要
        summary = response['choices'][0]['text']
        return JsonResponse({'summary': summary})


# Create your views here.
