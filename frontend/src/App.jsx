import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [memos, setMemos] = useState([]);
  const [newMemo, setNewMemo] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // 環境変数からAPIのベースURLを取得
  const apiUrl = import.meta.env.VITE_API_URL;

  // メモ一覧を取得する関数
  const fetchMemos = async () => {
    if (!apiUrl) {
      setError("エラー: APIのURLが設定されていません。");
      setLoading(false);
      return;
    }
    try {
      const response = await axios.get(apiUrl);
      setMemos(response.data);
    } catch (err) {
      setError('メモの取得に失敗しました。');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // 初回レンダリング時にメモを取得
  useEffect(() => {
    fetchMemos();
  }, []);

  // メモを登録する関数
  const handleAddMemo = async (e) => {
    e.preventDefault();
    if (!newMemo.trim()) return;

    try {
      const response = await axios.post(apiUrl, { content: newMemo });
      // 成功したら一覧を再取得する代わりに、ローカルのstateを更新して即時反映
      setMemos([...memos, response.data]);
      setNewMemo('');
    } catch (err) {
      setError('メモの追加に失敗しました。');
      console.error(err);
    }
  };

  return (
    <div className="App">
      <h1>サーバーレス メモアプリ</h1>
      <p>CDハンズオンへようこそ！</p>
      
      <form onSubmit={handleAddMemo} className="memo-form">
        <input
          type="text"
          value={newMemo}
          onChange={(e) => setNewMemo(e.target.value)}
          placeholder="新しいメモを入力..."
        />
        <button type="submit">追加</button>
      </form>

      {error && <p className="error">{error}</p>}

      <div className="memo-list">
        <h2>メモ一覧</h2>
        {loading ? (
          <p>読み込み中...</p>
        ) : (
          <ul>
            {memos.map((memo) => (
              <li key={memo.id}>{memo.content}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;