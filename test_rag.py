from utils.rag import RAGRetriever
from utils.gemini import ask_gemini

retriever = RAGRetriever()

question = input("Ask: ")

context, sources = retriever.retrieve(question)

answer = ask_gemini(question, context)

print("\nAnswer:\n")
print(answer)

print("\nSources:")

for src in sources:
    print("-", src)