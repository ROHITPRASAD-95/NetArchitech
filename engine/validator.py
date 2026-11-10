
class InputValidator:

    @staticmethod
    def validate_distance(distance):

        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be numeric")

        if distance <= 0:
            raise ValueError("Distance must be positive")

        return True

    @staticmethod
    def validate_endpoints(endpoints):

        if not isinstance(endpoints, int):
            raise TypeError("Endpoints must be an integer")

        if endpoints <= 0:
            raise ValueError("Endpoints must be positive")

        return True

    @staticmethod
    def validate_resiliency(level):

        allowed = ["low", "medium", "high"]

        if level.lower() not in allowed:
            raise ValueError("Invalid resiliency level")

        return True
