import sys, runpy, os
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'b2py')
sys.path.insert(0, os.path.abspath(d))
runpy.run_path(os.path.join(d, 'random_triangles.py'), run_name='__main__')
