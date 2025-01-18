# InstagramFeed\social/tasks.py
from celery import shared_task
from datetime import datetime
import time

@shared_task
def notify_new_comment(post_title, author_name, comment_content):
    # Simulate complex processing
    print(f"\n[{datetime.now()}] Starting to process comment notification...")
    print(f"Analyzing comment sentiment...")
    time.sleep(1000)  # Simulate sentiment analysis
    
    print(f"Fetching follower list for post: {post_title}...")
    time.sleep(30000)  # Simulate database query
    
    print(f"Sending email notifications to followers...")
    time.sleep(2)  # Simulate email sending
    
    print(f"\nCompleted processing comment by {author_name} on post '{post_title}'")
    print(f"Comment content: {comment_content}")
    return True