
import httpx
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

client=httpx.Client(verify=False)

llm=ChatOpenAI(
 base_url='https://genailab.tcs.in/',
 model='azure_ai/genailab-maas-DeepSeek-V3-0324',
 api_key='YOUR_API_KEY',
 http_client=client
)

embedding_model=OpenAIEmbeddings(
 base_url='https://genailab.tcs.in/',
 model='azure/genailab-maas-text-embedding-3-large',
 api_key='YOUR_API_KEY',
 http_client=client
)
