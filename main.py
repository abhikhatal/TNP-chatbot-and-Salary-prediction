api_key = "sec_qZYPzLfgwv2bapxOVP6vXnE9gzULdL9z"

import requests


files = [
    ('file', ('file', open('ilovepdf_merged.pdf', 'rb'), 'application/octet-stream'))
]

headers = {
    'x-api-key': api_key
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)


source_id = str(response.json()['sourceId'])
print(source_id)

# headers = {
#     'x-api-key': api_key,
#     "Content-Type": "application/json",
# }
# sr_id = "src_3iUmYHzF4AFnzL6libjq6"
# data = {
#     'sourceId': sr_id,
#     'messages': [
#         {
#             'role': "user",
#             'content': "What is the pdf about?",
#         }
#     ]
# }
# # src_gXbjAzDaH7RQQ2Xv1yJ7s
# response = requests.post(
#     'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

# if response.status_code == 200:
#     print('Result:', response.json()['content'])
# else:
#     print('Status:', response.status_code)
#     print('Error:', response.text)

    