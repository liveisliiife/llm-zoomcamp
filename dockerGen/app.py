from fastapi import FastAPI
from transformers import pipeline

# create a new FastAPI app instance
app = FastAPI()

# initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")


# homepage
@app.get("/")
def home():
    return {"message":"Hellooo"}


@app.get("/generate")
def generate(text:str):
    output = pipe(text)
    return {"output":output[0]["generated_text"]}

