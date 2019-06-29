# usar esse trecho de codigo para carregar modelos no pc
from textgenrnn import textgenrnn
textgen = textgenrnn(weights_path='modelo/colaboratory_weights.hdf5',
                       vocab_path='modelo/colaboratory_vocab.json',
                       config_path='modelo/colaboratory_config.json')

textgen.generate(max_gen_length=2000, temperature=0.7)
