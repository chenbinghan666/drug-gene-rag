from pubmed import search_pubmed
from pubmed import fetch_pubmed_details
from config import load_config
from zai_sdk import analyze
gene=input("请输入基因名称：")
drug=input("请输入药物名称：")
cancer=input("请输入癌症类型：")
if cancer=="":
    cancer="cancer"
query=f"{gene} AND {drug} AND {cancer}"
config=load_config()
email=config["email"]
idlist=search_pubmed(query, email)
print("查询结果的PubMed ID列表：\n", idlist)
details=fetch_pubmed_details(idlist, email)
print("正在调用智谱大模型分析文献……")
ans=analyze(gene,drug,cancer,details)
print("分析结果：\n", ans)