from dotenv import load_dotenv
from InquirerPy import inquirer

from src.agents import create_supervisor_agent
from src.tests import test_multi_agent

load_dotenv()

BUILT_IN_QUESTIONS = [
    "Find the name and height of the tallest building in the world, and calculate how many times taller it is compared to a building that is 100 meters high.",
    "Find the average calories in a banana, and calculate how many calories you would consume in a month (30 days) if you eat 3 bananas every day.",
    "Find the value of the speed of light, and calculate the distance light can travel in 1 minute.",
    "Find the straight-line distance from Beijing to Shanghai, and calculate how long it would take to travel at a speed of 300 kilometers per hour.",
    "Scrape the current population data of the United States and calculate the population density of the country.",
]


def ask(initial_question: str):
    supervisor = create_supervisor_agent()
    test_multi_agent(supervisor, initial_question)


def main():
    initial_question = inquirer.select(
        message="What do you want to know?",
        choices=["[Ask my own]"] + BUILT_IN_QUESTIONS,
    ).execute()
    if initial_question == "[Ask my own]":
        initial_question = inquirer.text(
            message="What do you want to know?",
        ).execute()
    ask(initial_question)


if __name__ == "__main__":
    main()
