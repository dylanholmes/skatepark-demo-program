import os
import sys
from griptape.events import EventListener
from griptape.drivers import GriptapeCloudEventListenerDriver, LocalEventListenerDriver
from griptape.rules import Rule, Ruleset
from griptape.structures import Agent
from dotenv import load_dotenv

load_dotenv()

GRIPTAPE_API_BASE_URL = os.environ["GRIPTAPE_API_BASE_URL"]
GRIPTAPE_API_KEY = os.environ["GRIPTAPE_API_KEY"]

print("Environment variables:")
for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))
print()

print("Arguments:")
for i, arg in enumerate(sys.argv):
    print(f"Arg {i}: {arg}")

agent = Agent(
    rulesets=[
        Ruleset(
            name="Danish Baker",
            rules=[
                Rule(
                    "Always talk like a Danish Baker. Mention your pastries in every response."
                )
            ],
        ),
    ],
    event_listeners=[
        EventListener(
            driver=GriptapeCloudEventListenerDriver(
                base_url=GRIPTAPE_API_BASE_URL,
                api_key=GRIPTAPE_API_KEY,
            )
        ),
        EventListener(
            driver=LocalEventListenerDriver(
                handler=lambda event: print(f"Local event handler: {event}")
            )
        )
    ],
)
agent.run(*sys.argv[1:])
