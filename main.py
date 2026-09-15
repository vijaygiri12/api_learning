from api_client import get_posts, create_post, update_post, delete_post

posts = get_posts()

print("Total posts:", len(posts))
"""for post in posts:
    print(post["id"], "-", post["title"])
"""
posted = create_post(
    "Learning Python APIs",
    "Building my first API client.",
     2
)
print(posted)
print(type(posted))

print(update_post(101, title="New title"))

print(update_post(101, body="New body"))

print(update_post(101, title="New title", body="New body"))

print(delete_post(101))
