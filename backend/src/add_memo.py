import json
import uuid

def lambda_handler(event, context):
    """
    メモを追加するフリをして、受け取った内容にIDを付けて返すだけの関数。
    データはどこにも保存されない。
    """
    try:
        body = json.loads(event.get('body', '{}'))
        content = body.get('content', 'No content')

        # 本物のAPIのように、作成されたリソースを模したレスポンスを返す
        new_item = {
            'id': str(uuid.uuid4()),
            'content': content
        }

        return {
            'statusCode': 201, # 201 Created
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
            'body': json.dumps(new_item)
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}