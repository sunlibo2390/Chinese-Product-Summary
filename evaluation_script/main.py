import random


def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")
    print("Submission related metadata:")
    """
    Evaluates the submission for a particular challenge phase adn returns score
    Arguments:

        `test_annotations_file`: Path to test_annotation_file on the server
        `user_submission_file`: Path to file submitted by the user
        `phase_codename`: Phase to which submission is made

        `**kwargs`: keyword arguments that contains additional submission
        metadata that challenge hosts can use to send slack notification.
        You can access the submission metadata
        with kwargs['submission_metadata']

        Example: A sample submission metadata can be accessed like this:
        >>> print(kwargs['submission_metadata'])
        {
            "status": u"running",
            "when_made_public": None,
            "participant_team": 5,
            "input_file": "https://abc.xyz/path/to/submission/file.json",
            "execution_time": u"123",
            "publication_url": u"ABC",
            "challenge_phase": 1,
            "created_by": u"ABC",
            "stdout_file": "https://abc.xyz/path/to/stdout/file.json",
            "method_name": u"Test",
            "stderr_file": "https://abc.xyz/path/to/stderr/file.json",
            "participant_team_name": u"Test Team",
            "project_url": u"http://foo.bar",
            "method_description": u"ABC",
            "is_public": False,
            "submission_result_file": "https://abc.xyz/path/result/file.json",
            "id": 123,
            "submitted_at": u"2017-03-20T19:22:03.880652Z",
        }
    """
    print(kwargs["submission_metadata"])
    output = {}
    print(phase_codename)
    if phase_codename == "product_csum":
        print("Evaluating for Product-Csum Phase")
        output["result"] = [
            {
                "product_csum": {
                    "BLEU":  41.38,
                    "ROUGE": 40.81,
                    "METEOR": 38.98,
                    "Fact.": 67.69 ,
                    "Compre.": 89.00,
                    "Relev.":  37.11,
                }
            }
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][0]["product_csum"]
        print("Completed evaluation for Product-Csum Phase")
    elif phase_codename == "product_csum_cross":
        print("Evaluating for Product-Csum-Cross Phase")
        output["result"] = [
            {
                "Cosmetic": {
                    "BLEU": 33.73,
                    "ROUGE": 32.47,
                    "METEOR": 27.87,
                    "Fact.": 36.21,
                    "Compre.": 54.93,
                    "Relev.": 26.17,
                },
                "Automobile": {
                    "BLEU": 34.00,
                    "ROUGE": 34.19,
                    "METEOR":  29.77,
                    "Fact.": 46.23,
                    "Compre.": 82.92,
                    "Relev.":  26.76,
                },
                "Restaurant": {
                    "BLEU": 28.88,
                    "ROUGE": 29.16,
                    "METEOR": 24.93,
                    "Fact.": 35.98,
                    "Compre.": 62.21,
                    "Relev.": 23.40,
                }
            }
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][0]
        print("Completed evaluation for Product-Csum-Cross Phase")
    return output
