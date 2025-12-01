# config.py
from dataclasses import dataclass

@dataclass
class BaseConfig:
    """Configuración básica que sirve para cualquier transformer grande"""
    hidden_size: int = 4096      # tamaño de los vectores internos
    num_layers: int = 32         # capas apiladas


@dataclass
class LlamaConfig(BaseConfig):
    """Configuración específica de modelos Llama"""
    vocab_size: int = 128256
    num_attention_heads: int = 32


# Ejemplo de uso
if __name__ == "__main__":
    # Configuración de Llama-3 8B
    config_8b = LlamaConfig()
    print("8B →", config_8b.hidden_size, "capas →", config_8b.num_layers)

    # Configuración de Llama-3 70B (sobreescribo valores)
    config_70b = LlamaConfig(hidden_size=8192, num_layers=80)
    print("70B →", config_70b.hidden_size, "capas →", config_70b.num_layers)