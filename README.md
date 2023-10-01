# CalYrDiv

## About me

Hi there! Thanks for taking the time to read this README. My name is Barry (‘Hello, other Barry’) and this is the first app I’ve ever developed! As someone without a background in anything software development or IT related, I’m actually a little proud of myself.

The last couple years I started taking an interest in data and data-analysis. I have been using Excel (or Apple Numbers) for insight in my personal finances for a while now but realized that I wanted to be able to do more than fiddle with formulas and pivot tables. So two months ago I started learning Python, reading and/or practicing for half an hour a day (and usually longer). Fast forward to October 2023 and here we are, my first app!

## About CalYrDiv

First, the name. CalYrDiv is short for Calculate Your Dividend and is chosen because it sounds somewhat mythological (and because I really like Zeppelins).

It’s is a very simple program written in Python that extracts the amount of dividend you’ve received from the stocks in your DeGiro portfolio. It takes .csv files as input, removes several columns that aren’t needed, looks for the lines that contain ‘dividend’ and calculates the total dividend per stock and per currency. The pandas library is used to do all this.

## Why go through all the trouble when there a dozen similar apps?

Good question! Of course there are numerous apps similar to this one. However, since I just started learning Python, I needed something real to keep practicing and learning. Of course there is still a lot I don’t know, but with this project I learned the basics of the pandas library and Streamlit.

## How to use

It’s very simple! First, log in with your DeGiro account, go to 'inbox' and select 'account statement'. Select the start and end date. Then export as .csv file. Use the file selector in the program to select or drag and drop the file from your downloads folder. The program should go to work right away!

## Two versions?

Yes! V0.9 is a .py file that can be used within an IDE and is the original code. The official version is made for deploying on Streamlit.

## What’s next?

Next, I’ll be adding different features and other relevant data.









