from . import jobs


def get_unique_job_types(path):
    read_content = jobs.read(path)

    jobs_dict = {}
    for job in read_content:
        jobs_dict[job['job_type']] = job['job_type']

    return jobs_dict


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    read_content = jobs.read(path)

    industries_dict = {}
    for industry in read_content:
        if industry['industry'] != "":
            industries_dict[industry['industry']] = industry['industry']

    return industries_dict


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


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
    if 'max_salary' not in job or 'min_salary' not in job:
        raise ValueError("invalid job!")

    if type(job['max_salary']) != int or type(job['min_salary']) != int:
        raise ValueError("invalid job!")

    if int(job['min_salary']) > int(job['max_salary']):
        raise ValueError("invalid job!")

    if type(salary) != int:
        raise ValueError("invalid job!")

    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


def filter_by_salary_range(jobs, salary):
    jobs_salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_salaries.append(job)
        except ValueError:
            print("Value Error")
    return jobs_salaries
