from langchain_community.tools.tavily_search.tool import TavilySearchResults

web_search = TavilySearchResults(
    name="web_search",
    max_results=5,
    include_answer=False,
    include_raw_content=False,
)
