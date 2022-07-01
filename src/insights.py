from . import jobs


def get_unique_job_types(path):
    read_content = jobs.read(path)

    jobs_dict = {}
    for job in read_content:
        jobs_dict[job['job_type']] = job['job_type']

    return jobs_dict


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """


def get_unique_industries(path):
    read_content = jobs.read(path)

    industries_dict = {}
    for industry in read_content:
        if industry['industry'] != "":
            industries_dict[industry['industry']] = industry['industry']

    return industries_dict


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    read_content = jobs.read(path)

    all_max_salaries = []
    for salary in read_content:
        if salary['max_salary'].isdigit():
            all_max_salaries.append(int(salary['max_salary']))
    all_max_salaries.sort(reverse=True)

    return all_max_salaries[0]


def get_min_salary(path):
    read_content = jobs.read(path)

    all_min_salaries = []
    for salary in read_content:
        if salary['min_salary'].isdigit():
            all_min_salaries.append(int(salary['min_salary']))
    all_min_salaries.sort()

    return all_min_salaries[0]


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
