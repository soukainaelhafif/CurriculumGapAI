from backend.nlp.skill_extractor import find_skill_gap, get_matching_skills, JOBMARKET_SKILLS

def test_skill_gap():
    uni = ["Python", "Java"]
    gap = find_skill_gap(uni, JOBMARKET_SKILLS)
    assert "Docker" in gap
    assert "Python" not in gap

def test_matching_skills():
    uni = ["Python", "Java", "SQL"]
    matching = get_matching_skills(uni, JOBMARKET_SKILLS)
    assert "Python" in matching
    assert "Java" in matching

def test_empty_skills():
    gap = find_skill_gap([], JOBMARKET_SKILLS)
    assert len(gap) == len(JOBMARKET_SKILLS)