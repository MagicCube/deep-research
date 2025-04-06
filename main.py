from dotenv import load_dotenv
from InquirerPy import inquirer

from src.agents import create_supervisor_agent
from src.tests import test_multi_agent

load_dotenv()

BUILT_IN_QUESTIONS = [
    "Find the name and height of the tallest building in the world, and calculate how many times taller it is compared to a building that is 217 meters high.",
    "Find the average calories in a banana, and calculate how many calories you would consume in a month (30 days) if you eat 3 bananas every day.",
    "Find the value of the speed of light, and calculate the distance light can travel in 1 minute.",
    "Find the straight-line distance from Beijing to Shanghai, and calculate how long it would take to travel at a speed of 300 kilometers per hour.",
    "Scrape the current population data of the United States and calculate the population density of the country.",
]

BUILT_IN_QUESTIONS_ZH_CN = [
    "查找世界上最高的建筑物的名称和高度，并计算它比一个217米高的建筑物高出多少倍。",
    "查找一根香蕉的平均热量，并计算如果你每天吃3根香蕉，一个月（30天）会摄入多少热量。",
    "查找光速的数值，并计算光在1分钟内可以传播的距离。",
    "查找北京到上海的直线距离，并计算如果以每小时300公里的速度行驶，需要多少时间到达。",
    "爬取美国的当前人口数据，并计算该国家的人口密度。",
]


def ask(initial_question: str):
    supervisor = create_supervisor_agent()
    test_multi_agent(supervisor, initial_question)


def main():
    initial_question = inquirer.select(
        message="What do you want to know?",
        choices=["[Ask my own]"] + BUILT_IN_QUESTIONS_ZH_CN,
    ).execute()
    if initial_question == "[Ask my own]":
        initial_question = inquirer.text(
            message="What do you want to know?",
        ).execute()
    ask(initial_question)


if __name__ == "__main__":
    main()
