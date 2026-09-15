from api_client import get_posts, create_post, update_post, delete_post, request


url="https://jsonplaceholder.typicode.com/posts"

result = request("GET", url)

print(type(result))
print(len(result))


posts = get_posts(limit=5)

print(type(posts))

print("Total posts:", len(posts))

new_post = create_post(
    "Testing reusable client",
    "POST now uses the request layer.",
    2
)

print(new_post)


print(update_post(101, title="New title"))
print(update_post(101, body="New body"))
print(update_post(101, title="New title", body="New body"))

print(delete_post(101))
