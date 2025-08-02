from main import config
from agents import Agent, Runner,enable_verbose_stdout_logging, handoff,RunContextWrapper
from pydantic import BaseModel

enable_verbose_stdout_logging()
class handoff_cls_Input(BaseModel):
    order_id:int
    reason:str

handoff_Input=handoff_cls_Input(order_id=12345, reason="Product Damage")
billing_agent=Agent(
    name="billing_agent",
    instructions="Your are a billing agent .Solve Quries related to billing and provide the solution",
    # handoff_description="you are a billing agent solve issues related to billing"
)

refund_agent=Agent(
    name="refund_agent",
    instructions="Your are a refund agent .Solve Quries related to refund and provide the solution",
    handoff_description="you are a refund agent solve issues related to billing"
)
# Handoff() Function
def handoff_on_billing (wrapper:RunContextWrapper,input):
    print("📦on_handoff function on billing")
    print(f"Order ID: {input.order_id}, Reason: {input.reason}")

def handoff_on_refund (wrapper:RunContextWrapper):
    print("💰on_handoff function on refund")
    print(f"Order ID: {input.order_id}, Reason: {input.reason}")

handoff_func_billing=handoff(
    agent=billing_agent,
    tool_name_override="Billing_Agent",
    tool_description_override="Use this tool to handle Billing queries",
    on_handoff=handoff_on_billing,
    input_type=handoff_cls_Input
)

handoff_func_refund=handoff(
    agent=refund_agent,
    tool_name_override="Refund_Agent",
    tool_description_override="Use this tool to handle Refund queries",
    on_handoff=handoff_on_refund

)

manager = Agent(
    name="main_agent",
    instructions="You handoff the agents when user asked about billing and refund problems",
    handoff_description="sadia",
    handoffs=[handoff_func_billing,handoff_func_refund]
)

result=Runner.run_sync(starting_agent=manager,input="I want to billing my money. Order ID is 12345 and the reason is incorrect charges."
,run_config=config)
print("📤OUTPUT",result.final_output)
print("👨‍💼 LAST AGENT WHO HANDLED:", result.last_agent.name)