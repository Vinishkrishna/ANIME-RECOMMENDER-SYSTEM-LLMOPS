from langchain.text_splitter import CharacterTextSplitter #to character split
from langchain_community.vectorstores import Chroma 
from langchain_community.document_loaders.csv_loader import CSVLoader #to load csv file
from langchain_huggingface import HuggingFaceEmbeddings #to convert text to embeddings so that it can be stored in chroma

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self,csv_path:str,persist_dir:str="chroma_db"): #path where vector store will get saved
        self.csv_path= csv_path
        self.persist_dir= persist_dir
        self.embedding= HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def build_and_save_vectorstore(self):
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding="utf-8",
            metadata_columns=[]
        )

        data=loader.load()

        splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
        texts = splitter.split_documents(data) #stored the splitted text in texts variable

        db=Chroma.from_documents(texts,self.embedding,persist_directory=self.persist_dir)#storing of data and embedding is done here only.
        db.persist() #it will save vector store to the disk

    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir,embedding_function=self.embedding)