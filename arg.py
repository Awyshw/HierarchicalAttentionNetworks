def add_args(parser):
    parser.add_argument('-embedding_size', type=int, default = 800)
    parser.add_argument('-rnn_size_char', type=int, default = 300,help="""the number of units of character encoder""")
    parser.add_argument('-rnn_size_sent', type=int, default = 300,help="""the number of units of sentence encoder""")
    parser.add_argument('-batch_size', type=int, default = 32)
    parser.add_argument('-learning_rate', type=float, default = 0.05)
    parser.add_argument('-epochs', type=int, default = 10)
    parser.add_argument('-checkpoint', type=str,default = None)
    parser.add_argument('-test', action="store_true")
    parser.add_argument('-models_dir',type=str, default = 'models/',help="""the directory to save checkpoints""")
    parser.add_argument('-tiny',action='store_true')
    parser.add_argument('-predict',action = 'store_true')