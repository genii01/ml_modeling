from argparse import ArgumentParser


def parse_args() -> ArgumentParser:
    main_parser = ArgumentParser()

    dataset_parser = main_parser.add_argument_group('dataset')
    dataset_parser.add_argument('--root_path', default='./', type=str, help='datasets root path')
    dataset_parser.add_argument('--down_sampling', default=0, type=int, help='negative label multiply #')
    dataset_parser.add_argument('--model_path', default='models', type=str)
    dataset_parser.add_argument('--visualization_path', default='visualizes', type=str)
    dataset_parser.add_argument('--simulation_path', default='simulation_result', type=str)
    dataset_parser.add_argument('--data_root', default='data', type=str)
    dataset_parser.add_argument('--entity_table', default='entities_bnpl_users', type=str)
    dataset_parser.add_argument(
        '--label_table',
        default='labels_kcb_unique',
        type=str,
        choices=['labels_kcb_unique', 'label_kcb_maxovddaysin12m'],
    )
    dataset_parser.add_argument(
        '--feature_tables',
        action='store',
        dest='feature_tables',
        type=str,
        nargs='*',
        default=[
            # 'features_tosspay',
            'features_card_transaction',
            'features_accnt_transaction',
            'features_kcbcps',
            'features_au',
        ],
        help='usage : --feature_tables features_tosspay features_au etc',
    )
    dataset_parser.add_argument('--simulation_feature_table', default='features_simulation_kcbcps', type=str)
    dataset_parser.add_argument(
        '--join_cond', default='and', type=str, choices=['and', 'or'], help='condition to join features'
    )
    dataset_parser.add_argument('--kcb_corr_threshold', default=0.9, type=float)

    model_parser = main_parser.add_argument_group('model')
    model_parser.add_argument(
        '--model_type', default='catboost', type=str, choices=['xgboost', 'catboost', 'lightgbm']
    )

    logger_parser = main_parser.add_argument_group('logger')
    logger_parser.add_argument('--mlflow_tracking_uri', default='http://mlflow.data.toss.bz', type=str)
    logger_parser.add_argument('--mlflow_experiment_name', default='bnpl-css', type=str)
    logger_parser.add_argument('--no_logger', action='store_true')

    process_parser = main_parser.add_argument_group('process')
    process_parser.add_argument('--num_folds', default=10, type=int, help='number of folds to split')
    process_parser.add_argument('--fold', default=0, type=int, help='fold number to validate')

    misc_parser = main_parser.add_argument_group('misc')
    misc_parser.add_argument(
        '--mode', default='all', type=str, choices=['all', 'train', 'simulation', 'ensemble', 'deploy']
    )
    misc_parser.add_argument('--num_workers', default=16, type=int, help='num of workers')
    misc_parser.add_argument('--use_gpu', action='store_true')
    misc_parser.add_argument('--seed', default=1337, type=int, help='seed for reproducibility')

    return main_parser.parse_args()
