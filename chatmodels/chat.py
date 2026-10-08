from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq"
)
 
#print(model) 
question = str(input("Ask me anything: "))
response = model.invoke(question)
print(response.content)