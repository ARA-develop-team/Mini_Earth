import yaml


def parse_data(file_name):
    with open(file_name) as file:
        data_dict = yaml.load(file, yaml.Loader)

        for data in data_dict:
            if data_dict[data] is None:
                raise Exception(f"[ParserError] {data} is empty!"
                                f"\nMake changes in the file '{file_name}'")

            if data == 'octave_value':
                if len(data_dict[data]) < len(data_dict['grid_value']):
                    raise Exception(f"[ParserError] {data} wasn't filled right!"
                                    f"\nMake changes in the file '{file_name}'")

        return data_dict
