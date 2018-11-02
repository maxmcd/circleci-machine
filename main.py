import requests

resp = requests.get(
    "https://circleci.com/api/v1.1/project/github/maxmcd/circleci-machine/4/output/105/0",
    headers={
        "x-csrftoken": "gLHg73A1QUm7T1fpz4u2r8gvnb63RXdq3BsXEZ8rkcgZ6lNjd2tzhaTThwSklbIaolCatWfiZZmMbfFn"
    },
)
# import ipdb; ipdb.set_trace()
print(resp.content)

resp = requests.post("https://circleci.com/api/v1.1/project/github/maxmcd/circleci-machine/5/cancel?circle-token=09ca4c223222d76691b632b9c22b0e280a0876e5")
print(resp, resp.content)
# resp = requests.post("https://circleci.com/api/v1.1/project/github/maxmcd/circleci-machine/3/ssh?circle-token=09ca4c223222d76691b632b9c22b0e280a0876e5")
# print(resp, resp.content)
