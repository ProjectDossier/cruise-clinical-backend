import argparse

from core.envdefault import EnvDefault


def str2bool(value):
    return value.lower == 'true'


def prepare_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action=EnvDefault, envvar='DEBUG', type=int, default=1)
    parser.add_argument('--host', action=EnvDefault, envvar='HOST', type=str, default='0.0.0.0')
    parser.add_argument('--port', action=EnvDefault, envvar='PORT', type=int, default=7777)

    parser.add_argument('--loglevel', action=EnvDefault, envvar='LOGLEVEL', type=str, default="DEBUG")

    env_args_function_dict = {'0': prepare_local_machine_args}

    env = '0'  # local env
    # env = '1'  # test env
    # env = '2'  # saas env

    env_args_function_dict[env](parser)
    args = parser.parse_known_args()
    return args[0]


def prepare_local_machine_args(parser):
    parser.add_argument('--mongo_host', action=EnvDefault, envvar='MONGO_HOST', type=str, default='0.0.0.0')

    parser.add_argument('--mongo_port', action=EnvDefault, envvar='MONGO_PORT', type=int, default=27017)

    parser.add_argument('--mongo_user', action=EnvDefault, envvar='MONGO_USER', type=str,
                        default="mongo_user")
    parser.add_argument('--mongo_password', action=EnvDefault, envvar='MONGO_PASSWORD', type=str,
                        default="mongo_secret")

    parser.add_argument('--dummy_data_path', action=EnvDefault, envvar='DUMMY_DATA_PATH', type=str,
                        default="/Users/ricky/PycharmProjects/CMED_Backend/data/dummy_patient_data.csv")

    parser.add_argument('--db_name', action=EnvDefault, envvar='DB_NAMEE', type=str,
                        default="MedCruise")

    parser.add_argument('--collection_name', action=EnvDefault, envvar='COLLECTION_NAME', type=str,
                        default="patient_data")