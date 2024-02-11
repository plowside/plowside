import itertools
import random
import os

##############################################################################
videos_path = "./videos/Escape From Tarkov" # Путь до папки с видео
output_path = "комбинации.txt" # Название файла, в который будут записаны все комбинации

##############################################################################
video_files = os.listdir(videos_path)
all_combs = list(itertools.combinations(video_files, 4))

if os.path.exists(output_path):
	with open(output_path, 'r') as f: _exists = set(line.strip() for line in f)
else: _exists = set()

new_comb = [comb for comb in all_combs if comb not in _exists]
_vars = []

for comb in new_comb:
	for i in range(2, 4):
		for x in itertools.combinations(comb, i):
			_new_comb = list(comb)
			for rep_file in x:
				_new_comb.remove(rep_file)
			_vars.append(_new_comb + list(x))

random.shuffle(_vars)
_exists.update(set(''.join(comb) for comb in _vars))
with open(output_path, 'a') as f:
	for x in _vars:
		f.write(f"{';'.join(x)}\n")

print(f"Работа скрипта завершена!\nВсего комбинаций: {len(_vars)}\nКомбинации записаны в {output_path}")