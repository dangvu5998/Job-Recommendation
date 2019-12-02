import numpy as np
from constants import LEVELS, SKILLS, ADDRESSES, PROPERTY_WEIGHTS, JOB_PROPERTY_TO_ID, \
    PROPERTY_COUNT, MAX_SALARY
def parse_description(description):
    skills = []
    levels = []
    description = description.lower()
    if 'lập trình' in description:
        description += 'phần mềm'
    for skill in SKILLS:
        if skill in description:
            skills.append(skill)
    for level in LEVELS:
        if level in description:
            levels.append(level)
    return skills, levels

def get_embedding(skills, levels, salary):
    embedding = np.zeros(PROPERTY_COUNT, dtype=np.float32)
    skills = set(skills)
    levels = set(levels)
    for skill in skills:
        skill = skill.lower()
        embedding[JOB_PROPERTY_TO_ID[skill]] = 1
    for level in levels:
        level = level.lower()
        embedding[JOB_PROPERTY_TO_ID[level]] = 1
    if salary is None or not isinstance(salary, int):
        salary = MAX_SALARY // 2
    if salary < 0:
        salary = 0
    if salary > MAX_SALARY:
        salary = MAX_SALARY
    salary = 1.0 * salary / MAX_SALARY
    embedding[-1] = salary
    return embedding