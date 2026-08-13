from Bio import Entrez
def search_pubmed(query, email):
    Entrez.email=email
    handle=Entrez.esearch(db="pubmed", term=query, retmax=10,sort="relevance")
    results=Entrez.read(handle)
    handle.close()
    idlist=results["IdList"]
    return idlist
def fetch_pubmed_details(idlist, email):
    Entrez.email=email
    handle=Entrez.efetch(db="pubmed", id=idlist, retmode="txt", rettype="abstract")
    results=handle.read()
    handle.close()
    return results