systematic_registry = {}

class Systematic:
    def __init__(self, **config):
        self.config = config
        print(f"Would now create systematic f{self.__class__.__name__} from config info: {config}")

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        name = cls.name if hasattr(cls, 'name') else cls.__name__
        name = name.lower()
        print(f"Register systematic {name}")
        systematic_registry[name] = cls

    @classmethod
    def from_info(cls, config):
        config  = config.copy()
        class_name = config.pop('type')
        if class_name is None:
            raise ValueError("Systematic is missing 'type' entry in param file")
        class_obj = systematic_registry.get(class_name.lower())
        if class_obj is None:
            raise ValueError(f"Systematic called {class_name} not known")

        systematic = class_obj(**config)
        return systematic


class CosmologySystematic(Systematic):
    pass

class SourceSystematic(Systematic):
    pass

class OutputSystematic(Systematic):
    pass
