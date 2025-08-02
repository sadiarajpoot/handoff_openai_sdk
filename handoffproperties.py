from main import config
# -------------------------------------------------------
from agents import Agent, Runner,enable_verbose_stdout_logging, Handoff,RunContextWrapper
# -------------------------------------------------------
from pydantic import BaseModel
# -------------------------------------------------------
#input_json_schema
class Schema_Model_Billing(BaseModel):
    input:str
My_Schema_Billing=Schema_Model_Billing.model_json_schema()
My_Schema_Billing["additionalProperties"]=False
# -------------------------------------------------------
enable_verbose_stdout_logging()
# -------------------------------------------------------
#on_invoke_handoff
async def my_invoke_function(Wrapper:RunContextWrapper,input:str):
    return billing_agent

# -------------------------------------------------------

billing_agent_handoff=Handoff(
    agent_name="billing_agent",
    tool_name="billing_agent",
    tool_description="you are a billing agent solve issues related to billing handoff()",
    input_json_schema=My_Schema_Billing,
    on_invoke_handoff=my_invoke_function
)

# -------------------------------------------------------
billing_agent=Agent(
    name="billing_agent",
    instructions="Your are a billing agent .Solve Quries related to billing and provide the solution", #  for define agent persona
    handoff_description="you are a billing agent solve issues related to billing"  # HD for LLM
)
# -------------------------------------------------------
refund_agent=Agent(
    name="refund_agent",
    instructions="Your are a refund agent .Solve Quries related to refund and provide the solution",
    handoff_description="you are a refund agent solve issues related to billing"
)
# -------------------------------------------------------
manager = Agent(
    name="main_agent",
    instructions="You handoff the agents when user asked about billing and refund problems",
    handoffs=[refund_agent,billing_agent_handoff]
)
# -------------------------------------------------------
result=Runner.run_sync(starting_agent=manager,input="I want to billing my money. "
,run_config=config)
# -------------------------------------------------------
print("📤OUTPUT",result.final_output)
print("👨‍💼 LAST AGENT WHO HANDLED:", result.last_agent.name)