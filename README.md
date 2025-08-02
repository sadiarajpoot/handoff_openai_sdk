# 🤖 OpenAI Agent SDK - Handoff System for Billing and Refund Support

## 🚀 handoff.py file 
This project demonstrates a multi-agent system using the [OpenAI Agent SDK](https://platform.openai.com/docs/assistants/agents) with **handoff capabilities** between agents based on the user’s intent (Billing or Refund).

---

## 🚀 Features

- **Multi-Agent Structure**: Three agents:
  - `main_agent` – acts as the central manager and delegates tasks.
  - `billing_agent` – handles billing issues.
  - `refund_agent` – handles refund-related queries.
  
- **Handoff Functionality**: 
  - User queries are intelligently routed using `handoff()` based on keywords (e.g., "billing", "refund").
  - Custom `on_handoff()` functions are triggered when handoffs occur.
  
- **Logging & Verbose Output**:
  - `enable_verbose_stdout_logging()` is used to clearly trace each step and decision made during agent interactions.

---

## 🛠 How It Works

1. **Define Agents**:
    - Agents are given specific instructions and handoff descriptions.
  
2. **Create Input Schema**:
    - A `handoff_cls_Input` Pydantic model captures user data like `order_id` and `reason`.

3. **Define Handoff Logic**:
    - `handoff_on_billing()` and `handoff_on_refund()` functions are defined to log context-specific data.
  
4. **Configure Handoff Tools**:
    - Each agent is wrapped using the `handoff()` function and registered under the `main_agent`.

5. **Run the System**:
    - The `Runner.run_sync()` function initiates the agent loop with a natural language user query.

---

## 📦 Example Output

```bash
📦on_handoff function on billing
Order ID: 12345, Reason: incorrect charges
📤OUTPUT: (final resolved message here)
👨‍💼 LAST AGENT WHO HANDLED: billing_agent


## 🚀 handoffproperties.py
# 🤖 Multi-Agent Handoff System

This project shows how to use OpenAI's Agents SDK to create a smart system that routes user queries to the right agent.

---

## 🔍 Features

- 🧠 Manager agent handles all user inputs
- 💳 Billing agent for billing issues
- 💸 Refund agent for refund problems
- 🔁 Smart handoff using `Handoff()` and input schema
- ✅ Schema validation with Pydantic

---

## ▶️ Run the Project


uv run handoffproperties.py
