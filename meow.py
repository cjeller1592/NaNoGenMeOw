import requests

##### Function to produce the 50k meows
def meow():

    list = []

    x = range(0, 50001)

    for cat in x:
        cat = 'meow'
        list.append(cat)

    resp = str('\n'.join(map(str, list)))

    return resp

##### Post the 50k meows to Write.as
def main():

# The Write.as posts endpoint you will send your meows to
    url = 'https://write.as/api/posts'

# Putting the 50k meows into the body variable
    body = meow()

# Data to send into the request - body and title (optional)
    data = {'body': body, 'title': 'NaNoGenMeOw'}

# Send the request to Write.as
    r = requests.post(url, data=data)

# If successful, get the post id from the json response
    id = r.json()['data']['id']

# Return the link to the Write.as post
    return 'Get your novel right meow: https://write.as/{}'.format(id)
