import json

def lambda_handler(event, context):
    """
    常に固定のメモ一覧を返す関数。
    """
    mock_memos = [
        {'id': '1', 'content': 'CDハンズオンの準備をする'},
        {'id': '2', 'content': 'Reactのコンポーネントを修正する'},
        {'id': '3', 'content': 'デプロイパイプラインを動かしてみる'}
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