## Project Proposal

My analysis is centered on the idea that the world soccer transfer market is volatile and clubs pay large sums of money (in excess of $200 million dollars) 
to sign one player; a question related to this is what key attributes (features) a soccer player has that makes them valuable or not? Sporting directors at 
soccer clubs, players, agents, managers, and fans alike could all benefit from this analysis.

The data I am using for this analysis is coming from webscraping the following 2 websites: https://fbref.com/en/ and https://www.transfermarkt.us/; an 
individual unit of data will represent the characteristics (age, nationality, position, etc.), as well as advanced performance statistics specific to postion, of one player for one season of play. I hope to model the monetary value of a player (in US dollars) on an open market based on their characteristics and statistics. In total I am to evaluate 500 players over 2 seasons to create 1000 data points

I intended to use a combination of Beautifulsoup as well as Selenium to meet the requirements of this project, along with using a variety of optional 
tools to complete the storing, cleaning, and visualization. These include SQL, NumPy, Sklearn, Seaborn, and others

My minimum viable product is a model that uses features such as age, nation, league, position, and basic performance statistics non-specific to position.
