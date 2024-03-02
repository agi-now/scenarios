from jinja2 import Environment, FileSystemLoader
from mistune import markdown
from bleach import clean
from os import listdir, remove, makedirs, rmdir
from os import path as os_path
from shutil import copy

def metadata_extractor_AST(AST_file):
    for i, file_line in enumerate(AST_file):
        if len(file_line) > 1:
            if list(file_line)[1] == "style":
                data = AST_file[:i] + AST_file[i + 1:]
                metadata = [item['raw'] for item in file_line['children'] if 'raw' in item]
                return (data, metadata)
    return False


def metadata_extractor_HTML(AST_file, HTML_file):
    for file_line in AST_file:
        if len(file_line) > 1:
            if list(file_line)[1] == "style":
                metadata = [item['raw'] for item in file_line['children'] if 'raw' in item]
                data = HTML_file.split("\n")
                data.pop(1)
                return (data, metadata)
    return False

file_names = listdir("docs")
for file_name in file_names:
    if file_name != "IMGS":
        remove("docs/" + file_name)
    else:
        img_file_names = listdir("docs/IMGS")
        for img_file in img_file_names:
            remove("docs/IMGS/" + img_file)
        rmdir("docs/IMGS")

with open(f'docs/CNAME', 'w') as file:
    file.write("colab.agi-now.com")


### OPENING ALL SCENARIOS FILES
path = "environments/circuits"
scenarios_file_names = listdir(path + "/scenarios")
files_paths = [path + "/scenarios/" + a for a in scenarios_file_names]
scenarios_names = [a.split(".")[0] for a in scenarios_file_names]
scenarios = []
scenarios_data = []
output_scenarios_paths = []
output_scenarios_names = []

for file_path, path_and_name in zip(files_paths, zip(scenarios_file_names, scenarios_names)):
    with open(file_path, 'r') as file:
        File = file.read()
    scenario_AST = markdown(clean(File), renderer="ast")  # Scenario.md -> AST
    scenario_HTML = markdown(clean(File), renderer="html")  # Scenario.md -> HTML

    if metadata_extractor_AST(scenario_AST):  # If scenario_AST has metadata
        SCE_data, SCE_metadata = metadata_extractor_AST(scenario_AST)  # Get the metadata
        scenarios.append([SCE_metadata, SCE_data])  # Save it in AST format
        SCE_data, SCE_metadata = metadata_extractor_HTML(scenario_AST, scenario_HTML)  # Get the metadata
        scenarios_data.append([SCE_metadata, SCE_data])  # Save it in HTML format
        output_scenarios_paths.append(path_and_name[0])  # Save the path to the scenario file
        output_scenarios_names.append(path_and_name[1])  # Save the name of the scenario file


### OPENING ALL PROBLEMS FILES
files_paths = [path + "/problems/" + a for a in listdir(path + "/problems")]
problems = []
problems_data = []
for file_path in files_paths:
    with open(file_path, 'r') as file:
        File = file.read()
    problem_AST = markdown(clean(File), renderer="ast")  # Problem.md -> AST
    problem_HTML = markdown(clean(File), renderer="html")  # Problem.md -> HTML

    if metadata_extractor_AST(problem_AST):  # If problem_AST has metadata
        PRO_data, PRO_metadata = metadata_extractor_AST(problem_AST)  # Get the metadata
        problems.append([PRO_metadata, PRO_data])  # Save it in AST format
        PRO_data, PRO_metadata = metadata_extractor_HTML(problem_AST, problem_HTML)  # Get the metadata
        problems_data.append([PRO_metadata, PRO_data])  # Save it in HTML format


### OPENING ALL IDEAS FILES
files_paths = [path + "/ideas/" + a for a in listdir(path + "/ideas")]
ideas = []
ideas_data = []
for file_path in files_paths:
    with open(file_path, 'r') as file:
        File = file.read()
    idea_AST = markdown(clean(File), renderer="ast")  # Idea.md -> AST
    idea_HTML = markdown(clean(File), renderer="html")  # Idea.md -> HTML

    if metadata_extractor_AST(idea_AST):  # If idea_AST has metadata
        IDE_data, IDE_metadata = metadata_extractor_AST(idea_AST)  # Get the metadata
        ideas.append([IDE_metadata, IDE_data])  # Save it in AST format
        IDE_data, IDE_metadata = metadata_extractor_HTML(idea_AST, idea_HTML)  # Get the metadata
        ideas_data.append([IDE_metadata, IDE_data])  # Save it in HTML format

# By this point scenarios contains:

# ['problems: 1, 2']
# ['problems: 4']
# ['problems: 2, 3, 5']      
# ['problems: 5, 1']
# ['problems: 1, 2, 3, 4, 5']

# And problems contains:

# ['id: 1', 'ideas: 1']
# ['id: 2', 'ideas: 1']
# ['id: 3', 'ideas: 2']
# ['id: 4', 'ideas: 2, 3']
# ['id: 5', 'ideas: 1, 2, 3']

# And ideas contains:

