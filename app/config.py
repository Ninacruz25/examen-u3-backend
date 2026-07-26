import os


class Settings:
    def __init__(self) -> None:
        self.port = int(os.getenv("PORT", "8000"))

        api_key = os.getenv("API_KEY")
        if not api_key:
            raise RuntimeError(
                "La variable de entorno API_KEY es obligatoria y no puede estar vacía."
            )
        self.api_key = api_key


settings = Settings()
