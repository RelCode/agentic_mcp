import asyncio
from llm_client import make_llm
from langchain_core.messages import HumanMessage

async def main():
    llm = make_llm()
    
    # Use ainvoke with proper message format (modern LangChain approach)
    messages = [HumanMessage(content="Say hello from LangChain + Azure Foundry")]
    resp = await llm.ainvoke(messages)
    
    print(resp.content)

if __name__ == "__main__":
    asyncio.run(main())
