from flask import Flask, render_template
import requests
import feedparser
from datetime import datetime

app = Flask(__name__)

# Weather API configuration
WEATHER_API_KEY = 'your_openweather_api_key'
CITY = 'your_city'
WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric"

# RSS Feed URL for news
RSS_FEED_URL = 'http://rss.cnn.com/rss/edition.rss'

# Get weather data
def get_weather():
    response = requests.get(WEATHER_URL)
    weather_data = response.json()
    return {
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'].capitalize(),
        'city': weather_data['name']
    }

# Get news headlines
def get_news():
    news_feed = feedparser.parse(RSS_FEED_URL)
    headlines = [entry.title for entry in news_feed.entries[:5]]
    return headlines

@app.route('/')
def index():
    now = datetime.now()
    time_str = now.strftime("%H:%M")
    date_str = now.strftime("%A, %B %d, %Y")
    
    weather = get_weather()
    news = get_news()

    # Random compliments or quotes
    compliments = ["You're amazing!", "Keep smiling!", "You're doing great!"]
    
    return render_template('index.html', time=time_str, date=date_str, weather=weather, news=news, compliments=compliments)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
