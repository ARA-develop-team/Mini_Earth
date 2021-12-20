import yaml


def parse_data(file_name):
    with open(file_name) as file:
        data_dict = yaml.load(file, yaml.Loader)

        for data in data_dict:
            if data_dict[data] is None:
                print(f"[ParserError] {data} is empty! \nMake changes in the file '{file_name}'")
                return False

            if data == 'octave_value':
                if len(data_dict[data]) < len(data_dict['grid_value']):
                    print(f"[ParserError] {data} wasn't filled right! \nMake changes in the file '{file_name}'")
                    return False

        return data_dict


if __name__ == '__main__':
    parse_data('data.yml')
