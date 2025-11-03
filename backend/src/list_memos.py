import json

def lambda_handler(event, context):
    """
    常に固定のメモ一覧を返す関数。
    """
    mock_memos = [
        {'id': '1', 'content': 'APIの実装をする'},
        {'id': '2', 'content': 'フロントエンドの実装をする'},
        {'id': '3', 'content': 'CI/CDの設定をする'},
    ]

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        },
        'body': json.dumps(mock_memos)
    }