def replace_img_sources(data):
    if isinstance(data, list):
        return [replace_img_sources(item) for item in data]
    elif isinstance(data, str):
        return data.replace("../", "")
    else:
        return data

# Your nested list
nested_list = [[{'problems': [2, 4]}, ['<hr />', '<h1>Plan beforehand</h1>', '<h2>Scenario</h2>', '<p><img src="../IMGS/8.png" alt="Image" /></p>', '<h2>Interaction</h2>', '<p><em>User</em>: Turn the LED on, you can only do 2 actions<br />', '<em>Agent</em>: ( flicks switch ), ( presses button )</p>', '<p>::: In here we discourage the agent from experimenting and accomplishing the goal thanks to probability, it has to reason all actions before carrying them out</p>', '']], [{'problems': [3]}, ['<hr />', "<h1>What's this?</h1>", '<h2>Scenario</h2>', '<p><img src="../IMGS/6.png" alt="Image" /><br />', '( random logical gate in between )</p>', '<h2>Interaction</h2>', '<p><em>User</em>: Understand the blank component<br />', '<em>Agent</em>: ( Goes on experimental loop to find out behaviour of component )</p>', '']], [{'problems': [1]}, ['<hr />', '<h1>Is the LED on?</h1>', '<h2>Scenario</h2>', '<p>one turned on LED</p>', '<h2>Interaction</h2>', '<p><em>User</em>: Is the led on?<br />', '<em>Agent</em>: &amp;lt; Some positive answer &amp;gt;</p>', '']], [{'problems': [2]}, ['<hr />', "<h1>Now one act isn't enough</h1>", '<h2>Scenario</h2>', '<p><img src="../IMGS/3.png" alt="Image" /></p>', '<h2>Interaction</h2>', '<p><em>User</em>: Turn the LED on<br />', '<em>Agent</em>: ( flickes 1st switch), ( flickes 2nd switch )</p>', '<p>::: Think about act sequentiation, may not need time understanding</p>', '']]]

new_nested_list = replace_img_sources(nested_list)
print(new_nested_list)