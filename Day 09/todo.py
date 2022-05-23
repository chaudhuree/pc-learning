header = '''
  _            _                           
 | |          | |                          
 | |_ ___   __| | ___     __ _ _ __  _ __  
 | __/ _ \\ / _` |/ _ \\   / _` | '_ \\| '_ \\ 
 | || (_) | (_| | (_) | | (_| | |_) | |_) |
  \__\\___/ \\__,_|\\___/   \__,_| .__/| .__/ 
                              | |   | |    
                              |_|   |_|    
'''
print(header)
todos = []
completd_task = []
while True:
    print('*'*40)
    print('''"q" to quit or "h" to have help \n \n''')
    command = input('>: ')

    if command == 'q':
        break
    elif command == 'h':
        print('''
        to add task ,type it and press enter
        to delete task,type the number of task and press enter
        "h" to have help
        "q" to quit
      ''')
    elif command.isnumeric():
        idx = int(command)-1
        if idx >= len(todos):
            print('No such task is available')
        else:
            done_task = todos.pop(idx)
            completd_task.append(done_task)
    else:
        if command:
            todos.append(command)
    for i in range(len(todos)):
        print(f'{i+1}) {todos[i]}')

if len(completd_task)>0:
  print(f'{len(completd_task)} task is completed today')
  for done in completd_task:
    
    print(f'*- {done}')

end_greetings = '''

                        _   _                
                       | | | |               
   __ _  ___   ___   __| | | |__  _   _  ___ 
  / _` |/ _ \\ / _ \\ / _` | | '_ \\| | | |/ _ \\
 | (_| | (_) | (_) | (_| | | |_) | |_| |  __/
  \\__, |\\___/ \\___/ \\__,_| |_.__/ \\__, |\\___|
   __/ |                           __/ |     
  |___/                           |___/      
'''
print(end_greetings)
