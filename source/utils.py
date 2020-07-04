import json


class AudioSample:
    def __init__(self, name, path, tags, users, volume):
        self.name = name
        self.path = path
        self.tags = tags
        self.users = users
        self.volume = volume

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["path"], data["tags"], data["users"], data["volume"])

    def print(self):
        print(f"Name: {self.name}, path: {self.path}, tags: {self.tags}, users: {self.users}, volume: {self.volume}")

def load_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


def get_sample_from_id(samples, sample_id):
    try:
        return AudioSample.from_dict(samples[str(sample_id)])
    except Exception as e:
        return None

def get_sample_from_name(samples, sample_name):
    try:
        for sample in samples:
            if samples[sample]["name"] == sample_name:
                return AudioSample.from_dict(samples[sample])
    except Exception as e:
        return None

if __name__ == "__main__":
    samples = load_json("samples.json")
    sample = get_sample_from_id(samples, 1)
    sample.print()
    sample = get_sample_from_name(samples, "invoker")
    sample.print()