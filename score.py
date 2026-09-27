def judge(question, expects, answer, results) -> bool:
    if not expects:
        return False
    return expects.strip().lower() in (answer or "".lower)
    """Return True if the answer is correct, False if not.

    `question` is the question you asked.
    `expects` is a word or short phrase you expect a correct answer to contain.
    `answer` is the answer you got back from the model.
    `results` is a list of all the results you got back from the model.

    You can use any of these to decide whether the answer is correct. You can
    also use your own knowledge of the world, but don't look at the corpus
    when deciding: you want to know whether your system would have gotten it
    right without looking at the corpus. If you do look at the corpus, you
    might be biased toward thinking your system is better than it really is.

    This function is called by run_eval.py for each question in QUESTIONS. It
    should return True if the answer is correct, False if not. You can also
    raise an exception if something went wrong and you can't judge it.
    """
    