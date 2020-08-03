import json
import logging


class AudioSample:
    def __init__(self, name, path, tags, users, volume):
        self.name = name
        self.path = path
        self.tags = tags
        self.users = users
        self.volume = volume

    @classmethod
    def from_dict(cls, data):
        return cls(data["path"].split(".")[0], data["path"], data["tags"], data["users"], data["volume"])

    def print(self):
        logging.info(f"Name: {self.name}, path: {self.path}, tags: {self.tags}, users: {self.users}, volume: {self.volume}")


def load_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


def get_sample_from_id(samples, sample_id):
    try:
        return AudioSample.from_dict(samples[str(sample_id)])
    except Exception as e:
        logging.error(f"Error in get_sample_from_id: {e}")
        return None


def get_sample_from_name(samples, sample_name):
    try:
        for sample in samples:
            if samples[sample]["name"] == sample_name:
                return AudioSample.from_dict(samples[sample])
    except Exception as e:
        logging.error(f"Error in get_sample_from_name: {e}")
        return None


def get_sample_from_tag(samples, tag):
    try:
        result = {}
        for sample in samples:
            if tag in samples[sample]["tags"]:
                result[sample] = samples[sample]
        return result
    except Exception as e:
        logging.error(f"Error in get_sample_from_tag: {e}")
        return None


if __name__ == "__main__":
    samples = load_json("samples.json")
    sample = get_sample_from_id(samples, 1)
    sample.print()
    sample = get_sample_from_name(samples, "invoker")
    sample.print()
