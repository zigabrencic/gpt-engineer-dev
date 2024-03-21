from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

model = ChatOpenAI(
    model="CodeLlama",
    temperature=0.1,
    callbacks=[StreamingStdOutCallbackHandler()],
    streaming=True
)

prompt = "Provide me with only the code for a simple python function that sums two numbers."

model.invoke(prompt)