from dotenv import load_dotenv

from src.agents import create_supervisor_agent
from src.tests import test_multi_agent

load_dotenv()


def main():
    supervisor = create_supervisor_agent()
    test_multi_agent(supervisor, "马云的岁数 + 刘强东的岁数之和是多少？")


if __name__ == "__main__":
    main()
