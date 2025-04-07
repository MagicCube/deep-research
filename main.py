from dotenv import load_dotenv
from InquirerPy import inquirer

from src.agents import create_supervisor_agent
from src.tests import test_multi_agent

load_dotenv()

BUILT_IN_QUESTIONS = [
    "Find the name and height of the tallest building in the world, and calculate how many times taller it is compared to a building that is 217 meters high.",
    "Find the average calories in a banana, and calculate how many calories you would consume if you eat 3 bananas every day.",
    "Find the value of the speed of light, and calculate the distance light can travel in 1 minute.",
    "Find the price of Apple and Tesla on March 1 and March 3, 2025.",
]

BUILT_IN_QUESTIONS_ZH_CN = [
    "查找世界上最高的建筑物的名称和高度，并计算它比一个217米高的建筑物高出多少倍。",
    "查找一根香蕉的平均热量，并计算如果你每天吃3根香蕉会摄入多少热量。",
    "查找光速的数值，并计算光在1分钟内可以传播的距离。",
    "查找2025年3月1日和3月3日，苹果和特斯拉的股价是多少？",
]


def ask(initial_question: str):
    supervisor = create_supervisor_agent()
    test_multi_agent(supervisor, initial_question)


def main():
    initial_question = inquirer.select(
        message="What do you want to know?",
        choices=BUILT_IN_QUESTIONS_ZH_CN + ["[Ask my own]"],
    ).execute()
    if initial_question == "[Ask my own]":
        initial_question = inquirer.text(
            message="What do you want to know?",
        ).execute()
    ask(initial_question)


if __name__ == "__main__":
    main()
