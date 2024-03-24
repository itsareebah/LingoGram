from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

from langchain_openai import ChatOpenAI
from enum import Enum
from .process import OPEN_API_KEY

class TONE(Enum):
    FORMAL = "formal"
    INFORMAL = "informal"
    OPTIMISTIC = "optimistic"
    WORRIED = "worried"
    FRIENDLY = "friendly"
    CURIOUS = "curious"
    ASSERTIVE = "assertive"
    ENCOURAGING = "encouraging"
    SUPRISED = "suprised"
    COOPERATIVE = "cooperative"

base_prompt_prefix = "Improve English for the following text and make its tone {tone}: {text}"

def generateText(text, tone):
    try:
        model = ChatOpenAI(openai_api_key = OPEN_API_KEY)
        prompt = PromptTemplate(
            template=base_prompt_prefix.format(tone=tone, text=text), 
            input_variables=["tone", "text"])
        
        chain = LLMChain(llm=model, prompt=prompt)
        chain_res = chain.invoke({'tone': tone, 'text': text})
        generated_text = {
            "text": chain_res['text']
        }
        return generated_text
    except Exception as e:
        print(e)