# ['id: 1']
# ['id: 2']
# ['id: 3']

# So let's turn that into dicts like {"id": [1]}


for i, scenario in enumerate(scenarios):
    element = scenario[0]  # element = metada
    md_problem = element[0].split(":")  # Get problem and split it
    md_problem[1] = list(map(int, md_problem[1].split(",")))  # Turn all elements into ints and make it a list

    dictionary = {md_problem[0]: md_problem[1]}  # Prepare final dictionary
    scenario[0] = dictionary  # Give it to scenarios list (AST format)
    scenarios_data[i][0] = dictionary  # Give it to scenarios_data list (HTML format)


for i, problem in enumerate(problems):
    elements = problem[0]  # elements = metadata
    md_id = elements[0].split(":")  # Get id part and split it
    md_idea = elements[1].split(":")  # Get idea part and split it
    md_idea[1] = list(map(int, md_idea[1].split(",")))  # Turn all elements into ints and make a list

    dictionary = {md_id[0]: int(md_id[1]), md_idea[0]: md_idea[1]} # Prepare final dictionary
    problem[0] = dictionary  # Give it to problems list (AST format)
    problems_data[i][0] = dictionary  # Give it to problems_data list (HTML format)


for i, idea in enumerate(ideas):
    element = idea[0]  # element = metadata
    md_id = element[0].split(":")  # Get id and split it

    dictionary = {md_id[0]: [int(md_id[1])]}  # Prepare final dictionary
    idea[0] = dictionary  # Give it to ideas list (AST format)
    ideas_data[i][0] = dictionary  # Give it to ideas_data list (HTML format)


# Now they look like this

# {'problems': [1, 2]}
# {'problems': [4]}
# {'problems': [2, 3, 5]}      
# {'problems': [5, 1]}
# {'problems': [1, 2, 3, 4, 5]}

# And this

# {'id': 1, 'ideas': [1]}      
# {'id': 2, 'ideas': [1]}      
# {'id': 3, 'ideas': [2]}      
# {'id': 4, 'ideas': [2, 3]}   
# {'id': 5, 'ideas': [1, 2, 3]}

# And this

# {'id': [1]}
# {'id': [2]}
# {'id': [3]}




### What if there's no metadata? like no problem to a scenario or not idea to a problem?

for problem in problems:
    for line in problem[1]:
        if line["type"] == "heading":
            problem[0]["title"] = line["children"][0]["raw"]


# Fixing source of Images for the HTML
def replace_img_source(data):
    if isinstance(data, list):
        return [replace_img_source(item) for item in data]
    elif isinstance(data, str):
        return data.replace("../", "")
    else:
        return data
    
scenarios_data = replace_img_source(scenarios_data)

# We'll make all scenarios.html
for i, scenario in enumerate(scenarios):  # For each scenario...
    Automator = []
    for problem, problem_data in zip(problems, problems_data):  # For each problem
        if problem[0]["id"] in scenario[0]['problems']:  # If this problem is in the scenario
            ideas_HTML = []
            for idea in ideas_data:  # For each idea
                if idea[0]["id"][0] in problem[0]["ideas"]:  # If this idea is in the problem
                    ideas_HTML.append(idea[1])  # Add it to the ideas for the HTML

            Automator.append(
                {"id": problem[0]["id"],  # This will be a private id to refer to this problem
                 "description": problem_data[1],  # This will be the description of the problem
                 "title": problem[0]["title"],  # This will be the name of the problem's button
                 "ideas": ideas_HTML  # This will be the description of the ideas
                 })

    with open('frontend/templates/scenario_template.html', 'r') as file:  # Prepare the scenario template
        template_content = file.read()


    environment = Environment(loader=FileSystemLoader("frontend/templates"))
    template = environment.get_template("scenario_template.html")
    output = template.render(
        scenario_content=scenarios_data[i][1],  # Description of each scenario
        problems=Automator,
        scenario_name=output_scenarios_names[i]  # This will be the title and header of the page
        )

    with open(f'docs/{output_scenarios_names[i]}.html', 'w') as file:
        file.write(output)  # Render the filled template

# Now the menu.html
list_of_scenarios = [{
    "path": path.split(".")[0]+".html",  # All scenario.html paths
    "description": "some description",  # Description for each scenario
    "title": name}  # Displayed name
    for path, name in zip(output_scenarios_paths, output_scenarios_names)]

environment = Environment(loader=FileSystemLoader("frontend/templates"))
template = environment.get_template("menu_template.html")
output = template.render(scenarios=list_of_scenarios)

with open(f'docs/index.html', 'w') as file:
    file.write(output)  # Render the filled template


# All of this copies the IMGS folder to the docs folder
# Could be upgraded to just use mentioned IMGS, not all of them
source_dir = path + "/IMGS"  
destination_dir = "docs/IMGS"

makedirs(destination_dir)
files = listdir(source_dir)

for file in files:
    source_file = os_path.join(source_dir, file)
    destination_file = os_path.join(destination_dir, file)
    copy(source_file, destination_file)
