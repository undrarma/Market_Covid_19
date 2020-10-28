

Stock Market during Covid-19 Pandemic
Andrea Armani 
2020/2021
Visual Analytics
Assignment 3
Introduction to the analysis

The analysis aims to show the effect that Covid-19’s pandemic had and is currently having on three stock markets around the world. Such stock markets are:

European Stock Market: it comprises the main stock markets in Europe and the UK;
Asian Stock Market: it comprises China, South Korea, Singapore and Hong Kong;
American Stock Market: it comprises the United States of America;

For every market I picked an index that is formed by the main companies. Such indices are:

STOXX 50 EU;
Hang Seng;
S&P 500;

Finally, since each of these indices is formed on top of the price of the major companies in that particular world region, I scraped the data of such companies and I developed my analysis around such data. Because companies operate in different markets, they also operate with different currencies. Therefore, after scraping the data, I uniformed them to the same currency, the US dollar. 

In the finance world there is a very common motto:

A rising tide lifts all the boats

That basically means that if something goes wrong somewhere, most probably it will be eventually followed in other parts of the world. However, in the last years such idea was complemented with a second sentence:

But You Find Out Whose Swimming Naked When The Tide Goes Out

which means that after an important event, either positive or negative, the companies that were not able to adapt to such a situation will pay a price. Such price to pay is what I want to inspect with this analysis. 

In the following, I present the questions that I will try to explain through visualizations.

How the crisis affected the companies in different regions of the world?
The lockdowns and the following crisis happened in all of these regions, however in different dates and with different consequences. What were the market's reactions? 

What happened in different market sectors?
The crisis impacted each sector in a different way: for instance, it’s hard to believe that the Technology sector and the Real Estate one experienced the same consequences. Which sectors were particularly damaged? Which ones reacted quickly? 

Are there companies that didn’t follow their sector’s trend? 
This final question arose after trying to explain the second one. However, the nature of the problem here is completely different: while in the previous I focused on sectors, here such sectors are nothing more than a detail. What it really matters is why some companies, if any, were able to differentiate in a positive way their results.

Analysis

First of all, let’s plot the country comprised in every region because it will be useful later during the analysis:

Countries in the European market

UK
Belgium
France
Switzerland
Spain
Netherlands
Italy
Ireland
Germany
Finland


Countries in the Asian market



China
Taiwan
Hong Kong
Singapore
South Korea
Macau


Countries in the American market





United States
Bermuda



Each day in the financial market is represented by 4 fundamental values:

Open value;
Close value;
Highest value;
Lowest value;

In order to roughly inspect the distribution of the data I calculated the average value between the highest and lowest price of the day. Although it doesn’t perfectly represent the day (if the high or low price was a mistake from a trader the average could change a lot),such average is often used in finance because a small error in a particular day doesn’t affect the overall trend of the stock and, however, is pretty rare.
 
This first visualization suggests that the european market holds more value compared to the american and asian. However, this chart doesn’t embed the time variable, so it represents both the situation pre-Covid and post-Covid.For such reason, it’s legitimate to think that it cannot depict the real situation. 
A refinement to this is to split the data and to produce two different charts, one for the days before the outbreak and one after: 

Although it’s hard to decide where to split, I considered that the first lockdown in China happened January 25th 2020 and its effects were perceived with a delay of some weeks around the world. For that reason, I fixed on March 1st 2020 the date in which I split the data. Using the same values for the x-axis is trivial to notice that all the regions moved backward in terms of value per day. Nevertheless, here I found the first surprise of the analysis. Before the pandemic, the European market was far from the Asian one, which in turn was far from the American one. It’s interesting to notice that after Covid-19 the markets are closer than before. Here the situation seems to reflect the first part of the motto: a rising tide (Covid outbreak) lifted all the boats (stock markets), however this chart is insufficient to explain the second part of the sentence. Who’s swimming naked?
Before finding a meaning to the second sentence it’s important to explain why the previous  is insufficient: The problem is that it doesn’t really exploit the time variable: although it shows that in the second part of the year the market shifted their averages, it doesn’t really explain the trends. 
Therefore, I created a new chart:


First things first, let’s get rid of the outlier. It seems that well before the first lockdown all the market experienced a significant vertical fall. I positioned a vertical dashed line on that day and I labelled it as ‘Christmas’. I think it’s self explanatory: during christmas day the stock markets close, therefore no data were registered. 
After this side note, let’s go back to the analysis. For every region, I identified the first lockdown that happened in a belonging country with a dashed line colored in the same way. 
It’s evident how the markets react to lockdown: European and Asian markets experienced a significant fall after their lockdown and America didn’t have such a drop after its lockdown only because the market lost a lot in the past week due to the other market’s losses. 
The continuous grey line represents the split I did on the date in the previous chart and it divides this chart in a left and a right part. 
The right part is where the markets reacted to the crisis and is also where I looked for ‘naked swimmers’: while the american and asian markets were fast to recover, the European struggles: the gap between Europe and the other indices is halved.  

