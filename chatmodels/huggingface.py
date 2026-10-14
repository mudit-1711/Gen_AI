from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
)
model=ChatHuggingFace(llm=llm)
response=model.invoke("Hello, who are you?")
print(response.content)