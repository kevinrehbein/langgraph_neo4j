import os

from dotenv import load_dotenv

load_dotenv()


def run(msg: str = "Hello world.") -> None:
    print(os.getenv("GREETINGS", "VALOR PADRAO"))
    print(msg)


if __name__ == "__main__":
    run("Rodando diretamente pelo python")
