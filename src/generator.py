from transformers import pipeline
class Generator:
    def __init__(self,device=-1):
        self.pipe=pipeline("text2text-generation",model="google/flan-t5-small",device=device)
    def generate(self,question,hits):
        ctx="\n---\n".join([f"Source: {h['id']}\n{h['document']}" for h in hits])
        prompt=f"You are an assistant. Use the context below to answer the question.\n\nContext:\n{ctx}\n\nQuestion: {question}\nAnswer concisely:"
        return self.pipe(prompt,max_new_tokens=150,do_sample=False)[0]["generated_text"]
