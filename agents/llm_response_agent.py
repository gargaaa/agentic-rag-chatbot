from utils.mcp import create_message
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class LLMResponseAgent:
    def run(self, context, trace_id):
        prompt = "\n".join(context["retrieved_context"]) + f"\n\nQ: {context['query']}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response['choices'][0]['message']['content']
        return create_message(
            sender="LLMResponseAgent",
            receiver="UI",
            type_="ANSWER",
            payload={"answer": answer},
            trace_id=trace_id
        )
