from asyncio.log import logger

import web_api_search as web_search

def main():
    print("Hello from web-agent!")
    while True:      
        prompt = input("USER: \n")
        if prompt.lower() in ["exit", "quit"]:
            logger.info("Exiting the chat.")
            break    
        response = web_search.duckduckgo_api_search(prompt)
        print("Search results:")
        for result in response:
            print(f"{result['id']}. {result['link']}\n  {result['title']}\n  {result['snippet']}\n")

if __name__ == "__main__":
    main()
