import os
import shutil
import distutils.dir_util

from jinja2 import Environment, FileSystemLoader
from mistune import markdown
from bleach import clean

def metadata_extractor_AST(AST_file):
    for i, file_line in enumerate(AST_file):
        if len(file_line) > 1:
            if list(file_line)[1] == "style":
                data = AST_file[:i] + AST_file[i + 1:]
                metadata = [item['raw'] for item in file_line['children'] if 'raw' in item]
                return (data, metadata)
    return (AST_file, None)

def metadata_extractor_HTML(AST_file, HTML_file):
    for file_line in AST_file:
        if len(file_line) > 1:
            if list(file_line)[1] == "style":
                metadata = [item['raw'] for item in file_line['children'] if 'raw' in item]
                data = HTML_file.split("\n")
                data.pop(1)
                return (data, metadata)
    return (HTML_file.split("\n"), None)

def replace_img_source(data):
    if isinstance(data, list):
        return [replace_img_source(item) for item in data]
    elif isinstance(data, str):
        return data.replace("../", "")
    else:
        return data

def setup():
    global SITE_BASE_URL
    SITE_BASE_URL = os.getenv("SITE_BASE_URL", "/scenarios/")

    if os.path.exists("docs/"):
        shutil.rmtree("docs/")
    os.makedirs("docs/", exist_ok=True)

def load_scenarios():
    global path, output_scenarios_paths, output_scenarios_names, scenarios, scenarios_data, appropiate_scenarios_names
    path = "environments/circuits"
    scenarios_file_names = os.listdir(path + "/scenarios")
    files_paths = [path + "/scenarios/" + a for a in scenarios_file_names]
    scenarios_names = [a.split(".")[0] for a in scenarios_file_names]
    scenarios = []
    scenarios_data = []
    output_scenarios_paths = scenarios_file_names.copy()
    output_scenarios_names = scenarios_names.copy()

    for file_path in files_paths:
        with open(file_path, 'r') as file:
            File = file.read()
        scenario_AST = markdown(clean(File), renderer="ast")  # Scenario.md -> AST
        scenario_HTML = markdown(clean(File), renderer="html")  # Scenario.md -> HTML

        SCE_data, SCE_metadata = metadata_extractor_AST(scenario_AST)  # Get the metadata
        scenarios.append([SCE_metadata, SCE_data])  # Save it in AST format
        SCE_data, SCE_metadata = metadata_extractor_HTML(scenario_AST, scenario_HTML)  # Get the metadata
        scenarios_data.append([SCE_metadata, SCE_data])  # Save it in HTML format

    # scenarios contains:

    # ['problems: 1, 2']
    # ['problems: 4']
    # ['problems: 2, 3, 5']      
    # ['problems: 5, 1']
    # ['problems: 1, 2, 3, 4, 5']

    for i, scenario in enumerate(scenarios):
        if (element:=scenario[0]) is None:
            dictionary = {'problems' : []}
        else:
            md_problem = element[0].split(":")  # Get problem and split it
            md_problem[1] = list(map(int, md_problem[1].split(",")))  # Turn all elements into ints and make it a list

            dictionary = {"problems": md_problem[1]}  # Prepare final dictionary
        scenario[0] = dictionary  # Give it to scenarios list (AST format)
        scenarios_data[i][0] = dictionary  # Give it to scenarios_data list (HTML format)

    # Now it looks like this

    # {'problems': [1, 2]}
    # {'problems': [4]}
    # {'problems': [2, 3, 5]}      
    # {'problems': [5, 1]}
    # {'problems': [1, 2, 3, 4, 5]}

    # Fixing source of Images for the HTML

    scenarios_data = replace_img_source(scenarios_data)  # Fixing the img sources

    appropiate_scenarios_names = []
    for scenario in scenarios:  # adressing scenarios by their heading instead of file name
        for i, line in enumerate(scenario[1]):
            if line["type"] == "heading" and line["attrs"] == {"level": 1}:
                appropiate_scenarios_names.append(line["children"][0]["raw"])
    # Remove title of contet
    scenarios_data = [[scenario[0],[a for a in scenario[1] if a[:4] != "<h1>"]] for scenario in scenarios_data]

