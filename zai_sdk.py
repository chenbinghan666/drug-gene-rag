from zai import ZhipuAiClient
from config import load_config
api_key=load_config()["ZAI_API_KEY"]
client = ZhipuAiClient(api_key=api_key)
def analyze(gene,drug,cancer,details):
    prompt=f"请分析以下文献内容，结合基因{gene}、药物{drug}和癌症类型{cancer}，总结出该药物对该基因在该癌症中的作用机制，并给出相关的研究结论和参考文献,判断该药物是否靶向该基因,给出判断依据和可信度,如果证据不足,请明确回答无法确定。最终结果要清晰列出关系判断：药物靶向基因关系判断,可信度:\n\n文献内容：\n{details}"
    response = client.chat.completions.create(
    model="glm-5.2",
    messages=[
        {
            "role": "system",
            "content": "你是一个生物医学文献分析助手。只能根据用户提供的文献作答，不要编造文献中没有的信息。"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.4
)
    ans=response.choices[0].message.content
    return ans