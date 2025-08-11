# Import necessary libraries
import time  # For adding delays between retry attempts
import redis  # Redis client library for database operations
from flask import Flask  # Flask web framework for creating the web application

# Create a Flask application instance
app = Flask(__name__)

# Establish connection to Redis server
# 'redis' is the hostname (The Docker service name)
# 6379 is the default Redis port
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    """
    Function to increment and return the hit counter with retry logic.
    Implements fault tolerance for Redis connection issues.
    """
    retries = 5  # Maximum number of retry attempts
    
    while True:  # Infinite loop until successful or all retries exhausted
        try:
            # Increment the 'hits' key in Redis by 1 and return the new value
            # incr() is atomic - safe for concurrent access
            return cache.incr('hits')
        
        except redis.exceptions.ConnectionError as exc:
            # Handle Redis connection failures
            if retries == 0:
                # No more retries left, re-raise the exception
                raise exc
            
            # Decrease retry counter
            retries -= 1
            # Wait 0.5 seconds before trying again
            time.sleep(0.5)

# Define the root route of the web application
@app.route('/')
def hello():
    """
    Main route handler for the homepage.
    Increments visit counter and displays greeting message.
    """
    # Get the current hit count (increments automatically)
    count = get_hit_count()
    
    # Return HTML response with personalized message and visit count
    # The .format() method inserts the count value into the string
    return 'Hi visitor! Welcome to the website!, I have been seen {} times.\n'.format(count)

# Note: To run this app, you would typically add:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
