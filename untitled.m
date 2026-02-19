reloadpy();
function reloadPy()
    warning('off','MATLAB:ClassInstanceExists')
    clear classes
    mod = py.importlib.import_module('arraysmaker');
    py.importlib.reload(mod);
end



