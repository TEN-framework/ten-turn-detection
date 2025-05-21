# 🗣️ Ten Turn Detection - WebSocket 协议说明

Ten Turn Detection 是一个基于 WebSocket 的轮次检测服务，用于判断用户发言是否已结束。适用于语音助手、对话系统等需要明确轮次边界的场景。

---

## 🔌 WebSocket 地址

---



## 📤 客户端 → 服务端 消息格式

客户端发送用户发言内容，请求判断本轮对话是否结束。

```json
{
  "type": "message",
  "payload": {
    "user_id": "user-123",
    "timestamp": 1716182400000,
    "text": "请帮我订一张明天下午三点去上海的票"
  }
}
```

| 字段名               | 类型     | 说明               |
|-------------------|--------|------------------|
| type              | string | 消息类型，固定为 message |
| payload.user_id   | string | 用户 id            |
| payload.timestamp | int64  | 毫米时间戳            |
| payload.text      | string | 用户说话的文本内容        |



## 📤 服务端 → 客户端 消息格式

---
```json
{
  "type": "turn_result",
  "payload": {
    "user_id": "user-123",
    "timestamp": 1716182400000,
    "status": "finished"
  }
}
```

| 字段名               | 类型     | 说明                           |
|-------------------|--------|------------------------------|
| type              | string | 消息类型，固定为 turn_result         |
| payload.user_id   | string | 用户 id                        |
| payload.timestamp | int64  | 毫米时间戳                        |
| payload.status      | string | 发言是否结束：finished 或 unfinished |


## 💓心跳
客户端每隔 N 秒发送一次 ping：
```json
{ "type": "ping", "payload": { "timestamp": 1690001234 } }
```
服务端回应：
```json
{ "type": "pong", "payload": { "timestamp": 1690001234 } }
```

