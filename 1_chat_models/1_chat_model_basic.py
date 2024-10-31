from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq

# Load environment variables from .env
load_dotenv()

# Create a model
model = ChatGroq(model="llama-3.1-70b-versatile",
                      stop_sequences="[end]")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
