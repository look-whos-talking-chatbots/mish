"""
File contains the text classification functions for mish-based chatbots.
"""

import spacy

from .settings import CLASSIFIER_PATHS


def intent_approximate_frequency(user_input, language):
    user_input = user_input.lower().replace('\'', '')

    # TODO: Check the word distance for negation words

    label = None

    negation_keywords = ['not', 'dont', 'arent', 'isnt']
    approximate_frequencies = {
        "negated_pairs": {  # these phrases are paired with negation_keywords
            "not-at-all": ["a lot", "lot", "much", "at all"],
            "sometimes": ["often", "all the time", "all time"],
            "mostly": [],
            "always": ["never"],
        },
        "keyword_singles": {
            "not-at-all": ["never", "rarely", "not at all", "not much",
                           "not a lot", "hardly", "almost never"],
            "sometimes": ["sometimes", "occasionally", "now and then",
                          "sometime", "once in a while", "not often",
                          "times to times", "time to time", "it depends", "when I can remember"],
            "mostly": ["mostly", "often", "quite often", "most of the time",
                       "pretty often", "quite often", "frequently", "most the time"],
            "always": ["always", "all the time", "all time",
                       "pretty much all the time", "pretty much all time",
                       "generally", "usually"]
        }
    }

    for key, keywords_list in approximate_frequencies['negated_pairs'].items():
        if (any(word in user_input for word in keywords_list if type(word) == str)
                and any(word in user_input for word in negation_keywords)):
            label = key
    if not label:
        for key, keywords_list in approximate_frequencies['keyword_singles'].items():
            if any(word in user_input for word in keywords_list if type(word) == str):
                label = key

    return label


def intent_sense_reason(user_input, language):
    user_input = user_input.lower()

    label = None
    threshold = 0.3

    nlp = spacy.load(CLASSIFIER_PATHS.format('sense-reason-en-mish-v2'))

    predictions = nlp(user_input).cats

    pred = max(predictions.items(), key=lambda x: x[1])

    if pred and pred[1] > threshold:
        label = pred[0]

    return label


def intent_change_benefit(user_input, language):
    user_input = user_input.lower()

    label = None
    threshold = 0.5

    nlp = spacy.load(CLASSIFIER_PATHS.format('change-benefit-en-mish-v3'))

    predictions = nlp(user_input).cats

    pred = max(predictions.items(), key=lambda x: x[1])

    if pred and pred[1] > threshold:
        label = pred[0]

    if label is not None:
        if any(word in user_input.split() for word in ['sti', 'std', 'hiv', 'aids', 'infections', 'infected', 'infect']
               if type(word) == str):
            label = label + '-sti'
        elif any(phrase in user_input for phrase in ['pregnant', 'pregnancy', 'preggers', 'prego', 'preggo',
                                                     'knocked up', 'baby', 'child', 'mistake', 'kids',
                                                     'having a kid', 'having a child', 'making a baby',
                                                     'becoming a parent', 'child support']
                 if type(phrase) == str):
            label = label + '-pregnancy'

    return label


def intent_change_downside(user_input, language):
    user_input = user_input.lower()

    label = None
    threshold = 0.5

    nlp = spacy.load(CLASSIFIER_PATHS.format('change-downside-en-mish-v3'))

    predictions = nlp(user_input).cats

    pred = max(predictions.items(), key=lambda x: x[1])

    if pred and pred[1] > threshold:
        label = pred[0]

    if label is not None:
        if any(word in user_input.split() for word in ['sti', 'std', 'hiv', 'aids', 'infections', 'infected', 'infect']
               if type(word) == str):
            label = label + '-sti'
        elif any(phrase in user_input for phrase in ['pregnant', 'pregnancy', 'preggers', 'prego', 'preggo',
                                                     'knocked up', 'baby', 'child', 'mistake', 'kids',
                                                     'having a kid', 'having a child', 'making a baby',
                                                     'becoming a parent', 'child support']
                 if type(phrase) == str):
            label = label + '-pregnancy'

    return label


