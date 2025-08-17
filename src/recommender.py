from langchain.chains import RetrievalQA #to make question answer chain
from langchain_groq import ChatGroq #used to initialise llm
from src.prompt_template import get_anime_prompt #to fetch prompt

class AnimeRecommender:
    def __init__(self,retriever,api_key:str,model_name:str): #retriever → will fetch documents (e.g., from a vector store of anime metadata).
        self.llm = ChatGroq(api_key=api_key,model=model_name,temperature=0) #temperature 0 ,means it not try to give any creative answer if not found any.
        self.prompt = get_anime_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff", # it will pull all the retrieved documents into the prompt as string context
            retriever=retriever,
            return_source_documents = True,
            chain_type_kwargs = {"prompt":self.prompt}
        )
    '''
    retriever=retriever → uses your retriever to fetch relevant anime info.
    return_source_documents=True → allows debugging (you can see which documents were used).
    prompt=self.prompt → custom anime prompt template.
    '''
    def get_recommendation(self,query:str):
        result = self.qa_chain({"query":query}) #answer of query in result
        return result['result'] #result(it is a dictionary) has many things(context,source documents) but we want the final result only.