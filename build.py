import os

output_dir = 'public'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


os.system('python site.py')

print("Сборка завершена!")