def intent_preparation_activities(user_input, language):
    user_input = user_input.lower().replace('\'', '')

    label = None
    keywords_set = {
        "buy": ["buy", "get", "find", "purchase", "obtain", "shop", "pick up", "get a hold of", "get hands on",
                "come by"],
        "carry": ["keep", "carry", "on hand", "access", "available", "forget", "remember", "take", "bring", "stash",
                  "put", "place"],
        "discuss": ["discuss", "talk", "speak", "bring up", "say", "communicate", "tell", "express", "chat",
                    "have a conversation", "reach out"],
        "try": ["try", "use", "using", "practice", "attempt", "dry run", "test, do", "open"],
    }

    for category, keywords in keywords_set.items():
        if any(word in user_input for word in keywords):
            label = category
            break

    return label


def intent_plan_challenges(user_input, language):
    user_input = user_input.replace('\'', '').lower()

    label = None

    keywords_set = {
        "buy-embarrassment": (
            ["buy", "get", "find", "purchase", "obtain", "shop", "pick up", "get a hold of", "get hands on",
             "come by"],
            ["embarrassed", "embarrassment", "self-conscious", "shy", "anxious", "nervous", "scared",
             "shame", "stigma", "judged", "judgmental", "judgy", "ashamed", "awkward", "weird", "strange",
             "creepy", "comfortable", "uncomfortable", "discomfort", "uneasy", "problematic"]
        ),
        "buy-logistic": (
            ["buy", "get", "find", "purchase", "obtain", "shop", "pick up", "get a hold of", "get hands on",
             "come by"],
            ["unsure", "dont know", "where", "how", "not sure", "difficult", "hard", "tough", "annoying",
             "expensive", "costly", "money", "cheap", "effort", "work", "tiring", "exhausting", "hassle"],
        ),
        "carry-embarrassment": (
            ["keep", "carry", "on hand", "access", "available", "forget", "remember", "take", "bring", "stash",
             "put", "place"],
            ["embarrassed", "embarrassment", "self-conscious", "shy", "anxious", "nervous", "scared",
             "shame", "stigma", "judged", "judgmental", "judgy", "ashamed", "awkward", "weird", "strange",
             "creepy", "comfortable", "uncomfortable", "discomfort", "uneasy", "problematic"],
        ),
        "carry-logistic": (
            ["keep", "carry", "on hand", "access", "available", "forget", "remember", "take", "bring", "stash",
             "put", "place"],
            ["unsure", "dont know", "where", "how", "not sure", "difficult", "hard", "tough", "annoying",
             "expensive", "costly", "money", "cheap", "effort", "work", "tiring", "exhausting", "hassle"],
        ),
        "discuss-embarrassment": (
            ["discuss", "talk", "speak", "bring up", "say", "communicate", "tell", "express", "chat",
             "have a conversation", "reach out"],
            ["embarrassed", "embarrassment", "self-conscious", "shy", "anxious", "nervous", "scared",
             "shame", "stigma", "judged", "judgmental", "judgy", "ashamed", "awkward", "weird", "strange",
             "creepy", "comfortable", "uncomfortable", "discomfort", "uneasy", "problematic"],
        ),
        "discuss-upset": (
            ["discuss", "talk", "speak", "bring up", "say", "communicate", "tell", "express", "chat",
             "have a conversation", "reach out"],
            ["upset", "sad", "unhappy", "angry", "mad", "annoyed", "trust", "cheating", "hurt", "heated",
             "irritated", "offended", "offend", "outraged", "bitter", "indignant"],
        ),
        "try-logistic": (
            ["try", "use", "using", "practice", "attempt", "dry run", "test, do", "open"],
            ["unsure", "dont know", "where", "how", "not sure", "difficult", "hard", "tough", "annoying",
             "expensive", "costly", "money", "cheap", "effort", "work", "tiring", "exhausting", "hassle"],
        ),
        "try-experience": (
            ["try", "use", "using", "practice", "attempt", "dry run", "test, do", "open"],
            ["feel", "feeling", "sensation", "sensitive", "sensitivity", "intimate", "pleasure",
             "comfortable", "uncomfortable", "unnatural", "interrupt", "interruption", "interfere", "moment",
             "experience", "in the way", "annoying", "trouble"]
        )
    }

    for category, keywords_tuple in keywords_set.items():
        if (any(word in user_input for word in keywords_tuple[0])
                and any(word in user_input for word in keywords_tuple[1])):
            label = category
            break

    return label
