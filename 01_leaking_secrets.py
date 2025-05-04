# Ref: https://python.langchain.com/docs/how_to/runnable_runtime_secrets/
from dotenv import load_dotenv
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langchain_core.tracers.context import tracing_v2_enabled

load_dotenv()


@tool
def call_api(input,config: RunnableConfig) -> str:
    """

    :param config:
    :return:
    """
    print(config)
    api_token = config["configurable"]["__api_token"]
    message = f"""calling {input} with api token """

    return message


with tracing_v2_enabled(project_name="secure_coding_with_masking"):
    result = call_api.invoke(input="api.smith.com",config={"configurable": {"__api_token": "lytu67io0789567tyuipqr", "traced_key": "api_key"}})
    print("Call api:", result)

# call_api.invoke({"configurable": {"__api_token": "lytu67io0789567tyuipqr", "traced_key": "api_key"}})
