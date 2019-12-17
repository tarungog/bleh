import json

import glob


all_funcs = glob.glob('tmp/*ici_features*')

features = {}
for file in all_funcs:
    func_name = file.replace('tmp/ici_features_function.', '').replace('.fre.ft','')
    with open(file) as fp:
        filestr = fp.read()
        hm = [x.strip().split('=') for x in filestr.split(', ')]

        build = {}
        for h in hm:
            build[int(h[0].replace('ft', ''))] = h[1]

    features[func_name] = build


with open('features.json', 'w') as fp:
    json.dump(features, fp)
