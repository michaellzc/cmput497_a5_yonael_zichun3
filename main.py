"""
Usage: main.py [OPTIONS]

Options:
  --train TEXT     Path to dataset to train the model.  [required]
  --test TEXT      Path to dataset to test the model.
  --evaluate TEXT  Path to dataset to evaluate the model.
  --help           Show this message and exit.
"""


import click

from cmput497_as5.classify import NaiveBayesClassifier
from cmput497_as5.utils import *


@click.command()
@click.option("--train", help="Path to dataset to train the model.", required=True)
@click.option("--test", help="Path to dataset to test the model.")
@click.option("--evaluate", help="Path to dataset to evaluate the model.")
def main(train, test, evaluate):
    train_dataset = get_dataset(train)

    if test:
        test_dataset = get_dataset(test)
    if evaluate:
        evaluate_dataset = get_dataset(evaluate)

    # TODO
    # train model
    # classifier = NaiveBayesClassifier.train()

    # classify model and save output
    # if test_dataset:
    #     test_predicited_labels = classifier.classify(test_dataset.text())
    #     test_dataset._set_predicted_labels(test_predicited_labels)
    #     save_output(test_dataset)

    # if evaluate_dataset:
    #     evaluate_predicited_labels = classifier.classify(evaluate_dataset.text())
    #     evaluate_dataset._set_predicted_labels(evaluate_predicited_labels)
    #     save_output(evaluate_dataset)


if __name__ == "__main__":
    main()