def load_problems():
    global problems, problems_data
    problems_names = os.listdir(path + "/problems")
    files_paths = [path + "/problems/" + a for a in problems_names]
    problems = []
    problems_data = []
    for file_path in files_paths:
        with open(file_path, 'r') as file:
            File = file.read()
        problem_AST = markdown(clean(File), renderer="ast")  # Problem.md -> AST
        problem_HTML = markdown(clean(File), renderer="html")  # Problem.md -> HTML

        PRO_data, PRO_metadata = metadata_extractor_AST(problem_AST)  # Get the metadata
        problems.append([PRO_metadata, PRO_data])  # Save it in AST format
        PRO_data, PRO_metadata = metadata_extractor_HTML(problem_AST, problem_HTML)  # Get the metadata
        problems_data.append([PRO_metadata, PRO_data])  # Save it in HTML format

    # problems contains:

    # ['id: 1', 'ideas: 1']
    # ['id: 2', 'ideas: 1']
    # ['id: 3', 'ideas: 2']
    # ['id: 4', 'ideas: 2, 3']
    # ['id: 5', 'ideas: 1, 2, 3']

    ids = []
    for i, problem in enumerate(problems):
        if (elements:=problem[0]) is not None:
            md_id = elements[0].split(":")  # Get id part and split it
            md_idea = elements[1].split(":")  # Get idea part and split it
            if (n:=md_id[1].split(",")[0]) != "":
                if int(n) in ids:
                    raise ValueError(f"{problems_names[i]}'s id has already been used, pick another one")
                md_id[1] = int(n)  # Turn all elements into ints and make a list
                ids.append(int(n))
            else:
                raise ValueError(f"{problems_names[i]} doesn't have any value for id in its metadata field, assign a value to id that no other problem shares")
            if (n:=md_idea[1].split(","))[0] != "":
                md_idea[1] = list(map(int, n))  # Turn all elements into ints and make a list
            else:
                md_idea[1] = None

            dictionary = {"id": md_id[1], "ideas": md_idea[1]} # Prepare final dictionary
            problem[0] = dictionary  # Give it to problems list (AST format)
            problems_data[i][0] = dictionary  # Give it to problems_data list (HTML format)
        else:
            raise ValueError(f"{problems_names[i]} is lacking its metadata field, paste this all the way up in your problem.md:\n---\nid: \nidea: \n---\n\nAnd assign a value to id that no other problem shares like id: 2\n")

    # Now it looks like this

    # {'id': 1, 'ideas': [1]}      
    # {'id': 2, 'ideas': [1]}      
    # {'id': 3, 'ideas': [2]}      
    # {'id': 4, 'ideas': [2, 3]}   
    # {'id': 5, 'ideas': [1, 2, 3]}

    for problem in problems: # Just a little setting of each problem's name based on their md title
        for line in problem[1]:
            if line["type"] == "heading":
                problem[0]["title"] = line["children"][0]["raw"]

