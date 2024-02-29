from jinja2 import Environment, FileSystemLoader
from mistune import markdown
from bleach import clean
from os import listdir, remove
from os import path as ospath

def metadata_extractor_AST(markdown_file):
    lock = 0
    for i in range(len(markdown_file)):
        if len(markdown_file[i]) > 1:
            if list(markdown_file[i])[1] == "style":
                data = markdown_file[:i] + markdown_file[i+1:]
                metadata = [item['raw'] for item in markdown_file[i]['children'] if 'raw' in item]
                lock = 1
                break
    if lock:
        return (data, metadata)
        
    else:
        return 0

def metadata_extractor_HTML(markdown_file,HTML_file):
    lock = 0
    for i in range(len(markdown_file)):
        if len(markdown_file[i]) > 1:
            if list(markdown_file[i])[1] == "style":
                metadata = [item['raw'] for item in markdown_file[i]['children'] if 'raw' in item]
                lock = 1
                break
    if lock:
        data = HTML_file.split("\n")
        data.pop(1)
        return (data, metadata)
        
    else:
        return 0
            
for filename in listdir("frontend\webpage"):
    file_path = ospath.join("frontend\webpage", filename)
    remove(file_path)

path = "environments/circuits"

###     OPENING ALL SCENARIOS
scenarios_paths=listdir(path+"/scenarios")
files_paths = [path+"/scenarios/"+a for a in scenarios_paths]
scenarios_names = [a.split(".")[0] for a in scenarios_paths]
scenarios=[]
output_scenarios_paths = []
output_scenarios_names = []
scenarios_data=[]
for file_path, pathandname in zip(files_paths,zip(scenarios_paths,scenarios_names)):
    with open(file_path, 'r') as file:
        File = file.read()
    scenario_AST = markdown(clean(File),renderer="ast")
    scenario_HTML = markdown(clean(File),renderer="html")
    if metadata_extractor_AST(scenario_AST):
        SCE_data, SCE_metadata = metadata_extractor_AST(scenario_AST)
        scenarios.append([SCE_metadata,SCE_data])
        SCE_data, SCE_metadata = metadata_extractor_HTML(scenario_AST,scenario_HTML)
        scenarios_data.append([SCE_metadata,SCE_data])
        output_scenarios_paths.append(pathandname[0])
        output_scenarios_names.append(pathandname[1])
###

###     OPENING ALL PROBLEMS
files_paths = [path+"/problems/"+a for a in listdir(path+"/problems")]
problems=[]
problems_data=[]
for file_path in files_paths:
    with open(file_path, 'r') as file:
        File = file.read()
    problem_AST = markdown(clean(File),renderer="ast")
    problem_HTML = markdown(clean(File),renderer="html")
    if metadata_extractor_AST(problem_AST):
        PRO_data, PRO_metadata = metadata_extractor_AST(problem_AST)
        problems.append([PRO_metadata,PRO_data])
        PRO_data, PRO_metadata = metadata_extractor_HTML(problem_AST,problem_HTML)
        problems_data.append([PRO_metadata,PRO_data])
###

###     OPENING ALL IDEAS
files_paths = [path+"/ideas/"+a for a in listdir(path+"/ideas")]
ideas = []
ideas_data = []
for file_path in files_paths:
    with open(file_path, 'r') as file:
        File = file.read()
    idea_AST = markdown(clean(File),renderer="ast")
    idea_HTML = markdown(clean(File),renderer="html")
    if metadata_extractor_AST(idea_AST):
        IDE_data, IDE_metadata = metadata_extractor_AST(idea_AST)
        ideas.append([IDE_metadata,IDE_data])
        IDE_data, IDE_metadata = metadata_extractor_HTML(idea_AST,idea_HTML)
        ideas_data.append([IDE_metadata,IDE_data])
###




# By this point scenarios contains:
    
#['problems: 1, 2']
#['problems: 4']
#['problems: 2, 3, 5']      
#['problems: 5, 1']
#['problems: 1, 2, 3, 4, 5']

# And problems contains:

#['id: 1', 'ideas: 1']
#['id: 2', 'ideas: 1']
#['id: 3', 'ideas: 2']
#['id: 4', 'ideas: 2, 3']
#['id: 5', 'ideas: 1, 2, 3']

# And ideas contains:

#['id: 1']
#['id: 2']
#['id: 3']



#So let's turn that into dicts like {"id":[1]}
    
for i in range(len(problems)):
    elements = problems[i][0]
    splited1 = elements[0].split(":")
    splited2 = elements[1].split(":")
    #print("1",splited1,"2",splited2)
    splited2[1] = list(map(int,splited2[1].split(",")))

    dictionary = {splited1[0]:int(splited1[1]),splited2[0]:splited2[1]}
    problems[i][0] = dictionary
    problems_data[i][0] = dictionary

for i in range(len(ideas)):
    element = ideas[i][0]
    splited = element[0].split(":")
    dictionary = {splited[0]:[int(splited[1])]}
    ideas[i][0] = dictionary
    ideas_data[i][0] = dictionary

for i in range(len(scenarios)):
    element = scenarios[i][0]
    splited = element[0].split(":")
    splited[1] = list(map(int,splited[1].split(",")))
    dictionary = {splited[0]:splited[1]}
    scenarios[i][0] = dictionary
    scenarios_data[i][0] = dictionary

#Now they look like this

#{'problems': [1, 2]}
#{'problems': [4]}
#{'problems': [2, 3, 5]}      
#{'problems': [5, 1]}
#{'problems': [1, 2, 3, 4, 5]}

#And this

#{'id': 1, 'ideas': [1]}      
#{'id': 2, 'ideas': [1]}      
#{'id': 3, 'ideas': [2]}      
#{'id': 4, 'ideas': [2, 3]}   
#{'id': 5, 'ideas': [1, 2, 3]}
    
#And this

#{'id': [1]}
#{'id': [2]}
#{'id': [3]}
    


    
###What if there's no metadata? like no problem to a scenario or not idea to a problem?

for p in range(len(problems)):
    for b in problems[p][1]:
        if b["type"] == "heading":
            problems[p][0]["title"] = b["children"][0]["raw"]


for i in range(len(scenarios)):
    placeholder = scenarios[i][0]['problems']

    Automator = []
    for problem, problem_data in zip(problems,problems_data):
        if problem[0]["id"] in placeholder:
            ideas_md = []
            for idea in ideas_data:
                if idea[0]["id"][0] in problem[0]["ideas"]:
                    ideas_md.append(idea[1])

            Automator.append({"id":problem[0]["id"],"description":problem_data[1],"title":problem[0]["title"],"ideas":ideas_md})

    with open('frontend\\templates\scenario_template.html', 'r') as file:
        template_content = file.read()

    environment = Environment(loader=FileSystemLoader("frontend\\templates"))
    template = environment.get_template("scenario_template.html")
    output = template.render(scenario_content=scenarios_data[i][1],problems=Automator,scenario_name=output_scenarios_names[i])


    # problems must be a list of dicts with id:name, description:description

    with open(f'frontend\webpage\{output_scenarios_names[i]}.html', 'w') as file:
        file.write(output)

list_of_scenarios = [{"path":path.split(".")[0]+".html", "description":"some description", "title":name} for path,name in zip(output_scenarios_paths,output_scenarios_names)]





environment = Environment(loader=FileSystemLoader("frontend\\templates"))
template = environment.get_template("menu_template.html")
output = template.render(scenarios=list_of_scenarios)

#lista de diccionarios con key:value

#title
#description 
#path path to html

with open(f'frontend\webpage\menu.html', 'w') as file:
    file.write(output)