So far, my analysis gave me an insight about  how the crisis affected the companies in different regions of the world. 

Although a stock index provides an overall feeling about the health of a market, for its own nature is very general, therefore it tends to underestimate some economic sectors and overestimate some others. The indices are no longer sufficient, so from now onward I’ll use the historical stock prices of several companies. 
Let’s take a look at the economic sectors represented in each region:




Even though all the markets have the same sectors represented, the weight of every sector can be very different, so let’s examine the ones that differ the most.
Let’s start with the Healthcare system:

Europe
Asia
America



11.61%
2.12%
12.589%

In China it’s basically free because the State provides it, therefore the sector is not relevant (The 2.12% that we can observe there belongs to a south korean company) whereas in America and Europe the private healthcare is a wealthy sector.

Let’s now move to the Industrials sector:

Europe
Asia
America



17.40%
4.29%
13.605%

This particular portion of the charts surprised me: while the Industrials is very influential in the american and european markets, it’s less than 5% in the asian one. Since half of the companies in the asian market are either chinese, from Hong Kong or from Macau I expected a high percentage of the Industrials sector in the asiatic market. The conclusion I had is that the non-chinese companies come from small countries (Taiwan, South Korea,Singapore,) and because of the small dimensions it’s very hard for the Industrials sector to result as profitable as the sectors that are based on immaterial or tech products.


In fact, almost 80% of the non-chinese companies confirm my hypothesis. 

Now that I have a better understanding of the sectors I want to know how they evolved during the last year. Let’s start with the European market:



The European sector confirms what we inspected in the analysis of the indices: most of them are struggling to get back to their original price. The only exception is Technology, which increased rapidly. Let’s take a closer look to it:
 
While the grey lines belong to companies that didn’t improve their stock price at the end of the year, the colored ones were the companies that were able to react in a fast way to the pandemic. Especially Adyen experienced a high growth during this period of time. Personally I didn’t know Adyen, but after a research it came up that it’s a company that offers businesses a way to accept online payments.

In the Asian market the situation is pretty close to the one in Europe: one specific sector grew a lot, while the others were pretty much stable. In this case the sector to analyze is the Basic Material:



it’s possible to notice that LG Chem improved its stock price in a relevant way. Such company has three main business areas: 

IT and electronics;
Basic material and chemicals;
Energy Solutions;

and it’s based in Seoul, South Korea. 

As for the American market, although after the pandemic all of the sectors are following a similar trend which is slightly positive, the Consumer Cyclical is the one that really stood out. By analyzing the trend of the company in this sector we can see that:



Most of the companies here are experiencing a growth, but none of them like Amazon. Throughout the last year Amazon was able to double its stock price. 
In fact, Amazon had such a big improvement that it sparked my curiosity to compare its stock to Alphabet and the results are the following:
 


While Alphabet suffered a big fall due to the pandemic, Amazon rapidly increased its stock price in these months. If before the crisis there was a big gap between Alphabet and Amazon, not only now this gap doesn’t exist, Amazon stock price even surpassed the Alphabet one, very impressive.
Moreover, Amazon growth made me wonder how other companies that have a similar core business did during the pandemic.
For such reason I analyzed Amazon, Ebay, Zalando, Alibaba and Asos:



Since they have very different stock prices I normalized their averages and then visualized such normalized data in the usual timeframe. Because I used a MinMax normalization, the data of each company are scaled according to its maximum and minimum value, the biggest the gap between the begin and the end of the line, the biggest the growth of the company during the year and it’s trivial to note how all of them grew, especially Amazon and Alibaba. The fact that these two companies had value close to zero at the beginning of the timeframe means that, even though they experienced the pandemic, they never performed worse than September 2019, so they were able to adapt to the economy and suffered a minimal loss. The same thing cannot be said for the other, nevertheless they had a noticeable year in terms of stock price performance.

Conclusions

Let’s wrap up the insights I had during my analysis:
During special times like the one we are experiencing, being able to adapt to a new scenario is extremely hard. It’s evident how the market in which a company operates influences the stock prices of the company itself. However, there are few cases of businesses that can outperform the overall trends, either for an opportunity that arises, like Adyen for instance, or because of their ability to provide a service in a better or more efficient way, like Amazon and Alibaba compared to the other ecommerce platforms.
The bottom line is that companies shouldn’t think of the stock market fluctuations as vortices that trap them, but more of new opportunities to catch. 

