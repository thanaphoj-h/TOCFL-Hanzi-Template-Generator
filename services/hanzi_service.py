from models.request.hanzi_request import HanziRequest
from models.response.hanzi_response import HanziResponseItem


class HanziService:

    @staticmethod
    def process_hanzi(request: HanziRequest) -> list[HanziResponseItem]:

        response = []

        for item in request.data:
            raw_words = item.words
            
            word_list = raw_words.strip().replace("\n", " ").split()

            response.append(
                HanziResponseItem(
                    words=word_list,
                    words_count=len(word_list)
                )
            )
        return response