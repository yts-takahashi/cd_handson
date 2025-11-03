import json

def lambda_handler(event, context):
    """
    常に固定のメモ一覧を返す関数。
    """
    mock_memos = generate_random_memos(5)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        },
        'body': json.dumps(mock_memos)
    }

def generate_random_memos(n):
    import random
    import string

    memos = []
    for i in range(n):
        content = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        memos.append({'id': str(i + 1), 'content': content})
    return memos