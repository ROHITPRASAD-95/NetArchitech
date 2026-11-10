class ExplainabilityEngine:

    @staticmethod
    def generate_explanation(media_result, routing_result):

        explanation = []

        explanation.append(
            "MEDIA SELECTION:"
        )
        explanation.append(
            f"Selected: {media_result['media']}"
        )
        explanation.append(
            f"Reason: {media_result['reason']}"
        )

        explanation.append(
            "\nROUTING SELECTION:"
        )
        explanation.append(
            f"Selected: {routing_result['protocol']}"
        )
        explanation.append(
            f"Reason: {routing_result['reason']}"
        )

        return "\n".join(explanation)