import scipy.io as sio
from os.path import join, isfile
from functools import cached_property





class Subject:
    def __init__(self, comp_file, test_file):
        self._comp_data = sio.loadmat(comp_file)
        self._test_data = sio.loadmat(test_file)

        self.train_ecog = self._comp_data['train_data']
        self.test_ecog = self._comp_data['test_data']

        self.train_fingers = self._comp_data['train_dg']
        self.test_fingers = self._test_data['test_dg']




class Dataset:
    def __init__(self, path):
        self.path = path


    @property
    def _subjects_files(self):
        return [(join(self.path, f'sub{i}_comp.mat'),
                 join(self.path, f'sub{i}_testlabels.mat')
                 )
                for i in range(1,4)]


    def _check_files(self):
        missing_files = []
        for comp, test in self._subjects_files:
            if not isfile(comp):
                missing_files.append(comp)

            if not isfile(test):
                missing_files.append(test)
                
        if missing_files:
            raise Exception(f'Missing file(s): {missing_files}') 


    @cached_property
    def subjects(self):
        self._check_files()
        return [Subject(comp_file, test_file) for comp_file, test_file in self._subjects_files]

    
    def __getitem__(self, i):
        return self.subjects[i]


    def __len__(self):
        return len(self.subjects)

        
