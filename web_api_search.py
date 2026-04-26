from ddgs import DDGS


def duckduckgo_api_search(query: str) -> list[dict]:
    """This function uses the duckduckgo_search library to perform a search query and return structured results.
    
    Args:        
        query (str): The search query to be sent to DuckDuckGo.
        keywords (str): The keywords to search for.
        #  https://duckduckgo.com/duckduckgo-help-pages/settings/params
        region (str): The region code for the search results (default is 'wt-wt').
        safesearch (str): The safesearch setting for the search results (default is 'Off').
        timelimit (str): The time limit for the search results (default is '10d').
        max_results (int): The maximum number of search results to return (default is 10).
    
    Returns:
        list: A list of dictionaries containing the search results, where each dictionary has the following keys:
            - 'id': The index of the search result (starting from 1).
            - 'link': The URL of the search result.
            - 'snippet': A brief description or snippet of the search result.
    """
    try:
        with DDGS() as ddgs:
            results = ddgs.text(
                query=query,
                region='ro-ro',
                safesearch='moderate',
                timelimit='10d', 
                max_results=10,
                backend= 'bing')
            formatted_results = []
            for i, result in enumerate(results, start=1):
                formatted_results.append({
                    'id': i,
                    'title': result.get('title', 'No title available'),
                    'link': result['href'],
                    'snippet': result.get('body', 'Description not available')
                })
            return formatted_results
    except Exception as e:
        print(f"An error occurred while performing the search: {e}")
        return []