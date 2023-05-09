"""
Contains the indices for the functions belong to this bot
"""

import os

from .actions import *
from .entity_extraction import *
from .text_categorisation import *

FLOWS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flows')

AGENT_INDEX = {
    '8owux06d74j': {
        'path': 'mish',
        'generators': None
    },
    'dlmuzc2g09': {
        'path': 'mishgen',
        'generators': ['gpt35'],
    },
    'mishgen-all': {
        'path': 'mishgen',
        'generators': ['all'],
    },
    'mishgen-gpt': {
        'path': 'mishgen',
        'generators': ['gpt3'],
    },
    'mishgen-dialogpt': {
        'path': 'mishgen',
        'generators': ['dialogpt'],
    }
}

CATEGORISATION_INDEX = {
    'approximate_frequency': intent_approximate_frequency,
    'sense_reason': intent_sense_reason,
    'change_benefit': intent_change_benefit,
    'change_downside': intent_change_downside,
    'preparation_activities': intent_preparation_activities,
    'plan_challenges': intent_plan_challenges,
}

ENTITY_EXTRACTION_INDEX = {}

ACTION_INDEX = {
    'count_focus_correct': count_focus_correct,
    'append_change_benefit': append_change_benefit,
    'count_change_benefit': count_change_benefit,
    'append_change_downside': append_change_downside,
    'count_change_downside': count_change_downside,
}

GENERATION_INDEX = {}
