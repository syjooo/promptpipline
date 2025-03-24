from fastapi import APIRouter
from app.services.chathistory_services import ChatHistoryService

router = APIRouter(prefix="/history", tags=["Chat History"])
history_service = ChatHistoryService()

@router.get("/savechat")
def save_chat():
    return {"conversation": history_service.save_chat()}



"""사용자별 저장 구현시 코드"""
""" 
from fastapi import APIRouter, Query
from pydantic import BaseModel
from app.services.chathistory_services import ChatHistoryService

router = APIRouter(prefix="/history", tags=["Chat History"])
history_service = ChatHistoryService()

# 요청 모델
class ChatInput(BaseModel):
    user_id: str
    user_input: str
    bot_response: str

# 새로운 세션 시작
@router.post("/start")
def start_new_session(user_id: str = Query(..., description="사용자 ID")):
    history_service.start_new_session(user_id)
    return {"message": f"{user_id}의 세션이 초기화되었습니다."}

# 대화 저장
@router.post("/save")
def save_chat(chat: ChatInput):
    history_service.save_chat(chat.user_id, chat.user_input, chat.bot_response)
    return {"message": "대화가 저장되었습니다."}

# 대화 기록 조회
@router.get("/{user_id}")
def get_chat_history(user_id: str):
    history = history_service.get_user_history(user_id)
    return {"conversation": history}
"""
