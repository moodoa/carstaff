import requests
import pandas as pd

from tqdm import tqdm


class CARSTAFF:
    def __init__(self, service_name):
        self.service_name = service_name
        self.url = "https://www.partslink24.com/p5jlr/extern/vehicle/"

    def main(self):
        infos = pd.DataFrame(data={"model": "", "engine": "", "gear": ""}, index=[0])
        for model in tqdm(self._get_models()):
            model_name = model["values"]["name"]
            model_code = model["id"]
            engines = self._get_engines(model_code)
            for engine in engines:
                if engine["values"]["code"] != "全部":
                    engine_code = engine["id"]
                    engine_name = engine["values"]["description"]
                    for gear in self._get_gears(engine_code, model_code):
                        if gear["values"]["code"] != "全部":
                            gear_code = gear["id"]
                            gear_name = gear["values"]["description"]
                            infos.loc[len(infos.index)] = [
                                model_name,
                                engine_name,
                                gear_name,
                            ]
        infos.drop(0, axis=0, inplace=True)
        infos.to_csv(f"{self.service_name}.csv", index=False, encoding="utf-8-sig")
        return "DONE"

    def _get_models(self):
        models = requests.get(
            f"{self.url}models?lang=zh-TW&serviceName={self.service_name}"
        ).json()
        return models["data"]["records"]

    def _get_engines(self, model_code):
        engines = requests.get(
            f"{self.url}engines?lang=zh-TW&mdl={model_code}&serviceName={self.service_name}&upds=2023-02-03--15-13"
        ).json()
        return engines["data"]["records"]

    def _get_gears(self, engine_code, model_code):
        gears = requests.get(
            f"{self.url}gearboxes?avsEn={engine_code}&lang=zh-TW&mdl={model_code}&serviceName={self.service_name}&upds=2023-02-03--15-13"
        ).json()
        return gears["data"]["records"]


if __name__ == "__main__":
    services = {0:"jaguar_parts", 1:"landrover_parts", }
    select = input("你想找哪款車？0: JAGUAR, 1:LAND ROVER")
    staff = CARSTAFF(services[int(select)])
    staff.main()
