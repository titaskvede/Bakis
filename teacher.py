import openai
import time


def calculate_time(func):
    """
    Decorator responsible for calculating the time it took to ask and receive a question
    :return: dictionary with time and result
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Function {} took {:.2f} seconds to run.".format(func.__name__, end_time - start_time))
        return [result, end_time - start_time]
    return wrapper


class Teacher:
    """
    Class responsible for asking the questions to the AI models.
    All the communication to API is done here
    """
    def __init__(self):
        # Setting the API key to use the OpenAI API
        openai.api_key = "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"
        self.messages = [
            {"role": "system", "content": "You are a teacher bot to help user understand bioinformatics."},
        ]

    def ask_davinci(self, model, message):
        response = openai.Completion.create(
            model=model,
            prompt=message,
            # max_tokens=5000
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["text"]})
        return response["choices"][0]["text"]

    def ask_turbo(self, model, message):
        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,

        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        return response["choices"][0]["message"].content

    @calculate_time
    def ask(self, message, model):
        try:
            print(f"\n\n \t {message} \n\n")
            if "turbo" in model:
                response = self.ask_turbo(model, message)
            else:
                # Models Davinci, Curie, Babbage and Ada are called in the same way
                response = self.ask_davinci(model, message)
            return response
        except openai.error.Timeout as e:
            print(e)
            return f"TIMEOUT: {e}"
        except openai.error.RateLimitError as e:
            print(e)
            time.sleep(30)
            return f"RATE LIMIT: {e}"
        except openai.error.APIError as e:
            print(e)
            return f"BAD GATEWAY: {e}"
        except openai.error.InvalidRequestError as e:
            print(e)
            return f"TOO LONG:{e}"

