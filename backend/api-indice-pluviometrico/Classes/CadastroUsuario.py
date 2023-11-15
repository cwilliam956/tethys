class CadastroUsuario:
    def BuscarPrecipitacao(self, latitude, longitude):
        import requests as r

        url = f"https://atlas.microsoft.com/weather/currentConditions/json?api-version=1.0&query={latitude},{longitude}&subscription-key=g9cogBIB7upc32WNQMsBt-fsO5z2jpNurTF-r3mwVLQ"
        valores = r.get(url)
        formatoDicionario = valores.json()
        resumoPrecipitação = formatoDicionario["results"][0]["precipitationSummary"]
        return resumoPrecipitação

    def realizarPrevisao(self, duracao: int, latitude: float, longitude: float):
        import requests as r

        url = f"https://atlas.microsoft.com/weather/forecast/daily/json?api-version=1.0&query={latitude},{longitude}&duration={duracao}&subscription-key=g9cogBIB7upc32WNQMsBt-fsO5z2jpNurTF-r3mwVLQ"
        valores = r.get(url)
        formatoDicionario = valores.json()
        valores = range(0, duracao)
        for valor in valores:
            ResumoPrecipitacao = formatoDicionario["forecasts"][valor]["day"][
                "totalLiquid"
            ]
            DiaPrecipitacao = formatoDicionario["forecasts"][valor]["date"]
        return ResumoPrecipitacao, DiaPrecipitacao
