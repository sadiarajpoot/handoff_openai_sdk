import os
from agents import Agent , AsyncOpenAI,OpenAIChatCompletionsModel, RunConfig,Runner,enable_verbose_stdout_logging,function_tool,set_tracing_disabled
from dotenv import load_dotenv

# --------------------------------------------------------------
from pydantic import BaseModel
# --------------------------------------------------------------
load_dotenv()
# enable_verbose_stdout_logging()
# --------------------------------------------------------------
set_tracing_disabled(disabled=True)
# --------------------------------------------------------------
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

# --------------------------------------------------------------
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is Missing...")
# --------------------------------------------------------------
@function_tool
def get_Weather(city:str)->str:
    return f"The Weather of {city} is Sunny."
# --------------------------------------------------------------


external_client=AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
# --------------------------------------------------------------
model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
# --------------------------------------------------------------
config=RunConfig(
    model=model,
    model_provider=external_client
)
#  # -------------------------------------------------------------- 

# agent=Agent(
#         name="My Agent",
#         instructions="You are an helpfull agent",
#         tools=[get_Weather]
#     )

# # --------------------------------------------------------------
# prompt=input("Enter Your Prompt : ")
# result=Runner.run_sync(agent,prompt,run_config=config)
# print(result.final_output)
   