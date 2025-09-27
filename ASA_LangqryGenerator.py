import dotenv
import os, json
import ast
import string
import pandas as pd
from datetime import date, datetime, timedelta
import openai
from langchain.chat_models import AzureChatOpenAi
from langchain.utilities import SQLDatbase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts.prompt import PromptTemplate
from sqlalchemy.engine import URL
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import generate_account_sas, BlobSasPermissions

chat_history = []
connection_string = "DefaultEndpointsProtocol=https:AccountName=openaipocadlsdev;AccountKey=eS51uTb176NEX1Y7AP7bqHeokZ6zzc9R359mlxaYpvLwupPu1IXSKDVExhMfz1hVUW36YHWUa+ASt0voBtQ==;EndpointSuffix=core.windows.net"
container_name = "openai-poc-genai-data"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)
account_name = 'opeaipocadla1dev'
account_key = 'eS51uTb176NEX1Y7AP7bqHFeoKZ6zzc9R359mlxaYpvLwupPu1IXSKDVExhKhMfz1hVUW36YHWUa+ASt0voBtQ'

url = ""
blob_name = ""
dotenv.load_dotenv()
current_data = date.today()

OPENAI_DEPPOYMENT_NAME=os.environ['OPENAI_DEPLOYEMENT_NAME']
OPENAI_API_TYPE = os.environ['OPENAI_API_TYPE']
OPENAI_API_BASE = os.environ['OPEN_API_BASE']
OPENAI_API_VERSION = os.environ['OPENAI_API_VERSION']
OPEN_API_KEY = os.environ['OPEN_API_KEY']


