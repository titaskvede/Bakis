import os
import json
from questions import Questions
import matplotlib.pyplot as plt

class Analysis:
    path_to_data = None
    model_answer_dict = None

    def __init__(self):
        self.questions = None
        self.path_to_data = os.path.join(os.getcwd(), "data")
        self.model_answer_dict = {
            "gpt-3.5-turbo-0301": {},
            "gpt-3.5-turbo_": {},
            "ada": {},
            "babbage": {},
            "davinci": {},
            "curie": {}
        }
        self.question_to_model_alignment = {
        }

    def group_answers(self):
        """
        Takes a data folder, and based on names separates into a different elements
        :return: None
        """
        for file in os.listdir(self.path_to_data):
            if os.path.isdir(os.path.join(self.path_to_data, file)):
                continue
            else:
                with open(os.path.join(self.path_to_data, file)) as f:
                    for model in self.model_answer_dict:
                        if model in file:
                            name_of_elem = file.split(model)[1]
                            try:
                                data_of_elem = json.load(f)
                            except json.decoder.JSONDecodeError:
                                print()
                            self.model_answer_dict[model][name_of_elem] = data_of_elem
                            break
        with open(os.path.join(os.getcwd(), "group_data.json"), 'a') as file:
            file.write('\n')  # Add a newline character to separate the data
            json.dump(self.model_answer_dict, file)

    def answer_to_model(self):
        """
        prepares a dict questions to model, for analysis
        :return:
        """
        question_list = Questions().questions

        for question in question_list:
            if question not in self.question_to_model_alignment:
                self.question_to_model_alignment[question] = {}
            for model in self.model_answer_dict:
                if model not in self.question_to_model_alignment[question]:
                    self.question_to_model_alignment[question][model] = {}
                for time_frame in self.model_answer_dict[model]:
                    self.question_to_model_alignment[question][model][time_frame] = \
                        self.model_answer_dict[model][time_frame][question]

        with open(os.path.join(os.getcwd(), "results.json"), 'a') as file:
            file.write('\n')  # Add a newline character to separate the data
            json.dump(self.question_to_model_alignment, file)

    @staticmethod
    def remove_unnecessary_data():
        change = False
        for file in os.listdir(os.path.join(os.getcwd(), "data")):
            if os.path.isdir(os.path.join(os.getcwd(), "data", file)):
                continue
            else:
                with open(os.path.join(os.getcwd(), "data", file)) as f:
                    temp = json.load(f)
                    if temp.__len__() < 99 or temp.__len__() == 100:
                        change = True
                if change:
                    os.rename(os.path.join(os.getcwd(), "data", file),
                              os.path.join(os.getcwd(), "data", "depricated_data", file))
                    change = False

    def load_data(self):
        with open("results.json") as file:
            self.model_answer_dict = json.load(file)
        with open("group_data.json") as file:
            self.question_to_model_alignment = json.load(file)
        print()

    def calculating_all_failed(self):
        total_tests = 0
        failed_tests = 0
        passed_tests = 0
        difficulty = {
            "easy": {
                "model_speed": [],
                "passed": 0,
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            },
            "medium": {
                "model_speed": [],
                "passed": 0,
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            },
            "hard": {
                "model_speed": [],
                "passed": 0,
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            },
            "very hard": {
                "model_speed": [],
                "passed": 0,
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            }
        }
        model_results = {
            "gpt-3.5-turbo-0301": {
                "passed": 0,
                "total": 0,
                "model_speed": [],
                "model_speed_difficulty": {
                    "easy": [],
                    "medium": [],
                    "hard": [],
                    "very hard": []
                },
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            },
            "gpt-3.5-turbo_": {
                "passed": 0,
                "total": 0,
                "model_speed": [],
                "model_speed_difficulty": {
                    "easy": [],
                    "medium": [],
                    "hard": [],
                    "very hard": []
                },
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            },
            "ada": {
                "passed": 0,
                "total": 0,
                "model_speed": [],
                "model_speed_difficulty": {
                    "easy": [],
                    "medium": [],
                    "hard": [],
                    "very hard": []
                },
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            },
            "babbage": {
                "passed": 0,
                "total": 0,
                "model_speed": [],
                "model_speed_difficulty": {
                    "easy": [],
                    "medium": [],
                    "hard": [],
                    "very hard": []
                },
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            },
            "davinci": {
                "passed": 0,
                "total": 0,
                "model_speed": [],
                "model_speed_difficulty": {
                    "easy": [],
                    "medium": [],
                    "hard": [],
                    "very hard": []
                },
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            },
            "curie": {
                "passed": 0,
                "total": 0,
                "model_speed": [],
                "model_speed_difficulty": {
                    "easy": [],
                    "medium": [],
                    "hard": [],
                    "very hard":[]
                },
                "TOO LONG": 0,
                "RATE LIMIT": 0,
                "BAD GATEWAY": 0,
                "failed": 0
            }
        }
        failures = {
            "TOO LONG": 0,
            "RATE LIMIT": 0,
            "BAD GATEWAY": 0,
        }
        questions_dict = Questions().return_dict_questions()
        for question in self.model_answer_dict:
            for model in self.model_answer_dict[question]:
                for timestamp in self.model_answer_dict[question][model]:
                    if self.model_answer_dict[question][model][timestamp]["answer"][0].isupper() and \
                            self.model_answer_dict[question][model][timestamp]["answer"][1].isupper():
                        model_results[model]["failed"] += 1
                        model_results[model]["total"] += 1
                        # model_results[model]["model_speed"].append(self.model_answer_dict[question][model]
                        #                                            [timestamp]["time"])
                        for reason in failures:
                            if reason in self.model_answer_dict[question][model][timestamp]["answer"]:
                                failures[reason] +=1
                                model_results[model][reason]+=1
                        failed_tests += 1
                        total_tests += 1
                        for diff in questions_dict:
                            for test in questions_dict[diff]:
                                if test == question:
                                    difficulty[diff]["failed"] +=1
                                    for reason in failures:
                                        if reason in self.model_answer_dict[question][model][timestamp]["answer"]:
                                            difficulty[diff][reason] += 1
                                    difficulty[diff]["model_speed"].append(self.model_answer_dict[question][model]
                                                                               [timestamp]["time"])

                    else:
                        model_results[model]["model_speed"].append(self.model_answer_dict[question][model]
                                                                   [timestamp]["time"])
                        for diff in questions_dict:
                            for test in questions_dict[diff]:
                                if test == question:
                                    difficulty[diff]["passed"] +=1
                                    for reason in failures:
                                        if reason in self.model_answer_dict[question][model][timestamp]["answer"]:
                                            difficulty[diff][reason] += 1
                                    difficulty[diff]["model_speed"].append(self.model_answer_dict[question][model]
                                                                               [timestamp]["time"])
                                    model_results[model]["model_speed_difficulty"][diff].append(
                                        self.model_answer_dict[question][model]
                                        [timestamp]["time"])
                        total_tests += 1
                        passed_tests += 1
                        model_results[model]["passed"] += 1
                        model_results[model]["total"] += 1

        ask_question = 'What is the difference between DNA and RNA?'
        ask_question = 'What is a protein?'
        ask_question = "What is a codon?"
        ask_question = "What is a hidden Markov model (HMM) and how is it used in bioinformatics?           "
        models_already_answered = []
        for question in self.model_answer_dict:
            if question == ask_question:
                for models in self.model_answer_dict[question]:
                    for date in self.model_answer_dict[question][models]:
                        # if 'Tue_May__9' in date:
                            if models in models_already_answered:
                                pass
                            elif "TOO LONG" in self.model_answer_dict[question][models][date]['answer']:
                                pass
                            elif "RATE LIMIT" in self.model_answer_dict[question][models][date]['answer']:
                                pass
                            else:
                                print(f"\n\t Modelis: {models} \n \t Atsakymas: "
                                      f" {self.model_answer_dict[question][models][date]['answer']}")
                                models_already_answered.append(models)

        # self.draw_pie_chart([total_tests, failed_tests])
        self.answer_length_analysis(questions_dict)
        # self.boxplot(
        #     [model_results["gpt-3.5-turbo_"]["model_speed"], model_results["gpt-3.5-turbo-0301"]["model_speed"],
        #      model_results["ada"]["model_speed"], model_results["babbage"]["model_speed"],
        #      model_results["davinci"]["model_speed"], model_results["curie"]["model_speed"]],
        #     ["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "ada", "babbage", "davinci", "curie"], "Models",
        #     "Time it took to answer", "Model speed")
        # self.boxplot([model_results["ada"]["model_speed_difficulty"]["easy"],
        #               model_results["ada"]["model_speed_difficulty"]["medium"],
        #               model_results["ada"]["model_speed_difficulty"]["hard"],
        #               model_results["ada"]["model_speed_difficulty"]["very hard"]],
        #              ["Easy", "Medium", "Hard", "Very Hard"], "Models", "Time it took to answer", "Model speed")

    def answer_length_analysis(self, questions_dict):
        results_dict = {
            "davinci": {
                "easy": {
                    "lengths": [],
                    "average_length": 0
                },
                "medium": {
                    "lengths": [],
                    "average_length": 0
                },
                "hard": {
                    "lengths": [],
                    "average_length": 0
                },
                "very hard": {
                    "lengths": [],
                    "average_length": 0
                }

                        },
            "ada": {
                "easy": {
                    "lengths": [],
                    "average_length": 0
                },
                "medium": {
                    "lengths": [],
                    "average_length": 0
                },
                "hard": {
                    "lengths": [],
                    "average_length": 0
                },
                "very hard": {
                    "lengths": [],
                    "average_length": 0
                }

                        },
            "curie": {
                "easy": {
                    "lengths": [],
                    "average_length": 0
                },
                "medium": {
                    "lengths": [],
                    "average_length": 0
                },
                "hard": {
                    "lengths": [],
                    "average_length": 0
                },
                "very hard": {
                    "lengths": [],
                    "average_length": 0
                }

                        },
            "babbage": {
                "easy": {
                    "lengths": [],
                    "average_length": 0
                },
                "medium": {
                    "lengths": [],
                    "average_length": 0
                },
                "hard": {
                    "lengths": [],
                    "average_length": 0
                },
                "very hard": {
                    "lengths": [],
                    "average_length": 0
                }

                        },
            "gpt-3.5-turbo-0301": {
                "easy": {
                    "lengths": [],
                    "average_length": 0
                },
                "medium": {
                    "lengths": [],
                    "average_length": 0
                },
                "hard": {
                    "lengths": [],
                    "average_length": 0
                },
                "very hard": {
                    "lengths": [],
                    "average_length": 0
                }

                        },
            "gpt-3.5-turbo_":{
                "easy": {
                    "lengths": [],
                    "average_length": 0
                },
                "medium": {
                    "lengths": [],
                    "average_length": 0
                },
                "hard": {
                    "lengths": [],
                    "average_length": 0
                },
                "very hard": {
                    "lengths": [],
                    "average_length": 0
                }

                        },
        }

        for model in self.question_to_model_alignment:
            for date in self.question_to_model_alignment[model]:
                for question in self.question_to_model_alignment[model][date]:
                    if self.question_to_model_alignment[model][date][question]["answer"][0].isupper() and \
                            self.question_to_model_alignment[model][date][question]["answer"][1].isupper() and \
                            "messages resulted in" not in self.question_to_model_alignment[model][date][question]["answer"]:
                        continue
                    elif "messages resulted in" in self.question_to_model_alignment[model][date][question]["answer"]:
                        length = self.find_four_digit_numbers(self.question_to_model_alignment[model][date][question]["answer"])
                        for difficulty in questions_dict:
                            for question_of_diff in questions_dict[difficulty]:
                                if question_of_diff == question:
                                    pass
                                    # results_dict[model][difficulty]["lengths"].append(int(length[1]))
                    else:
                        for difficulty in questions_dict:
                            for question_of_diff in questions_dict[difficulty]:
                                if question_of_diff == question:
                                    if "turbo-0301" in model:
                                        print(len(self.question_to_model_alignment[model][date][question]["answer"]))
                                        if len(self.question_to_model_alignment[model][date][question]["answer"]) > 1400:
                                            print()
                                    results_dict[model][difficulty]["lengths"].append(len(
                                        self.question_to_model_alignment[model][date][question]["answer"]))

        # Calculate average
        for model in results_dict:
            for difficulty in results_dict[model]:
                try:
                    average = sum(results_dict[model][difficulty]["lengths"])/len(results_dict[model][difficulty]["lengths"])
                except ZeroDivisionError:
                    average = 0
                results_dict[model][difficulty]["average_length"] = average


        for model in results_dict:
            list_of_number = []
            for difficulty in results_dict[model]:
                list_of_number.append(results_dict[model][difficulty]["average_length"])
            self.create_bar_graph(list_of_number, "Difficulties", "Average length", f"{model} average length")

        for difficulty in ["easy", "medium", "hard", "very hard"]:
            list_of_numbers = []
            models = []
            for model in results_dict:
                models.append(model)
                list_of_numbers.append(results_dict[model][difficulty]["average_length"])
            self.create_bar_graph(list_of_numbers, "Models", "Average length", f"Difficulty {difficulty} average length",
                                  models)

        print()


    @staticmethod
    def create_bar_graph(numbers, xlabel, ylabel, title, x_labels=None):
        plt.figure()

        if x_labels is None:
            x_labels = ['easy', 'medium', 'hard', 'very hard']
        x_positions = range(len(numbers))
        if "ada" in title:
            print()
        plt.bar(x_positions, numbers)
        plt.xticks(x_positions, x_labels)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        # plt.show()
        plt.savefig(f"{title}.jpg")


    @staticmethod
    def find_four_digit_numbers(string):
        numbers = []
        current_number = ''

        for char in string:
            if char.isdigit():
                current_number += char
                if len(current_number) == 4:
                    numbers.append(current_number)
                    current_number = ''
            else:
                current_number = ''

        return numbers

    @staticmethod
    def remove_floats_above_30_2d(lst_2d):
        return [[x for x in sublist if not isinstance(x, float) or x <= 30] for sublist in lst_2d]

    @staticmethod
    def draw_pie_chart(sizes, title, label=None, save='bar_graph.png'):

        # Create the pie chart
        if label is None:
            label = ['Slice 1', 'Slice 2']
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=label, autopct='%1.1f%%')
        # Add a title to the chart
        ax.set_title(title)

        # Show the chart
        plt.show()
        plt.savefig(save)
        print()

    def boxplot(self, data, labels, xlabel, ylabel, title):
        # Example data
        # data = [[32, 45, 56, 39, 48, 55, 62], [44, 55, 11, 66, 77, 55, 55, 55, 66]]
        # data = self.remove_floats_above_30_2d(data)
        # Create a figure and axis
        fig, ax = plt.subplots()
        # data = data[2:]
        # Create a box plot
        box_plot = ax.boxplot(data)

        # Customize x-axis tick labels
        # labels = ['test 1', 'test 2']
        ax.set_xticklabels(labels)

        # Set labels and title
        # xlabel = 'Box Label'
        # ylabel = 'Values'
        # title = 'Box Plot'
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        # Show the plot
        plt.show()
        print()


    @staticmethod
    def draw_bar_graph(x, y, xlabel='X Label', ylabel='Y Label', title='Bar Graph Example', save='bar_graph.png'):
        # Create the bar graph
        fig, ax = plt.subplots()
        ax.bar(x, y)

        # Add labels to the graph
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        # Show the graph
        plt.show()
        plt.savefig(save)

    def main(self, default=False):
        self.questions = Questions().questions
        if default:
            self.remove_unnecessary_data()
            self.group_answers()
            self.answer_to_model()
        else:
            self.load_data()
            self.calculating_all_failed()
            print()

if __name__ == "__main__":
    analysis = Analysis()
    analysis.main()
