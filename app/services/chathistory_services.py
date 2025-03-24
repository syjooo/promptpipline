import os
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatHistoryService:
    def __init__(self):
        base_path = os.path.join(os.path.dirname(__file__), "../data")
        self.chat_file = os.path.join(base_path, "chat_archive.json")

        if not os.path.exists(self.chat_file):
            with open(self.chat_file, "w", encoding="utf-8") as file:
                json.dump({"conversation": []}, file)

    def save_chat(self, user_input: str, bot_response: str):
        """사용자 입력과 챗봇 응답을 JSON 파일에 저장"""
        try:
            with open(self.chat_file, "r", encoding="utf-8") as file:
                chat_data = json.load(file)

            chat_data["conversation"].append({
                "user": user_input,
                "bot": bot_response
            })

            with open(self.chat_file, "w", encoding="utf-8") as file:
                json.dump(chat_data, file, ensure_ascii=False, indent=4)

            logger.info("대화가 저장되었습니다.")
        except Exception as e:
            logger.error(f"대화 기록 저장 중 오류 발생: {e}")