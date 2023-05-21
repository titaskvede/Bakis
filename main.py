from teacher import Teacher
from questions import Questions
import json
import os
import time


class Main:
    def __init__(self):
        """
        Main class of the program,
        :self.Questions: Holds a class Questions, which is responsible for all the questions which will be asked
        :self.data_res: Dictionary which holds results to question's and time it took to execute
        :self.model_list: Testable model list. This is a static list and is not changed.
        """
        self.Questions = Questions()
        self.data_res = {}
        self.model_list = [
            # "gpt-3.5-turbo",
            "gpt-3.5-turbo-0301",
            # "text-davinci-003",
            # "text-davinci-002",
            # "text-curie-001",
            # "text-babbage-001",
            # "text-ada-001"
        ]

    def test_chatgpt3(self, message_list, model="gpt-3.5-turbo"):
        """
        Function responsible for testing a specific model, with a given message list.
        :param message_list: a list of questions from class Questions
        :param model: a single model, from self.model_list
        :return: None
        """
        app = Teacher()
        for m in message_list:
            # if "turbo" in model:
            #     time.sleep(30)
            res = app.ask(m, model)
            # app.messages = [
            # {"role": "system", "content": "You are a teacher bot to help user understand bioinformatics."},
        # ]
            try:
                self.data_res[m] = {
                    "time": res[1],
                    "answer": res[0]
                }
            except AttributeError:
                self.data_res[m] = {
                    "time": res[1],
                    "answer": res[0][0]
                }

    @staticmethod
    def save_to_json(dict_to_save: dict, model_name: str,
                     json_name=time.asctime().replace(" ", "_")+".json", clean=False):
        """
        Function saves the created result dictionary to a json.
        :param dict_to_save: Result dictionary
        :param model_name: Tested model, this will be used in output name
        :param json_name: Jason name, which is created based on time the test was run
        :param clean: Flag which forces appending or cleaning the already existing jsons
        :return: None
        """
        json_name = json_name.replace(":", "_")
        json_name = f"{model_name}_{json_name}"
        if os.path.exists(json_name) and not clean:
            with open(json_name, 'r') as f1:
                dict1 = json.load(f1)
            dict_to_save = {**dict1, **dict_to_save}
        with open(json_name, "w") as outfile:
            # TODO make it save as a new line
            json.dump(dict_to_save, outfile)


main = Main()
for model in main.model_list:
    print(f"\t {model}")
    # main.test_chatgpt3(main.Questions.return_specific_questions("easy"), model)
    main.test_chatgpt3(main.Questions.questions, model)
    main.save_to_json(main.data_res, model, clean=True)

