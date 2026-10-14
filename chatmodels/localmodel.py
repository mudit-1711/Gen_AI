from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={
        "cache_dir": r"D:\Gen AI\LLMS\Tiny Lamma"
    },
    pipeline_kwargs={
        "max_new_tokens": 512,
        "do_sample": False,
        "repetition_penalty": 1.03,
    },
)
chat_model = ChatHuggingFace(llm=llm)
question = input("Ask TinyLlama: ")
response = chat_model.invoke(question)
print("\nTinyLlama:", response.content)
