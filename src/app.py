import os
import sys
from griptape.events import EventListener
from griptape.drivers import GriptapeCloudEventListenerDriver
from griptape.rules import Rule, Ruleset
from griptape.structures import Agent
from dotenv import load_dotenv

load_dotenv()

GRIPTAPE_API_BASE_URL = os.environ["GRIPTAPE_API_BASE_URL"]

def init_structure() -> Agent:

    rulesets = [
        Ruleset(
            name="Danish Baker",
            rules=[
                Rule(
                    "Always talk like a Danish Baker. Mention your pastries in every response."
                )
            ],
        ),
    ]

    return Agent(
        rulesets=rulesets,
        event_listeners=[
            EventListener(
                driver=GriptapeCloudEventListenerDriver(
                    base_url=GRIPTAPE_API_BASE_URL,
                )
            )
        ],
    )


if __name__ == "__main__":
    agent = init_structure()
    args = sys.argv[0:]
    i = 0
    for arg in args:
        print(f"Arg {i}: {arg}")
        i += 1
    agent.run(*sys.argv[1:])
