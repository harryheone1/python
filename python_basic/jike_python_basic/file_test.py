import os.path

print(os.path.abspath("."))
print(os.path.abspath(".."))
print(os.path.exists("."))
print(os.path.exists("bb"))
print(os.path.exists("../jike_python_basic"))
print(os.path.isdir('.'))
print(os.path.isdir('..'))
print(os.path.isfile("../jike_python_basic"))
os.path.join('/tmp/a', 'b/c')

from pathlib import Path
p = Path('.')
print(p.resolve())
print(p.is_dir())

f = Path('file_op.py')
print(f.resolve())
print(f.is_dir())

np = p.joinpath('test')
Path.mkdir(np, parents=True)

np.replace()

