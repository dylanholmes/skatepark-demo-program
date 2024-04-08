import sys
from griptape.rules import Rule, Ruleset
from griptape.structures import Agent


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

    return Agent(rulesets=rulesets)


if __name__ == "__main__":
    agent = init_structure()
    args = sys.argv[1:]
    agent.run(*args)