def load_ideas():
    global ideas_data
    ideas_names = os.listdir(path + "/ideas")
    files_paths = [path + "/ideas/" + a for a in ideas_names]
    ideas = []
    ideas_data = []
    for file_path in files_paths:
        with open(file_path, 'r') as file:
            File = file.read()
        idea_AST = markdown(clean(File), renderer="ast")  # Idea.md -> AST
        idea_HTML = markdown(clean(File), renderer="html")  # Idea.md -> HTML

        IDE_data, IDE_metadata = metadata_extractor_AST(idea_AST)  # Get the metadata
        ideas.append([IDE_metadata, IDE_data])  # Save it in AST format
        IDE_data, IDE_metadata = metadata_extractor_HTML(idea_AST, idea_HTML)  # Get the metadata
        ideas_data.append([IDE_metadata, IDE_data])  # Save it in HTML format

    # ideas contains:
    
    # ['id: 1']
    # ['id: 2']
    # ['id: 3']

    ids = []
    for i, idea in enumerate(ideas):
        if (element:=idea[0]) is not None:
            md_id = element[0].split(":")  # Get id and split it
            if (n:=md_id[1].split(",")[0]) != "":
                if int(n) in ids:
                    raise ValueError(f"{ideas_names[i]}'s id has already been used, pick another one")
                md_id[1] = int(n)  # Turn all elements into ints and make a list
                ids.append(int(n))
            else:
                raise ValueError(f"{ideas_names[i]} doesn't have any value for id in its metadata field, assign a value to id that no other problem shares")
            dictionary = {"id": [int(md_id[1])]}  # Prepare final dictionary
            idea[0] = dictionary  # Give it to ideas list (AST format)
            ideas_data[i][0] = dictionary  # Give it to ideas_data list (HTML format)
        else:
            raise ValueError(f"{ideas_names[i]} is lacking its metadata field, paste this all the way up in your problem.md:\n---\nid: \n---\n\nAnd assign a value to id that no other problem shares like id: 2\n")

    # Now it looks like this

    # {'id': [1]}
    # {'id': [2]}
    # {'id': [3]}

def make_scenarios_html():
    for i, scenario in enumerate(scenarios):  # For each scenario...
        if scenario[0]['problems'] is not None:
            Automator = []
            for problem, problem_data in zip(problems, problems_data):  # For each problem
                if problem[0]["id"] in scenario[0]['problems']:  # If this problem is in the scenario
                    ideas_HTML = []
                    for idea in ideas_data:  # For each idea
                        if (n:=problem[0]["ideas"]) is not None:
                            if idea[0]["id"][0] in n:  # If this idea is in the problem
                                ideas_HTML.append(idea[1])  # Add it to the ideas for the HTML

                    Automator.append(
                        {"id": problem[0]["id"],  # This will be a private id to refer to this problem
                        "description": problem_data[1][2:],  # This will be the description of the problem
                        "title": problem[0]["title"],  # This will be the name of the problem's button
                        "ideas": ideas_HTML  # This will be the description of the ideas
                        })


        environment = Environment(loader=FileSystemLoader("frontend/templates"))
        template = environment.get_template("scenario_template.html")
        output = template.render(
            scenario_content=scenarios_data[i][1],  # Description of each scenario
            problems=Automator,
            scenario_name=appropiate_scenarios_names[i],  # This will be the title and header of the page
            site_base_url=SITE_BASE_URL)

        with open(f'docs/{output_scenarios_names[i]}.html', 'w') as file:
            file.write(output)  # Render the filled template

def make_index_html():
    # Now the menu.html
    list_of_scenarios = [{
        "path": path.split(".")[0]+".html",  # All scenario.html paths
        "description": "some description",  # Description for each scenario
        "title": name
    } for path, name in zip(output_scenarios_paths, appropiate_scenarios_names)]

    environment = Environment(loader=FileSystemLoader("frontend/templates"))
    template = environment.get_template("menu_template.html")
    output = template.render(
        scenarios=list_of_scenarios, 
        site_base_url=SITE_BASE_URL,
    )

    with open(f'docs/index.html', 'w') as file:
        file.write(output)  # Render the filled template

def copy_folders():
    # All of this copies the IMGS folder to the docs folder
    # Could be upgraded to just use mentioned IMGS, not all of them
    source_dir = path + "/IMGS"  
    destination_dir = "docs/IMGS"

    os.makedirs(destination_dir)
    files = os.listdir(source_dir)

    for file in files:
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(destination_dir, file)
        shutil.copy(source_file, destination_file)

    distutils.dir_util.copy_tree("frontend/static", "docs/static")

def main():
    setup()

    load_scenarios()
    load_problems()
    load_ideas()

    make_scenarios_html()
    make_index_html()

    copy_folders()

if __name__ == "__main__":
    main()