import json

def json_function():
    data = '{"orders":[{"id":1,"customer":101,"items":["burger","fries"]}]}'
    parsed = json.loads(data)  # str → dict
    dumped = json.dumps(parsed, indent=2)  # dict → str


def main():
    pass


if __name__ == '__main__':
    main()