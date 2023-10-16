from project_service.service import GreetingService


def test_service():
    greeting_service: GreetingService = GreetingService()
    greeting_service.greet_message()