
from engine.validator import InputValidator


class MediaEngine:

    @staticmethod
    def recommend_media(distance):

        InputValidator.validate_distance(distance)

        if distance <= 100:
            return {
                "media": "Cat6a",
                "reason": "Suitable for distances up to 100 meters."
            }

        elif distance <= 400:
            return {
                "media": "OM4 Multimode Fiber",
                "reason": "Suitable for medium-distance connections."
            }

        else:
            return {
                "media": "OS2 Singlemode Fiber",
                "reason": "Suitable for long-distance connections."
            }
